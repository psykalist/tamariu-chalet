# Pool apartment page — Airbnb photo import (IN PROGRESS)

Picking this back up later. Here is exactly where things stand.

## The goal
Rebuild `accommodation/pool-apartment.html` so it shows the Airbnb listing's
photos grouped under the same headings the Airbnb photo tour uses.

Source listing (host photo tour, requires Kieran's login):
https://www.airbnb.co.uk/hosting/listings/editor/609819206280916574/details/photo-tour

## Photo tour structure (confirmed) — 24 photos across 9 rooms
| Heading        | Count | Suggested filenames                          |
|----------------|-------|----------------------------------------------|
| Living room    | 3     | living-room-1.jpg … living-room-3.jpg        |
| Kitchenette    | 1     | kitchenette-1.jpg                            |
| Dining area    | 3     | dining-area-1.jpg … dining-area-3.jpg        |
| Bedroom        | 6     | bedroom-1.jpg … bedroom-6.jpg                |
| Full bathroom  | 1     | bathroom-1.jpg                               |
| Office         | 1     | office-1.jpg                                 |
| Courtyard      | 2     | courtyard-1.jpg, courtyard-2.jpg             |
| Exterior       | 3     | exterior-1.jpg … exterior-3.jpg              |
| Pool           | 4     | pool-1.jpg … pool-4.jpg                       |

(The tour also has an "Additional photos" group of 6 with no room heading —
not yet decided whether to include these. Kieran to say.)

Target folder for the web-ready files:
`images/rooms/pool-apartment/`

## Why the photos are not here yet
The images could not be transferred from the browser to the project folder in
the Cowork environment. All three channels were blocked:
- **Chrome downloads** did not land in `C:\Users\kiera\Downloads` (a "save as"
  prompt appears to stack behind a window the agent cannot see; the browser is
  read-only to the agent so the dialog cannot be operated).
- **Reading image bytes through the page** (base64 bridge) is blocked by an
  anti-exfiltration filter as soon as the payload is a full image.
- **The Linux sandbox cannot reach `a0.muscache.com`** and does not have the
  signed image URLs.

Technical note for next time: the muscache image URLs are NOT signature-locked —
appending `?im_w=1200` to an image element's own `currentSrc` returns a proper
~40 KB web-size JPEG. So if the files can be made to download, `im_w=1200` is a
good size and no local resize is needed. `im_w=1600` for hero shots.

## Two ways to finish (Kieran to pick)
**A — Kieran saves, agent builds.** On each room in the photo tour, right-click
each photo → Save image, into `images/rooms/pool-apartment/` using the filenames
above. Then the agent builds the page, optimises, updates the sitemap, runs
`notes/scripts/check_site.py`, and deploys.

**B — Fix Chrome download setting.** Turn OFF Chrome Settings → Downloads →
"Ask where to save each file before downloading", then the agent re-runs the
grab; files land in Downloads and the agent moves them into place via File
Explorer.

## Current live page (unchanged)
`accommodation/pool-apartment.html` still uses its original 3 images:
`../images/rooms/pool-apartment/main.jpg`, `view2.jpg`, `view3.jpg`.
Nothing about the page has been changed yet — this task did not modify any
committed files.

## Also still open from earlier (separate, low priority)
- `.git/` folder still exists on the production server (dated 4 April). It is
  NOT web-readable (`/.git/config` returns an error page, checked), but it has no
  business on the host and is what fed stale refs back into the local repo. Was
  mid-deletion via WinSCP when interrupted; safe to delete the remote `.git/`.
- Orphan page `getting-here/3km Circular walk fron chalet.html` is still live on
  the server but no longer in the repo (moved to `notes/orphan-pages/`). Either
  give it a proper name + a link, or delete from prod.
