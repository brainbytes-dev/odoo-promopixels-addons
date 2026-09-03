# Copyright 2026 BrainBytes Studio, License AGPL-3.0 or later
#
# Source: Obsidian vault, 10 - Projekte/Web & SEO/Promopixels/Architektur/
# service-strategy.md, stand 2026-08-30 (Angebots-Architektur seit 2026-08-30).
# Upsert by name - safe to re-run on every boot (invoked explicitly, not just
# via post_init_hook, so edits here reach an already-installed database too).

from . import logo_data

PRODUCTS = [
    {
        "name": "Launch - Website-Paket",
        "list_price": 2900,
        "description_sale": (
            "Moderner Webauftritt (Onepager oder kompakte Site), live, mobil-optimiert, "
            "messbar. Fixpreis, einmalig. Timeline: 4 Wochen ab SOW + 50% Deposit."
        ),
        "description": """<p><strong>Enthalten:</strong></p>
<ul>
<li>Webdesign (Onepager oder bis 5 Unterseiten)</li>
<li>Basis-SEO (Titel, Meta, H-Struktur, Performance)</li>
<li>Tracking-Setup (Google Analytics / GA4, Conversion-Events)</li>
<li>Kontaktformular mit E-Mail-Weiterleitung</li>
<li>Mobile-Optimierung + Core Web Vitals</li>
<li>Korrekturen bis zu 2h innerhalb von 14 Tagen nach Delivery</li>
<li>30-minuetiger Walkthrough-Call bei Uebergabe</li>
</ul>
<p><strong>Nicht enthalten:</strong></p>
<ul>
<li>Texte/Copywriting (Client liefert oder separat buchbar)</li>
<li>Fotos/Bildmaterial (Client liefert oder Stockfotos auf Anfrage)</li>
<li>Hosting/Domain (Client richtet selbst ein, wir helfen beim Setup)</li>
<li>Ads-Setup, Blog, CRM-Integration, Mehrsprachigkeit</li>
<li>Rechtstexte (AGB, Datenschutz, Widerrufsrecht) - Kunde liefert Inhalt</li>
<li>Aenderungen nach Revision-Frist -&gt; neue Offerte</li>
</ul>
<p>Payment: 50% Deposit bei Signing, 50% bei Delivery.</p>""",
    },
    {
        "name": "Growth - Website-Paket",
        "list_price": 4900,
        "description_sale": (
            "Vollstaendiger KMU-Webauftritt mit erweiterter Site. Fixpreis, einmalig. "
            "Timeline: 4-6 Wochen ab SOW + 50% Deposit."
        ),
        "description": """<p><strong>Enthalten:</strong></p>
<ul>
<li>Alles aus Launch (inkl. Onepager bis kompakte Site)</li>
<li>Pixel-/Tracking-Integration fuer bestehende Ads-Konten (kein Kampagnen-Setup)</li>
<li>Landingpage-Optimierung (CTA-Struktur, Conversion-Fokus)</li>
<li>Blog/News-Sektion (Setup, 2 Starter-Artikel)</li>
<li>Korrekturen bis zu 4h innerhalb von 14 Tagen</li>
<li>45-minuetiger Walkthrough-Call bei Uebergabe</li>
</ul>
<p><strong>Nicht enthalten:</strong></p>
<ul>
<li>Ads-Kampagnen-Setup und -Management (eigenes Modul)</li>
<li>Erweiterte/laufende SEO ueber Basis-SEO hinaus (eigenes Modul)</li>
<li>Content-Erstellung ueber 2 Artikel hinaus</li>
<li>Hosting/Domain</li>
<li>Social-Media-Management</li>
<li>Rechtstexte (AGB, Datenschutz, Widerrufsrecht) - Kunde liefert Inhalt</li>
</ul>
<p>Payment: 50% Deposit bei Signing, 50% bei Delivery.</p>""",
    },
    {
        "name": "Scale - Website-Paket",
        "list_price": 8000,
        "description_sale": (
            "Individuell definiert. Ab CHF 8'000, Fixpreis nach Scope-Definition im Call."
        ),
        "description": """<p><strong>Typischer Scope (individuell verhandelt):</strong></p>
<ul>
<li>Umfassende Website + Strategie-Roadmap</li>
<li>CRM-Integration (z.B. HubSpot, Pipedrive)</li>
<li>KPI-Dashboard / Reporting-Setup</li>
<li>Laufende Betreuung optional (Retainer individuell)</li>
</ul>
<p>AI-Automationen und Branding/Visual-Identity nur im individuell verhandelten Scope, nie als fixer Bullet. Sales: immer Call, Custom Proposal same day.</p>""",
    },
    {
        "name": "Care-Retainer",
        "list_price": 240,
        "description_sale": "Website-Pflege, CHF 240/Monat.",
        "description": """<p><strong>Enthalten:</strong></p>
<ul>
<li>Technische Updates & Sicherheits-Patches</li>
<li>Performance-Monitoring & Core Web Vitals</li>
<li>Kleinere Content-Aenderungen (bis 2h/Monat)</li>
<li>Monatliche Kurzuebersicht</li>
</ul>
<p>Reine Website-Pflege - kein SEO/Ads mehr enthalten (eigene Module).</p>""",
    },
    {
        "name": "Google My Business Betreuung",
        "list_price": 150,
        "description_sale": "GMB-Betreuung, CHF 150/Monat.",
        "description": """<p><strong>Enthalten:</strong></p>
<ul>
<li>Profil-Pflege</li>
<li>Monatliche Posts</li>
<li>Review-Monitoring</li>
<li>NAP-Konsistenz (Name, Adresse, Telefon einheitlich)</li>
</ul>""",
    },
    {
        "name": "Ads-Setup (1 Kanal)",
        "list_price": 1850,
        "description_sale": "Ads-Setup fuer einen Kanal (Google oder Social). Einmalig.",
        "description": """<p><strong>Enthalten:</strong></p>
<ul>
<li>Setup fuer 1 Kanal (Google Ads oder ein Social-Kanal)</li>
</ul>
<p>Eigenstaendig buchbar, unabhaengig vom Website-Tier.</p>""",
    },
    {
        "name": "Ads-Betreuung",
        "list_price": 580,
        "description_sale": (
            "Laufende Ads-Betreuung, CHF 580/Monat. Retainer, 3 Monate Mindestlaufzeit."
        ),
        "description": """<p><strong>Enthalten:</strong></p>
<ul>
<li>Laufende Kampagnen-Betreuung und -Optimierung</li>
</ul>
<p>Mindestlaufzeit: 3 Monate.</p>""",
    },
    {
        "name": "SEO-Audit & Keyword-/Competitor-Plan",
        "list_price": 2900,
        "description_sale": "SEO-Audit inkl. Keyword- und Competitor-Plan. Einmalig.",
        "description": """<p><strong>Enthalten:</strong></p>
<ul>
<li>SEO-Audit der bestehenden Seite</li>
<li>Keyword-Plan</li>
<li>Competitor-Plan</li>
</ul>""",
    },
    {
        "name": "Local-SEO-Setup",
        "list_price": 1600,
        "description_sale": "GMB-Optimierung, Verzeichnisse, NAP. Einmalig, bewusster Einstiegspreis.",
        "description": """<p><strong>Enthalten:</strong></p>
<ul>
<li>GMB-Optimierung</li>
<li>Eintrag in relevante Verzeichnisse</li>
<li>NAP-Konsistenz (Name, Adresse, Telefon)</li>
</ul>""",
    },
    {
        "name": "SEO-Retainer",
        "list_price": 1200,
        "description_sale": "Laufende SEO-Betreuung, CHF 1'200/Monat.",
        "description": """<p><strong>Enthalten:</strong></p>
<ul>
<li>1 Artikel pro Monat</li>
<li>Technisches Monitoring</li>
</ul>""",
    },
    {
        "name": "AI Workflow Automation",
        "list_price": 2400,
        "description_sale": "Einmaliger Sprint fuer 1-3 Tools/Trigger-Automationen.",
        "description": """<p><strong>Enthalten:</strong></p>
<ul>
<li>Automation fuer 1-3 Tools/Trigger</li>
<li>Einmaliger Sprint, kein laufender Retainer</li>
</ul>
<p>Nie Bundle-Bestandteil eines Website-Pakets, immer separat besprochen.</p>""",
    },
    {
        "name": "KI-Chatbot-Integration",
        "list_price": 1850,
        "description_sale": "Chatbot-Integration mit bis zu 10 Wissensdokumenten. Einmalig.",
        "description": """<p><strong>Enthalten:</strong></p>
<ul>
<li>KI-Chatbot-Integration</li>
<li>Bis zu 10 Wissensdokumente eingebunden</li>
</ul>""",
    },
    {
        "name": "AI-Wartungs-SLA",
        "list_price": 150,
        "description_sale": "Laufende Wartung fuer AI-Automationen, CHF 150/Monat.",
        "description": """<p><strong>Enthalten:</strong></p>
<ul>
<li>Laufende Wartung bestehender AI-Automationen/Chatbots</li>
</ul>""",
    },
]


