#!/usr/bin/env python3
"""
Page shell (head / nav / footer) for generated translations.

The site is hand-written static HTML and stays that way: this module is an
authoring aid that emits plain HTML files which are then committed and can be
edited by hand like every other page. Nothing here runs at request time.

Relative paths are computed from the page's depth so the generated pages match
the existing hand-written ones rather than switching to root-absolute links.
"""

LANGS = ["en", "es", "ca", "fr", "nl"]
LANG_LABELS = {"en": "EN", "es": "ES", "ca": "CA", "fr": "FR", "nl": "NL"}

HTML_LANG = {"en": "en", "es": "es", "ca": "ca", "fr": "fr", "nl": "nl"}

# ── UI vocabulary ────────────────────────────────────────────────────────────
# Keys are stable identifiers; values are the string in each language. These
# match the wording already used in the existing translated pages so the new
# pages read consistently with them.
UI = {
    "nav_accommodation": {
        "en": "The Accommodation", "es": "El Alojamiento", "ca": "L'Allotjament",
        "fr": "L'Hébergement", "nl": "Het Verblijf",
    },
    "nav_things": {
        "en": "Things To Do", "es": "Qué Hacer", "ca": "Què Fer",
        "fr": "À Faire", "nl": "Wat Te Doen",
    },
    "nav_about": {
        "en": "About Catalunya", "es": "Sobre Catalunya", "ca": "Sobre Catalunya",
        "fr": "À Propos de la Catalogne", "nl": "Over Catalonië",
    },
    "nav_getting_here": {
        "en": "Getting Here", "es": "Cómo Llegar", "ca": "Com Arribar",
        "fr": "Comment Venir", "nl": "Hoe Te Bereiken",
    },
    "nav_contact": {
        "en": "Contact &amp; Book", "es": "Contactar y Reservar", "ca": "Contactar i Reservar",
        "fr": "Contact &amp; Réservation", "nl": "Contact &amp; Boeken",
    },
    # Rooms
    "double_room": {
        "en": "Double Room", "es": "Habitación Doble", "ca": "Habitació Doble",
        "fr": "Chambre Double", "nl": "Tweepersoonskamer",
    },
    "twin_1": {
        "en": "Double/Twin Room 1", "es": "Habitación Doble/Twin 1", "ca": "Habitació Doble/Twin 1",
        "fr": "Chambre Double/Lits Jumeaux 1", "nl": "Twee-/Tweepersoonskamer 1",
    },
    "twin_2": {
        "en": "Double/Twin Room 2", "es": "Habitación Doble/Twin 2", "ca": "Habitació Doble/Twin 2",
        "fr": "Chambre Double/Lits Jumeaux 2", "nl": "Twee-/Tweepersoonskamer 2",
    },
    "studio": {
        "en": "Studio Apartment", "es": "Apartamento Estudio", "ca": "Apartament Estudi",
        "fr": "Appartement Studio", "nl": "Studioappartement",
    },
    "shared_facilities": {
        "en": "Shared Bathrooms &amp; Kitchen", "es": "Baños y Cocina Compartidos",
        "ca": "Banys i Cuina Compartits", "fr": "Salles de Bain &amp; Cuisine Partagées",
        "nl": "Gedeelde Badkamers &amp; Keuken",
    },
    # Things to do
    "beach_walk": {
        "en": "Getting to the Beach", "es": "Cómo Llegar a la Playa", "ca": "Com Arribar a la Platja",
        "fr": "Aller à la Plage", "nl": "Naar het Strand",
    },
    "girona": {
        "en": "Visit Girona", "es": "Visitar Girona", "ca": "Visitar Girona",
        "fr": "Visiter Gérone", "nl": "Bezoek Girona",
    },
    "cycling": {
        "en": "Cycling", "es": "Ciclismo", "ca": "Ciclisme",
        "fr": "Cyclisme", "nl": "Fietsen",
    },
    "markets": {
        "en": "Local Markets", "es": "Mercados Locales", "ca": "Mercats Locals",
        "fr": "Marchés Locaux", "nl": "Lokale Markten",
    },
    "walking": {
        "en": "Walking", "es": "Senderismo", "ca": "Senderisme",
        "fr": "Randonnée", "nl": "Wandelen",
    },
    "tourist_info": {
        "en": "Tourist Information", "es": "Información Turística", "ca": "Informació Turística",
        "fr": "Office de Tourisme", "nl": "Toeristische Informatie",
    },
    "julivia": {
        "en": "Julivia Bus", "es": "Bus Julivia", "ca": "Bus Julivia",
        "fr": "Bus Julivia", "nl": "Julivia Bus",
    },
    "begur_bus": {
        "en": "Begur Beach Bus", "es": "Bus Playas de Begur", "ca": "Bus Platges de Begur",
        "fr": "Bus des Plages de Begur", "nl": "Begur Strandbus",
    },
    "local_beaches": {
        "en": "Local Beaches", "es": "Playas Locales", "ca": "Platges Locals",
        "fr": "Plages Locales", "nl": "Lokale Stranden",
    },
    "by_foot": {
        "en": "Tamariu by Foot", "es": "Tamariu a Pie", "ca": "Tamariu a Peu",
        "fr": "Tamariu à Pied", "nl": "Tamariu te Voet",
    },
    "restaurants": {
        "en": "Local Restaurants", "es": "Restaurantes Locales", "ca": "Restaurants Locals",
        "fr": "Restaurants Locaux", "nl": "Lokale Restaurants",
    },
    "water_sports": {
        "en": "Water Sports", "es": "Deportes Acuáticos", "ca": "Esports Aquàtics",
        "fr": "Sports Nautiques", "nl": "Watersport",
    },
    # About Catalunya
    "cuisine": {
        "en": "Catalonian Cuisine", "es": "Cocina Catalana", "ca": "Cuina Catalana",
        "fr": "Cuisine Catalane", "nl": "Catalaanse Keuken",
    },
    "language": {
        "en": "Catalonian Language", "es": "Idioma Catalán", "ca": "Llengua Catalana",
        "fr": "Langue Catalane", "nl": "Catalaanse Taal",
    },
    "culture": {
        "en": "Catalonian Culture", "es": "Cultura Catalana", "ca": "Cultura Catalana",
        "fr": "Culture Catalane", "nl": "Catalaanse Cultuur",
    },
    "history": {
        "en": "Catalonian History", "es": "Historia de Cataluña", "ca": "Història de Catalunya",
        "fr": "Histoire de la Catalogne", "nl": "Catalaanse Geschiedenis",
    },
    "cities": {
        "en": "Cities of Interest", "es": "Ciudades de Interés", "ca": "Ciutats d'Interès",
        "fr": "Villes d'Intérêt", "nl": "Interessante Steden",
    },
    "facts": {
        "en": "Catalonian Facts", "es": "Datos Curiosos", "ca": "Dades Curioses",
        "fr": "Faits sur la Catalogne", "nl": "Weetjes over Catalonië",
    },
    "map_directions": {
        "en": "Map &amp; Directions", "es": "Mapa y Direcciones", "ca": "Mapa i Indicacions",
        "fr": "Carte &amp; Itinéraire", "nl": "Kaart &amp; Routebeschrijving",
    },
    # Footer
    "footer_blurb": {
        "en": "Peaceful accommodation in the coastal village of Tamariu, Costa Brava, Catalunya.",
        "es": "Alojamiento tranquilo en el pueblo costero de Tamariu, Costa Brava, Catalunya.",
        "ca": "Allotjament tranquil al poble costaner de Tamariu, Costa Brava, Catalunya.",
        "fr": "Hébergement paisible dans le village côtier de Tamariu, Costa Brava, Catalogne.",
        "nl": "Rustig verblijf in het kustdorp Tamariu, Costa Brava, Catalonië.",
    },
    "footer_rooms": {
        "en": "The Rooms", "es": "Las Habitaciones", "ca": "Les Habitacions",
        "fr": "Les Chambres", "nl": "De Kamers",
    },
    "footer_contact": {
        "en": "Contact", "es": "Contacto", "ca": "Contacte",
        "fr": "Contact", "nl": "Contact",
    },
    "explore": {
        "en": "Explore", "es": "Explorar", "ca": "Explorar",
        "fr": "Explorer", "nl": "Ontdekken",
    },
    "book_now": {
        "en": "Book Now", "es": "Reservar Ahora", "ca": "Reservar Ara",
        "fr": "Réserver", "nl": "Nu Boeken",
    },
    "menu": {
        "en": "Menu", "es": "Menú", "ca": "Menú", "fr": "Menu", "nl": "Menu",
    },
}


