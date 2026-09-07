# Copyright 2026 BrainBytes Studio, License AGPL-3.0 or later
#
# Sends the standard quotation report to Documenso's v2 "envelope" API
# (sign.promopixels.ch, self-hosted) and tracks the signing state. Uses the
# envelope endpoints, not the legacy /document endpoints - Documenso's own
# docs mark /document for deprecation in favour of /envelope.

import logging

import requests

from odoo import _, fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

DEFAULT_API_URL = "https://sign.promopixels.ch/api/v2"


class SaleOrder(models.Model):
    _inherit = "sale.order"

    documenso_envelope_id = fields.Char(string="Documenso Envelope ID", copy=False, readonly=True)
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

        envelope = self._documenso_request(
            "POST", "envelope/create",
            json={"payload": {"title": f"Angebot {self.name}", "type": "DOCUMENT"}},
        )
        envelope_id = envelope["id"]

        items = self._documenso_request(
            "POST", "envelope/item/create-many",
            data={"payload": '{"envelopeId": "%s"}' % envelope_id},
            files={"files": (f"{self.name}.pdf", pdf_content, "application/pdf")},
        )
        envelope_item_id = items["data"][0]["id"]

        recipients = self._documenso_request(
            "POST", "envelope/recipient/create-many",
            json={
                "envelopeId": envelope_id,
                "data": [{"email": self.partner_id.email, "name": self.partner_id.name or self.partner_id.email, "role": "SIGNER"}],
            },
        )
        recipient_id = recipients["data"][0]["id"]

        # Position ist ein erster Schätzwert (unten rechts auf Seite 1, in %
        # der Seitenmasse) - beim ersten echten Testlauf im Documenso-
        # Dashboard visuell prüfen und ggf. anpassen.
        self._documenso_request(
            "POST", "envelope/field/create-many",
            json={
                "envelopeId": envelope_id,
                "data": [{
                    "type": "SIGNATURE",
                    "recipientId": recipient_id,
                    "envelopeItemId": envelope_item_id,
                    "page": 1,
                    "positionX": 65,
                    "positionY": 85,
                    "width": 25,
                    "height": 6,
                }],
            },
        )

        self._documenso_request(
            "POST", "envelope/distribute",
            json={
                "envelopeId": envelope_id,
                "meta": {
                    "subject": f"Bitte unterschreiben: Angebot {self.name}",
                    "distributionMethod": "EMAIL",
                    "language": "de",
                },
            },
        )

        self.write({
            "documenso_envelope_id": envelope_id,
            "documenso_state": "sent",
            "documenso_sent_date": fields.Datetime.now(),
        })
        self.message_post(body=_("Angebot zur Unterschrift an Documenso gesendet (%s).") % self.partner_id.email)
