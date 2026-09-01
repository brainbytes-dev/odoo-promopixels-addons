# Copyright 2019 ACSONE SA/NV, License AGPL-3.0 or later
# Adapted for Odoo 19: minimal field set for a brand's own printed identity
# (logo, custom header/footer text). Everything else a report layout might
# need (paperformat, colors, font, external_report_layout_id, background,
# etc.) is taken live from the real company via _get_branded_company below,
# instead of being re-declared and manually kept in sync here - a report
# layout can reference arbitrary res.company fields we can't predict, so
# copying the whole company and overriding only identity fields is the
# robust approach (an earlier version tried to mirror individual company
# fields one by one and broke every time a layout used one we'd missed).

from odoo import api, fields, models, tools


class ResBrand(models.Model):
    _inherit = "res.brand"

    is_company = fields.Boolean(default=True)
    logo = fields.Binary(
        related="partner_id.image_1920",
        string="Brand Logo",
        readonly=False,
    )
    report_header = fields.Html()
    report_footer = fields.Html(translate=True)
    company_details = fields.Html(string="Brand Details")
    is_company_details_empty = fields.Boolean(
        compute="_compute_is_company_details_empty"
    )

    @api.depends("company_details")
    def _compute_is_company_details_empty(self):
        for record in self:
            record.is_company_details_empty = not tools.html2plaintext(
                record.company_details or ""
            )

    def _get_branded_company(self, base_company):
        """An in-memory (unsaved) copy of base_company with this brand's
        identity fields overlaid - used by report templates instead of
        swapping to the brand record directly, so paperformat/colors/
        layout/etc keep working exactly like the real company's."""
        self.ensure_one()
        vals = base_company.copy_data()[0]
        vals.update(
            {
                "name": self.name,
                # Deliberately keep the real company's partner_id (not the
                # brand's own) so anything keyed off it - bank accounts for
                # the QR-bill IBAN, most notably - is shared automatically
                # instead of needing to be duplicated per brand.
                "partner_id": base_company.partner_id.id,
                "logo": self.logo,
                "street": self.street,
                "street2": self.street2,
                "zip": self.zip,
                "city": self.city,
                "state_id": self.state_id.id if self.state_id else False,
                "country_id": self.country_id.id if self.country_id else False,
                "phone": self.phone,
                "email": self.email,
                "website": self.website,
                "vat": self.vat,
            }
        )
        if self.report_header:
            vals["report_header"] = self.report_header
        if self.report_footer:
            vals["report_footer"] = self.report_footer
        if not self.is_company_details_empty:
            vals["company_details"] = self.company_details
        return base_company.new(vals)
