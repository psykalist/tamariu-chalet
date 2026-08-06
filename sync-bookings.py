#!/usr/bin/env python3
"""
sync-bookings.py — Tamariu Chalet availability sync (hardened)
==============================================================
Fetches iCal feeds from Airbnb (and/or Google Calendar) and rewrites
js/bookings.js so the availability calendar shows correct dates.

DESIGN — WHY THIS IS SAFE
-------------------------
The whole point of this script is that it can NEVER silently wipe your
live availability. The rules it follows:

  1. If a configured feed fails to fetch or returns something that is not
     a valid iCal file, the script does NOT rewrite bookings.js at all —
     it keeps the last-known-good file and exits with a non-zero status so
     the GitHub Action goes red and emails you. Nothing gets deployed.
  2. A room whose URL is temporarily missing keeps its previous bookings
     rather than being blanked.
  3. If NO live feed synced at all (e.g. every secret vanished), that is
     treated as a failure — the calendar is never replaced with an empty one.
  4. The file is only rewritten when the availability actually changed, so
     no-op hourly runs create no commits and no re-uploads.

MANUAL / DIRECT BOOKINGS
------------------------
Do NOT hand-edit the arrays in js/bookings.js — a sync will overwrite them.
Add direct/phone reservations to MANUAL_BOOKINGS below; they are merged into
every sync and always survive.

RUNNING LOCALLY
---------------
1. Set the AIRBNB_* environment variables (or paste URLs into ICAL_SOURCES).
2. Run:  python3 sync-bookings.py
3. Upload js/bookings.js — or just let the GitHub Action do it.

RUNNING VIA GITHUB ACTIONS (automated, hourly)
----------------------------------------------
URLs come from repository secrets so they stay out of the code:
  AIRBNB_DOUBLE_ROOM · AIRBNB_TWIN_1 · AIRBNB_TWIN_2 · AIRBNB_APARTMENT
  GOOGLE_CALENDAR (optional)

FIND YOUR AIRBNB ICAL URLS
--------------------------
Airbnb host dashboard → Calendar → Availability settings → Export calendar
→ copy the .ics link (one per listing).
"""

import sys
import time
import re
import os
import urllib.request
import urllib.error
from datetime import date, timedelta, datetime

# ── CONFIGURATION ────────────────────────────────────────────
SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
# BOOKINGS_JS_PATH env override exists only to make automated testing easy.
BOOKINGS_JS  = os.environ.get('BOOKINGS_JS_PATH') or os.path.join(SCRIPT_DIR, 'js', 'bookings.js')

HORIZON_DAYS         = 365   # how many days ahead to include
FETCH_TIMEOUT        = 20    # seconds per attempt
FETCH_RETRIES        = 3     # attempts per source before giving up
RETRY_BACKOFF        = 4     # base seconds between retries (grows each attempt)
REQUIRE_AT_LEAST_ONE = True  # fail if zero live feeds were successfully synced

ALL_KEYS = ['double-room', 'twin-room-1', 'twin-room-2', 'studio-apartment']


def _url(env_var, fallback=''):
    """Return env var value if set and non-empty, otherwise the fallback."""
    return os.environ.get(env_var, '').strip() or fallback


# ── ICAL SOURCES ─────────────────────────────────────────────
# room_key must match the values used by the availability calendar.
# room_key = None means the feed blocks ALL rooms (e.g. a whole-house calendar).
ICAL_SOURCES = [
    {'label': 'Airbnb — Double Room',      'room_key': 'double-room',      'url': _url('AIRBNB_DOUBLE_ROOM', '')},
    {'label': 'Airbnb — Twin Room 1',      'room_key': 'twin-room-1',      'url': _url('AIRBNB_TWIN_1', '')},
    {'label': 'Airbnb — Twin Room 2',      'room_key': 'twin-room-2',      'url': _url('AIRBNB_TWIN_2', '')},
    {'label': 'Airbnb — Studio Apartment', 'room_key': 'studio-apartment', 'url': _url('AIRBNB_APARTMENT', '')},
    # {'label': 'Google Calendar', 'room_key': None, 'url': _url('GOOGLE_CALENDAR', '')},
]