def post_init_hook(env):
    Product = env["product.template"]
    for data in PRODUCTS:
        existing = Product.search([("name", "=", data["name"])], limit=1)
        if existing:
            existing.write(data)
        else:
            Product.create(dict(data, type="service", sale_ok=True, purchase_ok=False))


# Brand facts sourced from the live PromoPixels repo (src/app/impressum/page.tsx,
# src/config/site.ts) via the Obsidian vault, UID confirmed by Henrik directly
# (2026-08-31). No logo file exists anywhere, and the phone number in the repo
# is an explicit placeholder, so neither is set here.
BRAND_FACTS = {
    "name": "PromoPixels",
    "street": "Buchenweg 18",
    "zip": "5036",
    "city": "Oberentfelden",
    "email": "info@promopixels.ch",
    "website": "https://promopixels.ch",
    "vat": "CHE-154.580.444",
}

DEMO_CUSTOMERS = {
    "Musterfirma Reinigung AG": {"street": "Musterstrasse 12", "zip": "5000", "city": "Aarau"},
    "Brauerei Talblick AG": {"street": "Bahnhofstrasse 5", "zip": "3000", "city": "Bern"},
    "Tennisschule Sonnenhof": {"street": "Sonnenweg 3", "zip": "8000", "city": "Zürich"},
}

