#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sync the English pages' top navigation from the single source of truth
(i18n_shell.py:NAV), the same table the translated pages are built from.

Only the <ul class="nav-menu"> … </ul> block is replaced. Each page's own
language switcher, hero, body and footer are left exactly as they are, so the
diff is limited to the menu items themselves.

    python3 notes/scripts/sync_en_nav.py           # dry run (lists changes)
    python3 notes/scripts/sync_en_nav.py --apply   # write files
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import build_pages as bp  # noqa: E402
import i18n_shell  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
TRANSLATED_DIRS = {"es", "ca", "fr", "nl", "de"}

# The nav-menu UL can contain nested <ul class="dropdown">…</ul>, so match up to
# the </ul> that is immediately followed by the switcher or hamburger button.
MENU_RE = re.compile(
    r'<ul class="nav-menu">.*?</ul>\s*(?=<div class="lang-switcher"|<button class="hamburger")',
    re.S,
)
# The "?" help link lives after the language switcher.
NAVHELP_RE = re.compile(r'\s*<a[^>]*class="nav-help".*?</a>', re.S)
SWITCHER_RE = re.compile(r'(<div class="lang-switcher">.*?</div>)', re.S)


def help_html(logical: str) -> str:
    # "?" opens the version/About modal (wired in js/main.js); href is just a hook.
    return '  <a href="#" class="nav-help" aria-label="About" title="About">?</a>'


def place_help(html: str, logical: str) -> str:
    """Drop any existing nav-help link and add a fresh one after the switcher."""
    html = NAVHELP_RE.sub("", html)
    return SWITCHER_RE.sub(
        lambda m: m.group(1) + "\n" + help_html(logical), html, count=1)


def english_pages():
    for p in ROOT.rglob("*.html"):
        rel = p.relative_to(ROOT)
        parts = rel.parts
        if parts[0] in TRANSLATED_DIRS or parts[0] == "notes":
            continue
        yield p, "/".join(parts)


def menu_html(logical: str) -> str:
    """Extract just the <ul class="nav-menu">…</ul> block from build_nav()."""
    nav = bp.build_nav(logical, "en")
    m = MENU_RE.search(nav)
    if not m:
        raise RuntimeError(f"could not extract nav-menu for {logical}")
    return m.group(0)


def main(apply: bool) -> int:
    changed = skipped = 0
    for path, logical in sorted(english_pages(), key=lambda t: t[1]):
        html = path.read_text(encoding="utf-8")
        if '<ul class="nav-menu">' not in html:
            skipped += 1
            continue
        new_menu = menu_html(logical)
        new_html, n = MENU_RE.subn(lambda _: new_menu, html, count=1)
        if n:
            new_html = place_help(new_html, logical)
        if n and new_html != html:
            changed += 1
            print(f"  update  {logical}")
            if apply:
                path.write_text(new_html, encoding="utf-8")
    print(f"\n{changed} pages updated, {skipped} skipped"
          f"{' (dry run)' if not apply else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
