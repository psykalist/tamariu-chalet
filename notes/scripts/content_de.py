#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
German (de) translations, injected into the existing content modules at build
time.

The other languages are authored inline via the T(es, ca, fr, nl) helper in
each content module. Rather than add a fifth positional argument to hundreds of
call sites, German lives here in one place, keyed by the English source string,
and is merged into the page tables by merge_german() below. This keeps the
German copy reviewable in a single file and leaves the existing tables intact.

  STRINGS_DE  english source string  -> German
  META_DE     logical page path      -> {"title", "desc"}
  PAGES_DE    logical page path      -> {"title", "desc", "content", ...}
              (full content for the pages authored per-language in-module)
"""

# ── Short chrome / labels and page prose (strings-mode pages) ────────────────
# The bulk German glossary is generated into de_data.py (english -> German),
# kept separate so this file stays readable. Falls back to empty if absent.
try:
    from de_data import STRINGS_DE  # noqa: F401
except Exception:
    STRINGS_DE = {}

# ── Per-page meta (title / description) for strings-mode pages ───────────────
META_DE = {
    "things-to-do/cycling.html": {
        "title": "Radfahren — Tamariu Chalet",
        "desc": "Radrouten rund um Tamariu, Costa Brava — malerische Straßen und Küstenwege der Umgebung von Palafrugell, vom Tamariu Chalet.",
    },
    "things-to-do/walking.html": {
        "title": "Wandern — Tamariu Chalet",
        "desc": "Wanderrouten rund um Tamariu, Costa Brava — der Küstenweg GR-92 und Wanderungen im Hinterland, vom Tamariu Chalet.",
    },
    "things-to-do/villages-tour.html": {
        "title": "Tour der mittelalterlichen Dörfer — Tamariu Chalet",
        "desc": "Selbstgeführte Tour durch sechs mittelalterliche Dörfer nahe dem Tamariu Chalet — Begur, Pals, Palau-sator, Peratallada, Ullastret und Monells. Routen, Parken, Sehenswertes, Cafés, Restaurants und Feste.",
    },
    "things-to-do/girona.html": {
        "title": "Girona besuchen — Tamariu Chalet",
        "desc": "Ausflugsführer nach Girona vom Tamariu Chalet — die mittelalterliche Altstadt, die Kathedrale und das jüdische Viertel der Kulturhauptstadt der Costa Brava.",
    },
    "things-to-do/restaurants.html": {
        "title": "Restaurants und Bars in Tamariu — Tamariu Chalet",
        "desc": "Wo man in Tamariu, Costa Brava, essen und trinken kann — Bars, Strandrestaurants, lokale Küche, Pizza zum Mitnehmen und nahe gelegene Geheimtipps. Unser persönlicher Führer für Gäste.",
    },
    "things-to-do/local-beaches.html": {
        "title": "Lokale Strände und Buchten — Tamariu Chalet",
        "desc": "Ehrlicher Führer zu den Stränden rund um Tamariu, Costa Brava — 12 Strände und Buchten mit Entfernungen, Parken, wo man isst und wofür sich jeder eignet.",
    },
}

# ── Full German content for pages authored per-language inside the modules ──
try:
    from de_pages import PAGES_DE  # noqa: F401
except Exception:
    PAGES_DE = {}


def merge_german(all_pages: dict) -> None:
    """Inject German into the assembled page tables (in place)."""
    for logical, page in all_pages.items():
        if page.get("mode") == "strings":
            table = page.get("strings", {})
            for en, langs in table.items():
                if not langs.get("de") and en in STRINGS_DE:
                    langs["de"] = STRINGS_DE[en]
            for en, langs in page.get("script_only", {}).items():
                if not langs.get("de") and en in STRINGS_DE:
                    langs["de"] = STRINGS_DE[en]
            if logical in META_DE:
                page.setdefault("meta", {})["de"] = META_DE[logical]
        else:
            if logical in PAGES_DE and "de" not in page:
                page["de"] = PAGES_DE[logical]
