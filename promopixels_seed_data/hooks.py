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


# P1 build-out (2026-09-05): real delivery process from the Obsidian vault
# (Notizen/client-onboarding-sop.md, Notizen/qa-checklist-delivery.md) wired
# into Odoo instead of living only as prose nobody re-reads mid-project.

DELIVERY_STAGES = [
    "Onboarding",
    "Asset-Sammlung",
    "Build",
    "QA & Review",
    "Übergabe",
    "Abgeschlossen",
]

DELIVERY_MILESTONES = [
    "Kickoff",
    "Zwischenstand geliefert",
    "QA bestanden",
    "Übergabe abgeschlossen",
]

WEBSITE_PACKAGE_PRODUCTS = [
    "Launch - Website-Paket",
    "Growth - Website-Paket",
]

# Scale is individually scoped/custom-negotiated (unlike the fixed-scope
# Launch/Growth packages), so it gets the raw Lytbox master template's
# design-approval gate before full build starts ("no build without approved
# design") - deliberately NOT applied to Launch/Growth, whose own SOP says a
# separate approval step isn't needed because their scope is fixed upfront.
SCALE_STAGES = [
    "Onboarding",
    "Asset-Sammlung",
    "Design-Freigabe",
    "Build",
    "QA & Review",
    "Übergabe",
    "Abgeschlossen",
]

SCALE_MILESTONES = [
    "Kickoff",
    "Design freigegeben",
    "Zwischenstand geliefert",
    "QA bestanden",
    "Übergabe abgeschlossen",
]


def _build_project_template(env, template_name, stage_names, milestone_names):
    """Creates (or fetches) one is_template=True project.project with the
    given stages and milestones. Safe to re-run: upserts by name, never
    duplicates stages/milestones on repeat boots."""
    Project = env["project.project"]
    Stage = env["project.task.type"]
    Milestone = env["project.milestone"]

    template = Project.search([("name", "=", template_name), ("is_template", "=", True)], limit=1)
    if not template:
        template = Project.create({"name": template_name, "is_template": True})

    for seq, stage_name in enumerate(stage_names):
        # Dedicated stage per template, never shared across templates - a
        # rename/reorder on one template's board must not silently affect
        # another template's board.
        already_on_template = Stage.search(
            [("name", "=", stage_name), ("project_ids", "in", template.id)], limit=1
        )
        if not already_on_template:
            Stage.create({"name": stage_name, "sequence": seq, "project_ids": [(4, template.id)]})

    for milestone_name in milestone_names:
        if not Milestone.search(
            [("name", "=", milestone_name), ("project_id", "=", template.id)], limit=1
        ):
            Milestone.create({"name": milestone_name, "project_id": template.id})

    return template


def setup_delivery_project_template(env):
    """Confirming a Launch/Growth sale order should not hand back a blank
    project - it should hand back the real delivery process (Obsidian:
    Notizen/client-onboarding-sop.md). Wired to the product via
    service_tracking=project_only + project_template_id."""
    Product = env["product.template"]

    template = _build_project_template(
        env, "Vorlage: Website-Projekt", DELIVERY_STAGES, DELIVERY_MILESTONES
    )

    for product_name in WEBSITE_PACKAGE_PRODUCTS:
        product = Product.search([("name", "=", product_name)], limit=1)
        if product:
            product.write({"service_tracking": "project_only", "project_template_id": template.id})

    env.cr.commit()
    print("DELIVERY_PROJECT_TEMPLATE_SETUP: done, template id", template.id)


def setup_scale_design_gate_template(env):
    """Scale - Website-Paket gets its own template with the extra
    design-approval gate (see SCALE_STAGES/SCALE_MILESTONES above), instead
    of sharing the simpler Launch/Growth template.

    Wrapped in try/except writing to ir.config_parameter - there is no
    container log access in this environment, so a failed hook otherwise
    just silently rolls back with zero way to diagnose why."""
    import traceback

    try:
        Product = env["product.template"]

        template = _build_project_template(
            env, "Vorlage: Scale-Projekt", SCALE_STAGES, SCALE_MILESTONES
        )

        product = Product.search([("name", "=", "Scale - Website-Paket")], limit=1)
        if product:
            product.write({"service_tracking": "project_only", "project_template_id": template.id})

        env.cr.commit()
        print("SCALE_DESIGN_GATE_TEMPLATE_SETUP: done, template id", template.id)
    except Exception:
        env.cr.rollback()
        env["ir.config_parameter"].sudo().set_param(
            "promopixels_seed_data.scale_template_error", traceback.format_exc()
        )
        env.cr.commit()
        print("SCALE_DESIGN_GATE_TEMPLATE_SETUP: FAILED, see ir.config_parameter promopixels_seed_data.scale_template_error")


