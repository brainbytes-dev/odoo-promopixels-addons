# Copyright 2026 BrainBytes Studio, License AGPL-3.0 or later
#
# Receives Documenso webhook calls (event/payload/createdAt/webhookEndpoint
# body shape, verified against documenso/documenso's own
# execute-webhook-call.ts on GitHub). Auth is a plain shared-secret string
# in the X-Documenso-Secret header - not HMAC, confirmed from the same
# source file, so a simple equality check is correct here.

import base64
import json
import logging

import requests

from odoo import fields, http
from odoo.http import request

_logger = logging.getLogger(__name__)


class DocumensoWebhookController(http.Controller):

    @http.route("/promopixels/documenso/webhook", type="http", auth="public", methods=["POST"], csrf=False)
    def documenso_webhook(self, **kwargs):
        env = request.env(su=True)
        expected_secret = env["ir.config_parameter"].get_param("documenso.webhook_secret")
        received_secret = request.httprequest.headers.get("X-Documenso-Secret")
        if not expected_secret or received_secret != expected_secret:
            _logger.warning("Documenso webhook: secret mismatch, rejecting")
            return request.make_json_response({"error": "invalid secret"}, status=401)

        try:
            body = json.loads(request.httprequest.data)
        except ValueError:
            return request.make_json_response({"error": "invalid json"}, status=400)
        event = body.get("event")
        payload = body.get("payload", {})
        envelope_id = payload.get("envelopeId")

        if not envelope_id:
            return request.make_json_response({"error": "missing envelopeId"}, status=400)

        order = env["sale.order"].search([("documenso_envelope_id", "=", envelope_id)], limit=1)
        if not order:
            _logger.warning("Documenso webhook: no sale.order found for envelope %s", envelope_id)
            return request.make_json_response({"ignored": True})

        if event == "DOCUMENT_COMPLETED":
            order.write({
                "documenso_state": "signed",
                "documenso_signed_date": fields.Datetime.now(),
            })
            order.message_post(body="Angebot wurde von %s unterschrieben (Documenso)." % order.partner_id.name)
            self._attach_signed_pdf(env, order, envelope_id)
        elif event == "DOCUMENT_REJECTED":
            order.write({"documenso_state": "rejected"})
            order.message_post(body="Signatur-Anfrage wurde vom Kunden abgelehnt (Documenso).")

        return request.make_json_response({"ok": True})

    @staticmethod
    def _attach_signed_pdf(env, order, envelope_id):
        api_key = env["ir.config_parameter"].get_param("documenso.api_key")
        api_url = env["ir.config_parameter"].get_param(
            "documenso.api_url", "https://sign.promopixels.ch/api/v2"
        ).rstrip("/")
        headers = {"Authorization": api_key}
        try:
            envelope = requests.get(f"{api_url}/envelope/{envelope_id}", headers=headers, timeout=30).json()
            items = envelope.get("envelopeItems") or []
            if not items:
                return
            item_id = items[0]["id"]
            pdf_resp = requests.get(
                f"{api_url}/envelope/item/{item_id}/download", headers=headers, timeout=30
            )
            if pdf_resp.ok:
                env["ir.attachment"].create({
                    "name": f"{order.name} - signiert.pdf",
                    "type": "binary",
                    "datas": base64.b64encode(pdf_resp.content),
                    "res_model": "sale.order",
                    "res_id": order.id,
                    "mimetype": "application/pdf",
                })
        except Exception:  # noqa: BLE001 - best-effort attachment, webhook ack must not fail because of this
            _logger.exception("Documenso webhook: failed to fetch/attach signed PDF for envelope %s", envelope_id)