DEMO_NOTE = "Fiktiver Demo-Kunde, angelegt zum Testen der Odoo-Konfiguration (Brand/Rechnung/Angebot)."


def seed_demo_data(env):
    Partner = env["res.partner"]
    Brand = env["res.brand"]
    country_ch = env["res.country"].search([("code", "=", "CH")], limit=1)

    brand = Brand.search([("name", "=", BRAND_FACTS["name"])], limit=1)
    brand_vals = dict(BRAND_FACTS)
    brand_vals["is_company"] = True
    if country_ch:
        brand_vals["country_id"] = country_ch.id
    brand_vals["report_footer"] = (
        "<p>HM Digital Consulting Rühe &middot; UID CHE-154.580.444 &middot; "
        "Mehrwertsteuerbefreit gemäss Art. 10 Abs. 2a MWSTG</p>"
    )
    # DIN5008's footer is a 4-column table (company_details | report_footer |
    # VAT/HRB | bank IBAN) - leaving company_details empty makes the footer
    # look lopsided (everything crammed into the report_footer column).
    brand_vals["company_details"] = (
        "<p>PromoPixels &mdash; Website &amp; Marketing für lokale Schweizer KMU</p>"
    )
    brand_vals["logo"] = logo_data.LOGO_PNG_B64
    if brand:
        brand.write(brand_vals)
    else:
        brand = Brand.create(brand_vals)

    customers = {}
    for name, addr in DEMO_CUSTOMERS.items():
        partner = Partner.search([("name", "=", name)], limit=1)
        addr_vals = dict(addr)
        if country_ch:
            addr_vals["country_id"] = country_ch.id
        if partner:
            partner.write(addr_vals)
        else:
            vals = dict(addr_vals, name=name, is_company=True, comment=DEMO_NOTE)
            partner = Partner.create(vals)
        customers[name] = partner

    launch = env["product.template"].search([("name", "=", "Launch - Website-Paket")], limit=1)
    seo_audit = env["product.template"].search(
        [("name", "=", "SEO-Audit & Keyword-/Competitor-Plan")], limit=1
    )

    result = {"brand": brand.id, "invoice": None, "quotation": None}

    Move = env["account.move"]
    existing_invoice = Move.search(
        [("partner_id", "=", customers["Musterfirma Reinigung AG"].id), ("ref", "=", "DEMO-PROMOPIXELS")],
        limit=1,
    )
    if not existing_invoice and launch:
        existing_invoice = Move.create(
            {
                "move_type": "out_invoice",
                "partner_id": customers["Musterfirma Reinigung AG"].id,
                "brand_id": brand.id,
                "ref": "DEMO-PROMOPIXELS",
                "invoice_line_ids": [
                    (0, 0, {
                        "product_id": launch.product_variant_id.id,
                        "name": launch.name,
                        "quantity": 1,
                        "price_unit": launch.list_price,
                    })
                ],
            }
        )
    if existing_invoice:
        if existing_invoice.state == "draft":
            try:
                existing_invoice.action_post()
                result["invoice"] = {"id": existing_invoice.id, "state": "posted"}
            except Exception as exc:  # noqa: BLE001
                result["invoice"] = {"id": existing_invoice.id, "state": "draft", "post_error": str(exc)}
        else:
            result["invoice"] = {"id": existing_invoice.id, "state": existing_invoice.state}

    try:
        Sale = env["sale.order"]
    except KeyError:
        Sale = None

    if Sale is not None and seo_audit:
        existing_quote = Sale.search(
            [("partner_id", "=", customers["Brauerei Talblick AG"].id), ("client_order_ref", "=", "DEMO-PROMOPIXELS")],
            limit=1,
        )
        if not existing_quote:
            quote = Sale.create(
                {
                    "partner_id": customers["Brauerei Talblick AG"].id,
                    "client_order_ref": "DEMO-PROMOPIXELS",
                    "order_line": [
                        (0, 0, {
                            "product_id": seo_audit.product_variant_id.id,
                            "name": seo_audit.name,
                            "product_uom_qty": 1,
                            "price_unit": seo_audit.list_price,
                        })
                    ],
                }
            )
            result["quotation"] = {"id": quote.id, "state": quote.state}
        else:
            result["quotation"] = {"id": existing_quote.id, "state": existing_quote.state}
    else:
        result["quotation"] = "skipped: sale.order not installed or SEO-Audit product missing"

    env.cr.commit()
    print("SEED_DEMO_RESULT:", result)


def grant_internal_users_document_access(env):
    """document_page's own security data only adds base.user_root and
    base.user_admin (the literal "admin" superuser) to its Manager group -
    every other internal user, even ones with full Administrator access
    rights otherwise, sees no Knowledge menu at all until added here.
    Superusers bypass group checks entirely, which is why "admin" always
    saw it and nobody else did. Runs every boot, safe no-op once everyone
    is already a member."""
    try:
        group = env.ref("document_page.group_document_manager")
    except ValueError:
        print("DOCUMENT_ACCESS_GRANT: skipped, module not installed yet")
        return
    internal_users = env["res.users"].search(
        [("share", "=", False), ("active", "=", True)]
    )
    to_add = internal_users - group.users
    if to_add:
        group.write({"users": [(4, u.id) for u in to_add]})
    env.cr.commit()
    print("DOCUMENT_ACCESS_GRANT:", internal_users.mapped("login"))
