#!/usr/bin/env python3
"""
backup.py — Tamariu Chalet site backup utility
===============================================
Creates a timestamped snapshot of all tracked source files into
_backups/YYYY-MM-DD_HH-MM/  before changes are made.

USAGE
-----
Run at the start of any editing session:
    python3 backup.py

The script copies every file listed in TRACKED_FILES into a
timestamped subdirectory of _backups/.  It never deletes old
backups — remove them manually if disk space is a concern.

RESTORING A FILE
----------------
Just copy the file you want from the relevant _backups/ folder
back to its original location, then upload it to the server.
"""

import os, shutil
from datetime import datetime

# ── Files to back up ────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

TRACKED_FILES = [
    # Core JS
    'js/main.js',
    'js/availability-calendar.js',
    'js/rates.js',
    'js/bookings.js',
    # CSS
    'css/style.css',
    # Availability page
    'availability/index.html',
    # Contact pages (all 5 languages)
    'contact/index.html',
    'es/contact/index.html',
    'ca/contact/index.html',
    'fr/contact/index.html',
    'nl/contact/index.html',
    # Accommodation pages — English
    'accommodation/double-room.html',
    'accommodation/twin-room-1.html',
    'accommodation/twin-room-2.html',
    'accommodation/pool-apartment.html',
    # Accommodation pages — Spanish
    'es/accommodation/double-room.html',
    'es/accommodation/twin-room-1.html',
    'es/accommodation/twin-room-2.html',
    'es/accommodation/pool-apartment.html',
    # Accommodation pages — Catalan
    'ca/accommodation/double-room.html',
    'ca/accommodation/twin-room-1.html',
    'ca/accommodation/twin-room-2.html',
    'ca/accommodation/pool-apartment.html',
    # Accommodation pages — French
    'fr/accommodation/double-room.html',
    'fr/accommodation/twin-room-1.html',
    'fr/accommodation/twin-room-2.html',
    'fr/accommodation/pool-apartment.html',
    # Accommodation pages — Dutch
    'nl/accommodation/double-room.html',
    'nl/accommodation/twin-room-1.html',
    'nl/accommodation/twin-room-2.html',
    'nl/accommodation/pool-apartment.html',
    # Home pages (all languages)
    'index.html',
    'es/index.html',
    'ca/index.html',
    'fr/index.html',
    'nl/index.html',
    # Sync / config
    'sync-bookings.py',
    'CHANGELOG.md',
]

# ── Run backup ───────────────────────────────────────────────────

def run():
    timestamp  = datetime.now().strftime('%Y-%m-%d_%H-%M')
    backup_dir = os.path.join(SCRIPT_DIR, '_backups', timestamp)
    os.makedirs(backup_dir, exist_ok=True)

    copied  = 0
    missing = []

    for rel_path in TRACKED_FILES:
        src = os.path.join(SCRIPT_DIR, rel_path)
        if not os.path.exists(src):
            missing.append(rel_path)
            continue
        dst = os.path.join(backup_dir, rel_path)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        copied += 1

    print(f'Tamariu Chalet — Backup')
    print(f'=======================')
    print(f'Snapshot:  _backups/{timestamp}/')
    print(f'Copied:    {copied} file(s)')
    if missing:
        print(f'Missing:   {len(missing)} file(s) (not yet created)')
        for m in missing:
            print(f'  - {m}')
    print(f'\nDone. Run again before the next editing session.')

if __name__ == '__main__':
    run()
