#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate strings that were left in English on the existing translated pages.

These predate the generated pages: the bodies were translated but a handful of
chrome strings (footer headings, contact labels, the page <title> on the contact
pages) were missed, so e.g. /es/contact/ still announced itself to Google as
"Contact & Book — Tamariu Chalet".

    python3 notes/scripts/fix_leftover_english.py --apply
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LANGS = ["es", "ca", "fr", "nl"]

# Exact substring replacements, applied per language.
# Anchored with surrounding markup so we never touch prose that merely
# contains the same word.
REPL = {
    "es": [
        (">Getting Here<", ">Cómo Llegar<"),
        (">Book Now<", ">Reservar Ahora<"),
        (">Contact Details<", ">Datos de Contacto<"),
        (">Email<", ">Correo Electrónico<"),
        (">Phone &amp; WhatsApp<", ">Teléfono y WhatsApp<"),
        (">Address<", ">Dirección<"),
        ("💬 WhatsApp Us", "💬 Escríbanos por WhatsApp"),
        ('aria-label="Close"', 'aria-label="Cerrar"'),
        ("<title>Contact &amp; Book — Tamariu Chalet</title>",
         "<title>Contactar y Reservar — Tamariu Chalet</title>"),
        ('content="Contact &amp; Book — Tamariu Chalet"',
         'content="Contactar y Reservar — Tamariu Chalet"'),
        ("We'd love to hear from you — whether you have a question about the accommodation, "
         "want to check availability or are ready to book. We aim to respond within 24 hours.",
         "Estaremos encantados de saber de usted — tanto si tiene alguna duda sobre el "
         "alojamiento, como si quiere consultar la disponibilidad o ya está listo para "
         "reservar. Procuramos responder en menos de 24 horas."),
        ("WhatsApp messages welcome — we'll reply as soon as possible.",
         "Puede escribirnos por WhatsApp — le responderemos lo antes posible."),
    ],
    "ca": [
        (">Getting Here<", ">Com Arribar<"),
        (">Book Now<", ">Reservar Ara<"),
        (">Contact Details<", ">Dades de Contacte<"),
        (">Email<", ">Correu Electrònic<"),
        (">Phone &amp; WhatsApp<", ">Telèfon i WhatsApp<"),
        (">Address<", ">Adreça<"),
        ("💬 WhatsApp Us", "💬 Escriviu-nos per WhatsApp"),
        ('aria-label="Close"', 'aria-label="Tancar"'),
        ("<title>Contact &amp; Book — Tamariu Chalet</title>",
         "<title>Contactar i Reservar — Tamariu Chalet</title>"),
        ('content="Contact &amp; Book — Tamariu Chalet"',
         'content="Contactar i Reservar — Tamariu Chalet"'),
        ("We'd love to hear from you — whether you have a question about the accommodation, "
         "want to check availability or are ready to book. We aim to respond within 24 hours.",
         "Ens encantarà tenir notícies vostres — tant si teniu algun dubte sobre "
         "l'allotjament, com si voleu consultar la disponibilitat o ja esteu a punt per "
         "reservar. Procurem respondre en menys de 24 hores."),
        ("WhatsApp messages welcome — we'll reply as soon as possible.",
         "Podeu escriure'ns per WhatsApp — us respondrem el més aviat possible."),
    ],
    "fr": [
        (">Getting Here<", ">Comment Venir<"),
        (">Book Now<", ">Réserver<"),
        (">Contact Details<", ">Coordonnées<"),
        (">Email<", ">E-mail<"),
        (">Phone &amp; WhatsApp<", ">Téléphone &amp; WhatsApp<"),
        (">Address<", ">Adresse<"),
        ("💬 WhatsApp Us", "💬 Nous Écrire sur WhatsApp"),
        ('aria-label="Close"', 'aria-label="Fermer"'),
        ("<title>Contact &amp; Book — Tamariu Chalet</title>",
         "<title>Contact &amp; Réservation — Tamariu Chalet</title>"),
        ('content="Contact &amp; Book — Tamariu Chalet"',
         'content="Contact &amp; Réservation — Tamariu Chalet"'),
        ("We'd love to hear from you — whether you have a question about the accommodation, "
         "want to check availability or are ready to book. We aim to respond within 24 hours.",
         "Nous serions ravis d'avoir de vos nouvelles — que vous ayez une question sur "
         "l'hébergement, que vous souhaitiez vérifier les disponibilités ou que vous soyez "
         "prêt à réserver. Nous nous efforçons de répondre sous 24 heures."),
        ("WhatsApp messages welcome — we'll reply as soon as possible.",
         "Vous pouvez nous écrire sur WhatsApp — nous répondrons dès que possible."),
    ],
    "nl": [
        (">Getting Here<", ">Hoe Te Bereiken<"),
        (">Book Now<", ">Nu Boeken<"),
        (">Contact Details<", ">Contactgegevens<"),
        (">Email<", ">E-mail<"),
        (">Phone &amp; WhatsApp<", ">Telefoon &amp; WhatsApp<"),
        (">Address<", ">Adres<"),
        ("💬 WhatsApp Us", "💬 Stuur ons een WhatsApp"),
        ('aria-label="Close"', 'aria-label="Sluiten"'),
        ("<title>Contact &amp; Book — Tamariu Chalet</title>",
         "<title>Contact &amp; Boeken — Tamariu Chalet</title>"),
        ('content="Contact &amp; Book — Tamariu Chalet"',
         'content="Contact &amp; Boeken — Tamariu Chalet"'),
        ("We'd love to hear from you — whether you have a question about the accommodation, "
         "want to check availability or are ready to book. We aim to respond within 24 hours.",
         "We horen graag van u — of u nu een vraag hebt over het verblijf, de beschikbaarheid "
         "wilt controleren of klaar bent om te boeken. We streven ernaar binnen 24 uur te "
         "reageren."),
        ("WhatsApp messages welcome — we'll reply as soon as possible.",
         "WhatsApp-berichten zijn welkom — we reageren zo snel mogelijk."),
    ],
}


def main():
    apply = "--apply" in sys.argv
    total = 0
    for lang in LANGS:
        for path in sorted((ROOT / lang).rglob("*.html")):
            text = path.read_text(encoding="utf-8")
            original = text
            hits = 0
            for src, dst in REPL[lang]:
                if src in text:
                    hits += text.count(src)
                    text = text.replace(src, dst)
            if text != original:
                total += hits
                print(f"  {'fixed' if apply else 'would fix'} "
                      f"{path.relative_to(ROOT).as_posix()}: {hits} strings")
                if apply:
                    path.write_text(text, encoding="utf-8")
    print(f"\n{total} strings {'translated' if apply else 'to translate'}"
          f"{'' if apply else '  (dry run - pass --apply)'}")


if __name__ == "__main__":
    main()