# ── MANUAL BOOKINGS ──────────────────────────────────────────
# Direct/phone reservations that are NOT in Airbnb. Always merged in and
# preserved across every sync. Same format as the generated arrays.
MANUAL_BOOKINGS = {
    # 'double-room': [
    #     {'from': '2026-12-24', 'to': '2026-12-28', 'note': 'Direct booking'},
    # ],
}


# ── iCAL FETCH + PARSE ───────────────────────────────────────

def fetch_ical(url):
    """Fetch a URL with retries. Raises on repeated failure or non-iCal content."""
    last_err = None
    for attempt in range(1, FETCH_RETRIES + 1):
        try:
            req = urllib.request.Request(
                url, headers={'User-Agent': 'TamariuChalet-Sync/2.0'})
            with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as resp:
                text = resp.read().decode('utf-8', errors='replace')
            if 'BEGIN:VCALENDAR' not in text:
                raise ValueError('response is not a valid iCal feed (no BEGIN:VCALENDAR)')
            return text
        except Exception as e:  # noqa: BLE001 — retry on anything transient
            last_err = e
            if attempt < FETCH_RETRIES:
                wait = RETRY_BACKOFF * attempt
                print(f'\n      attempt {attempt}/{FETCH_RETRIES} failed ({e}); retrying in {wait}s ...',
                      end=' ', flush=True)
                time.sleep(wait)
    raise last_err


def _unfold(text):
    """Undo RFC-5545 line folding (a CRLF followed by a space or tab)."""
    return re.sub(r'\r?\n[ \t]', '', text)


def parse_ical_events(text):
    events = []
    today  = date.today()
    cutoff = today + timedelta(days=HORIZON_DAYS)
    for block in re.findall(r'BEGIN:VEVENT(.*?)END:VEVENT', _unfold(text), re.DOTALL):
        dtstart = _extract_date(block, 'DTSTART')
        dtend   = _extract_date(block, 'DTEND')
        summary = _extract_field(block, 'SUMMARY') or 'Booking'
        if dtstart and dtend:
            if dtend <= today or dtstart > cutoff:
                continue
            dtstart = max(dtstart, today)
            events.append((dtstart, dtend, summary))
    return events


def _extract_date(block, field):
    m = re.search(rf'{field}(?:;[^:]+)?:(\S+)', block)
    if not m:
        return None
    raw = m.group(1).strip()
    if re.match(r'^\d{8}(T\d{6})?', raw):
        return date(int(raw[:4]), int(raw[4:6]), int(raw[6:8]))
    return None


def _extract_field(block, field):
    m = re.search(rf'^{field}[;:](.+)$', block, re.MULTILINE)
    return m.group(1).strip() if m else None


# ── READ EXISTING (last-known-good) ──────────────────────────

def read_existing_bookings():
    """Parse the current js/bookings.js so we can preserve data on failure."""
    result = {k: [] for k in ALL_KEYS}
    if not os.path.exists(BOOKINGS_JS):
        return result
    with open(BOOKINGS_JS, encoding='utf-8') as f:
        src = f.read()
    entry_re = re.compile(
        r"\{\s*from:\s*'([^']+)'\s*,\s*to:\s*'([^']+)'\s*,\s*note:\s*'((?:\\.|[^'\\])*)'\s*\}")
    for key in ALL_KEYS:
        m = re.search(rf"'{re.escape(key)}'\s*:\s*\[(.*?)\]", src, re.DOTALL)
        if not m:
            continue
        for em in entry_re.finditer(m.group(1)):
            note = em.group(3).replace("\\'", "'").replace('\\\\', '\\')
            result[key].append({'from': em.group(1), 'to': em.group(2), 'note': note})
    return result


# ── NORMALISE / COMPARE ──────────────────────────────────────

def _norm(entries):
    """Sort and de-duplicate a room's entries."""
    seen, out = set(), []
    for e in sorted(entries, key=lambda x: (x['from'], x['to'], x['note'])):
        sig = (e['from'], e['to'], e['note'])
        if sig in seen:
            continue
        seen.add(sig)
        out.append(e)
    return out


def _signature(bookings):
    return {k: [(e['from'], e['to'], e['note']) for e in _norm(v)] for k, v in bookings.items()}


# ── BUILD ────────────────────────────────────────────────────

