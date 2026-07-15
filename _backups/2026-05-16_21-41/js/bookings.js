// ============================================================
// TAMARIU CHALET — Booking Availability
// ============================================================
// This file controls which dates show as unavailable in the
// enquiry form cost calculator.
//
// You can edit this file manually, or run the sync script:
//   python3 sync-bookings.py
// which will pull live bookings from Airbnb and/or Google
// Calendar and overwrite this file automatically.
//
// DATE FORMAT: "YYYY-MM-DD"  e.g. "2026-07-15"
// from = check-in date of existing booking
// to   = check-out date of existing booking
// note = optional label (shown nowhere to guests, just for you)
// ============================================================

const BOOKINGS = {

  'double-room': [
    // Example — remove or replace with real bookings:
    // { from: '2026-06-14', to: '2026-06-21', note: 'Airbnb' },
  ],

  'twin-room-1': [
    //
  ],

  'twin-room-2': [
    //
  ],

  'studio-apartment': [
    //
  ],

};

// ── DO NOT EDIT BELOW THIS LINE ──────────────────────────────
// Helper used by main.js to test whether a date range overlaps
// any existing booking for a given room.
function isRoomAvailable(roomKey, checkIn, checkOut) {
  const bookings = BOOKINGS[roomKey];
  if (!bookings || bookings.length === 0) return true;
  const d1 = new Date(checkIn);
  const d2 = new Date(checkOut);
  return !bookings.some(b => {
    // Overlap condition: new check-in is before existing check-out
    // AND new check-out is after existing check-in
    return d1 < new Date(b.to) && d2 > new Date(b.from);
  });
}
