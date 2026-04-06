// ============================================================
// TAMARIU CHALET — Main JavaScript
// ============================================================

// ── NAV: Hamburger Toggle ──
const hamburger = document.querySelector('.hamburger');
const navMenu   = document.querySelector('.nav-menu');

if (hamburger) {
  hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('open');
  });
}

// Close nav on outside click
document.addEventListener('click', (e) => {
  if (navMenu && !navMenu.contains(e.target) && !hamburger.contains(e.target)) {
    navMenu.classList.remove('open');
  }
});

// ── CAROUSEL ──
const track    = document.querySelector('.carousel-track');
const prevBtn  = document.querySelector('.carousel-btn.prev');
const nextBtn  = document.querySelector('.carousel-btn.next');

if (track) {
  let currentIndex = 0;
  const slideWidth = 400; // slide + gap
  const totalSlides = track.children.length;
  let visibleCount = Math.floor(window.innerWidth / slideWidth) || 1;
  let autoTimer;

  function updateCarousel(animate = true) {
    if (!animate) track.style.transition = 'none';
    else track.style.transition = 'transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
    track.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
  }

  function nextSlide() {
    const maxIndex = totalSlides - visibleCount;
    currentIndex = currentIndex >= maxIndex ? 0 : currentIndex + 1;
    updateCarousel();
  }

  function prevSlide() {
    const maxIndex = totalSlides - visibleCount;
    currentIndex = currentIndex <= 0 ? maxIndex : currentIndex - 1;
    updateCarousel();
  }

  if (nextBtn) nextBtn.addEventListener('click', () => { nextSlide(); resetAuto(); });
  if (prevBtn) prevBtn.addEventListener('click', () => { prevSlide(); resetAuto(); });

  function startAuto() { autoTimer = setInterval(nextSlide, 4000); }
  function resetAuto()  { clearInterval(autoTimer); startAuto(); }
  startAuto();

  window.addEventListener('resize', () => {
    visibleCount = Math.floor(window.innerWidth / slideWidth) || 1;
  });
}

// ── RATES TABLE AUTO-RENDER ──
// Finds any <table class="rates-table"> with data-room-type="room" or "apartment"
// and populates it from SEASON_CONFIG in rates.js
// Cleaning fee is shown as a note below the table, not as a column.

function renderRatesTables() {
  document.querySelectorAll('table.rates-table[data-room-type]').forEach(table => {
    const type  = table.dataset.roomType;
    if (type === 'summary') return; // handled by renderSummaryTable
    const isApt = type === 'apartment';
    const tbody = table.querySelector('tbody');
    if (!tbody) return;
    tbody.innerHTML = '';
    SEASON_CONFIG.forEach(s => {
      const d      = isApt ? s.apt : s.room;
      const closed = d.rate === null;
      tbody.innerHTML += `
        <tr>
          <td class="season-name">${s.name}</td>
          <td>${s.dates}</td>
          <td>${closed ? '<span class="closed-cell">Closed</span>' : `<span class="rate-highlight">€${d.rate}</span>`}</td>
          <td>${closed ? '—' : `${d.minStay} nights`}</td>
        </tr>`;
    });

    // Insert cleaning fee note below the table if not already present
    const existing = table.parentElement.querySelector('.rates-cleaning-note');
    if (!existing) {
      const cleaningFee = isApt ? SEASON_CONFIG[1].apt.cleaning : SEASON_CONFIG[1].room.cleaning;
      const note = document.createElement('p');
      note.className = 'rates-cleaning-note';
      note.style.cssText = 'font-size:0.8rem;color:var(--stone);margin-top:10px;font-style:italic;';
      note.textContent = `A one-off cleaning fee of €${cleaningFee} applies per stay.`;
      table.insertAdjacentElement('afterend', note);
    }
  });
}

// Also render the summary table on the contact page (data-room-type="summary")
function renderSummaryTable() {
  document.querySelectorAll('table.rates-table[data-room-type="summary"]').forEach(table => {
    const tbody = table.querySelector('tbody');
    if (!tbody) return;
    tbody.innerHTML = '';
    SEASON_CONFIG.forEach(s => {
      const r = s.room, a = s.apt;
      tbody.innerHTML += `
        <tr>
          <td class="season-name">${s.name}</td>
          <td>${s.dates}</td>
          <td>${r.rate === null ? '<span class="closed-cell">Closed</span>' : `<span class="rate-highlight">€${r.rate}</span>`}</td>
          <td><span class="rate-highlight">€${a.rate}</span></td>
        </tr>`;
    });
  });
}

