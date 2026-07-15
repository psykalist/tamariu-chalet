// ============================================================
// TAMARIU CHALET — Availability Calendar
// ============================================================
// Renders an interactive per-room availability calendar.
// Reads booked dates from BOOKINGS (bookings.js) and
// open/closed seasons from SEASON_CONFIG (rates.js).
//
// Usage: included by availability/index.html
// ============================================================

(function () {
  'use strict';

  // ── Translations ────────────────────────────────────────────
  const I18N = {
    en: {
      months: ['January','February','March','April','May','June','July','August','September','October','November','December'],
      days:   ['Mo','Tu','We','Th','Fr','Sa','Su'],
      legend_avail:   'Available',
      legend_booked:  'Booked',
      legend_closed:  'Closed season',
      legend_past:    'Past / today',
      legend_selected:'Your dates',
      selectCheckin:  'Click a green date to set check-in',
      selectCheckout: 'Now click your check-out date',
      rangeBooked:    'That range includes booked or closed dates — please choose different dates.',
      rangePast:      'Check-in cannot be in the past.',
      rangeOrder:     'Check-out must be after check-in.',
      rangeMinStay:   function(n) { return 'Minimum stay is ' + n + ' night' + (n !== 1 ? 's' : '') + ' for this room and season. Please select a later check-out date.'; },
      nights:         'night',
      nightsP:        'nights',
      btnBook:        '📅 Book These Dates',
      btnClear:       'Clear selection',
      chooseRoom:     'Choose a room to view availability',
      rooms: {
        'double-room':      'Double Room',
        'twin-room-1':      'Double/Twin Room 1',
        'twin-room-2':      'Double/Twin Room 2',
        'studio-apartment': 'Studio Apartment',
      },
    },
    es: {
      months: ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
      days:   ['Lu','Ma','Mi','Ju','Vi','Sá','Do'],
      legend_avail:   'Disponible',
      legend_booked:  'Reservado',
      legend_closed:  'Temporada cerrada',
      legend_past:    'Pasado / hoy',
      legend_selected:'Sus fechas',
      selectCheckin:  'Haz clic en una fecha verde para elegir la entrada',
      selectCheckout: 'Ahora elige la fecha de salida',
      rangeBooked:    'Ese rango incluye fechas reservadas o cerradas — elige otras fechas.',
      rangePast:      'La entrada no puede ser en el pasado.',
      rangeOrder:     'La salida debe ser posterior a la entrada.',
      rangeMinStay:   function(n) { return 'La estancia mínima es de ' + n + ' noche' + (n !== 1 ? 's' : '') + ' para esta habitación y temporada. Por favor elige una fecha de salida más tarde.'; },
      nights:         'noche',
      nightsP:        'noches',
      btnBook:        '📅 Reservar estas fechas',
      btnClear:       'Borrar selección',
      chooseRoom:     'Elige una habitación para ver disponibilidad',
      rooms: {
        'double-room':      'Habitación Doble',
        'twin-room-1':      'Habitación Doble/Twin 1',
        'twin-room-2':      'Habitación Doble/Twin 2',
        'studio-apartment': 'Apartamento Estudio',
      },
    },
    ca: {
      months: ['Gener','Febrer','Març','Abril','Maig','Juny','Juliol','Agost','Setembre','Octubre','Novembre','Desembre'],
      days:   ['Dl','Dt','Dc','Dj','Dv','Ds','Dg'],
      legend_avail:   'Disponible',
      legend_booked:  'Reservat',
      legend_closed:  'Temporada tancada',
      legend_past:    'Passat / avui',
      legend_selected:'Les teves dates',
      selectCheckin:  'Fes clic en una data verda per triar l\'entrada',
      selectCheckout: 'Ara tria la data de sortida',
      rangeBooked:    'Aquest rang inclou dates reservades o tancades — tria altres dates.',
      rangePast:      'L\'entrada no pot ser en el passat.',
      rangeOrder:     'La sortida ha de ser posterior a l\'entrada.',
      rangeMinStay:   function(n) { return 'L\'estada mínima és de ' + n + ' nit' + (n !== 1 ? 's' : '') + ' per a aquesta habitació i temporada. Si us plau, tria una data de sortida més tardana.'; },
      nights:         'nit',
      nightsP:        'nits',
      btnBook:        '📅 Reservar aquestes dates',
      btnClear:       'Esborrar selecció',
      chooseRoom:     'Tria una habitació per veure la disponibilitat',
      rooms: {
        'double-room':      'Habitació Doble',
        'twin-room-1':      'Habitació Doble/Twin 1',
        'twin-room-2':      'Habitació Doble/Twin 2',
        'studio-apartment': 'Apartament Estudi',
      },
    },
    fr: {
      months: ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre'],
      days:   ['Lu','Ma','Me','Je','Ve','Sa','Di'],
      legend_avail:   'Disponible',
      legend_booked:  'Réservé',
      legend_closed:  'Saison fermée',
      legend_past:    'Passé / aujourd\'hui',
      legend_selected:'Vos dates',
      selectCheckin:  'Cliquez sur une date verte pour choisir l\'arrivée',
      selectCheckout: 'Maintenant choisissez la date de départ',
      rangeBooked:    'Cette période inclut des dates réservées ou fermées — veuillez choisir d\'autres dates.',
      rangePast:      'L\'arrivée ne peut pas être dans le passé.',
      rangeOrder:     'Le départ doit être après l\'arrivée.',
      rangeMinStay:   function(n) { return 'La durée minimale est de ' + n + ' nuit' + (n !== 1 ? 's' : '') + ' pour cette chambre et cette saison. Veuillez choisir une date de départ plus tardive.'; },
      nights:         'nuit',
      nightsP:        'nuits',
      btnBook:        '📅 Réserver ces dates',
      btnClear:       'Effacer la sélection',
      chooseRoom:     'Choisissez une chambre pour voir la disponibilité',
      rooms: {
        'double-room':      'Chambre Double',
        'twin-room-1':      'Chambre Double/Lits Jumeaux 1',
        'twin-room-2':      'Chambre Double/Lits Jumeaux 2',
        'studio-apartment': 'Appartement Studio',
      },
    },
    nl: {
      months: ['Januari','Februari','Maart','April','Mei','Juni','Juli','Augustus','September','Oktober','November','December'],
      days:   ['Ma','Di','Wo','Do','Vr','Za','Zo'],
      legend_avail:   'Beschikbaar',
      legend_booked:  'Gereserveerd',
      legend_closed:  'Gesloten seizoen',
      legend_past:    'Verleden / vandaag',
      legend_selected:'Uw datums',
      selectCheckin:  'Klik op een groene datum voor aankomst',
      selectCheckout: 'Klik nu op uw vertrekdatum',
      rangeBooked:    'Dit bereik bevat geboekte of gesloten datums — kies andere datums.',
      rangePast:      'Aankomst kan niet in het verleden liggen.',
      rangeOrder:     'Vertrek moet na aankomst zijn.',
      rangeMinStay:   function(n) { return 'Het minimaal verblijf is ' + n + ' nacht' + (n !== 1 ? 'en' : '') + ' voor deze kamer en dit seizoen. Kies een latere vertrekdatum.'; },
      nights:         'nacht',
      nightsP:        'nachten',
      btnBook:        '📅 Boek deze datums',
      btnClear:       'Selectie wissen',
      chooseRoom:     'Kies een kamer om beschikbaarheid te bekijken',
      rooms: {
        'double-room':      'Tweepersoonskamer',
        'twin-room-1':      'Dubbel-/Tweepersoonskamer 1',
        'twin-room-2':      'Dubbel-/Tweepersoonskamer 2',
        'studio-apartment': 'Studioflat',
      },
    },
  };

  // ── Helpers ─────────────────────────────────────────────────

  // Normalise to midnight UTC to avoid timezone surprises
  function ymd(dateObj) {
    return dateObj.toISOString().slice(0, 10);
  }
  function fromYMD(str) {
    // Parse YYYY-MM-DD as local midnight
    const [y, m, d] = str.split('-').map(Number);
    return new Date(y, m - 1, d);
  }
  function addDays(dateObj, n) {
    const d = new Date(dateObj);
    d.setDate(d.getDate() + n);
    return d;
  }
  function isSameDay(a, b) {
    return a.getFullYear() === b.getFullYear() &&
           a.getMonth()    === b.getMonth()    &&
           a.getDate()     === b.getDate();
  }

  // Is a date in the "closed season" for a given room type?
  function isClosedSeason(date, isApartment) {
    const m = date.getMonth() + 1;
    const d = date.getDate();
    const n = m * 100 + d;
    for (const s of SEASON_CONFIG) {
      const startN = s.start[0] * 100 + s.start[1];
      const endN   = s.end[0]   * 100 + s.end[1];
      if (n >= startN && n <= endN) {
        const rate = isApartment ? s.apt.rate : s.room.rate;
        return rate === null;
      }
    }
    return false; // shouldn't happen
  }

  // Is this date booked for the given room?
  function isDateBooked(date, roomKey) {
    const bookings = (typeof BOOKINGS !== 'undefined') ? (BOOKINGS[roomKey] || []) : [];
    return bookings.some(b => {
      const from = fromYMD(b.from);
      const to   = fromYMD(b.to);
      return date >= from && date < to;
    });
  }

  // Return the minimum stay (nights) for a given check-in date and room type
  function getMinStay(checkIn, isApartment) {
    const m = checkIn.getMonth() + 1;
    const d = checkIn.getDate();
    const n = m * 100 + d;
    for (const s of SEASON_CONFIG) {
      const startN = s.start[0] * 100 + s.start[1];
      const endN   = s.end[0]   * 100 + s.end[1];
      if (n >= startN && n <= endN) {
        const cfg = isApartment ? s.apt : s.room;
        return (cfg.rate !== null && cfg.minStay) ? cfg.minStay : 1;
      }
    }
    return 1;
  }

  // Does the range from checkIn to checkOut contain any booked/closed dates?
  function rangeHasConflict(checkIn, checkOut, roomKey, isApartment) {
    let d = new Date(checkIn);
    while (d < checkOut) {
      if (isClosedSeason(d, isApartment) || isDateBooked(d, roomKey)) return true;
      d = addDays(d, 1);
    }
    return false;
  }

  // ── Calendar State ───────────────────────────────────────────
  let state = {
    roomKey:    null,
    isApt:      false,
    lang:       'en',
    viewYear:   new Date().getFullYear(),
    viewMonth:  new Date().getMonth(),  // 0-based
    checkIn:    null,   // Date object or null
    checkOut:   null,   // Date object or null
    selecting:  'in',   // 'in' | 'out'
  };

  // ── DOM References ───────────────────────────────────────────
  let calRoot, msgEl, actionBar, btnBook, btnClear;

  // ── Public init ──────────────────────────────────────────────
  window.AvailabilityCalendar = {
    init: function (opts) {
      // opts: { rootId, roomKey, lang, contactPath }
      state.roomKey  = opts.roomKey  || null;
      state.isApt    = APARTMENT_ROOMS && APARTMENT_ROOMS.includes(state.roomKey);
      state.lang     = (opts.lang && I18N[opts.lang]) ? opts.lang : 'en';
      state.contactPath = opts.contactPath || '../contact/';

      calRoot = document.getElementById(opts.rootId || 'availability-calendar');
      if (!calRoot) return;

      // Fast-forward view to first open month from today
      const now = new Date();
      state.viewYear  = now.getFullYear();
      state.viewMonth = now.getMonth();

      _render();
    }
  };

  // ── Render ───────────────────────────────────────────────────
  function _render() {
    const t = I18N[state.lang];
    if (!state.roomKey) {
      calRoot.innerHTML = `<p class="cal-no-room">${t.chooseRoom}</p>`;
      return;
    }

    calRoot.innerHTML = '';

    // Build grid of 3 months
    const grid = document.createElement('div');
    grid.className = 'cal-grid';

    for (let offset = 0; offset < 3; offset++) {
      let y = state.viewYear;
      let m = state.viewMonth + offset;
      if (m > 11) { m -= 12; y += 1; }
      grid.appendChild(_buildMonth(y, m));
    }

    // Nav buttons
    const navRow = document.createElement('div');
    navRow.className = 'cal-nav';
    const btnPrev = document.createElement('button');
    btnPrev.className = 'cal-nav-btn';
    btnPrev.innerHTML = '&#8592; ' + (state.lang === 'en' ? 'Previous' : state.lang === 'fr' ? 'Précédent' : state.lang === 'es' ? 'Anterior' : state.lang === 'ca' ? 'Anterior' : 'Vorige');
    btnPrev.onclick = _prevMonths;

    const btnNext = document.createElement('button');
    btnNext.className = 'cal-nav-btn';
    btnNext.innerHTML = (state.lang === 'en' ? 'Next' : state.lang === 'fr' ? 'Suivant' : state.lang === 'es' ? 'Siguiente' : state.lang === 'ca' ? 'Següent' : 'Volgende') + ' &#8594;';
    btnNext.onclick = _nextMonths;

    // Disable prev if we're already at current month
    const now = new Date();
    if (state.viewYear === now.getFullYear() && state.viewMonth <= now.getMonth()) {
      btnPrev.disabled = true;
      btnPrev.style.opacity = '0.35';
    }

    navRow.appendChild(btnPrev);
    navRow.appendChild(btnNext);

    // Message bar
    msgEl = document.createElement('div');
    msgEl.className = 'cal-message';
    _updateMessage();

    // Action bar (Book / Clear)
    actionBar = document.createElement('div');
    actionBar.className = 'cal-action-bar';

    btnBook = document.createElement('a');
    btnBook.className = 'cal-btn-book';
    btnBook.textContent = t.btnBook;
    btnBook.style.display = 'none';

    btnClear = document.createElement('button');
    btnClear.className = 'cal-btn-clear';
    btnClear.textContent = t.btnClear;
    btnClear.style.display = 'none';
    btnClear.onclick = _clearSelection;

    actionBar.appendChild(btnBook);
    actionBar.appendChild(btnClear);

    // Legend
    const legend = _buildLegend();

    calRoot.appendChild(navRow);
    calRoot.appendChild(msgEl);
    calRoot.appendChild(grid);
    calRoot.appendChild(actionBar);
    calRoot.appendChild(legend);

    _refreshActionBar();
  }

  function _buildMonth(year, month) {
    const t = I18N[state.lang];
    const today = new Date();
    today.setHours(0,0,0,0);

    const wrap = document.createElement('div');
    wrap.className = 'cal-month';

    // Header
    const hdr = document.createElement('div');
    hdr.className = 'cal-month-hdr';
    hdr.textContent = t.months[month] + ' ' + year;
    wrap.appendChild(hdr);

    // Day-of-week labels (Mon-Sun)
    const dayRow = document.createElement('div');
    dayRow.className = 'cal-day-row cal-day-labels';
    t.days.forEach(d => {
      const cell = document.createElement('div');
      cell.className = 'cal-day-label';
      cell.textContent = d;
      dayRow.appendChild(cell);
    });
    wrap.appendChild(dayRow);

    // Cells grid
    const grid = document.createElement('div');
    grid.className = 'cal-day-row cal-cells';

    // First day of month (0=Sun…6=Sat → convert to Mon-first)
    const firstDay = new Date(year, month, 1);
    let startOffset = firstDay.getDay() - 1; // Mon=0
    if (startOffset < 0) startOffset = 6;    // Sun → 6

    for (let i = 0; i < startOffset; i++) {
      const empty = document.createElement('div');
      empty.className = 'cal-cell cal-cell-empty';
      grid.appendChild(empty);
    }

    const daysInMonth = new Date(year, month + 1, 0).getDate();
    for (let day = 1; day <= daysInMonth; day++) {
      const date = new Date(year, month, day);
      date.setHours(0,0,0,0);
      grid.appendChild(_buildCell(date, today));
    }

    wrap.appendChild(grid);
    return wrap;
  }

  function _buildCell(date, today) {
    const cell = document.createElement('div');
    cell.className = 'cal-cell';
    cell.textContent = date.getDate();

    const isPast   = date < today;
    const isToday  = isSameDay(date, today);
    const isClosed = isClosedSeason(date, state.isApt);
    const isBooked = !isClosed && isDateBooked(date, state.roomKey);

    // When selecting checkout, dates within the min-stay window are blocked
    const isTooShort = !isPast && !isToday && !isClosed && !isBooked &&
                       state.selecting === 'out' && state.checkIn &&
                       date > state.checkIn &&
                       date < addDays(state.checkIn, getMinStay(state.checkIn, state.isApt));

    // Range highlight
    const inRange = state.checkIn && state.checkOut &&
                    date > state.checkIn && date < state.checkOut;
    const isCI = state.checkIn  && isSameDay(date, state.checkIn);
    const isCO = state.checkOut && isSameDay(date, state.checkOut);

    if (isPast || isToday) {
      cell.classList.add('cal-past');
    } else if (isClosed) {
      cell.classList.add('cal-closed');
    } else if (isBooked) {
      cell.classList.add('cal-booked');
    } else if (isTooShort) {
      cell.classList.add('cal-too-short');   // greyed out, no click handler
    } else {
      cell.classList.add('cal-avail');
      cell.addEventListener('click', () => _handleClick(date));
    }

    if (isCI) cell.classList.add('cal-selected-in');
    if (isCO) cell.classList.add('cal-selected-out');
    if (inRange && !isCI && !isCO) cell.classList.add('cal-in-range');
    if (isToday) cell.classList.add('cal-today');

    return cell;
  }

  function _handleClick(date) {
    const today = new Date();
    today.setHours(0,0,0,0);

    if (state.selecting === 'in') {
      if (date <= today) { _showMsg(I18N[state.lang].rangePast, true); return; }
      state.checkIn  = date;
      state.checkOut = null;
      state.selecting = 'out';
    } else {
      // selecting check-out
      if (date <= state.checkIn) { _showMsg(I18N[state.lang].rangeOrder, true); return; }
      if (rangeHasConflict(state.checkIn, date, state.roomKey, state.isApt)) {
        _showMsg(I18N[state.lang].rangeBooked, true);
        return;
      }
      const minStay = getMinStay(state.checkIn, state.isApt);
      const nights  = Math.round((date - state.checkIn) / 86400000);
      if (nights < minStay) {
        _showMsg(I18N[state.lang].rangeMinStay(minStay), true);
        return;
      }
      state.checkOut  = date;
      state.selecting = 'in';
    }
    _render();
  }

  function _clearSelection() {
    state.checkIn   = null;
    state.checkOut  = null;
    state.selecting = 'in';
    _render();
  }

  function _prevMonths() {
    const now = new Date();
    state.viewMonth -= 3;
    if (state.viewMonth < 0) { state.viewMonth += 12; state.viewYear -= 1; }
    // Don't go before current month
    if (state.viewYear < now.getFullYear() ||
        (state.viewYear === now.getFullYear() && state.viewMonth < now.getMonth())) {
      state.viewYear  = now.getFullYear();
      state.viewMonth = now.getMonth();
    }
    _render();
  }

  function _nextMonths() {
    state.viewMonth += 3;
    if (state.viewMonth > 11) { state.viewMonth -= 12; state.viewYear += 1; }
    _render();
  }

  function _updateMessage() {
    const t = I18N[state.lang];
    if (!state.checkIn) {
      msgEl.textContent = t.selectCheckin;
      msgEl.className = 'cal-message cal-message-hint';
    } else if (!state.checkOut) {
      const minStay = getMinStay(state.checkIn, state.isApt);
      msgEl.innerHTML = t.selectCheckout + ' <strong>(min ' + minStay + ' night' + (minStay !== 1 ? 's' : '') + ')</strong>';
      msgEl.className = 'cal-message cal-message-hint';
    } else {
      const nights = Math.round((state.checkOut - state.checkIn) / 86400000);
      const ni     = nights === 1 ? t.nights : t.nightsP;
      const ci     = state.checkIn.toLocaleDateString(state.lang === 'en' ? 'en-GB' : state.lang, { day:'numeric', month:'short' });
      const co     = state.checkOut.toLocaleDateString(state.lang === 'en' ? 'en-GB' : state.lang, { day:'numeric', month:'short' });
      msgEl.textContent = ci + ' → ' + co + ' · ' + nights + ' ' + ni;
      msgEl.className = 'cal-message cal-message-dates';
    }
  }

  function _refreshActionBar() {
    if (!btnBook || !btnClear) return;
    const hasRange = state.checkIn && state.checkOut;
    btnBook.style.display  = hasRange ? '' : 'none';
    btnClear.style.display = (state.checkIn) ? '' : 'none';

    if (hasRange) {
      const ci = ymd(state.checkIn);
      const co = ymd(state.checkOut);
      btnBook.href = state.contactPath + '?room=' + state.roomKey +
                     '&checkin=' + ci + '&checkout=' + co;
    }
  }

  function _showMsg(text, isError) {
    if (!msgEl) return;
    msgEl.textContent = text;
    msgEl.className = 'cal-message ' + (isError ? 'cal-message-error' : 'cal-message-hint');
  }

  function _buildLegend() {
    const t = I18N[state.lang];
    const legend = document.createElement('div');
    legend.className = 'cal-legend';

    const items = [
      { cls: 'cal-avail',   label: t.legend_avail   },
      { cls: 'cal-booked',  label: t.legend_booked  },
      { cls: 'cal-closed',  label: t.legend_closed  },
      { cls: 'cal-pas