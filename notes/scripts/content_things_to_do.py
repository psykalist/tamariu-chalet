#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Authored translations for the things-to-do pages and shared facilities."""

FOOTER_STD = [
    ("footer_rooms", [
        ("double_room", "accommodation/double-room.html"),
        ("studio", "accommodation/pool-apartment.html"),
    ]),
    ("nav_things", [
        ("girona", "things-to-do/girona.html"),
        ("cycling", "things-to-do/cycling.html"),
        ("water_sports", "things-to-do/water-sports.html"),
    ]),
    ("footer_contact", [("book_now", "contact/index.html")]),
]

FOOTER_WATER = [
    ("footer_rooms", [
        ("double_room", "accommodation/double-room.html"),
        ("studio", "accommodation/pool-apartment.html"),
    ]),
    ("nav_things", [
        ("girona", "things-to-do/girona.html"),
        ("cycling", "things-to-do/cycling.html"),
        ("walking", "things-to-do/walking.html"),
    ]),
    ("footer_contact", [
        ("book_now", "contact/index.html"),
        ("nav_getting_here", "getting-here/index.html"),
    ]),
]

FOOTER_FACILITIES = [
    ("footer_rooms", [
        ("double_room", "accommodation/double-room.html"),
        ("twin_1", "accommodation/twin-room-1.html"),
        ("twin_2", "accommodation/twin-room-2.html"),
        ("studio", "accommodation/pool-apartment.html"),
    ]),
    ("explore", [
        ("girona", "things-to-do/girona.html"),
        ("cycling", "things-to-do/cycling.html"),
        ("water_sports", "things-to-do/water-sports.html"),
    ]),
    ("footer_contact", [
        ("book_now", "contact/index.html"),
        ("nav_getting_here", "getting-here/index.html"),
    ]),
]

PAGES = {}

# ─────────────────────────────────────────────────────────────────────────────
# things-to-do/markets.html
# ─────────────────────────────────────────────────────────────────────────────
# Market-day town names are Catalan place names and stay unchanged in every
# language; only the weekday headings are translated.
_MARKET_DAYS = [
    ("Torroella de Montgrí, Blanes, Cadaqués, Olot, Colera"),
    ("Girona, Lloret de Mar, Castelló d'Empúries"),
    ("Banyoles, Llançà, La Jonquera, St Pere Pescador, St Antoni de Calonge"),
    ("L'Estartit, Figueres, Tossa de Mar, Llagostera, Calonge"),
    ("La Bisbal, Platja d'Aro, Port de la Selva, Portbou"),
    ("Girona, Empuriabrava, Ullà"),
    ("L'Escala, Palafrugell, Roses, St Feliu Guíxols"),
]

_DAY_NAMES = {
    "es": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
    "ca": ["Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres", "Dissabte", "Diumenge"],
    "fr": ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"],
    "nl": ["Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag"],
}


def _day_grid(lang: str) -> str:
    cells = []
    for day, towns in zip(_DAY_NAMES[lang], _MARKET_DAYS):
        cells.append(
            f'    <div><h4 style="color:var(--deep-blue);margin-bottom:4px;">{day}</h4>'
            f'<p style="color:var(--stone);font-size:0.9rem;margin:0;">{towns}</p></div>'
        )
    return ('  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));'
            'gap:16px;margin-top:16px;margin-bottom:24px;">\n'
            + "\n".join(cells) + "\n  </div>")


