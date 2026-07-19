#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Site integrity check: broken internal links, broken images, hreflang
reciprocity, canonical agreement, and sitemap coverage.

    python3 notes/scripts/check_site.py
"""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[2]
BASE = "https://tamariuchalet.com"
SKIP_DIRS = {"notes", ".github", ".git", ".well-known"}

HREF_RE = re.compile(r'(?:href|src)="([^"]+)"')
CANON_RE = re.compile(r'<link rel="canonical" href="([^"]+)"')
ALT_RE = re.compile(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"')

errors = []
warnings = []


def pages():
    for p in sorted(ROOT.rglob("*.html")):
        if p.relative_to(ROOT).parts[0] in SKIP_DIRS:
            continue
        yield p


def url_to_file(url: str) -> Path | None:
    """Map a site URL back to the file that serves it."""
    path = url[len(BASE):] if url.startswith(BASE) else url
    path = path.split("#")[0].split("?")[0]
    if path.endswith("/"):
        path += "index.html"
    return ROOT / path.lstrip("/")


# ── internal links and assets ────────────────────────────────────────────────
for page in pages():
    rel_page = page.relative_to(ROOT).as_posix()
    text = page.read_text(encoding="utf-8")
    for raw in HREF_RE.findall(text):
        href = raw.strip()
        if (not href or href.startswith(("http://", "https://", "mailto:", "tel:",
                                         "#", "data:", "javascript:"))):
            continue
        # Cloudflare rewrites mailto: links into /cdn-cgi/l/email-protection
        # stubs that are resolved at the edge, so they have no file on disk.
        if href.startswith("/cdn-cgi/"):
            continue
        target = href.split("#")[0].split("?")[0]
        if not target:
            continue
        target = unquote(target)
        if target.startswith("/"):
            resolved = ROOT / target.lstrip("/")
        else:
            resolved = (page.parent / target).resolve()
        if target.endswith("/"):
            resolved = resolved / "index.html"
        if not resolved.exists():
            try:
                shown = resolved.relative_to(ROOT).as_posix()
            except ValueError:
                shown = str(resolved)
            errors.append(f"broken link  {rel_page}  ->  {href}   (missing {shown})")

# ── hreflang reciprocity + canonical agreement ───────────────────────────────
alt_map = {}
for page in pages():
    rel_page = page.relative_to(ROOT).as_posix()
    text = page.read_text(encoding="utf-8")

    canons = CANON_RE.findall(text)
    if len(canons) != 1:
        errors.append(f"canonical  {rel_page}  has {len(canons)} canonical tags")
        continue
    canon = canons[0]

    alts = ALT_RE.findall(text)
    alt_map[rel_page] = (canon, alts)

    # every alternate must point at a file that exists
    for lang, url in alts:
        f = url_to_file(url)
        if f is None or not f.exists():
            errors.append(f"hreflang   {rel_page}  ->  {lang}: {url}  (no such page)")

    # self-reference: a page carrying alternates must list itself
    if alts:
        selfs = [u for l, u in alts if l != "x-default" and url_to_file(u) == page]
        if not selfs:
            errors.append(f"hreflang   {rel_page}  has alternates but no self-reference")
        elif selfs[0] != canon:
            errors.append(
                f"canonical  {rel_page}  canonical={canon} disagrees with "
                f"self hreflang={selfs[0]}"
            )

# reciprocity: if A lists B, B must list A
for rel_page, (canon, alts) in alt_map.items():
    for lang, url in alts:
        if lang == "x-default":
            continue
        f = url_to_file(url)
        if f is None or not f.exists():
            continue
        other = f.relative_to(ROOT).as_posix()
        if other == rel_page:
            continue
        if other not in alt_map:
            errors.append(f"reciprocity {rel_page} -> {other}  (target has no tags)")
            continue
        back = {url_to_file(u) for l, u in alt_map[other][1] if l != "x-default"}
        if page_path := (ROOT / rel_page):
            if page_path not in back:
                errors.append(f"reciprocity {rel_page} -> {other}  (no link back)")

# ── sitemap coverage ─────────────────────────────────────────────────────────
sitemap = ROOT / "sitemap.xml"
if sitemap.exists():
    sm = sitemap.read_text(encoding="utf-8")
    locs = re.findall(r"<loc>([^<]+)</loc>", sm)
    for loc in locs:
        f = url_to_file(loc)
        if f is None or not f.exists():
            errors.append(f"sitemap    {loc}  (no such page)")
    indexed = {url_to_file(l) for l in locs}
    for page in pages():
        text = page.read_text(encoding="utf-8")
        if 'name="robots" content="noindex' in text:
            continue
        if page not in indexed:
            warnings.append(f"not in sitemap  {page.relative_to(ROOT).as_posix()}")

# ── report ───────────────────────────────────────────────────────────────────
for e in errors:
    print(f"ERROR  {e}")
for w in warnings:
    print(f"WARN   {w}")
print(f"\n{len(list(pages()))} pages checked · {len(errors)} errors · {len(warnings)} warnings")
sys.exit(1 if errors else 0)
