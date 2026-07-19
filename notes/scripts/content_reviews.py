#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
String tables for the four Reviews pages.

Deliberate policy: ONLY the page chrome is translated. Every guest testimonial
is left exactly as the guest wrote it, and the reviewer names are untouched.
Translating a review and presenting it as the guest's own words misrepresents
them, and the reviews are already a mix of English, Spanish, French and German —
which is itself evidence they are real.

The subtitle carries a short note, in the local language, explaining that
reviews appear in the language they were written in.

Dates are generated rather than hand-translated, so they cannot drift.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import strings_mode  # noqa: E402

LANGS = ["es", "ca", "fr", "nl"]

MONTHS = {
    "es": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
           "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
    "ca": ["gener", "febrer", "març", "abril", "maig", "juny", "juliol",
           "agost", "setembre", "octubre", "novembre", "desembre"],
    "fr": ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
           "août", "septembre", "octobre", "novembre", "décembre"],
    "nl": ["januari", "februari", "maart", "april", "mei", "juni", "juli",
           "augustus", "september", "oktober", "november", "december"],
}

EN_MONTHS = ["January", "February", "March", "April", "May", "June", "July",
             "August", "September", "October", "November", "December"]

DATE_RE = re.compile(r"^(\d{1,2}) ([A-Z][a-z]+) (\d{4})$")


def localise_date(day: int, month_idx: int, year: int, lang: str) -> str:
    m = MONTHS[lang][month_idx]
    if lang == "es":
        return f"{day} de {m} de {year}"
    if lang == "ca":
        # Catalan elides "de" before a vowel-initial month.
        art = "d'" if m[0] in "aeiouàèéíòóú" else "de "
        return f"{day} {art}{m} de {year}"
    if lang == "fr":
        return f"{'1er' if day == 1 else day} {m} {year}"
    return f"{day} {m} {year}"  # nl


def date_table(logical: str) -> dict:
    """Every 'D Month YYYY' on the page, mapped to each language."""
    out = {}
    for s in strings_mode.extract(logical):
        m = DATE_RE.match(s.strip())
        if not m:
            continue
        day, month, year = int(m.group(1)), m.group(2), int(m.group(3))
        if month not in EN_MONTHS:
            continue
        idx = EN_MONTHS.index(month)
        out[s] = {l: localise_date(day, idx, year, l) for l in LANGS}
    return out


# ── chrome ───────────────────────────────────────────────────────────────────
ROOMS = {
    "Reviews/double-room/index.html": {
        "en": "Double Room",
        "es": "Habitación Doble", "ca": "Habitació Doble",
        "fr": "Chambre Double", "nl": "Tweepersoonskamer",
    },
    "Reviews/twin-room1/index.html": {
        "en": "Double/Twin Room 1",
        "es": "Habitación Doble/Twin 1", "ca": "Habitació Doble/Twin 1",
        "fr": "Chambre Double/Lits Jumeaux 1", "nl": "Twee-/Tweepersoonskamer 1",
    },
    "Reviews/twin-room-2/index.html": {
        "en": "Double/Twin Room 2",
        "es": "Habitación Doble/Twin 2", "ca": "Habitació Doble/Twin 2",
        "fr": "Chambre Double/Lits Jumeaux 2", "nl": "Twee-/Tweepersoonskamer 2",
    },
    "Reviews/pool-apartment/index.html": {
        "en": "Studio Apartment",
        "es": "Apartamento Estudio", "ca": "Apartament Estudi",
        "fr": "Appartement Studio", "nl": "Studioappartement",
    },
}

GUEST_REVIEWS = {"es": "Opiniones de Huéspedes", "ca": "Opinions dels Hostes",
                 "fr": "Avis des Voyageurs", "nl": "Gastenbeoordelingen"}
BACK_TO = {"es": "Volver a", "ca": "Tornar a", "fr": "Retour à", "nl": "Terug naar"}
REVIEWS_N = {"es": "reseñas", "ca": "ressenyes", "fr": "avis", "nl": "recensies"}

SUBTITLE = {
    "es": "Lo que dicen nuestros huéspedes sobre su estancia · Las opiniones se muestran en el idioma en que fueron escritas",
    "ca": "El que diuen els nostres hostes sobre la seva estada · Les opinions es mostren en la llengua en què van ser escrites",
    "fr": "Ce que nos hôtes disent de leur séjour · Les avis sont affichés dans la langue dans laquelle ils ont été rédigés",
    "nl": "Wat onze gasten zeggen over hun verblijf · Beoordelingen worden weergegeven in de taal waarin ze zijn geschreven",
}

META_DESC = {
    "es": "Opiniones de huéspedes sobre la {room} en Tamariu Chalet, Tamariu, Costa Brava.",
    "ca": "Opinions dels hostes sobre l'{room} a Tamariu Chalet, Tamariu, Costa Brava.",
    "fr": "Avis des voyageurs sur la {room} au Tamariu Chalet, Tamariu, Costa Brava.",
    "nl": "Gastenbeoordelingen van de {room} in Tamariu Chalet, Tamariu, Costa Brava.",
}

FOOTER_REVIEWS = [
    ("footer_rooms", [
        ("double_room", "accommodation/double-room.html"),
        ("twin_1", "accommodation/twin-room-1.html"),
        ("twin_2", "accommodation/twin-room-2.html"),
        ("studio", "accommodation/pool-apartment.html"),
    ]),
    ("footer_contact", [
        ("book_now", "contact/index.html"),
        ("nav_getting_here", "getting-here/index.html"),
    ]),
]


def _count(logical: str) -> str | None:
    for s in strings_mode.extract(logical):
        m = re.match(r"^(\d+) reviews$", s.strip())
        if m:
            return m.group(0)
    return None


PAGES = {}

for _logical, _room in ROOMS.items():
    if not (Path(__file__).resolve().parents[2] / _logical).is_file():
        continue

    _table = date_table(_logical)
    _en_room = _room["en"]

    _table[f"Guest Reviews — {_en_room}"] = {
        l: f"{GUEST_REVIEWS[l]} — {_room[l]}" for l in LANGS
    }
    _table["What our guests say about their stay"] = {l: SUBTITLE[l] for l in LANGS}
    _table[f"Back to {_en_room}"] = {
        l: f"{BACK_TO[l]} {_room[l]}" for l in LANGS
    }
    _n = _count(_logical)
    if _n:
        _num = _n.split()[0]
        _table[_n] = {l: f"{_num} {REVIEWS_N[l]}" for l in LANGS}

    PAGES[_logical] = {
        "mode": "strings",
        "footer": FOOTER_REVIEWS,
        "meta": {
            l: {
                "title": f"{GUEST_REVIEWS[l]} — {_room[l]} — Tamariu Chalet",
                "desc": META_DESC[l].format(room=_room[l]),
            }
            for l in LANGS
        },
        "strings": _table,
    }
