#!/usr/bin/env python3
"""
Render the shell (head/nav/footer) around authored translated content and write
plain static HTML into the language folders.

Link resolution rule: a nav/footer link points at the same-language copy of a
page when that file exists on disk, and falls back to the English page when it
does not. So as more translations land, re-running this script upgrades the
links automatically instead of leaving dead ends.
"""

import posixpath
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from i18n_shell import LANG_LABELS, NAV, UI, t  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
TRANSLATED = ["es", "ca", "fr", "nl"]


def file_for(lang: str, logical: str) -> Path:
    return ROOT / logical if lang == "en" else ROOT / lang / logical


def exists(lang: str, logical: str) -> bool:
    return file_for(lang, logical).is_file()


def site_path(lang: str, logical: str) -> str:
    """Path relative to the site root, e.g. 'es/getting-here/index.html'."""
    return logical if lang == "en" else f"{lang}/{logical}"


def rel(from_logical: str, lang: str, to_logical: str, to_lang: str) -> str:
    """Relative href from one page to another, crossing language folders if needed."""
    src_dir = posixpath.dirname(site_path(lang, from_logical)) or "."
    dst = site_path(to_lang, to_logical)
    return posixpath.relpath(dst, src_dir)


def link(from_logical: str, lang: str, to_logical: str) -> tuple[str, bool]:
    """Resolve a link, preferring the same language, falling back to English."""
    if exists(lang, to_logical):
        return rel(from_logical, lang, to_logical, lang), True
    return rel(from_logical, lang, to_logical, "en"), False


def asset(from_logical: str, lang: str, path: str) -> str:
    src_dir = posixpath.dirname(site_path(lang, from_logical)) or "."
    return posixpath.relpath(path, src_dir)


REL_URL_RE = re.compile(r'\b(href|src)="(?!https?:|/|#|mailto:|tel:|data:|javascript:)([^"]+)"')


def rebase(content: str, logical: str, lang: str) -> str:
    """
    Fix relative links in content carried over from the English page.

    The English page sits one directory deep (things-to-do/x.html) while its
    translation sits two (nl/things-to-do/x.html), so an inherited "../images/"
    would resolve to nl/images/ and 404. Each relative URL is resolved back to a
    site-root path and re-expressed from the translated page's location,
    preferring a same-language target where one exists.
    """
    src_dir = posixpath.dirname(logical) or "."
    dst_dir = posixpath.dirname(site_path(lang, logical)) or "."

    def fix(m):
        attr, url = m.group(1), m.group(2)
        frag = ""
        if "#" in url:
            url, frag = url.split("#", 1)
            frag = "#" + frag
        if not url:
            return m.group(0)
        target = posixpath.normpath(posixpath.join(src_dir, url))
        if target.startswith(".."):
            return m.group(0)
        localised = f"{lang}/{target}"
        if (ROOT / localised).is_file():
            target = localised
        new = posixpath.relpath(target, dst_dir)
        return f'{attr}="{new}{frag}"'

    return REL_URL_RE.sub(fix, content)


def build_nav(from_logical: str, lang: str) -> str:
    home, _ = link(from_logical, lang, "index.html")
    out = ['<nav>']
    out.append(f'  <a href="{home}" class="nav-logo">Tamariu <span>Chalet</span></a>')
    out.append('  <ul class="nav-menu">')
    for group_key, _, items in NAV:
        lis = []
        for label_key, logical in items:
            href, _ = link(from_logical, lang, logical)
            lis.append(f'<li><a href="{href}">{t(label_key, lang)}</a></li>')
        out.append(
            f'    <li><a href="#">{t(group_key, lang)} <span class="arrow">▾</span></a>'
            f'<ul class="dropdown">{"".join(lis)}</ul></li>'
        )
    contact, _ = link(from_logical, lang, "contact/index.html")
    out.append(f'    <li><a href="{contact}">{t("nav_contact", lang)}</a></li>')
    out.append('  </ul>')
    out.append(build_lang_switcher(from_logical, lang))
    out.append(
        f'  <button class="hamburger" aria-label="{t("menu", lang)}">'
        '<span></span><span></span><span></span></button>'
    )
    out.append('</nav>')
    return "\n".join(out)


def build_lang_switcher(from_logical: str, lang: str) -> str:
    """Only offer languages whose version of THIS page actually exists."""
    available = [l for l in ["en"] + TRANSLATED if exists(l, from_logical)]
    if lang not in available:
        available.append(lang)  # the page being generated right now
        available = [l for l in ["en"] + TRANSLATED if l in available]
    if len(available) < 2:
        return '  <div class="lang-switcher"></div>'
    parts = []
    for i, l in enumerate(available):
        if i:
            parts.append('<span class="lang-sep">|</span>')
        href = rel(from_logical, lang, from_logical, l)
        cls = ' class="lang-active"' if l == lang else ""
        parts.append(f'<a href="{href}"{cls}>{LANG_LABELS[l]}</a>')
    return f'  <div class="lang-switcher">{"".join(parts)}</div>'


