# Copyright 2026 BrainBytes Studio, License AGPL-3.0 or later
#
# Receives Documenso webhook calls. Payload shape and X-Documenso-Secret
# auth verified against documenso/documenso's v1.12.10 tag on GitHub
# (packages/lib/jobs/definitions/internal/execute-webhook.handler.ts) -
# matches the self-hosted version actually deployed on sign.promopixels.ch.
# The webhook payload's "event" field is the raw enum (e.g.
# DOCUMENT_COMPLETED), not the friendly "document.completed" label shown
# in the Documenso UI - that's purely a display transform.

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
        document_id = payload.get("id")

        if document_id is None:
            return request.make_json_response({"error": "missing document id"}, status=400)

        order = env["sale.order"].search([("documenso_document_id", "=", str(document_id))], limit=1)
        if not order:
            _logger.warning("Documenso webhook: no sale.order found for document %s", document_id)
            return request.make_json_response({"ignored": True})

        if event == "DOCUMENT_COMPLETED":
            order.write({
                "documenso_state": "signed",
                "documenso_signed_date": fields.Datetime.now(),
            })
            order.message_post(body="Angebot wurde von %s unterschrieben (Documenso)." % order.partner_id.name)
            self._attach_signed_pdf(env, order, document_id)
        elif event == "DOCUMENT_REJECTED":
            order.write({"documenso_state": "rejected"})
            order.message_post(body="Signatur-Anfrage wurde vom Kunden abgelehnt (Documenso).")

        return request.make_json_response({"ok": True})

    @staticmethod
    def _attach_signed_pdf(env, order, document_id):
        api_key = env["ir.config_parameter"].get_param("documenso.api_key")
        api_url = env["ir.config_parameter"].get_param(
            "documenso.api_url", "https://sign.promopixels.ch/api/v1"
        ).rstrip("/")
        headers = {"Authorization": api_key}
        try:
            download_info = requests.get(
                f"{api_url}/documents/{document_id}/download", headers=headers, timeout=30
            ).json()
            download_url = download_info.get("downloadUrl")
            if not download_url:
                return
            pdf_resp = requests.get(download_url, timeout=30)
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
            _logger.exception("Documenso webhook: failed to fetch/attach signed PDF for document %s", document_id)
