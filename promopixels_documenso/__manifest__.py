# Copyright 2026 BrainBytes Studio
# License AGPL-3.0 or later
#
# Sends sale.order quotations to Documenso (self-hosted, sign.promopixels.ch)
# for e-signature. Odoo Sign is Enterprise-only and unavailable to us, so
# this wires the standard quotation report to Documenso's REST API instead.

{
    "name": "PromoPixels Documenso Signing",
    "summary": "Send quotations to Documenso for e-signature, track status via webhook",
    "version": "19.0.1.0.0",
    "category": "Sales",
    "license": "AGPL-3",
    "author": "BrainBytes Studio",
    "depends": ["sale", "mail"],
    "data": [
        "views/sale_order_views.xml",
    ],
    "installable": True,
}