def build_footer(from_logical: str, lang: str, cols: list) -> str:
    """cols: list of (heading_key, [(label_key, logical), ...])."""
    out = ['<footer>', '  <div class="footer-grid">']
    out.append(
        '    <div class="footer-brand"><div class="brand-name">Tamariu Chalet</div>'
        f'<p>{t("footer_blurb", lang)}</p></div>'
    )
    for heading_key, items in cols:
        lis = []
        for label_key, logical in items:
            href, _ = link(from_logical, lang, logical)
            lis.append(f'<li><a href="{href}">{t(label_key, lang)}</a></li>')
        out.append(
            f'    <div class="footer-col"><h4>{t(heading_key, lang)}</h4>'
            f'<ul>{"".join(lis)}</ul></div>'
        )
    out.append('  </div>')
    out.append(
        '  <div class="footer-bottom"><p>&copy; 2025 Tamariu Chalet</p>'
        '<p>Tamariu, Costa Brava, Catalunya</p></div>'
    )
    out.append('</footer>')
    return "\n".join(out)


STYLESHEET_RE = re.compile(r'[ \t]*<link rel="stylesheet"[^>]*>\n?')
STYLE_RE = re.compile(r"[ \t]*<style>.*?</style>\n?", re.S)
SCRIPT_SRC_RE = re.compile(r'[ \t]*<script[^>]*src="([^"]*)"[^>]*>\s*</script>\n?')
INLINE_SCRIPT_RE = re.compile(r"[ \t]*<script>.*?</script>\n?", re.S)


def extract_extras(logical: str, lang: str) -> tuple[str, str]:
    """
    Carry per-page CSS and JS over from the English source.

    Page-specific <style> blocks and inline <script> blocks are copied rather
    than duplicated into the content modules, so a styling fix on the English
    page automatically reaches all five languages on the next build.
    """
    src = ROOT / logical
    if not src.is_file():
        return "", ""
    text = src.read_text(encoding="utf-8")
    head_html = text.split("</head>")[0]

    head_bits = []
    for m in STYLESHEET_RE.finditer(head_html):
        tag = m.group(0)
        if "css/style.css" in tag:
            continue  # emitted by the main template
        if 'href="http' in tag:
            head_bits.append(tag.rstrip("\n"))
        else:
            href = re.search(r'href="([^"]*)"', tag).group(1)
            fixed = asset(logical, lang, posixpath.normpath(
                posixpath.join(posixpath.dirname(logical), href)))
            head_bits.append(tag.replace(f'href="{href}"', f'href="{fixed}"').rstrip("\n"))
    for m in STYLE_RE.finditer(head_html):
        head_bits.append(m.group(0).rstrip("\n"))

    body_html = text.split("</head>", 1)[-1]
    body_bits = []
    for m in SCRIPT_SRC_RE.finditer(body_html):
        srcpath = m.group(1)
        if srcpath.endswith("js/main.js"):
            continue  # emitted by the main template
        if srcpath.startswith("http"):
            body_bits.append(m.group(0).rstrip("\n"))
        else:
            fixed = asset(logical, lang, posixpath.normpath(
                posixpath.join(posixpath.dirname(logical), srcpath)))
            body_bits.append(m.group(0).replace(f'src="{srcpath}"',
                                                f'src="{fixed}"').rstrip("\n"))
    for m in INLINE_SCRIPT_RE.finditer(body_html):
        body_bits.append(m.group(0).rstrip("\n"))

    return "\n".join(head_bits), "\n".join(body_bits)


HEAD = """<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow">
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="https://tamariuchalet.com/images/shared/tamariu.jpg">
  <meta property="og:site_name" content="Tamariu Chalet">
  <meta property="og:locale" content="{locale}">
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="https://tamariuchalet.com/images/shared/tamariu.jpg">
  <title>{title}</title>
  <!-- Favicon -->
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#1A3A5C">

  <link rel="stylesheet" href="{css}">
{extra_head}</head>
<body>"""

LOCALES = {"en": "en_GB", "es": "es_ES", "ca": "ca_ES", "fr": "fr_FR", "nl": "nl_NL"}


def url_for(lang: str, logical: str) -> str:
    p = "" if logical == "index.html" else logical
    if p.endswith("/index.html"):
        p = p[: -len("index.html")]
    prefix = "" if lang == "en" else f"/{lang}"
    return f"https://tamariuchalet.com{prefix}/{p}"


def render(logical: str, lang: str, title: str, desc: str, content: str,
           footer_cols: list, script_strings: dict | None = None) -> str:
    extra_head, extra_body = extract_extras(logical, lang)
    if extra_head:
        extra_head += "\n"
    # Translate user-facing string literals inside carried-over inline scripts
    # (map popups, button labels and the like).
    for src, dst in (script_strings or {}).items():
        extra_body = extra_body.replace(src, dst)

    head = HEAD.format(
        lang=lang, title=title, desc=desc, url=url_for(lang, logical),
        locale=LOCALES[lang], css=asset(logical, lang, "css/style.css"),
        extra_head=extra_head,
    )
    parts = [
        head,
        build_nav(logical, lang),
        content.strip(),
        build_footer(logical, lang, footer_cols),
        f'<script src="{asset(logical, lang, "js/main.js")}"></script>',
    ]
    if extra_body:
        parts.append(extra_body)
    parts += ["</body>", "</html>", ""]
    return "\n".join(parts)


def write(logical: str, lang: str, **kw) -> Path:
    path = file_for(lang, logical)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render(logical, lang, **kw), encoding="utf-8")
    return path