def setup_timesheet_billing(env):
    """Consulting Stunde is sold by the hour - it should bill off logged
    time, not a quantity guessed at quoting time. Needs hr_timesheet /
    sale_timesheet installed before this hook runs (boot script installs
    them earlier in the -i list)."""
    Project = env["project.project"]
    Product = env["product.template"]

    consulting_project = Project.search([("name", "=", "Consulting & Support")], limit=1)
    if not consulting_project:
        consulting_project = Project.create(
            {"name": "Consulting & Support", "allow_timesheets": True, "allow_billable": True}
        )
    elif not consulting_project.allow_timesheets:
        consulting_project.write({"allow_timesheets": True, "allow_billable": True})

    consulting_product = Product.search([("name", "=", "Consulting Stunde")], limit=1)
    if consulting_product:
        consulting_product.write(
            {
                "service_tracking": "task_global_project",
                "service_policy": "delivered_timesheet",
                "project_id": consulting_project.id,
            }
        )

    env.cr.commit()
    print("TIMESHEET_BILLING_SETUP: done, project id", consulting_project.id)


KNOWLEDGE_PAGES = [
    {
        "name": "Client Onboarding SOP",
        "content": """<h2>Von Deposit-Eingang bis Projektstart-bereit</h2>
<p>Adaptiert aus Lytbox Client-Onboarding-SOP, angepasst an bestehenden PromoPixels-Stack (Tally/Formbricks &rarr; n8n &rarr; Odoo).</p>
<h3>1. Trigger</h3>
<p>Ausgel&ouml;st durch: Deposit-Zahlung eingegangen (Stripe-Webhook) ODER unterzeichnetes SOW, je nachdem was zuerst passiert.</p>
<p><strong>Sofort (automatisiert via n8n):</strong></p>
<ul>
<li>Onboarding-Formular-Link an Kunde senden (Tally/Formbricks, Paket vorausgef&uuml;llt)</li>
<li>CRM-Stage in Odoo: <em>Vertrag &amp; Rechnung</em> &rarr; <em>Abgeschlossen</em></li>
<li>Projekt in Odoo automatisch angelegt (aus der Vorlage &bdquo;Website-Projekt&ldquo;, siehe Sale-Order-Konfiguration)</li>
</ul>
<h3>2. Formular-Auswertung (innerhalb 24h nach Eingang)</h3>
<ul>
<li>Formular-Antworten lesen, in Projekt-Notiz (Odoo Project Description) zusammenfassen</li>
<li>Fehlende/unklare Antworten identifizieren &rarr; gezielte R&uuml;ckfrage per E-Mail, nicht das ganze Formular nochmal</li>
<li>Paket-Scope gegen Formular-Antworten gegenchecken (z.B. Kunde will Shop, hat aber nur Launch gebucht &rarr; Out-of-Scope-Handling greift)</li>
</ul>
<h3>3. Asset-Sammlung</h3>
<p><strong>Was gebraucht wird (abh&auml;ngig von Formular-Antworten):</strong></p>
<ul>
<li>Logo/Brand Colors (falls &bdquo;vorhanden&ldquo; angegeben)</li>
<li>Fotos/Bildmaterial (falls &bdquo;vorhanden&ldquo; angegeben)</li>
<li>Texte (falls &bdquo;liefere ich&ldquo; angegeben)</li>
<li>Domain-Zugang (falls bestehend)</li>
<li>Bestehende Analytics/Tracking-Zug&auml;nge (falls Growth/Scale)</li>
</ul>
<p><strong>Prozess:</strong></p>
<ul>
<li>Sammel-Link senden (Google Drive Ordner oder E-Mail-Anhang-Sammlung &mdash; kein neues Tool n&ouml;tig)</li>
<li>Frist setzen: 5 Werktage ab Onboarding-Formular</li>
<li>Bei Fristüberschreitung: 1 Reminder nach 3 Tagen, danach verschiebt sich der Projektstart entsprechend (Timeline h&auml;ngt an Asset-Lieferung, nicht fix ab Deposit)</li>
</ul>
<h3>4. Kickoff</h3>
<ul>
<li>Kurze Kickoff-Best&auml;tigung per E-Mail: &bdquo;Alles da, Start [Datum]&ldquo; ODER &bdquo;Fehlt noch X, Start verschiebt sich auf [Datum]&ldquo;</li>
<li>Kein separater Kickoff-Call n&ouml;tig bei Launch/Growth (Scope ist fix) &mdash; nur bei Scale, falls gew&uuml;nscht</li>
</ul>
<h3>5. W&auml;hrend des Builds</h3>
<ul>
<li>Fortschritts-Update nach jedem gr&ouml;sseren Meilenstein (nicht t&auml;glich &mdash; vermeidet Mikromanagement-Erwartung)</li>
<li>Zwischenstand-Link (Staging/Vercel-Preview) sobald Grundger&uuml;st steht, f&uuml;r fr&uuml;hes Feedback</li>
<li>Alle Kunden-R&uuml;ckmeldungen schriftlich (E-Mail oder Formular-Kommentar) &mdash; nie nur m&uuml;ndlich/Telefon</li>
</ul>
<h3>6. Vor &Uuml;bergabe</h3>
<p>Siehe Seite &bdquo;QA-Checkliste vor Delivery&ldquo; &mdash; vollst&auml;ndig abhaken vor jeder &Uuml;bergabe.</p>
<h3>7. &Uuml;bergabe</h3>
<ul>
<li>Loom-Walkthrough</li>
<li>Login-Daten/Hosting-Infos dokumentiert und &uuml;bergeben</li>
<li>Retainer-Pitch (Launch- bzw. Growth-Pitch)</li>
<li>CRM-Stage in Odoo: Projekt als abgeschlossen markieren, Retainer-Opportunity anlegen falls Kunde zusagt</li>
</ul>
<h3>8. VA-Verantwortlichkeiten (falls delegiert)</h3>
<ul>
<li>Asset-Sammlung-Status t&auml;glich pr&uuml;fen, &uuml;berf&auml;llige Fristen flaggen</li>
<li>Formular-Antworten in Odoo-Projekt-Notiz &uuml;bertragen</li>
<li>Keine Scope- oder Preis-Entscheidungen &mdash; nur Prozess und Nachverfolgung</li>
</ul>""",
    },
    {
        "name": "QA-Checkliste vor Delivery",
        "content": """<h2>Vor jeder &Uuml;bergabe vollst&auml;ndig abhaken</h2>
<h3>Performance</h3>
<ul>
<li>Lighthouse Score Desktop: 90+</li>
<li>Lighthouse Score Mobile: 85+</li>
<li>LCP (Largest Contentful Paint): unter 2.5s</li>
<li>CLS (Cumulative Layout Shift): unter 0.1</li>
<li>Keine grossen unkomprimierten Bilder (WebP, max. 200kb pro Bild)</li>
</ul>
<h3>Code-Qualit&auml;t</h3>
<ul>
<li>Browser-Konsole: keine Errors (nur Warnings akzeptabel)</li>
<li>Keine TODO-Kommentare im Code</li>
<li>Keine hardcoded API Keys oder Credentials</li>
<li>Keine Test-Inhalte (Lorem ipsum, Placeholder-Text, Dummy-Bilder)</li>
</ul>
<h3>Funktionalit&auml;t</h3>
<ul>
<li>Kontaktformular: Submit getestet, E-Mail kommt an</li>
<li>Alle Links funktionieren (intern + extern), keine 404s</li>
<li>Navigation: alle Anchor-Links scrollen korrekt</li>
<li>Mobile: alle Sektionen auf iPhone 12/14 getestet</li>
<li>Desktop: getestet auf Chrome + Safari</li>
<li>Alle CTAs f&uuml;hren zur richtigen Ziel-URL</li>
</ul>
<h3>SEO &amp; Meta</h3>
<ul>
<li>Title Tag gesetzt (max. 60 Zeichen, enth&auml;lt Keyword + Ortsname)</li>
<li>Meta Description gesetzt (max. 155 Zeichen)</li>
<li>H1 vorhanden (genau eine pro Seite)</li>
<li>H-Hierarchie korrekt (H1 &rarr; H2 &rarr; H3, keine Spr&uuml;nge)</li>
<li>Alt-Texte auf allen Bildern</li>
<li>Canonical URL gesetzt</li>
<li>robots.txt vorhanden</li>
<li>sitemap.xml vorhanden (oder generiert)</li>
</ul>
<h3>Tracking</h3>
<ul>
<li>GA4 Property verbunden, Events feuern</li>
<li>Kontaktformular-Submit als Conversion getrackt</li>
<li>CTA-Klicks getrackt</li>
<li>Google Search Console verkn&uuml;pft (oder vorbereitet)</li>
</ul>
<h3>&Uuml;bergabe-Readiness</h3>
<ul>
<li>Loom-Walkthrough aufgenommen (5-10 Min)</li>
<li>Login-Daten / Hosting-Infos dokumentiert</li>
<li>Domain live oder Staging-Link bereit</li>
<li>Retainer Pitch vorbereitet</li>
</ul>""",
    },
]


def setup_knowledge_base(env):
    """document_page was installed with an empty Knowledge menu - installed
    is not the same as usable. Imports the two SOPs the delivery process
    actually depends on (Obsidian: Notizen/client-onboarding-sop.md,
    Notizen/qa-checklist-delivery.md), verbatim, under one category page.
    Safe to re-run: upserts by name."""
    try:
        Page = env["document.page"]
    except KeyError:
        print("KNOWLEDGE_BASE_SETUP: skipped, document_page not installed yet")
        return

    parent = Page.search([("name", "=", "PromoPixels Prozesse")], limit=1)
    if not parent:
        parent = Page.create({"name": "PromoPixels Prozesse", "type": "category"})

    for page_data in KNOWLEDGE_PAGES:
        vals = dict(page_data, parent_id=parent.id, type="content")
        existing = Page.search([("name", "=", page_data["name"])], limit=1)
        if existing:
            existing.write(vals)
        else:
            Page.create(vals)

    env.cr.commit()
    print("KNOWLEDGE_BASE_SETUP: done,", len(KNOWLEDGE_PAGES), "pages under", parent.name)
