#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
One-off: add a parking line (pin + cost) under each of the four markets, on the
full-content markets page — English HTML + the es/ca/fr/nl blocks in
content_things_to_do.py + the German block in de_pages.py.

Idempotent. Run once:  python3 notes/scripts/insert_markets_parking.py --apply
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from content_parking import inline_line  # noqa: E402

ROOT = HERE.parents[1]
MAPS = "https://www.google.com/maps/search/?api=1&query="
APPLY = "--apply" in sys.argv

# market order on the page: Palafrugell, Pals, Palamós, Begur
MARKETS = [
    ("town_free",      "Aparcament+Palafrugell"),
    ("village_summer", "Aparcament+de+Pals"),
    ("palamos",        "Palamos+aparcament+platja"),
    ("village_summer", "Aparcament+Begur"),
]
BLOCK = re.compile(r"<h3>🛒.*?</h3>\s*<p>.*?</p>", re.S)


def patch(text, langs):
    """langs: list giving the language of each successive group of 4 blocks."""
    if "parking-note" in text:
        return text, 0
    blocks = list(BLOCK.finditer(text))
    if len(blocks) != 4 * len(langs):
        raise SystemExit(f"expected {4*len(langs)} market blocks, found {len(blocks)}")
    # splice from the end so earlier offsets stay valid
    out = text
    for idx in range(len(blocks) - 1, -1, -1):
        m = blocks[idx]
        lang = langs[idx // 4]
        cost, q = MARKETS[idx % 4]
        line = "\n  " + inline_line(lang, cost, MAPS + q)
        out = out[:m.end()] + line + out[m.end():]
    return out, len(blocks)


def run(rel, langs):
    p = ROOT / rel
    text = p.read_text(encoding="utf-8")
    new, n = patch(text, langs)
    if new == text:
        print(f"  no change  {rel}")
        return
    if APPLY:
        p.write_text(new, encoding="utf-8")
    print(f"  {'wrote' if APPLY else 'would edit'}  {rel}  ({n} blocks)")


if __name__ == "__main__":
    run("things-to-do/markets.html", ["en"])
    run("notes/scripts/content_things_to_do.py", ["es", "ca", "fr", "nl"])
    run("notes/scripts/de_pages.py", ["de"])
    print("done" + ("" if APPLY else "  (dry run — pass --apply)"))
