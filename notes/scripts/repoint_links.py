#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Repoint links on translated pages to same-language targets where they exist.

The hand-written translated pages link out to the English versions of pages
that had no translation at the time. Now that those translations exist, a
Spanish visitor clicking "Mercados Locales" should land on /es/things-to-do/
markets.html rather than being dropped back into English.

Only links that resolve to an English page with a same-language counterpart are
touched. Anything still English-only is left alone.

    python3 notes/scripts/repoint_links.py --apply
"""

import posixpath
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TRANSLATED = ["es", "ca", "fr", "nl"]
SKIP_DIRS = {"notes", ".github", ".git", ".well-known"}

LINK_RE = re.compile(r'(href=")([^"#?][^"]*?)(")')

# The language switcher deliberately links OUT of the current language - its
# "EN" entry must keep pointing at the English page. Rewriting it would make
# every language button lead back to the page you are already on.
SWITCHER_RE = re.compile(r'<div class="lang-switcher">.*?</div>', re.S)


def main():
    apply = "--apply" in sys.argv
    total = 0
    for lang in TRANSLATED:
        for path in sorted((ROOT / lang).rglob("*.html")):
            rel_dir = path.parent.relative_to(ROOT).as_posix()
            text = path.read_text(encoding="utf-8")
            hits = []

            def swap(m):
                nonlocal hits
                pre, href, post = m.groups()
                if href.startswith(("http://", "https://", "mailto:", "tel:",
                                    "data:", "javascript:", "/")):
                    return m.group(0)
                # where does this link land, relative to the site root?
                target = posixpath.normpath(posixpath.join(rel_dir, href))
                if target.startswith(".."):
                    return m.group(0)
                first = target.split("/")[0]
                if first in TRANSLATED or first in SKIP_DIRS:
                    return m.group(0)  # already language-local
                localised = f"{lang}/{target}"
                if not (ROOT / localised).is_file():
                    return m.group(0)  # no translation exists yet
                new_href = posixpath.relpath(localised, rel_dir)
                hits.append((href, new_href))
                return f"{pre}{new_href}{post}"

            # Mask the switcher out, rewrite everything else, then restore it.
            switchers = []

            def stash(m):
                switchers.append(m.group(0))
                return f"\x00SWITCHER{len(switchers) - 1}\x00"

            masked = SWITCHER_RE.sub(stash, text)
            new_text = LINK_RE.sub(swap, masked)
            for i, block in enumerate(switchers):
                new_text = new_text.replace(f"\x00SWITCHER{i}\x00", block)
            if hits:
                total += len(hits)
                print(f"  {'repointed' if apply else 'would repoint'} "
                      f"{path.relative_to(ROOT).as_posix()}: {len(hits)} links")
                if apply:
                    path.write_text(new_text, encoding="utf-8")
    print(f"\n{total} links {'repointed' if apply else 'to repoint'}"
          f"{'' if apply else '  (dry run - pass --apply)'}")


if __name__ == "__main__":
    main()