def t(key: str, lang: str) -> str:
    return UI[key][lang]


# ── Link targets ─────────────────────────────────────────────────────────────
# logical path -> whether a translated copy exists for a given language is
# decided at build time by the caller, so nav can fall back to English.
NAV = [
    ("nav_accommodation", None, [
        ("double_room", "accommodation/double-room.html"),
        ("twin_1", "accommodation/twin-room-1.html"),
        ("twin_2", "accommodation/twin-room-2.html"),
        ("studio", "accommodation/pool-apartment.html"),
        ("shared_facilities", "accommodation/shared-facilities.html"),
    ]),
    ("nav_things", None, [
        ("beach_walk", "getting-here/getting-to-the-beach.html"),
        ("girona", "things-to-do/girona.html"),
        ("cycling", "things-to-do/cycling.html"),
        ("markets", "things-to-do/markets.html"),
        ("walking", "things-to-do/walking.html"),
        ("tourist_info", "things-to-do/tourist-info.html"),
        ("julivia", "getting-here/julivia-bus.html"),
        ("begur_bus", "getting-here/begur-bus.html"),
        ("local_beaches", "things-to-do/local-beaches.html"),
        ("by_foot", "things-to-do/tamariu-by-foot.html"),
        ("restaurants", "things-to-do/restaurants.html"),
        ("water_sports", "things-to-do/water-sports.html"),
    ]),
    ("nav_about", None, [
        ("cuisine", "about-catalunya/cuisine.html"),
        ("language", "about-catalunya/language.html"),
        ("culture", "about-catalunya/culture.html"),
        ("history", "about-catalunya/history.html"),
        ("cities", "about-catalunya/cities.html"),
        ("facts", "about-catalunya/facts.html"),
    ]),
    ("nav_getting_here", None, [
        ("map_directions", "getting-here/index.html"),
    ]),
]
