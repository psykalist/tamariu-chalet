#!/usr/bin/env python3
"""
Normalise canonical + hreflang across the Tamariu Chalet site.

Rules applied:
  * Every page gets exactly one <link rel="canonical"> pointing at its own URL.
  * hreflang alternates are emitted ONLY for languages where the file really
    exists on disk. Pointing hreflang at a 404 is worse than omitting it.
  * x-default always points at the English version.
  * index.html pages use directory-form URLs (/contact/) consistently in BOTH
    canonical and hreflang. The site previously mixed the two, which makes a
    page's canonical disagree with its own self-referencing hreflang.
  * A page with no translations gets canonical only - no hreflang block.

Run from the site root. Idempotent.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = "https://tamariuchalet.com"
LANGS = ["en", "es", "ca", "fr", "nl"]
TRANSLATED = ["es", "ca", "fr", "nl"]

# Directories that are not part of the deployed site
SKIP_DIRS = {"notes", ".github", ".git", ".well-known"}

# availability/ is a single URL that self-translates via ?lang=; it must not
# claim per-language alternates because those URLs do not exist as pages.
SINGLE_URL_PAGES = {"availability/index.html"}


def logical_path(path: Path) -> str:
    """Path of the page relative to its language root, e.g. 'contact/index.html'."""
    rel = path.relative_to(ROOT).as_posix()
    parts = rel.split("/")
    if parts[0] in TRANSLATED:
        return "/".join(parts[1:])
    return rel


def page_lang(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    first = rel.split("/")[0]
    return first if first in TRANSLATED else "en"


def url_for(lang: str, logical: str) -> str:
    """Build the canonical URL, collapsing index.html to directory form."""
    p = logical
    if p == "index.html":
        p = ""
    elif p.endswith("/index.html"):
        p = p[: -len("index.html")]
    prefix = "" if lang == "en" else f"/{lang}"
    return f"{BASE}{prefix}/{p}"


def file_for(lang: str, logical: str) -> Path:
    return ROOT / logical if lang == "en" else ROOT / lang / logical


def site_pages():
    for p in sorted(ROOT.rglob("*.html")):
        rel_parts = p.relative_to(ROOT).parts
        if rel_parts[0] in SKIP_DIRS:
            continue
        yield p


CANON_RE = re.compile(r'[ \t]*<link rel="canonical"[^>]*>\n?')
ALT_RE = re.compile(r'[ \t]*<link rel="alternate" hreflang="[^"]*"[^>]*>\n?')
# Anchor: insert the block straight after the robots meta, else after viewport.
ROBOTS_RE = re.compile(r'([ \t]*<meta name="robots"[^>]*>\n)')
VIEWPORT_RE = re.compile(r'([ \t]*<meta name="viewport"[^>]*>\n)')


def build_block(lang: str, logical: str, available: list[str]) -> str:
    lines = [f'  <link rel="canonical" href="{url_for(lang, logical)}">']
    if len(available) > 1:
        for l in LANGS:
            if l in available:
                lines.append(
                    f'  <link rel="alternate" hreflang="{l}" href="{url_for(l, logical)}">'
                )
        if "en" in available:
            lines.append(
                f'  <link rel="alternate" hreflang="x-default" href="{url_for("en", logical)}">'
            )
    return "\n".join(lines) + "\n"


def process(path: Path, apply: bool) -> tuple[str, int]:
    text = path.read_text(encoding="utf-8")
    original = text
    logical = logical_path(path)
    lang = page_lang(path)

    if logical in SINGLE_URL_PAGES:
        available = ["en"]
    else:
        available = [l for l in LANGS if file_for(l, logical).is_file()]

    block = build_block(lang, logical, available)

    text = CANON_RE.sub("", text)
    text = ALT_RE.sub("", text)

    if ROBOTS_RE.search(text):
        text = ROBOTS_RE.sub(lambda m: m.group(1) + block, text, count=1)
    elif VIEWPORT_RE.search(text):
        text = VIEWPORT_RE.sub(lambda m: m.group(1) + block, text, count=1)
    else:
        print(f"  !! no anchor found, skipped: {path.relative_to(ROOT)}")
        return "skip", 0

    n_alt = len(available) if len(available) > 1 else 0
    if text != original:
        if apply:
            path.write_text(text, encoding="utf-8")
        return "changed", n_alt
    return "same", n_alt


def main():
    apply = "--apply" in sys.argv
    changed = same = 0
    for p in site_pages():
        status, n = process(p, apply)
        if status == "changed":
            changed += 1
            rel = p.relative_to(ROOT).as_posix()
            print(f"  {'wrote' if apply else 'would fix'}: {rel}  ({n or 'no'} alternates)")
        elif status == "same":
            same += 1
    print(f"\n{changed} changed, {same} already correct."
          f"{'' if apply else '  (dry run - pass --apply to write)'}")


if __name__ == "__main__":
    main()
