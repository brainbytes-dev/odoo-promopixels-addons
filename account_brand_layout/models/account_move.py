# Copyright 2019 Open Source Integrators, License AGPL-3.0 or later
# Adapted for Odoo 19 (minimal scope, no per-brand AR/AP routing).
#
# Uses classical single-model _inherit (not the res.brand.mixin multi-inherit
# pattern) - that pattern's field merge did not take effect against
# account.move on this Odoo 19 build, so the mixin's fields are reimplemented
# directly here instead.

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class AccountMove(models.Model):
    _inherit = "account.move"

    brand_id = fields.Many2one(comodel_name="res.brand", string="Brand")
    is_brand_required = fields.Boolean(compute="_compute_is_brand_required")

    @api.depends("company_id", "move_type")
    def _compute_is_brand_required(self):
        for move in self:
            move.is_brand_required = (
                move.move_type in ("out_invoice", "out_refund", "in_invoice", "in_refund")
                and move.company_id.brand_use_level == "required"
            )

    @api.constrains("brand_id", "company_id")
    def _check_brand_company_id(self):
        for move in self:
            if move.brand_id.company_id and move.brand_id.company_id != move.company_id:
                raise ValidationError(
                    self.env._(
                        "Brand company must match document company for %(doc_name)s",
                        doc_name=move.display_name,
                    )
                )
