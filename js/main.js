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
function renderRatesTables() {
  document.querySelectorAll('table.rates-table[data-room-type]').forEach(table => {
    const type  = table.dataset.roomType;
    if (type === 'summary') return;
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

function daysBetween(d1, d2) {
  return Math.round((d2 - d1) / (1000 * 60 * 60 * 24));
}

function getSeason(date) {
  const m = date.getMonth() + 1;
  const d = date.getDate();
  const n = m * 100 + d;
  for (const s of SEASON_CONFIG) {
    const startN = s.start[0] * 100 + s.start[1];
    const endN   = s.end[0]   * 100 + s.end[1];
    if (n >= startN && n <= endN) return s;
  }
  return SEASON_CONFIG[0];
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
    // Still update the checkout min/hint even if checkout isn't chosen yet
    updateCheckoutMin();
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

  // Update checkout min attribute + show/hide warning banner
  updateCheckoutMin();

  checked.forEach(cb => {
    const val   = cb.value;
    const isApt = APARTMENT_ROOMS.includes(val);
    const d     = isApt ? season.apt : season.room;
    const name  = ROOM_NAMES[val] || val;

    if (typeof isRoomAvailable === 'function' && !isRoomAvailable(val, checkIn, checkOut)) {
      lines.push('<span style="color:#c0392b">❌ ' + name + ': not available for those dates</span>');
      hasUnavailable = true;
      hasError = true;
      return;
    }

    if (!d.rate) {
      lines.push('⚠️ ' + name + ': closed in ' + season.name + ' season');
      hasError = true; return;
    }
    if (nights < d.minStay) {
      lines.push('⚠️ ' + name + ': min ' + d.minStay + ' nights in ' + season.name);
      hasError = true; return;
    }

    let roomCost = nights * d.rate + d.cleaning;
    if (isApt && extraGuests > 0) {
      const extra = extraGuests * 50 * nights;
      roomCost += extra;
      lines.push('✅ ' + name + ': ' + nights + 'n \xd7 €' + d.rate +
        ' + ' + extraGuests + ' extra guest' + (extraGuests > 1 ? 's' : '') +
        ' \xd7 €50 \xd7 ' + nights + 'n + €' + d.cleaning + ' cleaning = €' + roomCost);
    } else {
      lines.push('✅ ' + name + ': ' + nights + 'n \xd7 €' + d.rate +
        ' + €' + d.cleaning + ' cleaning = €' + roomCost);
    }
    totalCost += roomCost;
  });

  if (hasUnavailable) {
    costEl.textContent = 'Not available';
    costEl.style.color = '#c0392b';
  } else {
    const displayCost = (!hasError || totalCost > 0) ? ('€' + totalCost) : '—';
    costEl.textContent = displayCost;
    costEl.style.color = '';
    if (hidden) hidden.value = displayCost;
  }

  if (breakEl) breakEl.innerHTML = lines.join('<br>');
  _updateSubmitAvailability(!hasUnavailable);

  const roomsHidden = document.getElementById('rooms-hidden');
  if (roomsHidden) roomsHidden.value = checked.map(c => ROOM_NAMES[c.value] || c.value).join(', ');
}

// ── MIN-STAY CHECKOUT ENFORCEMENT ──────────────────────────────
// Called from calcCost() whenever rooms or dates change.
// Sets the 'min' attribute on the checkout date input so browsers
// prevent the guest selecting fewer nights than required, and
// shows / hides the amber warning banner.
function updateCheckoutMin() {
  const ciInput  = document.getElementById('booking-checkin');
  const coInput  = document.getElementById('booking-checkout');
  const warnDiv  = document.getElementById('min-stay-warning');
  const warnText = document.getElementById('min-stay-text');
  if (!coInput) return;

  const checkIn = ciInput?.value;
  const checked = Array.from(document.querySelectorAll('.room-checkbox:checked'));

  if (!checkIn || checked.length === 0) {
    coInput.removeAttribute('min');
    if (warnDiv) warnDiv.style.display = 'none';
    return;
  }

  const d1 = new Date(checkIn);
  if (isNaN(d1)) { if (warnDiv) warnDiv.style.display = 'none'; return; }

  const season = getSeason(d1);
  let maxMin = 0, maxMinSeason = '';
  checked.forEach(cb => {
    const isApt = APARTMENT_ROOMS.includes(cb.value);
    const d     = isApt ? season.apt : season.room;
    if (d.rate !== null && d.minStay > maxMin) {
      maxMin       = d.minStay;
      maxMinSeason = season.name;
    }
  });

  if (maxMin === 0) {
    coInput.removeAttribute('min');
    if (warnDiv) warnDiv.style.display = 'none';
    return;
  }

  // Set the minimum allowed checkout date
  const minCo = new Date(d1);
  minCo.setDate(minCo.getDate() + maxMin);
  const minCoStr = minCo.toISOString().split('T')[0];
  coInput.min = minCoStr;

  if (!warnDiv || !warnText) return;

  const checkOut = coInput.value;
  if (!checkOut) {
    // No checkout yet — show a hint so guests know what's expected
    warnDiv.style.display = '';
    warnText.textContent  =
      'Minimum stay is ' + maxMin + ' nights during ' + maxMinSeason +
      ' season. Please select your check-out date accordingly.';
  } else {
    const nights = daysBetween(d1, new Date(checkOut));
    if (nights < maxMin) {
      const fmt = minCo.toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' });
      warnDiv.style.display = '';
      warnText.textContent  =
        'Minimum stay is ' + maxMin + ' nights during ' + maxMinSeason +
        ' season. Your check-out must be ' + fmt + ' or later.';
    } else {
      warnDiv.style.display = 'none';
    }
  }
}

function _updateSubmitAvailability(available) {
  const btn = document.getElementById('submit-btn');
  if (!btn) return;
  btn.disabled = !available;
  btn.title    = available ? '' : 'Please choose different dates — one or more rooms are already booked for this period';
  btn.style.opacity = available ? '' : '0.5';
}

function toggleEnquiryType() {
  const val       = document.querySelector('input[name="enquiry-type"]:checked')?.value;
  const isBook    = val === 'booking';
  const sect      = document.getElementById('booking-section');
  const typeHid   = document.getElementById('enquiry-type-hidden');
  const submitBtn = document.getElementById('submit-btn');
  const langGroup = document.getElementById('invoice-lang-group');
  if (sect)      sect.style.display       = isBook ? '' : 'none';
  if (typeHid)   typeHid.value            = isBook ? 'Booking Enquiry' : 'General Message';
  if (submitBtn) submitBtn.dataset.booking = isBook ? '1' : '';
  if (langGroup) langGroup.style.display  = isBook ? '' : 'none';
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

// ── EMAILJS CONFIGURATION ──────────────────────────────────────
// 1. Sign up free at https://www.emailjs.com
// 2. Add an Email Service (connect your Gmail: tamariuchalet@gmail.com)
// 3. Create an Email Template with these fields:
//      To Email : {{to_email}}
//      To Name  : {{to_name}}
//      Subject  : {{subject}}
//      Body     : {{message}}
// 4. Fill in your credentials below:
const EMAILJS_PUBLIC_KEY  = 'ooRh9XbjSEoX4M5cc';       // Account > API Keys
const EMAILJS_SERVICE_ID  = 'service_006p22o';          // Email Services tab
const EMAILJS_TEMPLATE_ID = 'template_wb6mqai';         // Email Templates tab
// ──────────────────────────────────────────────────────────────

// Email subject lines per language
const EMAIL_SUBJECTS = {
  en: 'Tamariu Chalet — Provisional Booking Confirmation',
  es: 'Tamariu Chalet — Confirmación Provisional de Reserva',
  ca: 'Tamariu Chalet — Confirmació Provisional de Reserva',
  fr: 'Tamariu Chalet — Confirmation de Réservation Provisoire',
  nl: 'Tamariu Chalet — Voorlopige Boekingsbevestiging',
};


// ── BOOKING EMAIL TRANSLATIONS ───────────────────────────────
// Used by composeGuestEmail() (in guest's language) and
// composeOwnerEmail() (always English via PDF_LANG.en)

// Translations for booking confirmation emails in all 5 site languages
const PDF_LANG = {
  en: {
    title:    'Provisional Booking Confirmation',
    dear:     'Dear',
    intro:    function(room) { return 'Thank you for your enquiry. We have reserved the ' + room + ' for you'; },
    dates:    function(ci, co) { return 'between ' + ci + ' and ' + co + '.'; },
    roomLine: function(room, nights, rate, extra, cleaning, roomTotal) {
      var s = '  ' + room + ': ' + nights + ' night' + (nights !== 1 ? 's' : '') + ' x €' + rate + '/night';
      if (extra) s += ' + ' + extra + ' extra guest' + (extra > 1 ? 's' : '') + ' x €50/night';
      s += ' + €' + cleaning + ' cleaning = €' + roomTotal;
      return s;
    },
    totalLabel:  'TOTAL DUE',
    payment48:   'This payment must be made within 48 hours of receipt of this document.',
    payTo:       function(total) { return 'Please pay €' + total + ' to Kieran Reid at IBAN BE14967986191383.'; },
    reserve:     'Your booking will be reserved on receipt of the payment.',
    cancel:      'Your booking will be subject to our 7-day cancellation policy as stated on the website.',
    regards:     'Kind regards,',
    team:        'The Tamariu Chalet Team',
    issued:      'Issued',
    ref:         'Ref',
    costHeading: 'Cost Breakdown',
  },
  es: {
    title:    'Confirmación Provisional de Reserva',
    dear:     'Estimado/a',
    intro:    function(room) { return 'Gracias por su consulta. Hemos reservado ' + room + ' para usted'; },
    dates:    function(ci, co) { return 'entre el ' + ci + ' y el ' + co + '.'; },
    roomLine: function(room, nights, rate, extra, cleaning, roomTotal) {
      var s = '  ' + room + ': ' + nights + ' noche' + (nights !== 1 ? 's' : '') + ' x €' + rate + '/noche';
      if (extra) s += ' + ' + extra + ' huésped' + (extra > 1 ? 'es' : '') + ' extra x €50/noche';
      s += ' + €' + cleaning + ' limpieza = €' + roomTotal;
      return s;
    },
    totalLabel:  'TOTAL A PAGAR',
    payment48:   'Este pago debe realizarse en las 48 horas siguientes a la recepción de este documento.',
    payTo:       function(total) { return 'Por favor, pague €' + total + ' a Kieran Reid en el IBAN BE14967986191383.'; },
    reserve:     'Su reserva quedará confirmada una vez recibido el pago.',
    cancel:      'Su reserva estará sujeta a nuestra política de cancelación de 7 días, como se indica en el sitio web.',
    regards:     'Atentamente,',
    team:        'El equipo de Tamariu Chalet',
    issued:      'Emitido',
    ref:         'Ref',
    costHeading: 'Desglose de Costes',
  },
  ca: {
    title:    'Confirmació Provisional de Reserva',
    dear:     'Estimat/da',
    intro:    function(room) { return 'Gràcies per la seva consulta. Hem reservat ' + room + ' per a vostè'; },
    dates:    function(ci, co) { return 'entre el ' + ci + ' i el ' + co + '.'; },
    roomLine: function(room, nights, rate, extra, cleaning, roomTotal) {
      var s = '  ' + room + ': ' + nights + ' nit' + (nights !== 1 ? 's' : '') + ' x €' + rate + '/nit';
      if (extra) s += ' + ' + extra + ' hoste' + (extra > 1 ? 's' : '') + ' extra x €50/nit';
      s += ' + €' + cleaning + ' neteja = €' + roomTotal;
      return s;
    },
    totalLabel:  'TOTAL A PAGAR',
    payment48:   'Aquest pagament s\'ha de fer en les 48 hores següents a la recepció d\'aquest document.',
    payTo:       function(total) { return 'Si us plau, pagui €' + total + ' a Kieran Reid a l\'IBAN BE14967986191383.'; },
    reserve:     'La seva reserva quedarà confirmada un cop rebut el pagament.',
    cancel:      'La seva reserva estarà subjecta a la nostra política de cancel·lació de 7 dies, tal com s\'indica al lloc web.',
    regards:     'Cordialment,',
    team:        'L\'equip de Tamariu Chalet',
    issued:      'Emès',
    ref:         'Ref',
    costHeading: 'Desglossament de Costos',
  },
  fr: {
    title:    'Confirmation de Réservation Provisoire',
    dear:     'Cher/Chère',
    intro:    function(room) { return 'Merci pour votre demande. Nous avons réservé ' + room + ' pour vous'; },
    dates:    function(ci, co) { return 'du ' + ci + ' au ' + co + '.'; },
    roomLine: function(room, nights, rate, extra, cleaning, roomTotal) {
      var s = '  ' + room + ': ' + nights + ' nuit' + (nights !== 1 ? 's' : '') + ' x €' + rate + '/nuit';
      if (extra) s += ' + ' + extra + ' hôte' + (extra > 1 ? 's' : '') + ' suppl. x €50/nuit';
      s += ' + €' + cleaning + ' ménage = €' + roomTotal;
      return s;
    },
    totalLabel:  'TOTAL DÛ',
    payment48:   'Ce paiement doit être effectué dans les 48 heures suivant la réception de ce document.',
    payTo:       function(total) { return 'Veuillez payer €' + total + ' à Kieran Reid à l\'IBAN BE14967986191383.'; },
    reserve:     'Votre réservation sera confirmée dès réception du paiement.',
    cancel:      'Votre réservation sera soumise à notre politique d\'annulation de 7 jours, telle qu\'indiquée sur le site web.',
    regards:     'Cordialement,',
    team:        'L\'équipe Tamariu Chalet',
    issued:      'Émis le',
    ref:         'Réf',
    costHeading: 'Détail des Coûts',
  },
  nl: {
    title:    'Voorlopige Boekingsbevestiging',
    dear:     'Beste',
    intro:    function(room) { return 'Bedankt voor uw aanvraag. Wij hebben ' + room + ' voor u gereserveerd'; },
    dates:    function(ci, co) { return 'van ' + ci + ' tot ' + co + '.'; },
    roomLine: function(room, nights, rate, extra, cleaning, roomTotal) {
      var s = '  ' + room + ': ' + nights + ' nacht' + (nights !== 1 ? 'en' : '') + ' x €' + rate + '/nacht';
      if (extra) s += ' + ' + extra + ' extra gast' + (extra > 1 ? 'en' : '') + ' x €50/nacht';
      s += ' + €' + cleaning + ' schoonmaak = €' + roomTotal;
      return s;
    },
    totalLabel:  'TOTAAL VERSCHULDIGD',
    payment48:   'Deze betaling moet worden voldaan binnen 48 uur na ontvangst van dit document.',
    payTo:       function(total) { return 'Betaal €' + total + ' aan Kieran Reid op IBAN BE14967986191383.'; },
    reserve:     'Uw reservering wordt bevestigd na ontvangst van de betaling.',
    cancel:      'Uw reservering is onderworpen aan ons 7-daagse annuleringsbeleid zoals vermeld op de website.',
    regards:     'Met vriendelijke groet,',
    team:        'Het Tamariu Chalet team',
    issued:      'Uitgegeven op',
    ref:         'Ref',
    costHeading: 'Kostenoverzicht',
  },
};

// Collect structured cost data (shared by PDF generator and email composer)
function buildCostData() {
  var checkIn     = document.getElementById('booking-checkin')  ? document.getElementById('booking-checkin').value  : '';
  var checkOut    = document.getElementById('booking-checkout') ? document.getElementById('booking-checkout').value : '';
  var checked     = Array.from(document.querySelectorAll('.room-checkbox:checked'));
  var extraGuests = parseInt((document.getElementById('extra-guests') ? document.getElementById('extra-guests').value : '0') || '0');
  if (!checkIn || !checkOut || checked.length === 0) return null;
  var d1 = new Date(checkIn), d2 = new Date(checkOut);
  if (isNaN(d1.getTime()) || isNaN(d2.getTime()) || d2 <= d1) return null;
  var nights = daysBetween(d1, d2);
  var season = getSeason(d1);
  var rooms  = [];
  var total  = 0;
  checked.forEach(function(cb) {
    var val   = cb.value;
    var isApt = APARTMENT_ROOMS.includes(val);
    var d     = isApt ? season.apt : season.room;
    var name  = ROOM_NAMES[val] || val;
    if (!d.rate) return;
    var extra     = isApt ? extraGuests : 0;
    var roomTotal = nights * d.rate + d.cleaning + (extra * 50 * nights);
    total += roomTotal;
    rooms.push({ name: name, nights: nights, rate: d.rate, extra: extra, cleaning: d.cleaning, roomTotal: roomTotal });
  });
  if (rooms.length === 0) return null;
  return { checkIn: checkIn, checkOut: checkOut, nights: nights, rooms: rooms, totalCost: total };
}

// Format "YYYY-MM-DD" as "1 Jan 2026"
function fmtDate(iso) {
  var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var d = new Date(iso);
  return d.getDate() + ' ' + months[d.getMonth()] + ' ' + d.getFullYear();
}

// Compose booking confirmation email for the guest (in their chosen language)
function composeGuestEmail(guestName, langKey, data) {
  var t   = PDF_LANG[langKey] || PDF_LANG.en;
  var sep = '----------------------------------------';

  var roomNames = data.rooms.map(function(r) { return r.name; }).join(' & ');

  var body  = t.dear + ' ' + guestName + ',\n\n';
  body += t.intro(roomNames) + ' ' + t.dates(fmtDate(data.checkIn), fmtDate(data.checkOut)) + '\n\n';

  body += t.costHeading + ':\n';
  data.rooms.forEach(function(r) {
    body += t.roomLine(r.name, r.nights, r.rate, r.extra, r.cleaning, r.roomTotal) + '\n';
  });
  body += sep + '\n';
  body += t.totalLabel + ': €' + data.totalCost + '\n\n';

  body += t.payment48 + '\n\n';
  body += t.payTo(data.totalCost) + '\n\n';
  body += t.reserve + '\n\n';
  body += t.cancel + '\n\n';
  body += sep + '\n';
  body += t.regards + '\n';
  body += t.team + '\n';
  body += 'tamariuchalet@gmail.com  |  +34 626 788 866  |  tamariuchalet.com';

  return body;
}



// ── CONTACT FORM SUBMISSION ──
const contactForm = document.getElementById('contact-form');
if (contactForm) {
  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();

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
    btn.textContent = 'Sending…';

    const isBooking = document.querySelector('input[name="enquiry-type"]:checked')?.value === 'booking';
    const guestName = document.getElementById('guest-name')?.value || '';
    const guestEmail = document.getElementById('guest-email')?.value || '';
    const langKey   = document.getElementById('invoice-lang')?.value || 'en';

    try {
      // 1. Send enquiry data to owner via Formspree
      const response = await fetch('https://formspree.io/f/xleqevwo', {
        method: 'POST',
        body: new FormData(contactForm),
        headers: { 'Accept': 'application/json' }
      });
      const result = await response.json();

      if (result.ok) {
        if (isBooking) {
          const costData = buildCostData();

          // 2. Send booking confirmation email via EmailJS (CC copies tamariuchalet@gmail.com)
          if (EMAILJS_PUBLIC_KEY !== 'YOUR_PUBLIC_KEY' && guestEmail && costData) {
            try {
              emailjs.init({ publicKey: EMAILJS_PUBLIC_KEY });

              await emailjs.send(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, {
                to_email: guestEmail,
                to_name:  guestName,
                cc_email: 'tamariuchalet@gmail.com',
                subject:  EMAIL_SUBJECTS[langKey] || EMAIL_SUBJECTS.en,
                message:  composeGuestEmail(guestName, langKey, costData),
              });

            } catch (ejsErr) {
              console.warn('EmailJS error:', ejsErr);
            }
          }
        }

        successEl.style.display = 'block';
        contactForm.reset();
        const bCost  = document.getElementById('booking-cost');
        const bBreak = document.getElementById('booking-breakdown');
        if (bCost)  bCost.textContent  = '—';
        if (bBreak) bBreak.textContent = 'Select rooms & dates';
        const aptDiv = document.getElementById('apt-extra-guests');
        if (aptDiv) aptDiv.style.display = 'none';
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

// ── CONTACT FORM — Pre-fill from URL params ──────────────────
// Reads ?room=double-room&checkin=2026-07-01&checkout=2026-07-08
(function prefillFromURL() {
  const contactForm = document.getElementById('contact-form');
  if (!contactForm) return;

  const params   = new URLSearchParams(window.location.search);
  const room     = params.get('room');
  const checkin  = params.get('checkin');
  const checkout = params.get('checkout');

  if (room) {
    const checkbox = document.querySelector(`.room-checkbox[value="${room}"]`);
    if (checkbox) {
      checkbox.checked = true;
      if (room === 'studio-apartment' && typeof handleAptChange === 'function') {
        handleAptChange();
      }
    }
  }

  const ciInput = document.getElementById('booking-checkin');
  const coInput = document.getElementById('booking-checkout');
  if (checkin  && ciInput) ciInput.value  = checkin;
  if (checkout && coInput) coInput.value = checkout;

  if ((room || checkin || checkout) && typeof calcCost === 'function') {
    calcCost();
  }

  if (checkin && checkout) {
    setTimeout(() => {
      const formEl = document.querySelector('.booking-form');
      if (formEl) formEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 350);
  }
})();

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
