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
  const langGroup = document.getElementById('invoice-lang-group');
  if (sect)      sect.style.display      = isBook ? '' : 'none';
  if (typeHid)   typeHid.value           = isBook ? 'Booking Enquiry' : 'General Message';
  if (submitBtn) submitBtn.dataset.booking = isBook ? '1' : '';
  if (langGroup) langGroup.style.display = isBook ? '' : 'none';
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

// ── PDF BOOKING CONFIRMATION ─────────────────────────────────

// Translations for PDF text in all 5 site languages
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
    title:    'Confirmacion Provisional de Reserva',
    dear:     'Estimado/a',
    intro:    function(room) { return 'Gracias por su consulta. Hemos reservado ' + room + ' para usted'; },
    dates:    function(ci, co) { return 'entre el ' + ci + ' y el ' + co + '.'; },
    roomLine: function(room, nights, rate, extra, cleaning, roomTotal) {
      var s = '  ' + room + ': ' + nights + ' noche' + (nights !== 1 ? 's' : '') + ' x €' + rate + '/noche';
      if (extra) s += ' + ' + extra + ' huesped' + (extra > 1 ? 'es' : '') + ' extra x €50/noche';
      s += ' + €' + cleaning + ' limpieza = €' + roomTotal;
      return s;
    },
    totalLabel:  'TOTAL A PAGAR',
    payment48:   'Este pago debe realizarse en las 48 horas siguientes a la recepcion de este documento.',
    payTo:       function(total) { return 'Por favor, pague €' + total + ' a Kieran Reid en el IBAN BE14967986191383.'; },
    reserve:     'Su reserva quedara confirmada una vez recibido el pago.',
    cancel:      'Su reserva estara sujeta a nuestra politica de cancelacion de 7 dias, como se indica en el sitio web.',
    regards:     'Atentamente,',
    team:        'El equipo de Tamariu Chalet',
    issued:      'Emitido',
    ref:         'Ref',
    costHeading: 'Desglose de Costes',
  },
  ca: {
    title:    'Confirmacio Provisional de Reserva',
    dear:     'Estimat/da',
    intro:    function(room) { return 'Gracies per la seva consulta. Hem reservat ' + room + ' per a voste'; },
    dates:    function(ci, co) { return 'entre el ' + ci + ' i el ' + co + '.'; },
    roomLine: function(room, nights, rate, extra, cleaning, roomTotal) {
      var s = '  ' + room + ': ' + nights + ' nit' + (nights !== 1 ? 's' : '') + ' x €' + rate + '/nit';
      if (extra) s += ' + ' + extra + ' hoste' + (extra > 1 ? 's' : '') + ' extra x €50/nit';
      s += ' + €' + cleaning + ' neteja = €' + roomTotal;
      return s;
    },
    totalLabel:  'TOTAL A PAGAR',
    payment48:   "Aquest pagament s'ha de fer en les 48 hores seguents a la recepcio d'aquest document.",
    payTo:       function(total) { return "Si us plau, pagui €" + total + " a Kieran Reid a l'IBAN BE14967986191383."; },
    reserve:     'La seva reserva quedara confirmada un cop rebut el pagament.',
    cancel:      "La seva reserva estara subjecta a la nostra politica de cancel lacio de 7 dies, tal com s'indica al lloc web.",
    regards:     'Cordialment,',
    team:        "L'equip de Tamariu Chalet",
    issued:      'Emes',
    ref:         'Ref',
    costHeading: 'Desglossament de Costos',
  },
  fr: {
    title:    'Confirmation de Reservation Provisoire',
    dear:     'Cher/Chere',
    intro:    function(room) { return 'Merci pour votre demande. Nous avons reserve ' + room + ' pour vous'; },
    dates:    function(ci, co) { return 'du ' + ci + ' au ' + co + '.'; },
    roomLine: function(room, nights, rate, extra, cleaning, roomTotal) {
      var s = '  ' + room + ': ' + nights + ' nuit' + (nights !== 1 ? 's' : '') + ' x €' + rate + '/nuit';
      if (extra) s += ' + ' + extra + ' hote' + (extra > 1 ? 's' : '') + ' suppl. x €50/nuit';
      s += ' + €' + cleaning + ' menage = €' + roomTotal;
      return s;
    },
    totalLabel:  'TOTAL DU',
    payment48:   'Ce paiement doit etre effectue dans les 48 heures suivant la reception de ce document.',
    payTo:       function(total) { return "Veuillez payer €" + total + " a Kieran Reid a l'IBAN BE14967986191383."; },
    reserve:     'Votre reservation sera confirmee des reception du paiement.',
    cancel:      "Votre reservation sera soumise a notre politique d'annulation de 7 jours, telle qu'indiquee sur le site web.",
    regards:     'Cordialement,',
    team:        "L'equipe Tamariu Chalet",
    issued:      'Emis le',
    ref:         'Ref',
    costHeading: 'Detail des Couts',
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

// Collect structured cost data for PDF generation
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

// Generate and auto-download the booking confirmation PDF
function generateBookingPDF(guestName, langKey) {
  var data = buildCostData();
  if (!data) return false;
  if (typeof window.jspdf === 'undefined') {
    console.warn('jsPDF not loaded - PDF skipped');
    return false;
  }
  var jsPDF = window.jspdf.jsPDF;
  var doc   = new jsPDF({ unit: 'mm', format: 'a4' });
  var t     = PDF_LANG[langKey] || PDF_LANG.en;
  var lm = 20, rm = 190, pw = rm - lm, y = 20;

  // Header band
  doc.setFillColor(30, 60, 100);
  doc.rect(0, 0, 210, 28, 'F');
  doc.setFont('helvetica', 'bold');
  doc.setFontSize(18);
  doc.setTextColor(255, 255, 255);
  doc.text('Tamariu Chalet', lm, 13);
  doc.setFontSize(8);
  doc.setFont('helvetica', 'normal');
  doc.text("Carrer de la Punta De L'Estela 7  •  Tamariu, Costa Brava, Spain  •  tamariuchalet.com", lm, 21);
  y = 40;

  // Title
  doc.setFont('helvetica', 'bold');
  doc.setFontSize(13);
  doc.setTextColor(30, 60, 100);
  doc.text(t.title, lm, y);
  y += 7;

  // Ref & date
  var now    = new Date();
  var refNum = 'TC-' + now.getFullYear() +
               String(now.getMonth() + 1).padStart(2,'0') +
               String(now.getDate()).padStart(2,'0') + '-' +
               String(now.getHours()).padStart(2,'0') +
               String(now.getMinutes()).padStart(2,'0');
  doc.setFont('helvetica', 'normal');
  doc.setFontSize(8);
  doc.setTextColor(120, 120, 120);
  doc.text(t.issued + ': ' + fmtDate(now.toISOString().slice(0,10)) + '   ' + t.ref + ': ' + refNum, lm, y);
  y += 10;

  // Salutation
  doc.setFontSize(11);
  doc.setTextColor(40, 40, 40);
  doc.text(t.dear + ' ' + guestName + ',', lm, y);
  y += 8;

  // Intro
  var roomNames = data.rooms.map(function(r){ return r.name; }).join(' & ');
  var introText = t.intro(roomNames) + ' ' + t.dates(fmtDate(data.checkIn), fmtDate(data.checkOut));
  doc.setFontSize(10.5);
  var introW = doc.splitTextToSize(introText, pw);
  doc.text(introW, lm, y);
  y += introW.length * 6 + 6;

  // Cost box
  var boxH = data.rooms.length * 8 + 22;
  doc.setFillColor(245, 242, 235);
  doc.rect(lm, y, pw, boxH, 'F');
  doc.setDrawColor(30, 60, 100);
  doc.setLineWidth(0.5);
  doc.rect(lm, y, pw, boxH, 'D');
  y += 7;
  doc.setFont('helvetica', 'bold');
  doc.setFontSize(9);
  doc.setTextColor(30, 60, 100);
  doc.text(t.costHeading, lm + 4, y);
  y += 6;
  doc.setFont('helvetica', 'normal');
  doc.setFontSize(9);
  doc.setTextColor(40, 40, 40);
  data.rooms.forEach(function(r) {
    var line = t.roomLine(r.name, r.nights, r.rate, r.extra, r.cleaning, r.roomTotal);
    var lw   = doc.splitTextToSize(line, pw - 8);
    doc.text(lw, lm + 4, y);
    y += lw.length * 5.5 + 1;
  });
  y += 3;
  doc.setDrawColor(30, 60, 100);
  doc.setLineWidth(0.3);
  doc.line(lm + 4, y, rm - 4, y);
  y += 5;
  doc.setFont('helvetica', 'bold');
  doc.setFontSize(10);
  doc.setTextColor(30, 60, 100);
  doc.text(t.totalLabel + ': €' + data.totalCost, lm + 4, y);
  y += 12;

  // Payment paragraphs
  doc.setFont('helvetica', 'normal');
  doc.setFontSize(10.5);
  doc.setTextColor(40, 40, 40);
  [t.payment48, t.payTo(data.totalCost), t.reserve, t.cancel].forEach(function(para) {
    var pw2 = doc.splitTextToSize(para, pw);
    doc.text(pw2, lm, y);
    y += pw2.length * 6 + 3;
  });

  y += 4;
  doc.text(t.regards, lm, y);  y += 6;
  doc.setFont('helvetica', 'bold');
  doc.text(t.team, lm, y);     y += 5;
  doc.setFontSize(8);
  doc.setFont('helvetica', 'normal');
  doc.setTextColor(120, 120, 120);
  doc.text('tamariuchalet@gmail.com  •  +34 626 788 866  •  tamariuchalet.com', lm, y);

  // Page footer
  doc.setDrawColor(30, 60, 100);
  doc.setLineWidth(0.4);
  doc.line(lm, 285, rm, 285);
  doc.setFontSize(7.5);
  doc.text('Tamariu Chalet  •  tamariuchalet.com  •  tamariuchalet@gmail.com', 105, 290, { align: 'center' });

  var safe = (guestName || 'guest').replace(/[^a-z0-9]/gi, '_');
  doc.save('TamariuChalet_Booking_' + safe + '_' + data.checkIn + '.pdf');
  return true;
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

    try {
      const response = await fetch('https://formspree.io/f/xleqevwo', {
        method: 'POST',
        body: new FormData(contactForm),
        headers: { 'Accept': 'application/json' }
      });
      const result = await response.json();
      if (result.ok) {
        // Generate & download PDF for booking enquiries
        if (isBooking) {
          const guestName = document.getElementById('guest-name')?.value || '';
          const langKey   = document.getElementById('invoice-lang')?.value || 'en';
          generateBookingPDF(guestName, langKey);
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
// These are set by the availability calendar "Book These Dates" link.
(function prefillFromURL() {
  const contactForm = document.getElementById('contact-form');
  if (!contactForm) return; // only runs on contact page

  const params   = new URLSearchParams(window.location.search);
  const room     = params.get('room');
  const checkin  = params.get('checkin');
  const checkout = params.get('checkout');

  // Pre-select room checkbox
  if (room) {
    const checkbox = document.querySelector(`.room-checkbox[value="${room}"]`);
    if (checkbox) {
      checkbox.checked = true;
      // Trigger apt extra-guest row if needed
      if (room === 'studio-apartment' && typeof handleAptChange === 'function') {
        handleAptChange();
      }
    }
  }

  // Pre-fill dates
  const ciInput = document.getElementById('booking-checkin');
  const coInput = document.getElementById('booking-checkout');
  if (checkin  && ciInput) ciInput.value  = checkin;
  if (checkout && coInput) coInput.value = checkout;

  // Recalculate cost if we have all three
  if ((room || checkin || checkout) && typeof calcCost === 'function') {
    calcCost();
  }

  // If dates were passed, scroll booking form into view gently
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
