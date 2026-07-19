#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the translated pages.

    python3 notes/scripts/build_translations.py          # dry run
    python3 notes/scripts/build_translations.py --apply  # write files

Two passes are run when applying: the first creates the files, the second
re-renders them now that the targets exist, so nav links and language
switchers upgrade from English fallbacks to the real translated pages.
Afterwards run fix_hreflang.py --apply to refresh the tag blocks.
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import build_pages as bp  # noqa: E402
import strings_mode  # noqa: E402
import content_getting_here as c_gh  # noqa: E402
import content_getting_here_index as c_ghi  # noqa: E402
import content_things_to_do as c_ttd  # noqa: E402
import content_tourist_water as c_tw  # noqa: E402
import content_guides as c_guides  # noqa: E402
import content_girona as c_girona  # noqa: E402
import content_restaurants as c_rest  # noqa: E402
import content_reviews as c_rev  # noqa: E402
import content_beaches as c_beach  # noqa: E402

TRANSLATED = ["es", "ca", "fr", "nl"]

ALL_PAGES = {}
for mod in (c_gh, c_ghi, c_ttd, c_tw, c_guides, c_girona, c_rest, c_rev, c_beach):
    ALL_PAGES.update(mod.PAGES)

# Placeholders inside authored content that must resolve to real, existing pages.
PLACEHOLDERS = {
    "contact": "contact/index.html",
    "julivia": "getting-here/julivia-bus.html",
    "begur": "getting-here/begur-bus.html",
    "double": "accommodation/double-room.html",
    "twin1": "accommodation/twin-room-1.html",
    "twin2": "accommodation/twin-room-2.html",
}


def resolve(content: str, logical: str, lang: str) -> str:
    for name, target in PLACEHOLDERS.items():
        token = "{" + name + "}"
        if token in content:
            href, _ = bp.link(logical, lang, target)
            content = content.replace(token, href)
    return content


def build(apply: bool) -> list:
    written = []
    for logical, page in sorted(ALL_PAGES.items()):
        footer = page["footer"]

        if page.get("mode") == "strings":
            # Structured pages: English markup is the source, only words differ.
            english = strings_mode.content_of(logical)
            table = page["strings"]
            for lang in TRANSLATED:
                meta = page["meta"][lang]
                content = strings_mode.apply(english, table, lang)
                content = bp.rebase(content, logical, lang)
                content = resolve(content, logical, lang)
                if apply:
                    bp.write(logical, lang, title=meta["title"], desc=meta["desc"],
                             content=content, footer_cols=footer,
                             script_strings=_script_strings(table, lang,
                                                            page.get("script_only", {})))
                written.append(bp.file_for(lang, logical))
            continue

        for lang in TRANSLATED:
            if lang not in page:
                continue
            data = page[lang]
            content = resolve(data["content"], logical, lang)
            target = bp.file_for(lang, logical)
            if apply:
                bp.write(logical, lang, title=data["title"], desc=data["desc"],
                         content=content, footer_cols=footer,
                         script_strings=data.get("script_strings"))
            written.append(target)
    return written


def _script_strings(table: dict, lang: str, script_only: dict) -> dict:
    """String literals to translate inside carried-over inline scripts."""
    out = {}
    for en, langs in list(table.items()) + list(script_only.items()):
        dst = langs.get(lang)
        if dst and dst != en:
            out[f'"{en}"'] = f'"{dst}"'
            out[f"'{en}'"] = f"'{dst}'"
    return out


def main():
    apply = "--apply" in sys.argv
    if not apply:
        pages = build(False)
        for p in pages:
            print(f"  would write: {p.relative_to(bp.ROOT).as_posix()}")
        print(f"\n{len(pages)} files (dry run - pass --apply to write)")
        return

    # Pass 1 creates the files; pass 2 re-renders so cross-links between the
    # newly created translations resolve to each other rather than to English.
    build(True)
    pages = build(True)
    for p in pages:
        print(f"  wrote: {p.relative_to(bp.ROOT).as_posix()}")
    print(f"\n{len(pages)} files written.")


if __name__ == "__main__":
    main()
