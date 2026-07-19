#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
String-table translation for the large structured pages.

The long guides (restaurants, local-beaches, tamariu-by-foot, girona...) are
heavy on markup: venue cards, carousels, image grids. Retyping that markup per
language invites drift and broken structure, so instead these pages keep the
English markup as the single source and substitute translated text into it.

Consequence worth knowing: a markup change on the English page automatically
flows to all four translations on the next build. Only the words are per
language.

Helpers here:
  extract(logical)          -> the translatable strings of a page, in order
  apply(content, table, l)  -> English content with language l substituted in
"""

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Text that must never be translated: proper nouns, phone numbers, addresses,
# ratings, prices, and anything that is purely markup or symbols.
SKIP_RE = re.compile(
    r"""^(
        [\s\W\d]*                      # pure punctuation / digits / symbols
        |[★☆⭐→←↺▶]+
        |\d[\d\s.,:/–-]*(km|m|h|min|€|%|/5)?
        |\+?\d[\d\s()-]{6,}            # phone numbers
        |[A-Za-zÀ-ÿ'’.]+\.(jpg|png|svg|webp)
        |https?://\S+
    )$""",
    re.X | re.I,
)

# Block-level text nodes and the attributes that carry user-visible text.
TEXT_RE = re.compile(r">([^<>]+)<")
ATTR_RE = re.compile(r'\b(alt|title|aria-label|placeholder)="([^"]+)"')


def content_of(logical: str) -> str:
    """The English page body between </nav> and <footer>."""
    text = (ROOT / logical).read_text(encoding="utf-8")
    m = re.search(r"</nav>(.*?)<footer", text, re.S)
    return m.group(1).strip() if m else ""


def _candidates(content: str):
    for m in TEXT_RE.finditer(content):
        yield m.group(1)
    for m in ATTR_RE.finditer(content):
        yield m.group(2)


def extract(logical: str) -> list[str]:
    """Ordered, de-duplicated translatable strings of a page."""
    content = content_of(logical)
    seen, out = set(), []
    for raw in _candidates(content):
        s = raw.strip()
        if not s or s in seen:
            continue
        if SKIP_RE.match(s):
            continue
        if len(s) < 2:
            continue
        seen.add(s)
        out.append(s)
    return out


def apply(content: str, table: dict, lang: str) -> str:
    """
    Substitute language `lang` into the English content.

    Replacements are applied longest-first so that a short string can never
    clobber part of a longer one that contains it.
    """
    pairs = []
    for en, langs in table.items():
        dst = langs.get(lang)
        if dst and dst != en:
            pairs.append((en, dst))
    pairs.sort(key=lambda p: len(p[0]), reverse=True)

    # Substitute only inside text nodes and translatable attributes, so a word
    # appearing in a class name or URL is never touched.
    def sub_text(m):
        inner = m.group(1)
        stripped = inner.strip()
        for en, dst in pairs:
            if stripped == en:
                return ">" + inner.replace(en, dst) + "<"
        return m.group(0)

    def sub_attr(m):
        attr, val = m.group(1), m.group(2)
        for en, dst in pairs:
            if val.strip() == en:
                return f'{attr}="{val.replace(en, dst)}"'
        return m.group(0)

    out = TEXT_RE.sub(sub_text, content)
    out = ATTR_RE.sub(sub_attr, out)
    return out


def coverage(logical: str, table: dict, lang: str) -> list[str]:
    """Strings on the page that have no translation for `lang` yet."""
    missing = []
    for s in extract(logical):
        entry = table.get(s)
        if not entry or not entry.get(lang):
            missing.append(s)
    return missing


if __name__ == "__main__":
    import sys
    page = sys.argv[1]
    for s in extract(page):
        print(html.unescape(s))
