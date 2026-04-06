#!/usr/bin/env python3
"""
sync-bookings.py — Tamariu Chalet availability sync
====================================================
Fetches iCal feeds from Airbnb and/or Google Calendar and
rewrites js/bookings.js so the contact form shows correct
availability to guests.

RUNNING LOCALLY
---------------
1. Paste your Airbnb iCal URLs into the ICAL_SOURCES list below.
2. Run:  python3 sync-bookings.py
3. Upload js/bookings.js to your server.

RUNNING VIA GITHUB ACTIONS (automated)
---------------------------------------
URLs are read from environment variables so they stay out of your
code. Set these in GitHub → Settings → Secrets and variables →
Actions → New repository secret:

  AIRBNB_DOUBLE_ROOM     — iCal URL for Double Room listing
  AIRBNB_TWIN_1          — iCal URL for Twin Room 1 listing
  AIRBNB_TWIN_2          — iCal URL for Twin Room 2 listing
  AIRBNB_APARTMENT       — iCal URL for Studio Apartment listing
  GOOGLE_CALENDAR        — (optional) Google Calendar iCal URL

HOW TO FIND YOUR AIRBNB ICAL URLS
-----------------------------------
Airbnb host dashboard → Calendar → Availability settings
→ Export calendar → copy the .ics link (one per listing)
"""

import urllib.request
import re
import os
from datetime import date, timedelta, datetime

# ── CONFIGURATION ────────────────────────────────────────────
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
BOOKINGS_JS = os.path.join(SCRIPT_DIR, 'js', 'bookings.js')
HORIZON_DAYS = 365  # how many days ahead to include

# ── ICAL SOURCES ─────────────────────────────────────────────
# Each entry: label, room_key, url.
# URLs are read from environment variables first (for GitHub Actions),
# falling back to the hardcoded value below (for local use).
# room_key must match the checkbox values in the contact form.

def _url(env_var, fallback=''):
    """Return env var value if set and non-empty, otherwise fallback."""
    return os.environ.get(env_var, '').strip() or fallback

ICAL_SOURCES = [
    {
        'label':    'Airbnb — Double Room',
        'room_key': 'double-room',
        'url':      _url('AIRBNB_DOUBLE_ROOM',
                         # Paste your URL here for local use:
                         ''),
    },
    {
        'label':    'Airbnb — Twin Room 1',
        'room_key': 'twin-room-1',
        'url':      _url('AIRBNB_TWIN_1', ''),
    },
    {
        'label':    'Airbnb — Twin Room 2',
        'room_key': 'twin-room-2',
        'url':      _url('AIRBNB_TWIN_2', ''),
    },
    {
        'label':    'Airbnb — Studio Apartment',
        'room_key': 'studio-apartment',
        'url':      _url('AIRBNB_APARTMENT', ''),
    },
    # Google Calendar — uncomment and add secret GOOGLE_CALENDAR if needed:
    # {
    #     'label':    'Google Calendar',
    #     'room_key': None,   # None = applies to ALL rooms
    #     'url':      _url('GOOGLE_CALENDAR', ''),
    # },
]

# ── iCAL PARSER ──────────────────────────────────────────────

def fetch_ical(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'TamariuChalet-Sync/1.0'})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode('utf-8', errors='replace')


def parse_ical_events(text):
    events  = []
    today   = date.today()
    cutoff  = today + timedelta(days=HORIZON_DAYS)
    blocks  = re.findall(r'BEGIN:VEVENT(.*?)END:VEVENT', text, re.DOTALL)
    for block in blocks:
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
    if re.match(r'^\d{8}$', raw):
        return date(int(raw[:4]), int(raw[4:6]), int(raw[6:8]))
    if re.match(r'^\d{8}T\d{6}', raw):
        return date(int(raw[:4]), int(raw[4:6]), int(raw[6:8]))
    return None


def _extract_field(block, field):
    m = re.search(rf'^{field}[;:](.+)$', block, re.MULTILINE)
    return m.group(1).strip() if m else None


# ── BUILD BOOKINGS ────────────────────────────────────────────

def build_bookings(sources):
    all_keys = ['double-room', 'twin-room-1', 'twin-room-2', 'studio-apartment']
    bookings = {k: [] for k in all_keys}
    errors   = []

    for source in sources:
        url = source['url']
        if not url:
            print(f"  ⚠  Skipped '{source['label']}' — URL not configured")
            continue

        print(f"  Fetching: {source['label']} ...", end=' ', flush=True)
        try:
            text   = fetch_ical(url)
            events = parse_ical_events(text)
            print(f'{len(events)} event(s)')
            targets = all_keys if source['room_key'] is None else [source['room_key']]
            for (d_from, d_to, summary) in events:
                entry = {'from': d_from.isoformat(), 'to': d_to.isoformat(), 'note': summary}
                for key in targets:
                    bookings[key].append(entry)
        except Exception as e:
            print(f'ERROR — {e}')
            errors.append(f"{source['label']}: {e}")

    return bookings, errors


# ── WRITE bookings.js ─────────────────────────────────────────

def write_bookings_js(bookings, errors):
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    lines = [
        '// ============================================================',
        '// TAMARIU CHALET — Booking Availability',
        '// ============================================================',
        f'// Auto-generated by sync-bookings.py on {now}',
        '// To regenerate:  python3 sync-bookings.py',
        '// Manual entries: add to the arrays below and upload the file.',
        '//',
        '// DATE FORMAT: "YYYY-MM-DD"',
        '// from = check-in · to = check-out · note = your reference',
        '// ============================================================',
        '',
        'const BOOKINGS = {',
    ]
    if errors:
        for err in errors:
            lines.insert(-1, f'//  ⚠ WARNING: {err}')

    for room_key, entries in bookings.items():
        lines.append(f"  '{room_key}': [")
        for e in sorted(entries, key=lambda x: x['from']):
            note = e['note'].replace("'", "\\'")
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
    print(f'\n  Written → {BOOKINGS_JS}')


# ── MAIN ──────────────────────────────────────────────────────

if __name__ == '__main__':
    print('Tamariu Chalet — Availability Sync')
    print('=' * 40)
    bookings, errors = build_bookings(ICAL_SOURCES)
    total = sum(len(v) for v in bookings.values())
    print(f'\nTotal bookings imported: {total}')
    for key, entries in bookings.items():
        if entries:
            print(f'  {key}: {len(entries)}')
    write_bookings_js(bookings, errors)
    print('\nDone. Upload js/bookings.js to your server.')
    if errors:
        print(f'\n⚠  {len(errors)} source(s) had errors — check above.')
