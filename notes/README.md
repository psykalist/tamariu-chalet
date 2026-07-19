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

## Authoring scripts (`notes/scripts/`)

The site remains plain static HTML with no serve-time build step. These scripts
generate HTML that is then committed like any other page, and are safe to re-run.

    python3 notes/scripts/build_translations.py --apply   # translated pages
    python3 notes/scripts/fix_hreflang.py --apply         # canonical + hreflang
    python3 notes/scripts/build_sitemap.py --apply        # sitemap.xml from disk
    python3 notes/scripts/check_site.py                   # verification gate

Run the first three after any page change, then `check_site.py` — it should
report 0 errors. It checks broken internal links, hreflang reciprocity,
canonical agreement and sitemap coverage.

Translated prose lives in `content_*.py`; shared nav/footer wording is in
`i18n_shell.py`. Nav links fall back to English where a translation does not
exist yet, so re-running upgrades them automatically as pages are added.

Note: `availability/index.html` self-translates via a `?lang=` query parameter
and is deliberately a single URL — do not create language-folder copies of it.
