# Copyright 2019 Open Source Integrators, ACSONE SA/NV, Odoo Community Association (OCA)
# Copyright 2026 BrainBytes Studio
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# Minimal Odoo 19 port of OCA/brand's account_brand + brand_external_report_layout
# (no 19.0 release exists yet upstream). Scope intentionally reduced to: a brand
# selector on customer invoices/refunds, and swapping the printed logo/address/
# footer to the selected brand. No per-brand AR/AP account routing, no custom
# fonts/colors/paperformat wizard - see the OCA modules for that once ported.

{
    "name": "Account Brand Layout (minimal 19.0 port)",
    "summary": "Tag customer invoices and quotations with a brand; PDF shows that brand's identity",
    "version": "19.0.1.0.0",
    "category": "Accounting",
    "license": "AGPL-3",
    "author": "BrainBytes Studio (based on OCA/brand)",
    "website": "https://github.com/OCA/brand",
    "depends": ["account", "brand", "sale", "l10n_din5008"],
    "data": [
        "views/account_move_views.xml",
        "views/report_invoice_brand.xml",
        "views/sale_order_views.xml",
        "views/report_quotation_brand.xml",
        "views/res_brand_views.xml",
        "views/report_din5008_cleanup.xml",
    ],
    "installable": True,
}