def build_bookings(sources, existing):
    bookings    = {k: [] for k in ALL_KEYS}
    errors      = []
    live_synced = 0
    configured  = 0

    for source in sources:
        key = source['room_key']
        url = source['url']
        targets = ALL_KEYS if key is None else [key]

        if not url:
            print(f"  ⚠  {source['label']}: URL not configured — keeping last-known-good")
            for k in targets:
                bookings[k] = list(existing.get(k, []))
            continue

        configured += 1
        print(f"  Fetching {source['label']} ...", end=' ', flush=True)
        try:
            events = parse_ical_events(fetch_ical(url))
            print(f'{len(events)} event(s)')
            for (d_from, d_to, summary) in events:
                entry = {'from': d_from.isoformat(), 'to': d_to.isoformat(), 'note': summary}
                for k in targets:
                    bookings[k].append(entry)
            live_synced += 1
        except Exception as e:  # noqa: BLE001
            print(f'ERROR — {e}')
            errors.append(f"{source['label']}: {e}")
            for k in targets:            # preserve rather than degrade
                bookings[k] = list(existing.get(k, []))

    # Merge manual bookings (always survive).
    for k, entries in MANUAL_BOOKINGS.items():
        if k in bookings:
            bookings[k].extend(entries)

    bookings = {k: _norm(v) for k, v in bookings.items()}
    return bookings, errors, live_synced, configured


# ── WRITE ────────────────────────────────────────────────────

def write_bookings_js(bookings):
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    lines = [
        '// ============================================================',
        '// TAMARIU CHALET — Booking Availability',
        '// ============================================================',
        f'// Auto-generated by sync-bookings.py on {now}',
        '// DO NOT hand-edit — a sync will overwrite this file.',
        '// Add direct/phone bookings to MANUAL_BOOKINGS in sync-bookings.py.',
        '//',
        '// DATE FORMAT: "YYYY-MM-DD"   from = check-in · to = check-out',
        '// ============================================================',
        '',
        'const BOOKINGS = {',
    ]
    for room_key in ALL_KEYS:
        lines.append(f"  '{room_key}': [")
        for e in sorted(bookings.get(room_key, []), key=lambda x: (x['from'], x['to'])):
            note = e['note'].replace('\\', '\\\\').replace("'", "\\'")
            lines.append(f"    {{ from: '{e['from']}', to: '{e['to']}', note: '{note}' }},")
        lines.append('  ],')
        lines.append('')
    lines += [
        '};',
        '',
        '// ── DO NOT EDIT BELOW THIS LINE ─────────────────────────────',
        'function isRoomAvailable(roomKey, checkIn, checkOut) {',
        '  const bookings = BOOKINGS[roomKey];',
        '  if (!bookings || bookings.length === 0) return true;',
        '  const d1 = new Date(checkIn);',
        '  const d2 = new Date(checkOut);',
        '  return !bookings.some(b => d1 < new Date(b.to) && d2 > new Date(b.from));',
        '}',
    ]
    with open(BOOKINGS_JS, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


# ── MAIN ─────────────────────────────────────────────────────

def main():
    print('Tamariu Chalet — Availability Sync (hardened)')
    print('=' * 46)

    existing = read_existing_bookings()
    bookings, errors, live_synced, configured = build_bookings(ICAL_SOURCES, existing)

    # 1) Any configured feed failed → do not touch the file; fail loudly.
    if errors:
        print('\n✖ One or more feeds failed:')
        for err in errors:
            print(f'    - {err}')
        print('\nLeaving js/bookings.js UNCHANGED (last-known-good preserved).')
        print('Nothing will be committed or deployed. Fix the feed(s) and re-run.')
        return 1

    # 2) Nothing synced at all → misconfiguration; never publish an empty calendar.
    if REQUIRE_AT_LEAST_ONE and live_synced == 0:
        print('\n✖ No live feeds were synced (all URLs empty/unconfigured).')
        print('Check the AIRBNB_* secrets. Leaving js/bookings.js UNCHANGED.')
        return 1

    total = sum(len(v) for v in bookings.values())
    print(f'\nLive feeds synced: {live_synced}/{configured} · total bookings: {total}')

    # 3) No change → leave the file untouched (stable hash, no commit/upload).
    if _signature(bookings) == _signature(existing):
        print('No availability change since last sync — file left untouched.')
        return 0

    write_bookings_js(bookings)
    print(f'\n✔ Updated {BOOKINGS_JS} — safe to deploy.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
