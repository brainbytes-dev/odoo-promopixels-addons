# Copyright 2026 BrainBytes Studio
# License AGPL-3.0 or later
#
# One-shot seed data for PromoPixels' service catalog, sourced verbatim from
# the Obsidian vault (10 - Projekte/Web & SEO/Promopixels/Architektur/
# service-strategy.md, stand 2026-08-30). Creates product.template records
# via post_init_hook - runs once on install, no-op on later reinstalls.

{
    "name": "PromoPixels Seed Data",
    "summary": "One-time seed of PromoPixels' service catalog as sellable products",
    "version": "19.0.1.0.0",
    "category": "Sales",
    "license": "AGPL-3",
    "author": "BrainBytes Studio",
    "depends": ["product"],
    "data": [],
    "installable": True,
    "post_init_hook": "post_init_hook",
}
