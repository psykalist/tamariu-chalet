# Tamariu Chalet Website — Directory Guide

## How to Use This Website

Open `index.html` in any browser to see the site. For a live server (to avoid
cross-origin issues with some browsers), use VS Code Live Server or run:
    npx serve .

---

## Complete Directory Structure

```
tamariu-chalet/
│
├── index.html                        ← LANDING PAGE (edit this first)
│
├── css/
│   └── style.css                     ← All styles — colours, fonts, layout
│
├── js/
│   └── main.js                       ← Nav, carousel, booking calculator
│
├── accommodation/
│   ├── double-room.html
│   ├── twin-room-1.html
│   ├── twin-room-2.html
│   └── pool-apartment.html
│
├── things-to-do/
│   ├── girona.html
│   ├── cycling.html
│   ├── markets.html
│   ├── walking.html                  ← Add Wikiloc URLs here
│   ├── tourist-info.html
│   ├── restaurants.html
│   └── water-sports.html
│
├── getting-here/
│   ├── index.html                    ← Map & directions
│   ├── julivia-bus.html
│   └── begur-bus.html
│
├── contact/
│   └── index.html                    ← Booking enquiry with cost calculator
│
└── images/                           ← *** YOU POPULATE THIS FOLDER ***
    │
    ├── background.jpg                ← HERO background (1920×1080 min)
    │
    ├── carousel/                     ← Carousel images on landing page
    │   ├── tamariu-beach.jpg
    │   ├── llafranc.jpg
    │   ├── girona.jpg
    │   ├── calella.jpg
    │   ├── begur.jpg
    │   ├── peratallada.jpg
    │   └── coves.jpg
    │
    ├── rooms/
    │   ├── double-room/
    │   │   ├── main.jpg              ← Large main image (landscape)
    │   │   ├── view2.jpg             ← Smaller thumbnail
    │   │   └── view3.jpg             ← Smaller thumbnail
    │   ├── twin-room-1/
    │   │   ├── main.jpg
    │   │   ├── view2.jpg
    │   │   └── view3.jpg
    │   ├── twin-room-2/
    │   │   ├── main.jpg
    │   │   ├── view2.jpg
    │   │   └── view3.jpg
    │   └── pool-apartment/
    │       ├── main.jpg
    │       ├── view2.jpg
    │       └── view3.jpg
    │
    └── shared/                       ← Photos used across the site
        ├── pool.jpg
        ├── garden.jpg
        ├── patio.jpg
        └── tamariu-view.jpg
```

---

## Things You Need to Update

### 1. Images
Place all your photos in the `images/` folders as named above.
Then uncomment the `<img>` tags in each HTML file (look for the `<!-- <img...> -->`
comments — they're next to each placeholder).

### 2. Google Calendar Availability Links
In each room page (`double-room.html`, `twin-room-1.html`, etc.), find the
"Check Availability" button and replace the `href="https://calendar.google.com"`
with your actual Google Calendar embed or sharing URL.

### 3. Walking Routes (Wikiloc)
Open `things-to-do/walking.html` and replace each `href="#"` in the
external-link-card elements with your actual Wikiloc route URLs.

### 4. WhatsApp Link
In `contact/index.html`, find `href="https://wa.me/YOURPHONENUMBER"`
and replace YOURPHONENUMBER with your number in international format
(e.g. for +34 972 123456 use: 34972123456).

### 5. Phone Number
In `contact/index.html`, find "Add your phone number here" and replace it.

### 6. Girona Images
Add your own photos to an `images/girona/` folder and uncomment the
`<img>` tags on the `things-to-do/girona.html` page.

### 7. Cycling Images
Add cycling photos to `images/cycling/` and uncomment on `cycling.html`.

---

## Recommended Image Sizes
- `background.jpg` — 1920×1080 px minimum (this is the hero backdrop)
- Carousel images — 800×600 px (3:2 ratio works well)
- Room main image — 1200×800 px
- Room thumbnail — 600×400 px
- Shared/garden images — 800×600 px

All images should be compressed for web. Use squoosh.app or TinyPNG.

---

## Colour Scheme (easy to customise in css/style.css)
```
--terracotta: #C4693A     (buttons, accents, prices)
--deep-blue:  #1A3A5C     (nav, headings)
--sea-blue:   #2D6A9F     (links)
--linen:      #F5EFE6     (section backgrounds)
--gold:       #B8963A     (highlights, nav hover)
```

---

## Hosting
Upload the entire `tamariu-chalet/` folder to any web host.
Works with Netlify (free drag-and-drop), GitHub Pages, or any standard web host.
No server-side code — it's all plain HTML, CSS and JavaScript.