renderRatesTables();
renderSummaryTable();

// ── BOOKING FORM — Cost Calculator (multi-room + extra guests) ──

// Returns the number of whole days between two Date objects
function daysBetween(d1, d2) {
  return Math.round((d2 - d1) / (1000 * 60 * 60 * 24));
}

// Returns the SEASON_CONFIG entry whose start/end range contains the given date
function getSeason(date) {
  const m = date.getMonth() + 1; // 1-based month
  const d = date.getDate();
  const n = m * 100 + d; // comparable number e.g. 605 = Jun 5
  for (const s of SEASON_CONFIG) {
    const startN = s.start[0] * 100 + s.start[1];
    const endN   = s.end[0]   * 100 + s.end[1];
    if (n >= startN && n <= endN) return s;
  }
  return SEASON_CONFIG[0]; // fallback (shouldn't happen for valid dates)
}

const ROOM_NAMES = {
  'double-room':      'Double Room',
  'twin-room-1':      'Double/Twin Room 1',
  'twin-room-2':      'Double/Twin Room 2',
  'studio-apartment': 'Studio Apartment',
};

function calcCost() {
  const costEl  = document.getElementById('booking-cost');
  const breakEl = document.getElementById('booking-breakdown');
  const hidden  = document.getElementById('cost-hidden');
  if (!costEl) return;

  const checkIn  = document.getElementById('booking-checkin')?.value;
  const checkOut = document.getElementById('booking-checkout')?.value;
  const checked  = Array.from(document.querySelectorAll('.room-checkbox:checked'));

  if (checked.length === 0 || !checkIn || !checkOut) {
    costEl.textContent = '—';
    costEl.style.color = '';
    if (breakEl) breakEl.innerHTML = checked.length === 0 ? 'Select at least one room' : 'Select dates';
    if (hidden)  hidden.value = '—';
    _updateSubmitAvailability(true);
    return;
  }

  const d1 = new Date(checkIn), d2 = new Date(checkOut);
  if (isNaN(d1) || isNaN(d2) || d2 <= d1) {
    costEl.textContent = '—';
    costEl.style.color = '';
    if (breakEl) breakEl.innerHTML = 'Check-out must be after check-in';
    return;
  }

  const nights      = daysBetween(d1, d2);
  const season      = getSeason(d1);
  const extraGuests = parseInt(document.getElementById('extra-guests')?.value || '0');
  let totalCost = 0, lines = [], hasError = false, hasUnavailable = false;

  checked.forEach(cb => {
    const val   = cb.value;
    const isApt = APARTMENT_ROOMS.includes(val);
    const d     = isApt ? season.apt : season.room;
    const name  = ROOM_NAMES[val] || val;

    // ── Availability check ──────────────────────────────────
    if (typeof isRoomAvailable === 'function' && !isRoomAvailable(val, checkIn, checkOut)) {
      lines.push('<span style="color:#c0392b">\u274c ' + name + ': not available for those dates</span>');
      hasUnavailable = true;
      hasError = true;
      return;
    }

    // ── Season / min-stay checks ────────────────────────────
    if (!d.rate) {
      lines.push('\u26a0\ufe0f ' + name + ': closed in ' + season.name + ' season');
      hasError = true; return;
    }
    if (nights < d.minStay) {
      lines.push('\u26a0\ufe0f ' + name + ': min ' + d.minStay + ' nights in ' + season.name);
      hasError = true; return;
    }

    // ── Cost calculation ────────────────────────────────────
    let roomCost = nights * d.rate + d.cleaning;
    if (isApt && extraGuests > 0) {
      const extra = extraGuests * 50 * nights;
      roomCost += extra;
      lines.push('\u2705 ' + name + ': ' + nights + 'n \xd7 \u20ac' + d.rate +
        ' + ' + extraGuests + ' extra guest' + (extraGuests > 1 ? 's' : '') +
        ' \xd7 \u20ac50 \xd7 ' + nights + 'n + \u20ac' + d.cleaning + ' cleaning = \u20ac' + roomCost);
    } else {
      lines.push('\u2705 ' + name + ': ' + nights + 'n \xd7 \u20ac' + d.rate +
        ' + \u20ac' + d.cleaning + ' cleaning = \u20ac' + roomCost);
    }
    totalCost += roomCost;
  });

  if (hasUnavailable) {
    costEl.textContent = 'Not available';
    costEl.style.color = '#c0392b';
  } else {
    const displayCost = (!hasError || totalCost > 0) ? ('\u20ac' + totalCost) : '—';
    costEl.textContent = displayCost;
    costEl.style.color = '';
    if (hidden) hidden.value = displayCost;
  }

  if (breakEl) breakEl.innerHTML = lines.join('<br>');
  _updateSubmitAvailability(!hasUnavailable);

  // Build combined rooms string for hidden field
  const roomsHidden = document.getElementById('rooms-hidden');
  if (roomsHidden) roomsHidden.value = checked.map(c => ROOM_NAMES[c.value] || c.value).join(', ');
}