PAGES["things-to-do/markets.html"] = {
    "footer": FOOTER_STD,
    "es": {
        "title": "Mercados Locales — Tamariu Chalet",
        "desc": "Mercados semanales cerca de Tamariu, Costa Brava — mercados de productores y puestos artesanales en Palafrugell y los pueblos vecinos.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">Qué Hacer → Mercados Locales</p><h1>Mercados Locales</h1></div></div>
<div class="content-page">
  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">Los mercados del Baix Empordà son uno de los grandes atractivos de cualquier estancia — animados, llenos de color y repletos de producto local, artesanía y el ambiente de la auténtica vida catalana.</p>

  <h2>Mercados Semanales</h2>
  <h3>🛒 Mercado de Palafrugell — miércoles y sábados por la mañana</h3>
  <p>El mercado más cómodo para los huéspedes de Tamariu Chalet — a solo 4 km. El mercado bisemanal de Palafrugell llena la plaza del pueblo con puestos de fruta y verdura fresca, aceitunas, embutidos, quesos, flores y artículos para el hogar. El de los sábados es más grande y especialmente animado.</p>

  <h3>🛒 Mercado de Pals — martes por la mañana</h3>
  <p>Un mercado con encanto en el pueblo medieval de Pals, con producto local y artesanía. El propio pueblo — con su torre gótica del siglo XV y sus calles empedradas — merece una visita por sí solo.</p>

  <h3>🛒 Mercado de Palamós — martes y viernes por la mañana</h3>
  <p>Un mercado más grande en el puerto pesquero de Palamós, fuerte en pescado y marisco (como es de esperar), producto fresco y ropa. La subasta de pescado del puerto merece la pena si madruga.</p>

  <h3>🛒 Mercado de Begur — miércoles por la mañana</h3>
  <p>Un mercado popular a los pies de las murallas del castillo de Begur. Buena mezcla de producto local, artesanía y antigüedades. Los cafés del pueblo son un sitio excelente para desayunar antes.</p>

  <h2>Mercados Artesanales</h2>
  <p>Durante todo el verano, los mercados nocturnos de artesanía y las ferias de artesanos surgen en los pueblos de la costa — Calella de Palafrugell y Llafranc acogen mercados nocturnos de verano con regularidad. Pregúntenos por el calendario vigente cuando llegue.</p>

  <h2>Días de Mercado en la Comarca</h2>
  <p>Si va a explorar más lejos, la mayoría de poblaciones del Baix Empordà y del norte de la Costa Brava celebran su propio mercado semanal. Esto es lo que hay, día a día (además de los mercados ya mencionados):</p>
""" + _day_grid("es") + """

  <h2>Consejos para Ir al Mercado</h2>
  <ul>
    <li>Lleve efectivo — no todos los puestos aceptan tarjeta</li>
    <li>Vaya temprano para encontrar el mejor producto fresco</li>
    <li>Lleve bolsa o cesta — rara vez dan bolsas de plástico</li>
    <li>Pruebe la miel, el aceite de oliva, el vino y los quesos artesanos de la zona — todos excepcionales</li>
    <li>Los mercados suelen durar hasta las 13:00–14:00</li>
  </ul>
</div>
""",
    },
    "ca": {
        "title": "Mercats Locals — Tamariu Chalet",
        "desc": "Mercats setmanals a prop de Tamariu, Costa Brava — mercats de pagès i parades artesanals a Palafrugell i els pobles veïns.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">Què Fer → Mercats Locals</p><h1>Mercats Locals</h1></div></div>
<div class="content-page">
  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">Els mercats del Baix Empordà són un dels grans atractius de qualsevol estada — animats, plens de color i curulls de producte local, artesania i l'ambient de la vida catalana autèntica.</p>

  <h2>Mercats Setmanals</h2>
  <h3>🛒 Mercat de Palafrugell — dimecres i dissabtes al matí</h3>
  <p>El mercat més còmode per als hostes de Tamariu Chalet — a només 4 km. El mercat bisetmanal de Palafrugell omple la plaça de la vila amb parades de fruita i verdura fresca, olives, embotits, formatges, flors i articles per a la llar. El de dissabte és més gran i especialment animat.</p>

  <h3>🛒 Mercat de Pals — dimarts al matí</h3>
  <p>Un mercat amb encant al poble medieval de Pals, amb producte local i artesania. El poble mateix — amb la seva torre gòtica del segle XV i els carrers empedrats — ja mereix una visita.</p>

  <h3>🛒 Mercat de Palamós — dimarts i divendres al matí</h3>
  <p>Un mercat més gran al port pesquer de Palamós, fort en peix i marisc (com és d'esperar), producte fresc i roba. La subhasta de peix del port val la pena si sou matiners.</p>

  <h3>🛒 Mercat de Begur — dimecres al matí</h3>
  <p>Un mercat popular als peus de les muralles del castell de Begur. Bona barreja de producte local, artesania i antiguitats. Els cafès de la vila són un lloc excel·lent per esmorzar abans.</p>

  <h2>Mercats Artesanals</h2>
  <p>Durant tot l'estiu, els mercats nocturns d'artesania i les fires d'artesans apareixen als pobles de la costa — Calella de Palafrugell i Llafranc acullen mercats nocturns d'estiu amb regularitat. Pregunteu-nos pel calendari vigent quan arribeu.</p>

  <h2>Dies de Mercat a la Comarca</h2>
  <p>Si voleu explorar més enllà, la majoria de poblacions del Baix Empordà i del nord de la Costa Brava celebren el seu propi mercat setmanal. Això és el que hi ha, dia a dia (a més dels mercats ja esmentats):</p>
""" + _day_grid("ca") + """

  <h2>Consells per Anar al Mercat</h2>
  <ul>
    <li>Porteu efectiu — no totes les parades accepten targeta</li>
    <li>Aneu-hi aviat per trobar el millor producte fresc</li>
    <li>Porteu bossa o cistell — poques vegades donen bosses de plàstic</li>
    <li>Tasteu la mel, l'oli d'oliva, el vi i els formatges artesans de la zona — tots excepcionals</li>
    <li>Els mercats solen durar fins a les 13:00–14:00</li>
  </ul>
</div>
""",
    },
    "fr": {
        "title": "Marchés Locaux — Tamariu Chalet",
        "desc": "Marchés hebdomadaires près de Tamariu, Costa Brava — marchés de producteurs et étals artisanaux à Palafrugell et dans les villages alentour.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">À Faire → Marchés Locaux</p><h1>Marchés Locaux</h1></div></div>
<div class="content-page">
  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">Les marchés du Baix Empordà sont l'un des grands plaisirs d'un séjour ici — animés, colorés et débordants de produits locaux, d'artisanat et de l'atmosphère de la vraie vie catalane.</p>

  <h2>Marchés Hebdomadaires</h2>
  <h3>🛒 Marché de Palafrugell — mercredi et samedi matin</h3>
  <p>Le marché le plus pratique pour les hôtes du Tamariu Chalet — à seulement 4 km. Le marché bihebdomadaire de Palafrugell remplit la place du village d'étals de fruits et légumes frais, d'olives, de charcuterie, de fromages, de fleurs et d'articles ménagers. Celui du samedi est plus grand et particulièrement animé.</p>

  <h3>🛒 Marché de Pals — mardi matin</h3>
  <p>Un marché charmant dans le village médiéval de Pals, avec produits locaux et artisanat. Le village lui-même — avec sa tour gothique du XVe siècle et ses ruelles pavées — mérite à lui seul la visite.</p>

  <h3>🛒 Marché de Palamós — mardi et vendredi matin</h3>
  <p>Un marché de plus grande taille dans le port de pêche de Palamós, riche en poissons et fruits de mer (naturellement), produits frais et vêtements. La criée du port vaut le détour si vous êtes matinal.</p>

  <h3>🛒 Marché de Begur — mercredi matin</h3>
  <p>Un marché apprécié au pied des murailles du château de Begur. Bon mélange de produits locaux, d'artisanat et d'antiquités. Les cafés du village sont parfaits pour un petit-déjeuner avant.</p>

  <h2>Marchés Artisanaux</h2>
  <p>Tout l'été, des marchés nocturnes d'artisanat et des foires d'artisans s'installent dans les villages du littoral — Calella de Palafrugell et Llafranc accueillent régulièrement des marchés nocturnes estivaux. Demandez-nous le calendrier en cours à votre arrivée.</p>

  <h2>Jours de Marché dans la Région</h2>
  <p>Si vous partez plus loin, la plupart des communes du Baix Empordà et du nord de la Costa Brava tiennent leur propre marché hebdomadaire. Voici le programme, jour par jour (en plus des marchés cités ci-dessus) :</p>
""" + _day_grid("fr") + """

  <h2>Conseils pour le Marché</h2>
  <ul>
    <li>Prenez des espèces — tous les étals n'acceptent pas la carte</li>
    <li>Venez tôt pour le meilleur choix de produits frais</li>
    <li>Apportez un sac ou un panier — les sacs plastique sont rarement fournis</li>
    <li>Goûtez le miel, l'huile d'olive, le vin et les fromages artisanaux locaux — tous excellents</li>
    <li>Les marchés se terminent généralement entre 13h00 et 14h00</li>
  </ul>
</div>
""",
    },
    "nl": {
        "title": "Lokale Markten — Tamariu Chalet",
        "desc": "Wekelijkse markten bij Tamariu, Costa Brava — boerenmarkten en ambachtelijke kraampjes in Palafrugell en de omliggende dorpen.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">Wat Te Doen → Lokale Markten</p><h1>Lokale Markten</h1></div></div>
<div class="content-page">
  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">De markten van de Baix Empordà zijn een hoogtepunt van elk verblijf — druk, kleurrijk en vol lokale producten, ambachtelijk werk en de sfeer van het echte Catalaanse leven.</p>

  <h2>Wekelijkse Markten</h2>
  <h3>🛒 Markt van Palafrugell — woensdag- en zaterdagochtend</h3>
  <p>De handigste markt voor gasten van Tamariu Chalet — op slechts 4 km. De tweewekelijkse markt van Palafrugell vult het dorpsplein met kramen vol vers fruit en groenten, olijven, vleeswaren, kaas, bloemen en huishoudelijke artikelen. De zaterdagmarkt is groter en bijzonder levendig.</p>

  <h3>🛒 Markt van Pals — dinsdagochtend</h3>
  <p>Een charmante markt in het middeleeuwse dorp Pals, met lokale producten en ambachtelijke waren. Het dorp zelf — met zijn 15e-eeuwse gotische toren en geplaveide straatjes — is op zichzelf al een bezoek waard.</p>

  <h3>🛒 Markt van Palamós — dinsdag- en vrijdagochtend</h3>
  <p>Een grotere markt in de werkende vissershaven van Palamós, sterk in vis en zeevruchten (uiteraard), verse producten en kleding. De visafslag in de haven is de moeite waard als u vroeg opstaat.</p>

  <h3>🛒 Markt van Begur — woensdagochtend</h3>
  <p>Een populaire markt onder de kasteelmuren van Begur. Een goede mix van lokale producten, ambachtelijk werk en antiek. De cafés van het stadje zijn uitstekend voor een ontbijt vooraf.</p>

  <h2>Ambachts- en Kunstmarkten</h2>
  <p>De hele zomer door duiken er avondmarkten met ambachten en kunstnijverheid op in de kustdorpen — Calella de Palafrugell en Llafranc houden beide regelmatig zomerse avondmarkten. Vraag ons bij aankomst naar de actuele agenda.</p>

  <h2>Marktdagen in de Regio</h2>
  <p>Als u verder op pad gaat: de meeste plaatsen in de Baix Empordà en aan de noordelijke Costa Brava houden hun eigen wekelijkse markt. Dit is het overzicht per dag (naast de hierboven genoemde markten):</p>
""" + _day_grid("nl") + """

  <h2>Tips voor de Markt</h2>
  <ul>
    <li>Neem contant geld mee — niet elke kraam accepteert kaarten</li>
    <li>Ga vroeg voor de beste keuze aan verse producten</li>
    <li>Neem een tas of mand mee — plastic zakjes worden zelden verstrekt</li>
    <li>Probeer de lokale honing, olijfolie, wijn en ambachtelijke kazen — allemaal uitzonderlijk</li>
    <li>Markten duren doorgaans tot 13:00–14:00 uur</li>
  </ul>
</div>
""",
    },
}
