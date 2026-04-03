// ============================================================
// TAMARIU CHALET — RATES CONFIGURATION
// ============================================================
// Edit this file to update ALL rates tables and the cost
// calculator across the entire website at once.
//
// DATE FORMAT: "DD MMM" e.g. "1 Jan", "30 Apr"
// RATE: nightly rate in euros, or null if closed
// MIN_STAY: minimum number of nights
// CLEANING: one-off cleaning fee per stay
// ============================================================

const SEASON_CONFIG = [
  {
    name:     'Early Season',
    dates:    '1 Jan – 30 Apr',
    start:    [1, 1],    // [month, day]
    end:      [4, 30],
    room:     { rate: null, minStay: 2, cleaning: 30  },   // null = Closed
    apt:      { rate: 100,  minStay: 2, cleaning: 30  },
  },
  {
    name:     'Spring',
    dates:    '1 May – 30 Jun',
    start:    [5, 1],
    end:      [6, 30],
    room:     { rate: 110,  minStay: 2, cleaning: 30  },
    apt:      { rate: 120,  minStay: 2, cleaning: 30  },
  },
  {
    name:     'Summer',
    dates:    '1 Jul – 31 Aug',
    start:    [7, 1],
    end:      [8, 31],
    room:     { rate: 125,  minStay: 3, cleaning: 45  },
    apt:      { rate: 175,  minStay: 3, cleaning: 45  },
  },
  {
    name:     'Late Season',
    dates:    '1 Sep – 31 Dec',
    start:    [9, 1],
    end:      [12, 31],
    room:     { rate: 110,  minStay: 2, cleaning: 30  },
    apt:      { rate: 120,  minStay: 2, cleaning: 30  },
  },
];

// Which rooms are apartments (higher rate) vs standard rooms
const APARTMENT_ROOMS = ['studio-apartment'];
