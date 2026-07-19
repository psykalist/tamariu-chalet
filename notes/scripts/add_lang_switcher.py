#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add the language switcher to English pages that have translations but no way
to reach them.

Fourteen English pages carried translations that a visitor could only find by
editing the URL. The switcher is injected in the same place and same shape the
hand-written pages already use (root-absolute hrefs, immediately before the
hamburger button), and lists only languages whose copy of that page exists.

    python3 notes/scripts/add_lang_switcher.py --apply
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LANGS = ["en", "es", "ca", "fr", "nl"]
LABELS = {"en": "EN", "es": "ES", "ca": "CA", "fr": "FR", "nl": "NL"}
TRANSLATED = ["es", "ca", "fr", "nl"]
SKIP_DIRS = {"notes", ".github", ".git", ".well-known"}

HAMBURGER_RE = re.compile(r'([ \t]*)(<button class="hamburger")')


def logical(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    parts = rel.split("/")
    return "/".join(parts[1:]) if parts[0] in TRANSLATED else rel


def lang_of(path: Path) -> str:
    first = path.relative_to(ROOT).parts[0]
    return first if first in TRANSLATED else "en"


def url_path(lang: str, log: str) -> str:
    prefix = "" if lang == "en" else f"/{lang}"
    return f"{prefix}/{log}"


def file_for(lang: str, log: str) -> Path:
    return ROOT / log if lang == "en" else ROOT / lang / log


def switcher(lang: str, log: str) -> str:
    available = [l for l in LANGS if file_for(l, log).is_file()]
    if len(available) < 2:
        return ""
    parts = []
    for i, l in enumerate(available):
        if i:
            parts.append('<span class="lang-sep">|</span>')
        cls = ' class="lang-active"' if l == lang else ""
        parts.append(f'<a href="{url_path(l, log)}"{cls}>{LABELS[l]}</a>')
    return f'<div class="lang-switcher">{"".join(parts)}</div>'


def main():
    apply = "--apply" in sys.argv
    changed = 0
    for path in sorted(ROOT.rglob("*.html")):
        if path.relative_to(ROOT).parts[0] in SKIP_DIRS:
            continue
        text = path.read_text(encoding="utf-8")
        if "lang-switcher" in text:
            continue
        log, lang = logical(path), lang_of(path)
        sw = switcher(lang, log)
        if not sw:
            continue
        m = HAMBURGER_RE.search(text)
        if not m:
            print(f"  !! no hamburger anchor, skipped: {path.relative_to(ROOT).as_posix()}")
            continue
        indent = m.group(1)
        text = HAMBURGER_RE.sub(lambda mm: f"{indent}{sw}\n{mm.group(1)}{mm.group(2)}",
                                text, count=1)
        changed += 1
        print(f"  {'added' if apply else 'would add'}: {path.relative_to(ROOT).as_posix()}")
        if apply:
            path.write_text(text, encoding="utf-8")
    print(f"\n{changed} pages{'' if apply else '  (dry run - pass --apply)'}")


if __name__ == "__main__":
    main()
