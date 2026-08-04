#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sync the footer from the single source of truth (i18n_shell.py:FOOTER) on every
page that the translation build does NOT regenerate:

  * all English pages, and
  * the es/ca/fr/nl copies of the hand-authored standalone pages
    (homepage, rooms, about-catalunya, contact).

Module-authored translated pages get their footer from build_translations.py,
and the German standalone pages from build_de_standalone.py, so those are left
alone here. Only the <footer> … </footer> block is replaced.

Run after editing FOOTER/UI and before build_de_standalone.py.

    python3 notes/scripts/sync_en_footer.py           # dry run
    python3 notes/scripts/sync_en_footer.py --apply   # write files
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import build_pages as bp        # noqa: E402
import i18n_shell               # noqa: E402
import build_de_standalone as bds  # noqa: E402  (STANDALONE page list)

ROOT = Path(__file__).resolve().parents[2]
TRANSLATED_DIRS = {"es", "ca", "fr", "nl", "de"}
STANDALONE_LANGS = ["es", "ca", "fr", "nl"]   # de handled by build_de_standalone
FOOTER_RE = re.compile(r"<footer>.*?</footer>", re.S)


def targets():
    # English pages (everything outside the language dirs and notes/).
    for p in ROOT.rglob("*.html"):
        parts = p.relative_to(ROOT).parts
        if parts[0] in TRANSLATED_DIRS or parts[0] == "notes":
            continue
        yield p, "/".join(parts), "en"
    # Translated copies of the standalone pages.
    for lang in STANDALONE_LANGS:
        for logical in bds.PAGES:
            p = ROOT / lang / logical
            if p.is_file():
                yield p, logical, lang


def main(apply: bool) -> int:
    changed = skipped = 0
    for path, logical, lang in sorted(targets(), key=lambda t: (t[2], t[1])):
        html = path.read_text(encoding="utf-8")
        if "<footer>" not in html:
            skipped += 1
            continue
        new_footer = bp.build_footer(logical, lang, i18n_shell.FOOTER)
        new_html, n = FOOTER_RE.subn(lambda _: new_footer, html, count=1)
        if n and new_html != html:
            changed += 1
            print(f"  update  {lang}/{logical}")
            if apply:
                path.write_text(new_html, encoding="utf-8")
    print(f"\n{changed} footers updated, {skipped} skipped"
          f"{' (dry run)' if not apply else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
