# Tamariu Chalet — Site Changelog

All notable changes to the website are documented here.
Most recent changes are at the top.

---

## 2026-05-17 — Session 3

### Restaurant & Bar Guide — Complete Rebuild
**Files:** `things-to-do/restaurants.html`
- Complete rewrite of the placeholder restaurants page into a full styled guide
- Sections: Bars in Tamariu (Ona, Mossec), Beach & Promenade Restaurants (El Palanquí, Royal, Hotel Tamariu, Es Dofí), Town & Local Restaurants (El Clot dels Mussols, La Pasta Tamariu), Worth the Drive (Mooma, El Far, La Malcontenta, La Xicra), Takeaway (El Camí de Ronda)
- Each venue card includes: address, phone number, opening hours, website link, Google Maps link, star rating, category label, description
- Custom page hero using existing `images/tamariu views/tamariu-beach.jpg`
- Hotel Tamariu photo from `images/tamariu views/hotel-tamariu-costa-brava--2-.jpg`
- CSS-only styled placeholders for venues without photos
- TripAdvisor/review scores included where available
- Seasonal indicator badge for El Camí de Ronda (summer only)
- Local tips callout boxes throughout

### Navigation — Restaurants & Bars Moved to Top of Things To Do
**Files:** `index.html`, `es/index.html`, `ca/index.html`, `fr/index.html`, `nl/index.html`
- "Local Restaurants" renamed to "Restaurants & Bars" (ES: Restaurantes y Bares, CA: Restaurants i Bars, FR: Restaurants & Bars, NL: Restaurants & Bars)
- Moved from bottom of Things To Do dropdown to first position across all 5 language home pages

---

All notable changes to the website are documented here.
Most recent changes are at the top.

---

## 2026-05-16 — Session 2

### Availability Calendar — Min Stay Visual Enforcement
**Files:** `js/availability-calendar.js`, `availability/index.html`
- After a check-in date is selected, dates within the minimum stay window are now rendered as `cal-too-short` (muted, italic, no click handler) — browser-agnostic, user cannot select them at all
- Hint message after check-in now reads e.g. *"Now click your check-out date (min 3 nights)"* so guests know the requirement upfront
- Added `cal-too-short` CSS class to `availability/index.html` inline styles
- Min-stay error message retained as a secondary guard if a valid-looking date is somehow submitted

### EmailJS — Simplified to Single Send with CC
**Files:** `js/main.js`
- Removed `composeOwnerEmail()` function entirely (~35 lines)
- Collapsed two `emailjs.send()` calls into one; owner copy delivered via `cc_email: 'tamariuchalet@gmail.com'`
- Counts as 1 EmailJS credit per booking instead of 2
- Removed now-unused `guestPhone` / `guestMessage` variables from submit handler

### Removed "Enquire Now" Button
**Files:** All 20 accommodation pages (4 rooms × 5 languages)
- Removed the "Ready to Book? / Enquire Now" box from every accommodation page as it duplicated the Check Availability button
- Affected: `accommodation/`, `es/accommodation/`, `ca/accommodation/`, `fr/accommodation/`, `nl/accommodation/`

### Backup System Created
**Files:** `backup.py`, `_backups/` directory, `CHANGELOG.md`
- `backup.py` creates timestamped snapshots of all 38 tracked files into `_backups/YYYY-MM-DD_HH-MM/`
- Run `python3 backup.py` at the start of each editing session
- First snapshot taken: `_backups/2026-05-16_21-41/`

---

## 2026-05-15 — Session 1

### Rates Panel Redesign
**Files:** `css/style.css`, all 5 contact pages (`contact/index.html`, `es/`, `ca/`, `fr/`, `nl/`)
- Rates panel split into two separate tables: 🛏 Rooms and 🏠 Studio Apartment
- Added `.rates-section-label` headings with uppercase letter-spaced styling
- Each table now has a dedicated Min Stay column using `.min-stay-cell` (bold)
- `rates-table th` font weight increased to 700; colour set to `var(--deep-blue)`
- `rates-table td` font weight set to 500
- `rates-table .season-name` font weight increased to 700

### Min Stay Enforcement in Booking Form
**Files:** `js/main.js`, all 5 contact pages
- Added `updateCheckoutMin()` function to `main.js`
  - Sets the `min` attribute on the checkout date input dynamically based on selected room and check-in season
  - Shows amber warning banner (`#min-stay-warning`) if a checkout date violating the minimum is selected
  - Warning text includes the minimum nights and the earliest valid checkout date
- Added `min-stay-warning` div to all 5 contact pages (between date inputs and cost display)
- `calcCost()` updated to call `updateCheckoutMin()` on both early-return and normal paths

### PDF Removed — EmailJS Confirmation Emails Added
**Files:** `js/main.js`, all 5 contact pages
- Removed jsPDF library CDN script tag from all 5 contact pages
- Removed `generateBookingPDF()` function (~120 lines) from `main.js`
- Removed `PDF_NOTES` constant from `main.js`
- Added EmailJS browser SDK (v4) via jsDelivr CDN to all 5 contact pages
- Added EmailJS credentials to `main.js`:
  - Public Key: `ooRh9XbjSEoX4M5cc`
  - Service ID: `service_006p22o`
  - Template ID: `template_wb6mqai`
- Added `EMAIL_SUBJECTS` object with subject lines in all 5 languages
- Added `composeGuestEmail()` function — generates booking confirmation body in guest's chosen language
- Added `buildCostData()` helper — extracts structured cost data from form inputs
- Added `fmtDate()` helper — formats YYYY-MM-DD as "1 Jan 2026"
- Submit handler updated to send EmailJS confirmation after successful Formspree submission
- Success message updated across all 5 contact pages (no PDF mention)
- Invoice language label updated across all 5 contact pages

### Availability Calendar — Min Stay Check Added
**Files:** `js/availability-calendar.js`
- Added `getMinStay(checkIn, isApartment)` helper — looks up minimum stay from `SEASON_CONFIG`
- Added `rangeMinStay` error string to `I18N` for all 5 languages (EN, ES, CA, FR, NL) with correct pluralisation
- `_handleClick()` updated: when selecting checkout, validates nights ≥ minStay before accepting the date; shows error and returns early if violated

---

## Pre-session baseline

### Core Architecture
- Static site — no backend required; hosted on iFastNet
- Five languages: English (root), Spanish (`es/`), Catalan (`ca/`), French (`fr/`), Dutch (`nl/`)
- `js/rates.js` — single source of truth for all seasonal rates and minimum stays
- `js/bookings.js` — auto-generated hourly from Airbnb iCal feeds via `sync-bookings.py` + GitHub Actions
- `js/main.js` — booking form logic, cost calculator, EmailJS sends
- `js/availability-calendar.js` — interactive per-room availability calendar
- `css/style.css` — site-wide styles
- Formspree (`xleqevwo`) — captures all form submissions as a data backup
- EmailJS (`service_006p22o` / `template_wb6mqai`) — sends booking confirmation emails
- GitHub repo: `psykalist/tamariu-chalet`
- GitHub Actions workflow (`.github/workflows/sync-bookings.yml`) — syncs Airbnb bookings every hour via FTP to production

---

*To restore any file: copy from `_backups/YYYY-MM-DD_HH-MM/` back to its original path and upload to server.*
