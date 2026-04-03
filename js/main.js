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

function renderRatesTables() {
  document.querySelectorAll('table.rates-table[data-room-type]').forEach(table => {
    const isApt = table.dataset.roomType === 'apartment';
    const tbody = table.querySelector('tbody');
    if (!tbody) return;
    tbody.innerHTML = '';
    SEASON_CONFIG.forEach(s => {
      const d = isApt ? s.apt : s.room;
      const closed = d.rate === null;
      tbody.innerHTML += `
        <tr>
          <td class="season-name">${s.name}</td>
          <td>${s.dates}</td>
          <td>${closed ? '<span class="closed-cell">Closed</span>' : `<span class="rate-highlight">€${d.rate}</span>`}</td>
          <td>${closed ? '—' : `${d.minStay} nights`}</td>
          <td>${closed ? '—' : `€${d.cleaning}`}</td>
        </tr>`;
    });
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

// ── BOOKING FORM — Cost Calculator ──

function getSeason(date) {
  const m = date.getMonth() + 1;
  const d = date.getDate();
  for (const s of SEASON_CONFIG) {
    const [sm, sd] = s.start;
    const [em, ed] = s.end;
    const afterStart = m > sm || (m === sm && d >= sd);
    const beforeEnd  = m < em || (m === em && d <= ed);
    if (afterStart && beforeEnd) return s;
  }
  return SEASON_CONFIG[SEASON_CONFIG.length - 1];
}

function daysBetween(d1, d2) {
  return Math.round((d2 - d1) / 86400000);
}

function calcCost() {
  const roomVal  = document.getElementById('booking-room')?.value;
  const checkIn  = document.getElementById('booking-checkin')?.value;
  const checkOut = document.getElementById('booking-checkout')?.value;
  const costEl   = document.getElementById('booking-cost');
  const breakEl  = document.getElementById('booking-breakdown');

  if (!roomVal || !checkIn || !checkOut || !costEl) return;

  const d1 = new Date(checkIn);
  const d2 = new Date(checkOut);
  if (d2 <= d1) { costEl.textContent = '—'; breakEl.textContent = 'Check-out must be after check-in'; return; }

  const nights   = daysBetween(d1, d2);
  const season   = getSeason(d1);
  const isApt    = APARTMENT_ROOMS.includes(roomVal);
  const rateData = isApt ? season.apt : season.room;

  if (!rateData.rate) {
    costEl.textContent = '—';
    breakEl.textContent = `Rooms closed in ${season.name} (Jan–Apr)`;
    return;
  }

  if (nights < rateData.minStay) {
    costEl.textContent = '—';
    breakEl.textContent = `Minimum ${rateData.minStay} nights in ${season.name}`;
    return;
  }

  const accom  = nights * rateData.rate;
  const total  = accom + rateData.cleaning;
  costEl.textContent = `€${total}`;
  breakEl.textContent = `${nights} nights × €${rateData.rate} + €${rateData.cleaning} cleaning`;
}

// Bind events
['booking-room','booking-checkin','booking-checkout'].forEach(id => {
  const el = document.getElementById(id);
  if (el) el.addEventListener('change', calcCost);
});

// ── CONTACT FORM SUBMISSION — PHP mailer ──
// Keep cost-hidden field in sync with the displayed cost
document.addEventListener('change', () => {
  const costEl  = document.getElementById('booking-cost');
  const hidden  = document.getElementById('cost-hidden');
  if (costEl && hidden) hidden.value = costEl.textContent;
});

const contactForm = document.getElementById('contact-form');
if (contactForm) {
  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Sync hidden cost field before submit
    const costEl = document.getElementById('booking-cost');
    const hidden = document.getElementById('cost-hidden');
    if (costEl && hidden) hidden.value = costEl.textContent;

    const btn       = document.getElementById('submit-btn');
    const successEl = document.getElementById('form-success');
    const errorEl   = document.getElementById('form-error');
    const errorText = document.getElementById('error-text');

    // Reset messages
    successEl.style.display = 'none';
    errorEl.style.display   = 'none';

    // Disable button while sending
    btn.disabled    = true;
    btn.textContent = 'Sending…';

    try {
      const formData = new FormData(contactForm);

      // send-mail.php lives at the site root, one level up from /contact/
      const response = await fetch('../send-mail.php', {
        method: 'POST',
        body: formData
      });

      const result = await response.json();

      if (result.success) {
        successEl.style.display = 'block';
        contactForm.reset();
        document.getElementById('booking-cost').textContent     = '—';
        document.getElementById('booking-breakdown').textContent = 'Select room & dates';
      } else {
        errorText.textContent  = result.message || 'Something went wrong. Please email us directly at tamariuchalet@gmail.com';
        errorEl.style.display  = 'block';
      }
    } catch (err) {
      errorText.textContent = 'Could not connect to the server. Please email us directly at tamariuchalet@gmail.com';
      errorEl.style.display = 'block';
    } finally {
      btn.disabled    = false;
      btn.textContent = 'Send Enquiry';
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
