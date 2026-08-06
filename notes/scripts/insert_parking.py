#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
One-off: insert parking notes (pin + cost) into the English guide pages.

Idempotent — skips a page that already carries a parking-note/parking-pin.
Run once:  python3 notes/scripts/insert_parking.py --apply
Then rebuild translations / hreflang / sitemap as usual.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from content_parking import html_line, pin_line  # noqa: E402

ROOT = HERE.parents[1]
MAPS = "https://www.google.com/maps/search/?api=1&query="

APPLY = "--apply" in sys.argv


def edit(rel, fn):
    p = ROOT / rel
    html = p.read_text(encoding="utf-8")
    new = fn(html)
    if new == html:
        print(f"  no change  {rel}")
        return
    if APPLY:
        p.write_text(new, encoding="utf-8")
    print(f"  {'wrote' if APPLY else 'would edit'}  {rel}")


def after(html, anchor, addition):
    """Insert `addition` immediately after the first `anchor` (must be unique)."""
    i = html.find(anchor)
    if i == -1:
        raise SystemExit(f"anchor not found: {anchor[:60]!r}")
    i += len(anchor)
    return html[:i] + addition + html[i:]


# ── Villages tour ────────────────────────────────────────────────────────────
VILLAGES = [
    ("short walk back up.</p>",                 "village_summer", "Aparcament+Begur"),
    ("arrive earlier in the day.</p>",          "village_summer", "Aparcament+de+Pals"),
    ("outside the busiest weekends.</p>",       "free",           "Palau-sator"),
    ("the last few minutes into the centre.</p>", "peratallada",  "Aparcament+Peratallada"),
    ("has its own car park a short drive away.</p>", "free",       "Ullastret+aparcament"),
    ("the easiest of the six for parking.</p>", "free",           "Aparcament+Monells"),
]


def do_villages(html):
    if "parking-note" in html:
        return html
    for anchor, cost, q in VILLAGES:
        html = after(html, anchor, "\n    " + html_line(cost, MAPS + q))
    return html


# ── Girona ───────────────────────────────────────────────────────────────────
def do_girona(html):
    if "parking-note" in html:
        return html
    anchor = "<h2>Top Things to Do</h2>"
    line = html_line("girona", MAPS + "Aparcament+Devesa+Girona")
    return html.replace(anchor, line + "\n\n  " + anchor, 1)


# ── Restaurants (worth the drive) ────────────────────────────────────────────
def do_restaurants(html):
    if "parking-note" in html:
        return html
    # Mooma: swap its plain map-link for the pin+cost line.
    html = html.replace(
        '<a class="map-link" href="https://maps.google.com/?q=Mooma+Palau-Sator" '
        'target="_blank" rel="noopener">📍 View on Google Maps</a>',
        html_line("onsite", MAPS + "Mooma+Palau-Sator"), 1)
    inserts = [
        ("elfar.net</a></div>",             "onsite",    "El+Far+Llafranc"),
        ("+34 972 31 23 30</a></div>",       "calella",   "La+Malcontenta+Calella"),
        ("+34 972 30 56 30</a></div>",       "town_free", "La+Xicra+Palafrugell"),
        ("+34 653 864 831</a></div>",        "onsite",    "Alfok+Esclanya"),
        ("+34 972 66 76 56</a></div>",       "big_free",  "Machetes+Platja+de+Pals"),
    ]
    for anchor, cost, q in inserts:
        html = after(html, anchor, "\n            " + html_line(cost, MAPS + q))
    return html


# ── Local beaches (already state cost — add a pin to each Parking block) ──────
BEACHES = [
    ("Platja de Tamariu",      "Aparcament+Tamariu"),
    ("Cala Pedrosa",           "Cala+Pedrosa+Tamariu"),
    ("Aiguablava",             "Aiguablava+aparcament"),
    ("Aigua Xelida",           "Aigua+Xelida"),
    ("Llafranc",               "Llafranc+aparcament"),
    ("Calella de Palafrugell", "Calella+de+Palafrugell+aparcament"),
    ("El Golfet",              "El+Golfet+Calella+de+Palafrugell"),
    ("Sa Riera",               "Sa+Riera+aparcament"),
    ("Sa Tuna",                "Sa+Tuna+aparcament"),
    ("Platja de Pals",         "Aparcament+Platja+de+Pals"),
    ("Platja de Castell",      "Aparcament+Platja+de+Castell"),
    ("La Fosca",               "La+Fosca+aparcament"),
]


def do_beaches(html):
    if "parking-pin" in html:
        return html
    # positions of each beach's <h3>, in document order
    marks = sorted((html.find(f">{name}</h3>"), name, q) for name, q in BEACHES)
    for pos, name, q in marks:
        if pos == -1:
            raise SystemExit(f"beach h3 not found: {name}")
    # walk each section; insert after the first "<h4>Parking</h4>" in it
    out = html
    for i, (pos, name, q) in enumerate(marks):
        # recompute pos in the mutated string (names are unique)
        h3 = out.find(f">{name}</h3>")
        park = out.find("<h4>Parking</h4>", h3)
        if park == -1:
            raise SystemExit(f"no Parking block for {name}")
        park += len("<h4>Parking</h4>")
        out = out[:park] + "\n            " + pin_line(MAPS + q) + out[park:]
    return out


if __name__ == "__main__":
    edit("things-to-do/villages-tour.html", do_villages)
    edit("things-to-do/girona.html", do_girona)
    edit("things-to-do/restaurants.html", do_restaurants)
    edit("things-to-do/local-beaches.html", do_beaches)
    print("done" + ("" if APPLY else "  (dry run — pass --apply)"))