// Disable/re-enable the submit button if unavailable dates are selected
function _updateSubmitAvailability(available) {
  const btn = document.getElementById('submit-btn');
  if (!btn) return;
  btn.disabled = !available;
  btn.title    = available ? '' : 'Please choose different dates — one or more rooms are already booked for this period';
  btn.style.opacity = available ? '' : '0.5';
}

function toggleEnquiryType() {
  const val      = document.querySelector('input[name="enquiry-type"]:checked')?.value;
  const isBook   = val === 'booking';
  const sect     = document.getElementById('booking-section');
  const typeHid  = document.getElementById('enquiry-type-hidden');
  const submitBtn = document.getElementById('submit-btn');
  if (sect)     sect.style.display    = isBook ? '' : 'none';
  if (typeHid)  typeHid.value         = isBook ? 'Booking Enquiry' : 'General Message';
  if (submitBtn) submitBtn.dataset.booking = isBook ? '1' : '';
}

function handleAptChange() {
  const aptBox   = document.querySelector('.room-checkbox[value="studio-apartment"]');
  const extraDiv = document.getElementById('apt-extra-guests');
  if (extraDiv) extraDiv.style.display = (aptBox && aptBox.checked) ? '' : 'none';
  if (aptBox && !aptBox.checked) {
    const eg = document.getElementById('extra-guests');
    if (eg) eg.value = '0';
  }
  calcCost();
}

// ── CONTACT FORM SUBMISSION ──
const contactForm = document.getElementById('contact-form');
if (contactForm) {
  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Sync cost hidden field
    const costEl = document.getElementById('booking-cost');
    const hidden = document.getElementById('cost-hidden');
    if (costEl && hidden) hidden.value = costEl.textContent;

    const btn       = document.getElementById('submit-btn');
    const successEl = document.getElementById('form-success');
    const errorEl   = document.getElementById('form-error');
    const errorText = document.getElementById('error-text');

    successEl.style.display = 'none';
    errorEl.style.display   = 'none';
    btn.disabled    = true;
    btn.textContent = 'Sending\u2026';

    try {
      const response = await fetch('https://formspree.io/f/xleqevwo', {
        method: 'POST',
        body: new FormData(contactForm),
        headers: { 'Accept': 'application/json' }
      });
      const result = await response.json();
      if (result.ok) {
        successEl.style.display = 'block';
        contactForm.reset();
        const bCost = document.getElementById('booking-cost');
        const bBreak = document.getElementById('booking-breakdown');
        if (bCost)  bCost.textContent  = '\u2014';
        if (bBreak) bBreak.textContent = 'Select rooms \u0026 dates';
        const aptDiv = document.getElementById('apt-extra-guests');
        if (aptDiv) aptDiv.style.display = 'none';
        // Reset to booking mode
        const bookRadio = document.querySelector('input[name="enquiry-type"][value="booking"]');
        if (bookRadio) { bookRadio.checked = true; toggleEnquiryType(); }
      } else {
        errorText.textContent = result.message || 'Something went wrong. Please email us directly at tamariuchalet@gmail.com';
        errorEl.style.display = 'block';
      }
    } catch (err) {
      errorText.textContent = 'Could not connect to the server. Please email us directly at tamariuchalet@gmail.com';
      errorEl.style.display = 'block';
    } finally {
      btn.disabled    = false;
      btn.textContent = btn.dataset.bookingLabel || 'Send Enquiry';
    }
  });
}

// ── FADE IN ON SCROLL ──
const fadeEls = document.querySelectorAll('.fade-in');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });

fadeEls.forEach(el => observer.observe(el));

// Add fade-in CSS dynamically
const style = document.createElement('style');
style.textContent = `
  .fade-in { opacity: 0; transform: translateY(20px); transition: opacity 0.6s ease, transform 0.6s ease; }
  .fade-in.visible { opacity: 1; transform: translateY(0); }
`;
document.head.appendChild(style);
