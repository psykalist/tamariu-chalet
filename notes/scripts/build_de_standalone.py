#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build the German copies of the 13 hand-authored standalone pages (homepage,
room pages, about-catalunya, contact) from their English source.

These pages are not part of build_translations (they have bespoke layouts:
galleries, pricing tables, review carousels). This script copies the English
markup and:
  * substitutes German text (text nodes + alt/title/aria-label/placeholder,
    <title> and <meta name="description">), from the shared UI vocabulary +
    STRINGS_DE glossary + de_standalone glossary. Untranslated strings (e.g.
    guest testimonials) are deliberately left as written.
  * bumps css/js/images asset paths one level deeper (de/ pages sit one folder
    lower than their English counterparts).
  * sets <html lang="de"> and rebuilds the language switcher with DE active.
canonical/hreflang are left for fix_hreflang.py to regenerate.

    python3 notes/scripts/build_de_standalone.py            # dry run
    python3 notes/scripts/build_de_standalone.py --apply
"""

import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import i18n_shell as ish          # noqa: E402
import content_de as cde          # noqa: E402

ROOT = Path(__file__).resolve().parents[2]

PAGES = [
    "index.html",
    "accommodation/double-room.html",
    "accommodation/twin-room-1.html",
    "accommodation/twin-room-2.html",
    "accommodation/pool-apartment.html",
    "about-catalunya/cuisine.html",
    "about-catalunya/language.html",
    "about-catalunya/culture.html",
    "about-catalunya/history.html",
    "about-catalunya/cities.html",
    "about-catalunya/facts.html",
    "contact/index.html",
    "contact/house-rules.html",
]

LANGS = ["en", "es", "ca", "fr", "nl", "de"]
LABELS = {"en": "EN", "es": "ES", "ca": "CA", "fr": "FR", "nl": "NL", "de": "DE"}


def load_lookup():
    look = {}
    for _k, l in ish.UI.items():
        if l.get("de"):
            look[html.unescape(l["en"])] = l["de"]
    for en, de in cde.STRINGS_DE.items():
        look[html.unescape(en)] = de
    try:
        from de_standalone import STRINGS_DE_STANDALONE as extra
        for en, de in extra.items():
            look[html.unescape(en)] = de
    except Exception:
        pass
    return look


TEXT_RE = re.compile(r">([^<>]+)<")
ATTR_RE = re.compile(r'\b(alt|title|aria-label|placeholder)="([^"]+)"')
BLOCK_RE = re.compile(r"(<style[^>]*>.*?</style>|<script[^>]*>.*?</script>)", re.S)


def protect(text):
    blocks = []

    def repl(m):
        blocks.append(m.group(1))
        return f"\x00{len(blocks) - 1}\x00"
    return BLOCK_RE.sub(repl, text), blocks


def restore(text, blocks):
    for i, b in enumerate(blocks):
        text = text.replace(f"\x00{i}\x00", b)
    return text


def substitute(text, look):
    def sub_text(m):
        inner = m.group(1)
        key = html.unescape(inner.strip())
        de = look.get(key)
        if de is not None and de != key:
            lead = inner[: len(inner) - len(inner.lstrip())]
            trail = inner[len(inner.rstrip()):]
            return ">" + lead + de + trail + "<"
        return m.group(0)

    def sub_attr(m):
        attr, val = m.group(1), m.group(2)
        de = look.get(html.unescape(val.strip()))
        if de is not None and de != html.unescape(val.strip()):
            return f'{attr}="{de}"'
        return m.group(0)

    text = TEXT_RE.sub(sub_text, text)
    text = ATTR_RE.sub(sub_attr, text)
    return text


def fix_paths(text):
    # css/js/images relative refs move one level deeper.
    text = re.sub(r'(src|href)="((?:\.\./)*)(css/|js/|images/)',
                  r'\1="../\2\3', text)
    text = re.sub(r'url\(((?:\.\./)*)(images/)', r'url(../\1\2', text)
    return text


def switcher_html(logical):
    parts = []
    for i, l in enumerate(LANGS):
        if i:
            parts.append('<span class="lang-sep">|</span>')
        href = f"/{logical}" if l == "en" else f"/{l}/{logical}"
        cls = ' class="lang-active"' if l == "de" else ""
        parts.append(f'<a href="{href}"{cls}>{LABELS[l]}</a>')
    return f'<div class="lang-switcher">{"".join(parts)}</div>'


def meta_desc_de(text, look):
    m = re.search(r'<meta name="description" content="([^"]+)"', text)
    if m:
        de = look.get(html.unescape(m.group(1).strip()))
        if de:
            text = text.replace(m.group(0), f'<meta name="description" content="{de}">')
    return text


def title_de(text, look):
    m = re.search(r"<title>([^<]+)</title>", text)
    if m:
        de = look.get(html.unescape(m.group(1).strip()))
        if de:
            text = text.replace(m.group(0), f"<title>{de}</title>")
    return text


import posixpath

LINK_RE = re.compile(r'(href=")([^"#][^"]*?)(")')


def de_link_fallback(text, logical, de_exists):
    """Relative .html/dir links whose de target does not exist point to English."""
    page_dir = posixpath.dirname(logical)

    def swap(m):
        pre, href, post = m.groups()
        if href.startswith(("http://", "https://", "mailto:", "tel:", "data:",
                            "javascript:", "/", "#")):
            return m.group(0)
        path = href.split("?")[0].split("#")[0]
        suffix = href[len(path):]
        target = posixpath.normpath(posixpath.join(page_dir, path))
        if target.startswith(".."):
            return m.group(0)                       # shared root asset - leave
        if target in ("", "."):
            target = "index.html"
        if target.endswith("/"):
            target += "index.html"
        elif not target.endswith(".html"):
            target = target + "/index.html"
        if target in de_exists:
            return m.group(0)                       # de copy exists - keep
        return f'{pre}/{target}{suffix}{post}'      # fall back to English root

    return LINK_RE.sub(swap, text)


def build_one(logical, look, apply, de_exists):
    src = ROOT / logical
    text = src.read_text(encoding="utf-8")
    text = fix_paths(text)
    protected, blocks = protect(text)
    protected = substitute(protected, look)
    protected = title_de(protected, look)
    protected = meta_desc_de(protected, look)
    protected = protected.replace('<html lang="en">', '<html lang="de">', 1)
    protected = re.sub(r'<div class="lang-switcher">.*?</div>',
                       switcher_html(logical), protected, count=1, flags=re.S)
    out = restore(protected, blocks)
    out = de_link_fallback(out, logical, de_exists)
    dst = ROOT / "de" / logical
    if apply:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(out, encoding="utf-8")
    return dst


def de_existing_set():
    s = set(PAGES)
    de_root = ROOT / "de"
    if de_root.is_dir():
        for p in de_root.rglob("*.html"):
            s.add(p.relative_to(de_root).as_posix())
    return s


def main():
    apply = "--apply" in sys.argv
    look = load_lookup()
    de_exists = de_existing_set()
    for logical in PAGES:
        dst = build_one(logical, look, apply, de_exists)
        print(f"  {'wrote' if apply else 'would write'}: {dst.relative_to(ROOT).as_posix()}")
    print(f"\n{len(PAGES)} pages{'' if apply else '  (dry run)'} · lookup size {len(look)}")


if __name__ == "__main__":
    main()
