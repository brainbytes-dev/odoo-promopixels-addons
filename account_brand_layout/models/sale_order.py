# Copyright 2026 BrainBytes Studio, License AGPL-3.0 or later
#
# Mirrors the account.move brand tagging (classical single-model _inherit,
# same reasoning as models/account_move.py) so quotations can carry a brand
# too, not just invoices.

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    brand_id = fields.Many2one(comodel_name="res.brand", string="Brand")
