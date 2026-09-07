# Copyright 2026 BrainBytes Studio, License AGPL-3.0 or later
#
# Sends the standard quotation report to Documenso's v1 Document API
# (sign.promopixels.ch, self-hosted documenso/documenso:v1.12.10 - the
# newer "envelope" v2 API from Documenso's hosted docs does not exist on
# this pinned version, verified against the v1.12.10 tag's own
# packages/api/v1/examples on GitHub).

import logging

import requests

from odoo import _, fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

DEFAULT_API_URL = "https://sign.promopixels.ch/api/v1"


class SaleOrder(models.Model):
    _inherit = "sale.order"

    documenso_document_id = fields.Char(string="Documenso Document ID", copy=False, readonly=True)
    documenso_state = fields.Selection(
        [
            ("not_sent", "Nicht gesendet"),
            ("sent", "Wartet auf Unterschrift"),
            ("signed", "Signiert"),
            ("rejected", "Abgelehnt"),
        ],
        string="Signatur-Status",
        default="not_sent",
        copy=False,
        readonly=True,
        tracking=True,
    )
    documenso_sent_date = fields.Datetime(string="Zur Signatur gesendet am", copy=False, readonly=True)
    documenso_signed_date = fields.Datetime(string="Signiert am", copy=False, readonly=True)

    def _documenso_config(self):
        ICP = self.env["ir.config_parameter"].sudo()
        api_key = ICP.get_param("documenso.api_key")
        if not api_key:
            raise UserError(_(
                "Documenso API-Key ist nicht konfiguriert. "
                "Bitte Systemparameter 'documenso.api_key' setzen."
            ))
        api_url = ICP.get_param("documenso.api_url", DEFAULT_API_URL)
        return api_url.rstrip("/"), api_key

    def _documenso_request(self, method, path, **kwargs):
        api_url, api_key = self._documenso_config()
        url = f"{api_url}/{path.lstrip('/')}"
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = api_key
        resp = requests.request(method, url, headers=headers, timeout=30, **kwargs)
        if not resp.ok:
            _logger.error("Documenso API error %s on %s: %s", resp.status_code, path, resp.text)
            raise UserError(_("Documenso hat die Anfrage abgelehnt (%s): %s") % (resp.status_code, resp.text))
        return resp.json()

    def action_send_to_documenso(self):
        self.ensure_one()
        if not self.partner_id.email:
            raise UserError(_("Der Kunde %s hat keine E-Mail-Adresse hinterlegt.") % self.partner_id.name)

        pdf_content, _report_type = self.env["ir.actions.report"]._render_qweb_pdf(
            "sale.action_report_saleorder", self.ids
        )

        document = self._documenso_request(
            "POST", "documents",
            json={
                "title": f"Angebot {self.name}",
                "recipients": [{
                    "name": self.partner_id.name or self.partner_id.email,
                    "email": self.partner_id.email,
                    "role": "SIGNER",
                }],
                "meta": {
                    "subject": f"Bitte unterschreiben: Angebot {self.name}",
                    "message": f"Hallo, bitte unterschreiben Sie das beigefügte Angebot {self.name}.",
                },
            },
        )
        document_id = document["documentId"]
        recipient_id = document["recipients"][0]["recipientId"]

        upload_resp = requests.put(
            document["uploadUrl"],
            data=pdf_content,
            headers={"Content-Type": "application/octet-stream"},
            timeout=60,
        )
        if not upload_resp.ok:
            _logger.error("Documenso upload failed %s: %s", upload_resp.status_code, upload_resp.text)
            raise UserError(_("Documenso-PDF-Upload fehlgeschlagen (%s).") % upload_resp.status_code)

        # Position ist ein erster Schätzwert (unten rechts auf Seite 1, in %
        # der Seitenmasse) - beim ersten echten Testlauf im Documenso-
        # Dashboard visuell prüfen und ggf. anpassen.
        self._documenso_request(
            "POST", f"documents/{document_id}/fields",
            json={
                "type": "SIGNATURE",
                "recipientId": recipient_id,
                "pageNumber": 1,
                "pageX": 65,
                "pageY": 85,
                "pageWidth": 25,
                "pageHeight": 6,
            },
        )

        self._documenso_request("POST", f"documents/{document_id}/send", json={"sendEmail": True})

        self.write({
            "documenso_document_id": str(document_id),
            "documenso_state": "sent",
            "documenso_sent_date": fields.Datetime.now(),
        })
        self.message_post(body=_("Angebot zur Unterschrift an Documenso gesendet (%s).") % self.partner_id.email)
