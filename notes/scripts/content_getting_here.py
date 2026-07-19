#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Authored translations for the getting-here pages.

Proper nouns, road numbers (AP-7, C-31, GI-660), operator names, prices and
distances are deliberately left untouched in every language.
"""

FOOTER = [
    ("nav_getting_here", [
        ("map_directions", "getting-here/index.html"),
        ("beach_walk", "getting-here/getting-to-the-beach.html"),
    ]),
    ("footer_contact", [("book_now", "contact/index.html")]),
]

PAGES = {}

# ─────────────────────────────────────────────────────────────────────────────
# getting-here/julivia-bus.html
# ─────────────────────────────────────────────────────────────────────────────
PAGES["getting-here/julivia-bus.html"] = {
    "footer": FOOTER,
    "es": {
        "title": "Bus Julivia — Tamariu Chalet",
        "desc": "El servicio de bus Julivia de Palafrugell a Tamariu, Costa Brava — horarios y paradas para los huéspedes de Tamariu Chalet.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">Cómo Llegar → Bus Julivia</p><h1>El Bus Julivia</h1></div></div>
<div class="content-page">
  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">El Bus Julivia es un servicio de autobús turístico de temporada que conecta los pueblos costeros y las localidades del interior de la zona de Palafrugell — una forma cómoda y agradable de explorar la región sin coche.</p>

  <a href="https://visitpalafrugell.cat/wp-content/uploads/2024/06/triptic-julivia-2026.pdf" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Bus Julivia — Horarios 2026 (PDF)</h4>
      <p>Información completa de rutas, horarios, paradas y precios para la temporada 2026, desde la web oficial de Visit Palafrugell.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Sobre el Servicio</h2>
  <p>El Bus Julivia une la localidad interior de Palafrugell con los pueblos costeros de Tamariu, Llafranc y Calella de Palafrugell — lo que facilita moverse entre la costa y el pueblo sin preocuparse por el aparcamiento. También da servicio a algunos puntos culturales e históricos del interior.</p>
  <ul>
    <li>Servicio de temporada — normalmente funciona de mayo a octubre</li>
    <li>Billetes asequibles — se paga a bordo</li>
    <li>Conecta Tamariu directamente con el centro de Palafrugell (mercados, tiendas, restaurantes)</li>
    <li>Permite explorar cómodamente los tres pueblos costeros en transporte público</li>
    <li>Consulte la web oficial más arriba para los horarios y el mapa de rutas del año en curso</li>
  </ul>
  <p style="margin-top:20px;">Combinado con la red de autobuses regionales Sarfa, el Bus Julivia hace perfectamente viable explorar la zona sin coche durante la temporada alta.</p>
</div>
""",
    },
    "ca": {
        "title": "Bus Julivia — Tamariu Chalet",
        "desc": "El servei de bus Julivia de Palafrugell a Tamariu, Costa Brava — horaris i parades per als hostes de Tamariu Chalet.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">Com Arribar → Bus Julivia</p><h1>El Bus Julivia</h1></div></div>
<div class="content-page">
  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">El Bus Julivia és un servei d'autobús turístic de temporada que connecta els pobles costaners i les poblacions de l'interior de la zona de Palafrugell — una manera còmoda i agradable d'explorar la comarca sense cotxe.</p>

  <a href="https://visitpalafrugell.cat/wp-content/uploads/2024/06/triptic-julivia-2026.pdf" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Bus Julivia — Horaris 2026 (PDF)</h4>
      <p>Informació completa de rutes, horaris, parades i preus per a la temporada 2026, des del web oficial de Visit Palafrugell.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Sobre el Servei</h2>
  <p>El Bus Julivia uneix la vila interior de Palafrugell amb els pobles costaners de Tamariu, Llafranc i Calella de Palafrugell — cosa que facilita moure's entre la costa i la vila sense preocupar-se per l'aparcament. També dona servei a alguns indrets culturals i històrics de l'interior.</p>
  <ul>
    <li>Servei de temporada — normalment funciona de maig a octubre</li>
    <li>Bitllets assequibles — es paga a bord</li>
    <li>Connecta Tamariu directament amb el centre de Palafrugell (mercats, botigues, restaurants)</li>
    <li>Permet explorar còmodament els tres pobles costaners amb transport públic</li>
    <li>Consulteu el web oficial més amunt per als horaris i el mapa de rutes de l'any en curs</li>
  </ul>
  <p style="margin-top:20px;">Combinat amb la xarxa d'autobusos regionals Sarfa, el Bus Julivia fa perfectament viable explorar la zona sense cotxe durant la temporada alta.</p>
</div>
""",
    },
    "fr": {
        "title": "Bus Julivia — Tamariu Chalet",
        "desc": "Le service de bus Julivia de Palafrugell à Tamariu, Costa Brava — horaires et arrêts pour les hôtes du Tamariu Chalet.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">Comment Venir → Bus Julivia</p><h1>Le Bus Julivia</h1></div></div>
<div class="content-page">
  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">Le Bus Julivia est un service d'autobus touristique saisonnier reliant les villages côtiers et les communes de l'intérieur de la région de Palafrugell — un moyen pratique et agréable d'explorer la région sans voiture.</p>

  <a href="https://visitpalafrugell.cat/wp-content/uploads/2024/06/triptic-julivia-2026.pdf" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Bus Julivia — Horaires 2026 (PDF)</h4>
      <p>Informations complètes sur les itinéraires, horaires, arrêts et tarifs pour la saison 2026, depuis le site officiel de Visit Palafrugell.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">À Propos du Service</h2>
  <p>Le Bus Julivia relie la ville intérieure de Palafrugell aux villages côtiers de Tamariu, Llafranc et Calella de Palafrugell — ce qui facilite les déplacements entre la côte et la ville sans souci de stationnement. Il dessert également quelques sites culturels et historiques de l'intérieur.</p>
  <ul>
    <li>Service saisonnier — circule généralement de mai à octobre</li>
    <li>Billets abordables — paiement à bord</li>
    <li>Relie Tamariu directement au centre de Palafrugell (marchés, commerces, restaurants)</li>
    <li>Permet d'explorer facilement les trois villages côtiers en transport public</li>
    <li>Consultez le site officiel ci-dessus pour les horaires et le plan des lignes de l'année en cours</li>
  </ul>
  <p style="margin-top:20px;">Associé au réseau de bus régional Sarfa, le Bus Julivia rend tout à fait possible l'exploration de la région sans voiture pendant la haute saison.</p>
</div>
""",
    },
    "nl": {
        "title": "Julivia Bus — Tamariu Chalet",
        "desc": "De Julivia busdienst van Palafrugell naar Tamariu, Costa Brava — dienstregeling en haltes voor gasten van Tamariu Chalet.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">Hoe Te Bereiken → Julivia Bus</p><h1>De Julivia Bus</h1></div></div>
<div class="content-page">
  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">De Julivia Bus is een seizoensgebonden toeristische busdienst die de kustdorpen en de plaatsen in het binnenland rond Palafrugell verbindt — een handige en aangename manier om de streek zonder auto te verkennen.</p>

  <a href="https://visitpalafrugell.cat/wp-content/uploads/2024/06/triptic-julivia-2026.pdf" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Julivia Bus — Dienstregeling 2026 (PDF)</h4>
      <p>Volledige informatie over routes, dienstregeling, haltes en tarieven voor het seizoen 2026, van de officiële website van Visit Palafrugell.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Over de Dienst</h2>
  <p>De Julivia Bus verbindt het in het binnenland gelegen Palafrugell met de kustdorpen Tamariu, Llafranc en Calella de Palafrugell — zo reist u eenvoudig tussen kust en dorp zonder u zorgen te maken over parkeren. De bus bedient ook enkele culturele en historische bezienswaardigheden in het binnenland.</p>
  <ul>
    <li>Seizoensdienst — rijdt doorgaans van mei tot oktober</li>
    <li>Betaalbare tickets — u betaalt in de bus</li>
    <li>Verbindt Tamariu rechtstreeks met het centrum van Palafrugell (markten, winkels, restaurants)</li>
    <li>Maakt het eenvoudig om alle drie de kustdorpen met het openbaar vervoer te verkennen</li>
    <li>Raadpleeg de officiële website hierboven voor de dienstregeling en routekaart van dit jaar</li>
  </ul>
  <p style="margin-top:20px;">In combinatie met het regionale busnetwerk van Sarfa maakt de Julivia Bus het uitstekend mogelijk om de streek in het hoogseizoen zonder auto te verkennen.</p>
</div>
""",
    },
}

# ─────────────────────────────────────────────────────────────────────────────
# getting-here/begur-bus.html
# ─────────────────────────────────────────────────────────────────────────────
PAGES["getting-here/begur-bus.html"] = {
    "footer": FOOTER,
    "es": {
        "title": "Bus Playas de Begur — Tamariu Chalet",
        "desc": "El bus de playas de Begur (Bus Platges Begur) — servicio de temporada a las calas de Sa Tuna, Aiguafreda, Fornells y Sa Riera en la Costa Brava.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">Cómo Llegar → Bus Playas de Begur</p><h1>Bus Playas de Begur</h1></div></div>
<div class="content-page">
  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">El Bus Platges Begur es un servicio lanzadera de temporada que conecta el pueblo de Begur, en lo alto de la colina, con su rosario de preciosas calas — una forma excelente de descubrir algunos de los tramos de costa más espectaculares de la Costa Brava.</p>

  <a href="https://www.beguronline.com/bus.htm" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Bus Playas de Begur — Horarios 2026</h4>
      <p>Consulte el horario completo y el mapa de rutas 2026 del bus de playas de Begur. Incluye todas las paradas: Sa Tuna, Aiguafreda, Fornells y Sa Riera.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Sobre el Servicio</h2>
  <p>Begur es un precioso pueblo con castillo situado en lo alto de una colina, a unos 10 km al norte de Tamariu. Sus playas están entre las más bonitas de la Costa Brava — a varias solo se llega en el bus de playas o a pie, lo que las mantiene deliciosamente tranquilas incluso en pleno verano.</p>

  <h3>Playas con Parada</h3>
  <ul>
    <li><strong>Sa Riera</strong> — Una bonita cala resguardada con una pequeña playa y excelentes restaurantes</li>
    <li><strong>Aiguafreda</strong> — Cala diminuta e íntima — una de las más bellas de la costa</li>
    <li><strong>Sa Tuna</strong> — Pintoresca cala de pueblo pesquero con agua cristalina</li>
    <li><strong>Fornells</strong> — Una bahía más amplia con playa de arena y alquiler de deportes acuáticos</li>
    <li><strong>Platja de Pals</strong> — Una playa de arena más larga rodeada de pinos</li>
  </ul>

  <h3>Consejos para Usar el Bus</h3>
  <ul>
    <li>El servicio funciona a diario en julio y agosto; horario reducido en junio y septiembre</li>
    <li>Sale del centro de Begur; consulte el PDF de horarios vigente</li>
    <li>Ideal para ir de cala en cala — baje en bus y vuelva andando (o al revés) por el camino de ronda</li>
    <li>Desde Tamariu: vaya en coche o tome el Bus Julivia hasta Palafrugell, y de allí a Begur en coche o taxi (10 min)</li>
  </ul>
</div>
""",
    },
    "ca": {
        "title": "Bus Platges de Begur — Tamariu Chalet",
        "desc": "El bus de platges de Begur (Bus Platges Begur) — servei de temporada a les cales de Sa Tuna, Aiguafreda, Fornells i Sa Riera a la Costa Brava.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">Com Arribar → Bus Platges de Begur</p><h1>Bus Platges de Begur</h1></div></div>
<div class="content-page">
  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">El Bus Platges Begur és un servei llançadora de temporada que connecta la vila de Begur, dalt del turó, amb el seu reguitzell de cales precioses — una manera excel·lent de descobrir alguns dels trams de costa més espectaculars de la Costa Brava.</p>

  <a href="https://www.beguronline.com/bus.htm" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Bus Platges de Begur — Horaris 2026</h4>
      <p>Consulteu l'horari complet i el mapa de rutes 2026 del bus de platges de Begur. Inclou totes les parades: Sa Tuna, Aiguafreda, Fornells i Sa Riera.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Sobre el Servei</h2>
  <p>Begur és una vila preciosa amb castell situada dalt d'un turó, a uns 10 km al nord de Tamariu. Les seves platges són de les més boniques de la Costa Brava — a diverses només s'hi arriba amb el bus de platges o a peu, cosa que les manté deliciosament tranquil·les fins i tot en ple estiu.</p>

  <h3>Platges amb Parada</h3>
  <ul>
    <li><strong>Sa Riera</strong> — Una bonica cala arrecerada amb una petita platja i excel·lents restaurants</li>
    <li><strong>Aiguafreda</strong> — Cala diminuta i íntima — una de les més belles de la costa</li>
    <li><strong>Sa Tuna</strong> — Pintoresca cala de poble pescador amb aigua cristal·lina</li>
    <li><strong>Fornells</strong> — Una badia més ampla amb platja de sorra i lloguer d'esports aquàtics</li>
    <li><strong>Platja de Pals</strong> — Una platja de sorra més llarga envoltada de pins</li>
  </ul>

  <h3>Consells per Utilitzar el Bus</h3>
  <ul>
    <li>El servei funciona diàriament el juliol i l'agost; horari reduït el juny i el setembre</li>
    <li>Surt del centre de Begur; consulteu el PDF d'horaris vigent</li>
    <li>Ideal per anar de cala en cala — baixeu amb bus i torneu caminant (o a l'inrevés) pel camí de ronda</li>
    <li>Des de Tamariu: aneu-hi amb cotxe o agafeu el Bus Julivia fins a Palafrugell, i d'allà a Begur amb cotxe o taxi (10 min)</li>
  </ul>
</div>
""",
    },
    "fr": {
        "title": "Bus des Plages de Begur — Tamariu Chalet",
        "desc": "Le bus des plages de Begur (Bus Platges Begur) — navette saisonnière vers les criques de Sa Tuna, Aiguafreda, Fornells et Sa Riera sur la Costa Brava.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">Comment Venir → Bus des Plages de Begur</p><h1>Bus des Plages de Begur</h1></div></div>
<div class="content-page">
  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">Le Bus Platges Begur est une navette saisonnière reliant le village perché de Begur au chapelet de ses magnifiques criques — une excellente façon de découvrir quelques-uns des littoraux les plus spectaculaires de la Costa Brava.</p>

  <a href="https://www.beguronline.com/bus.htm" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Bus des Plages de Begur — Horaires 2026</h4>
      <p>Consultez les horaires complets et le plan des lignes 2026 du bus des plages de Begur. Dessert tous les arrêts, dont Sa Tuna, Aiguafreda, Fornells et Sa Riera.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">À Propos du Service</h2>
  <p>Begur est un superbe village perché doté d'un château, à environ 10 km au nord de Tamariu. Ses plages comptent parmi les plus belles de la Costa Brava — plusieurs ne sont accessibles qu'en bus des plages ou à pied, ce qui les garde délicieusement peu fréquentées même en plein été.</p>

  <h3>Plages Desservies</h3>
  <ul>
    <li><strong>Sa Riera</strong> — Une jolie crique abritée avec une petite plage et d'excellents restaurants</li>
    <li><strong>Aiguafreda</strong> — Crique minuscule et intime — l'une des plus belles de la côte</li>
    <li><strong>Sa Tuna</strong> — Pittoresque crique de village de pêcheurs à l'eau cristalline</li>
    <li><strong>Fornells</strong> — Une baie plus vaste avec plage de sable et location de sports nautiques</li>
    <li><strong>Platja de Pals</strong> — Une plage de sable plus longue bordée de pins</li>
  </ul>

  <h3>Conseils d'Utilisation</h3>
  <ul>
    <li>Le service circule tous les jours en juillet et août ; horaires réduits en juin et septembre</li>
    <li>Départ du centre de Begur ; consultez le PDF des horaires en vigueur</li>
    <li>Idéal pour enchaîner les criques — descendez en bus et remontez à pied (ou l'inverse) par le chemin côtier</li>
    <li>Depuis Tamariu : en voiture, ou prenez le Bus Julivia jusqu'à Palafrugell puis rejoignez Begur en voiture ou en taxi (10 min)</li>
  </ul>
</div>
""",
    },
    "nl": {
        "title": "Begur Strandbus — Tamariu Chalet",
        "desc": "De strandbus van Begur (Bus Platges Begur) — seizoensdienst naar de baaien Sa Tuna, Aiguafreda, Fornells en Sa Riera aan de Costa Brava.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">Hoe Te Bereiken → Begur Strandbus</p><h1>Begur Strandbus</h1></div></div>
<div class="content-page">
  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">De Bus Platges Begur is een seizoensgebonden pendeldienst die het op een heuvel gelegen stadje Begur verbindt met zijn reeks prachtige baaien — een uitstekende manier om enkele van de spectaculairste kuststroken van de Costa Brava te ontdekken.</p>

  <a href="https://www.beguronline.com/bus.htm" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Begur Strandbus — Dienstregeling 2026</h4>
      <p>Bekijk de volledige dienstregeling en routekaart 2026 van de strandbus van Begur. Met alle haltes, waaronder Sa Tuna, Aiguafreda, Fornells en Sa Riera.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Over de Dienst</h2>
  <p>Begur is een schitterend heuveldorp met kasteel, ongeveer 10 km ten noorden van Tamariu. De stranden behoren tot de mooiste van de Costa Brava — verschillende zijn alleen bereikbaar met de strandbus of te voet, waardoor ze zelfs in het hoogseizoen heerlijk rustig blijven.</p>

  <h3>Bediende Stranden</h3>
  <ul>
    <li><strong>Sa Riera</strong> — Een mooie beschutte baai met een klein strand en uitstekende restaurants</li>
    <li><strong>Aiguafreda</strong> — Piepkleine, intieme baai — een van de mooiste van de kust</li>
    <li><strong>Sa Tuna</strong> — Schilderachtige baai bij een vissersdorp met kristalhelder water</li>
    <li><strong>Fornells</strong> — Een grotere baai met zandstrand en verhuur van watersportmateriaal</li>
    <li><strong>Platja de Pals</strong> — Een langer zandstrand met dennenbomen erachter</li>
  </ul>

  <h3>Tips voor het Gebruik</h3>
  <ul>
    <li>De dienst rijdt dagelijks in juli en augustus; beperkte dienstregeling in juni en september</li>
    <li>Vertrekt vanuit het centrum van Begur; raadpleeg de actuele PDF-dienstregeling</li>
    <li>Ideaal om baaien af te struinen — neem de bus heen en loop terug (of andersom) over het kustpad</li>
    <li>Vanuit Tamariu: met de auto, of neem de Julivia Bus naar Palafrugell en vandaar met auto of taxi naar Begur (10 min)</li>
  </ul>
</div>
""",
    },
}

# ─────────────────────────────────────────────────────────────────────────────
# getting-here/getting-to-the-beach.html
# ─────────────────────────────────────────────────────────────────────────────
_BEACH_IMG = ('  <img src="{img}" alt="{alt}" '
              'style="display:block;width:100%;max-width:560px;height:auto;'
              'margin:0 auto 32px;border-radius:8px;'
              'box-shadow:0 6px 24px rgba(26,58,92,0.15);">')

PAGES["getting-here/getting-to-the-beach.html"] = {
    "footer": FOOTER,
    "es": {
        "title": "Cómo Llegar a la Playa — Tamariu Chalet",
        "desc": "La playa de Tamariu está a solo 750 metros de la casa — indicaciones paso a paso para bajar andando desde Tamariu Chalet.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">Cómo Llegar → Cómo Llegar a la Playa</p><h1>Cómo Llegar a la Playa</h1></div></div>
<div class="content-page">

  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:28px;max-width:720px;">La playa está a solo 750 metros de la casa — un paseo corto y fácil bajando por las tranquilas calles residenciales del pueblo. Hay algunos tramos de escaleras por el camino y se tarda apenas unos minutos a pie.</p>

""" + _BEACH_IMG.format(img="../../images/way-to-beach/way-to-beach.jpg",
                        alt="El camino desde la casa hasta la playa de Tamariu") + """

  <h2>De un Vistazo</h2>
  <ul>
    <li><strong>Distancia:</strong> unos 750 metros desde la casa</li>
    <li><strong>A pie:</strong> apenas unos minutos, casi todo cuesta abajo</li>
    <li><strong>Recorrido:</strong> calles residenciales tranquilas con algunas escaleras</li>
  </ul>

  <h2 style="margin-top:32px;">Indicaciones hasta la Playa</h2>
  <ol style="max-width:720px;line-height:1.75;color:var(--stone);">
    <li>Al salir de la casa, gire a la izquierda y camine hasta el final de la calle.</li>
    <li>Justo pasado el número 19 encontrará unas escaleras. Bájelas y, al llegar abajo, gire a la derecha.</li>
    <li>Siga la calle y luego baje un tramo empinado. Donde la calle gira a la derecha, hay otras escaleras a la izquierda.</li>
    <li>Baje esas escaleras y, al final, gire a la derecha. A unos 20 metros llegará a unas escaleras que suben hasta la parte alta del pueblo.</li>
    <li>Siga la calle según gira a la izquierda — el supermercado Spar más grande quedará enfrente, al otro lado de la carretera principal.</li>
    <li>Tome cualquier calle a la izquierda desde aquí y le llevará hasta la playa.</li>
  </ol>

</div>
""",
    },
    "ca": {
        "title": "Com Arribar a la Platja — Tamariu Chalet",
        "desc": "La platja de Tamariu és a només 750 metres de la casa — indicacions pas a pas per baixar-hi a peu des de Tamariu Chalet.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">Com Arribar → Com Arribar a la Platja</p><h1>Com Arribar a la Platja</h1></div></div>
<div class="content-page">

  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:28px;max-width:720px;">La platja és a només 750 metres de la casa — un passeig curt i fàcil baixant pels carrers residencials tranquils del poble. Hi ha alguns trams d'escales pel camí i s'hi triga tot just uns minuts a peu.</p>

""" + _BEACH_IMG.format(img="../../images/way-to-beach/way-to-beach.jpg",
                        alt="El camí des de la casa fins a la platja de Tamariu") + """

  <h2>D'un Cop d'Ull</h2>
  <ul>
    <li><strong>Distància:</strong> uns 750 metres des de la casa</li>
    <li><strong>A peu:</strong> tot just uns minuts, gairebé tot costa avall</li>
    <li><strong>Recorregut:</strong> carrers residencials tranquils amb algunes escales</li>
  </ul>

  <h2 style="margin-top:32px;">Indicacions fins a la Platja</h2>
  <ol style="max-width:720px;line-height:1.75;color:var(--stone);">
    <li>En sortir de la casa, gireu a l'esquerra i camineu fins al final del carrer.</li>
    <li>Just passat el número 19 trobareu unes escales. Baixeu-les i, un cop a baix, gireu a la dreta.</li>
    <li>Seguiu el carrer i després baixeu un tram costerut. Allà on el carrer gira a la dreta, hi ha unes altres escales a l'esquerra.</li>
    <li>Baixeu aquestes escales i, al final, gireu a la dreta. A uns 20 metres arribareu a unes escales que pugen fins a la part alta del poble.</li>
    <li>Seguiu el carrer mentre gira a l'esquerra — el supermercat Spar més gran us quedarà al davant, a l'altra banda de la carretera principal.</li>
    <li>Agafeu qualsevol carrer a l'esquerra des d'aquí i us portarà fins a la platja.</li>
  </ol>

</div>
""",
    },
    "fr": {
        "title": "Aller à la Plage — Tamariu Chalet",
        "desc": "La plage de Tamariu est à seulement 750 mètres de la maison — itinéraire pas à pas pour y descendre à pied depuis le Tamariu Chalet.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">Comment Venir → Aller à la Plage</p><h1>Aller à la Plage</h1></div></div>
<div class="content-page">

  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:28px;max-width:720px;">La plage n'est qu'à 750 mètres de la maison — une courte descente facile par les rues résidentielles tranquilles du village. Quelques escaliers jalonnent le parcours et il ne faut que quelques minutes à pied.</p>

""" + _BEACH_IMG.format(img="../../images/way-to-beach/way-to-beach.jpg",
                        alt="Le chemin de la maison jusqu'à la plage de Tamariu") + """

  <h2>En Bref</h2>
  <ul>
    <li><strong>Distance :</strong> environ 750 mètres depuis la maison</li>
    <li><strong>À pied :</strong> quelques minutes seulement, essentiellement en descente</li>
    <li><strong>Parcours :</strong> rues résidentielles tranquilles avec quelques escaliers</li>
  </ul>

  <h2 style="margin-top:32px;">Itinéraire vers la Plage</h2>
  <ol style="max-width:720px;line-height:1.75;color:var(--stone);">
    <li>En sortant de la propriété, tournez à gauche et marchez jusqu'au bout de la rue.</li>
    <li>Juste après le numéro 19, vous trouverez un escalier. Descendez-le puis, en bas, tournez à droite.</li>
    <li>Suivez la route, puis descendez une section raide. Là où la route oblique à droite, un autre escalier se trouve sur la gauche.</li>
    <li>Descendez cet escalier et, en bas, tournez à droite. Après une vingtaine de mètres, vous arriverez à un escalier qui monte vers le haut du village.</li>
    <li>Suivez la route qui tourne à gauche — le grand supermarché Spar sera devant vous, de l'autre côté de la route principale.</li>
    <li>Prenez n'importe quelle rue sur la gauche à partir d'ici : elle vous mènera à la plage.</li>
  </ol>

</div>
""",
    },
    "nl": {
        "title": "Naar het Strand — Tamariu Chalet",
        "desc": "Het strand van Tamariu ligt op slechts 750 meter van het huis — stap-voor-stap routebeschrijving vanaf Tamariu Chalet.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">Hoe Te Bereiken → Naar het Strand</p><h1>Naar het Strand</h1></div></div>
<div class="content-page">

  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:28px;max-width:720px;">Het strand ligt op slechts 750 meter van het huis — een korte, makkelijke wandeling naar beneden door de rustige woonstraten van het dorp. Onderweg zijn er enkele trappen en te voet duurt het maar een paar minuten.</p>

""" + _BEACH_IMG.format(img="../../images/way-to-beach/way-to-beach.jpg",
                        alt="De wandeling van het huis naar het strand van Tamariu") + """

  <h2>In het Kort</h2>
  <ul>
    <li><strong>Afstand:</strong> ongeveer 750 meter vanaf het huis</li>
    <li><strong>Te voet:</strong> slechts een paar minuten, grotendeels bergafwaarts</li>
    <li><strong>Route:</strong> rustige woonstraten met enkele trappen</li>
  </ul>

  <h2 style="margin-top:32px;">Routebeschrijving naar het Strand</h2>
  <ol style="max-width:720px;line-height:1.75;color:var(--stone);">
    <li>Ga bij het verlaten van het huis linksaf en loop tot het einde van de straat.</li>
    <li>Net voorbij nummer 19 vindt u een trap. Ga deze af en sla onderaan rechtsaf.</li>
    <li>Volg de weg en daarna een steil stuk naar beneden. Waar de weg naar rechts buigt, ligt links nog een trap.</li>
    <li>Ga deze trap af en sla onderaan rechtsaf. Na ongeveer 20 meter komt u bij een trap die omhoog naar het hoger gelegen deel van het dorp leidt.</li>
    <li>Volg de weg die naar links buigt — de grotere Spar-supermarkt ligt dan recht voor u, aan de overkant van de hoofdweg.</li>
    <li>Neem vanaf hier een willekeurige straat naar links; die brengt u naar het strand.</li>
  </ol>

</div>
""",
    },
}
