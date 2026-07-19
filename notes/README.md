# notes/

Everything in this folder is for reference or maintenance only. **None of it is
required for the live site to run, and none of it is uploaded to production** —
`deploy.bat` excludes `notes/` from the sync.

| Item | What it is |
|---|---|
| `CHANGELOG.md` | Running history of site changes |
| `tamariu-chalet-technical-docs.docx` | Technical documentation for the site |
| `dutch_text.docx` | Source copy for the Dutch translation |
| `_nav-reference.html` | Reference copy of the standard nav markup |
| `backup.py` | Local backup helper script |
| `deploy.log` | WinSCP transfer log from the last deploy |
| `backups/` | Dated snapshots of earlier versions of the site |
| `beach-image-originals/` | Full-size originals of the beach photos, before resizing |
| `review-exports/` | Spreadsheet exports of guest reviews |

## What deliberately stayed at the root

These look like clutter but are load-bearing — do not move them:

- `77cddc9375e7750b1d161ed6c3f82379.txt` — IndexNow verification key. Search
  engines fetch it from the web root; moving it breaks URL submission.
- `.github/workflows/` — GitHub Actions only reads workflows from this exact
  path. Runs the IndexNow submission and the booking sync.
- `sync-bookings.py` — invoked as `python3 sync-bookings.py` from the repo root
  by the sync-bookings workflow. Generates `js/bookings.js`. Excluded from
  upload by the `*.py` filemask, but must stay where it is.
- `deploy.bat` — uses its own location (`%~dp0`) as the sync source. Moving it
  would make it upload the wrong directory.
- `.cpanel.yml` — cPanel deployment configuration.
- `*.gpx` at root — linked from `things-to-do/walking.html`, so these are live
  site content.
