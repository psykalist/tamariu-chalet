#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Authored translations for tourist-info, water-sports and shared-facilities."""

from content_things_to_do import FOOTER_STD, FOOTER_WATER, FOOTER_FACILITIES

PAGES = {}

# ─────────────────────────────────────────────────────────────────────────────
# things-to-do/tourist-info.html
# {julivia} and {begur} are resolved by the builder so the links point at the
# translated bus pages where they exist.
# ─────────────────────────────────────────────────────────────────────────────
PAGES["things-to-do/tourist-info.html"] = {
    "footer": FOOTER_STD,
    "es": {
        "title": "Información Turística — Tamariu Chalet",
        "desc": "Información turística de Tamariu y la Costa Brava — playas, actividades, consejos locales y transporte desde Tamariu Chalet.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">Qué Hacer → Información Turística</p><h1>Oficina de Turismo de Palafrugell</h1></div></div>
<div class="content-page">
  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">La Oficina de Turismo de Palafrugell es un recurso excelente para planificar su estancia en la zona — con información actualizada sobre eventos, actividades, transporte y atractivos locales.</p>

  <a href="https://visitpalafrugell.cat/palafrugell/" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Visit Palafrugell — Web Oficial de Turismo</h4>
      <p>El portal oficial de turismo de Palafrugell, que cubre Tamariu, Llafranc, Calella de Palafrugell y el conjunto del municipio. Eventos, playas, actividades e información práctica.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Oficina de Turismo — Palafrugell</h2>
  <p>La oficina principal de turismo está en el centro de Palafrugell. El equipo puede facilitarle mapas, programación de eventos, horarios de autobús y recomendaciones personales. Se habla inglés.</p>
  <ul>
    <li>Abierta de lunes a sábado en temporada; horario reducido fuera de temporada</li>
    <li>Mapas gratuitos del camino de ronda y de las rutas ciclistas</li>
    <li>Programación actualizada de conciertos, mercados y fiestas</li>
    <li>Información sobre el festival de habaneras (un famoso evento anual en Calella de Palafrugell)</li>
  </ul>

  <h2 style="margin-top:32px;">Servicios de Autobús Locales</h2>
  <p>Dos servicios de autobús de temporada permiten explorar la zona sin coche:</p>

  <a href="{julivia}" class="external-link-card" style="margin-top:16px;">
    <div>
      <h4>Bus Julivia</h4>
      <p>Un autobús turístico de temporada que une Palafrugell con los pueblos costeros de Tamariu, Llafranc y Calella de Palafrugell. Funciona aproximadamente de mayo a octubre — económico, se paga a bordo.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <a href="{begur}" class="external-link-card" style="margin-top:12px;">
    <div>
      <h4>Bus Playas de Begur</h4>
      <p>Un servicio lanzadera que conecta Begur con sus calas y playas — ideal para llegar a los rincones más apartados sin coche ni preocupaciones de aparcamiento.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Información Local Útil</h2>
  <ul>
    <li>Tamariu tiene un pequeño supermercado abierto en temporada; Palafrugell cuenta con supermercados más grandes como Mercadona y Lidl</li>
    <li>La farmacia más cercana está en el centro de Palafrugell</li>
    <li>El hospital más cercano está en Palamós (Hospital de Palamós), a 15 minutos en coche</li>
    <li>Las gasolineras están en Palafrugell; en Tamariu no hay</li>
    <li>El aparcamiento en Tamariu es limitado en pleno verano — se recomienda llegar temprano</li>
  </ul>
</div>
""",
    },
    "ca": {
        "title": "Informació Turística — Tamariu Chalet",
        "desc": "Informació turística de Tamariu i la Costa Brava — platges, activitats, consells locals i transport des de Tamariu Chalet.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">Què Fer → Informació Turística</p><h1>Oficina de Turisme de Palafrugell</h1></div></div>
<div class="content-page">
  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">L'Oficina de Turisme de Palafrugell és un recurs excel·lent per planificar la vostra estada a la zona — amb informació actualitzada sobre esdeveniments, activitats, transport i atractius locals.</p>

  <a href="https://visitpalafrugell.cat/palafrugell/" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Visit Palafrugell — Web Oficial de Turisme</h4>
      <p>El portal oficial de turisme de Palafrugell, que cobreix Tamariu, Llafranc, Calella de Palafrugell i el conjunt del municipi. Esdeveniments, platges, activitats i informació pràctica.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Oficina de Turisme — Palafrugell</h2>
  <p>L'oficina principal de turisme és al centre de Palafrugell. L'equip us pot facilitar mapes, programació d'esdeveniments, horaris d'autobús i recomanacions personals. S'hi parla anglès.</p>
  <ul>
    <li>Oberta de dilluns a dissabte en temporada; horari reduït fora de temporada</li>
    <li>Mapes gratuïts del camí de ronda i de les rutes ciclistes</li>
    <li>Programació actualitzada de concerts, mercats i festes</li>
    <li>Informació sobre el festival d'havaneres (un famós esdeveniment anual a Calella de Palafrugell)</li>
  </ul>

  <h2 style="margin-top:32px;">Serveis d'Autobús Locals</h2>
  <p>Dos serveis d'autobús de temporada permeten explorar la zona sense cotxe:</p>

  <a href="{julivia}" class="external-link-card" style="margin-top:16px;">
    <div>
      <h4>Bus Julivia</h4>
      <p>Un autobús turístic de temporada que uneix Palafrugell amb els pobles costaners de Tamariu, Llafranc i Calella de Palafrugell. Funciona aproximadament de maig a octubre — econòmic, es paga a bord.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <a href="{begur}" class="external-link-card" style="margin-top:12px;">
    <div>
      <h4>Bus Platges de Begur</h4>
      <p>Un servei llançadora que connecta Begur amb les seves cales i platges — ideal per arribar als racons més apartats sense cotxe ni maldecaps d'aparcament.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Informació Local Útil</h2>
  <ul>
    <li>Tamariu té un petit supermercat obert en temporada; Palafrugell compta amb supermercats més grans com Mercadona i Lidl</li>
    <li>La farmàcia més propera és al centre de Palafrugell</li>
    <li>L'hospital més proper és a Palamós (Hospital de Palamós), a 15 minuts en cotxe</li>
    <li>Les benzineres són a Palafrugell; a Tamariu no n'hi ha</li>
    <li>L'aparcament a Tamariu és limitat en ple estiu — es recomana arribar aviat</li>
  </ul>
</div>
""",
    },
    "fr": {
        "title": "Office de Tourisme — Tamariu Chalet",
        "desc": "Informations touristiques sur Tamariu et la Costa Brava — plages, activités, conseils locaux et transports depuis le Tamariu Chalet.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">À Faire → Office de Tourisme</p><h1>Office de Tourisme de Palafrugell</h1></div></div>
<div class="content-page">
  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">L'office de tourisme de Palafrugell est une excellente ressource pour organiser votre séjour dans la région — avec des informations à jour sur les événements, les activités, les transports et les sites à découvrir.</p>

  <a href="https://visitpalafrugell.cat/palafrugell/" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Visit Palafrugell — Site Officiel du Tourisme</h4>
      <p>Le portail touristique officiel de Palafrugell, couvrant Tamariu, Llafranc, Calella de Palafrugell et l'ensemble de la commune. Événements, plages, activités et informations pratiques.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Office de Tourisme — Palafrugell</h2>
  <p>L'office principal se trouve dans le centre de Palafrugell. L'équipe fournit cartes, programmes d'événements, horaires de bus et recommandations personnalisées. L'anglais y est parlé.</p>
  <ul>
    <li>Ouvert du lundi au samedi en saison ; horaires réduits hors saison</li>
    <li>Cartes gratuites du chemin côtier et des itinéraires cyclables</li>
    <li>Programme actualisé des concerts, marchés et fêtes</li>
    <li>Informations sur le festival de havaneres (célèbre rendez-vous annuel à Calella de Palafrugell)</li>
  </ul>

  <h2 style="margin-top:32px;">Lignes de Bus Locales</h2>
  <p>Deux services de bus saisonniers permettent d'explorer la région sans voiture :</p>

  <a href="{julivia}" class="external-link-card" style="margin-top:16px;">
    <div>
      <h4>Bus Julivia</h4>
      <p>Un bus touristique saisonnier reliant Palafrugell aux villages côtiers de Tamariu, Llafranc et Calella de Palafrugell. Circule environ de mai à octobre — abordable, paiement à bord.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <a href="{begur}" class="external-link-card" style="margin-top:12px;">
    <div>
      <h4>Bus des Plages de Begur</h4>
      <p>Une navette reliant Begur à ses criques et plages environnantes — idéale pour accéder aux endroits les plus reculés sans voiture ni souci de stationnement.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Informations Pratiques</h2>
  <ul>
    <li>Tamariu dispose d'une petite supérette ouverte en saison ; Palafrugell compte de plus grands supermarchés dont Mercadona et Lidl</li>
    <li>La pharmacie la plus proche se trouve dans le centre de Palafrugell</li>
    <li>L'hôpital le plus proche est à Palamós (Hospital de Palamós), à 15 minutes en voiture</li>
    <li>Les stations-service sont à Palafrugell ; il n'y en a pas à Tamariu</li>
    <li>Le stationnement à Tamariu est limité en plein été — arrivée matinale recommandée</li>
  </ul>
</div>
""",
    },
    "nl": {
        "title": "Toeristische Informatie — Tamariu Chalet",
        "desc": "Toeristische informatie over Tamariu en de Costa Brava — stranden, activiteiten, lokale tips en vervoer vanaf Tamariu Chalet.",
        "content": """
<div class="page-hero"><div class="page-hero-content"><p class="breadcrumb">Wat Te Doen → Toeristische Informatie</p><h1>VVV Palafrugell</h1></div></div>
<div class="content-page">
  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">Het toeristenbureau van Palafrugell is een uitstekende bron om uw tijd in de streek te plannen — met actuele informatie over evenementen, activiteiten, vervoer en bezienswaardigheden.</p>

  <a href="https://visitpalafrugell.cat/palafrugell/" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Visit Palafrugell — Officiële Toerismewebsite</h4>
      <p>Het officiële toerismeportaal van Palafrugell, met Tamariu, Llafranc, Calella de Palafrugell en de hele gemeente. Evenementen, stranden, activiteiten en praktische informatie.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Toeristenbureau — Palafrugell</h2>
  <p>Het hoofdkantoor bevindt zich in het centrum van Palafrugell. Het team helpt met kaarten, evenementenoverzichten, busdienstregelingen en persoonlijke tips. Er wordt Engels gesproken.</p>
  <ul>
    <li>Geopend van maandag tot zaterdag in het seizoen; beperkte openingstijden daarbuiten</li>
    <li>Gratis kaarten van het kustpad en de fietsroutes</li>
    <li>Actueel overzicht van concerten, markten en feesten</li>
    <li>Informatie over het habanera-zangfestival (een bekend jaarlijks evenement in Calella de Palafrugell)</li>
  </ul>

  <h2 style="margin-top:32px;">Lokale Busdiensten</h2>
  <p>Twee seizoensgebonden busdiensten maken het eenvoudig om de streek zonder auto te verkennen:</p>

  <a href="{julivia}" class="external-link-card" style="margin-top:16px;">
    <div>
      <h4>Julivia Bus</h4>
      <p>Een seizoensgebonden toeristenbus die Palafrugell verbindt met de kustdorpen Tamariu, Llafranc en Calella de Palafrugell. Rijdt ongeveer van mei tot oktober — betaalbaar, u betaalt in de bus.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <a href="{begur}" class="external-link-card" style="margin-top:12px;">
    <div>
      <h4>Begur Strandbus</h4>
      <p>Een pendeldienst tussen Begur en de omliggende baaien en stranden — ideaal om de afgelegen plekjes te bereiken zonder auto of parkeerzorgen.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Handige Lokale Informatie</h2>
  <ul>
    <li>Tamariu heeft een kleine supermarkt die in het seizoen open is; Palafrugell heeft grotere supermarkten waaronder Mercadona en Lidl</li>
    <li>De dichtstbijzijnde apotheek is in het centrum van Palafrugell</li>
    <li>Het dichtstbijzijnde ziekenhuis is in Palamós (Hospital de Palamós), 15 minuten met de auto</li>
    <li>Tankstations bevinden zich in Palafrugell; in Tamariu zelf zijn er geen</li>
    <li>Parkeren in Tamariu is beperkt in het hoogseizoen — vroeg aankomen wordt aangeraden</li>
  </ul>
</div>
""",
    },
}

# ─────────────────────────────────────────────────────────────────────────────
# things-to-do/water-sports.html
# ─────────────────────────────────────────────────────────────────────────────
PAGES["things-to-do/water-sports.html"] = {
    "footer": FOOTER_WATER,
    "es": {
        "title": "Deportes Acuáticos — Tamariu Chalet",
        "desc": "Deportes acuáticos cerca de Tamariu, Costa Brava — kayak, buceo, snorkel y paddle surf en las calas de aguas cristalinas de la Costa Brava.",
        "content": """
<div class="page-hero">
  <div class="page-hero-content">
    <p class="breadcrumb">Qué Hacer → Deportes Acuáticos</p>
    <h1>Deportes Acuáticos y Actividades en el Mar</h1>
  </div>
</div>

<div class="content-page">

  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">
    Las aguas claras y tranquilas de la Costa Brava la convierten en uno de los mejores lugares del
    Mediterráneo para todo tipo de deportes acuáticos. La cala resguardada de Tamariu es una base
    perfecta — aquí el mar es notablemente transparente y los promontorios rocosos de la bocana
    rebosan de vida marina.
  </p>

  <h2>Paddle Surf</h2>
  <p>El paddle surf (SUP) es maravilloso en la bahía tranquila de Tamariu, sobre todo a primera hora de la mañana, antes de que se levante la brisa. En verano hay alquiler de tablas en la playa. Remar junto a los acantilados al amanecer es inolvidable.</p>

  <h2>Alquiler de Barcas</h2>
  <p>En verano se pueden alquilar pequeñas embarcaciones a motor en la playa de Tamariu, lo que permite explorar las calas escondidas y las cuevas marinas de la costa al norte y al sur — muchas inaccesibles a pie. No se requiere titulación para las embarcaciones de menos de 5 CV. Pregunte en el pueblo al llegar por la disponibilidad de alquiler.</p>

  <h2>Snorkel</h2>
  <p>Los arrecifes rocosos justo enfrente de la playa de Tamariu son excelentes para el snorkel, con buena visibilidad y variedad de peces, pulpos y erizos de mar. Las praderas de posidonia de la bocana son un hábitat protegido y una señal de la excepcional calidad del agua. Traiga sus gafas y aletas o alquílelas en los quioscos de la playa en verano.</p>

  <h2>Submarinismo</h2>
  <p>La Costa Brava es uno de los mejores destinos de buceo del Mediterráneo, con una topografía submarina espectacular, excelente visibilidad y abundante vida marina. Recomendamos especialmente Stollis Dive Base, un centro de buceo excelente y de gran prestigio en la zona.</p>

  <a href="https://stollis-divebase.com/en/index.html" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Stollis Dive Base</h4>
      <p>Centro de buceo profesional que ofrece cursos, inmersiones guiadas y alquiler de equipo en la Costa Brava. Apto para todos los niveles, de principiantes a buceadores avanzados.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Kayak</h2>
  <p>El kayak de mar por este tramo de costa es excepcional — hay excursiones guiadas que salen de Tamariu hacia el sur bordeando los acantilados, explorando cuevas marinas, puntos de snorkel y calas apartadas. Kayaking Costa Brava ofrece una magnífica excursión guiada de medio día con salida desde Tamariu.</p>

  <a href="https://kayakingcostabrava.com/en/activities/guided-excursions/tamariu-south-half-day/" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Kayaking Costa Brava — Tamariu Sur, Medio Día</h4>
      <p>Excursión guiada en kayak de mar desde Tamariu hacia el sur por una costa espectacular. Incluye paradas para hacer snorkel y explorar cuevas marinas escondidas. Apta para todos los niveles.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Consejos para el Mar</h2>
  <ul>
    <li>El mar en Tamariu es tranquilo, pero compruebe las condiciones antes de salir — la tramuntana puede levantarse de repente</li>
    <li>El calzado de agua resulta útil en las entradas rocosas de la bahía</li>
    <li>La protección solar es imprescindible — el sol mediterráneo pega fuerte incluso con brisa marina</li>
    <li>La playa tiene socorrista en verano; las banderas indican el estado del mar</li>
    <li>Reserve las excursiones de kayak y buceo con antelación en julio y agosto</li>
  </ul>

</div>
""",
    },
    "ca": {
        "title": "Esports Aquàtics — Tamariu Chalet",
        "desc": "Esports aquàtics a prop de Tamariu, Costa Brava — caiac, submarinisme, snorkel i paddle surf a les cales d'aigües cristal·lines de la Costa Brava.",
        "content": """
<div class="page-hero">
  <div class="page-hero-content">
    <p class="breadcrumb">Què Fer → Esports Aquàtics</p>
    <h1>Esports Aquàtics i Activitats al Mar</h1>
  </div>
</div>

<div class="content-page">

  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">
    Les aigües clares i tranquil·les de la Costa Brava la converteixen en un dels millors indrets
    del Mediterrani per a tota mena d'esports aquàtics. La cala arrecerada de Tamariu és una base
    perfecta — aquí el mar és notablement transparent i els caps rocosos de la bocana són plens
    de vida marina.
  </p>

  <h2>Paddle Surf</h2>
  <p>El paddle surf (SUP) és meravellós a la badia tranquil·la de Tamariu, sobretot a primera hora del matí, abans que s'aixequi la brisa. A l'estiu hi ha lloguer de taules a la platja. Remar arran dels penya-segats a trenc d'alba és inoblidable.</p>

  <h2>Lloguer de Barques</h2>
  <p>A l'estiu es poden llogar petites embarcacions a motor a la platja de Tamariu, cosa que permet explorar les cales amagades i les coves marines de la costa cap al nord i cap al sud — moltes inaccessibles a peu. No cal titulació per a embarcacions de menys de 5 CV. Pregunteu al poble en arribar per la disponibilitat de lloguer.</p>

  <h2>Snorkel</h2>
  <p>Els esculls rocosos just davant de la platja de Tamariu són excel·lents per fer snorkel, amb bona visibilitat i varietat de peixos, pops i eriçons de mar. Les praderies de posidònia de la bocana són un hàbitat protegit i un senyal de l'excepcional qualitat de l'aigua. Porteu ulleres i aletes o llogueu-les als quioscos de la platja a l'estiu.</p>

  <h2>Submarinisme</h2>
  <p>La Costa Brava és una de les millors destinacions de busseig del Mediterrani, amb una topografia submarina espectacular, excel·lent visibilitat i vida marina abundant. Recomanem especialment Stollis Dive Base, un centre de busseig excel·lent i de gran prestigi a la zona.</p>

  <a href="https://stollis-divebase.com/en/index.html" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Stollis Dive Base</h4>
      <p>Centre de busseig professional que ofereix cursos, immersions guiades i lloguer d'equip a la Costa Brava. Apte per a tots els nivells, de principiants a bussejadors avançats.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Caiac</h2>
  <p>El caiac de mar per aquest tram de costa és excepcional — hi ha excursions guiades que surten de Tamariu cap al sud vorejant els penya-segats, explorant coves marines, punts de snorkel i cales apartades. Kayaking Costa Brava ofereix una magnífica excursió guiada de mig dia amb sortida des de Tamariu.</p>

  <a href="https://kayakingcostabrava.com/en/activities/guided-excursions/tamariu-south-half-day/" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Kayaking Costa Brava — Tamariu Sud, Mig Dia</h4>
      <p>Excursió guiada en caiac de mar des de Tamariu cap al sud per una costa espectacular. Inclou parades per fer snorkel i explorar coves marines amagades. Apta per a tots els nivells.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Consells per al Mar</h2>
  <ul>
    <li>El mar a Tamariu és tranquil, però comproveu les condicions abans de sortir — la tramuntana pot aixecar-se de sobte</li>
    <li>El calçat d'aigua és útil a les entrades rocoses de la badia</li>
    <li>La protecció solar és imprescindible — el sol mediterrani pica fort fins i tot amb brisa marina</li>
    <li>La platja té socorrista a l'estiu; les banderes indiquen l'estat del mar</li>
    <li>Reserveu les excursions de caiac i busseig amb antelació el juliol i l'agost</li>
  </ul>

</div>
""",
    },
    "fr": {
        "title": "Sports Nautiques — Tamariu Chalet",
        "desc": "Sports nautiques près de Tamariu, Costa Brava — kayak, plongée, snorkeling et paddle dans les criques aux eaux cristallines de la Costa Brava.",
        "content": """
<div class="page-hero">
  <div class="page-hero-content">
    <p class="breadcrumb">À Faire → Sports Nautiques</p>
    <h1>Sports Nautiques &amp; Activités en Mer</h1>
  </div>
</div>

<div class="content-page">

  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">
    Les eaux claires et calmes de la Costa Brava en font l'un des meilleurs spots de Méditerranée
    pour les sports nautiques en tout genre. La crique abritée de Tamariu est une base idéale —
    la mer y est remarquablement limpide et les pointes rocheuses toutes proches regorgent de
    vie marine.
  </p>

  <h2>Paddle</h2>
  <p>Le stand-up paddle (SUP) est un vrai plaisir dans la baie calme de Tamariu, surtout tôt le matin avant que la brise ne se lève. Location de planches sur la plage en été. Pagayer le long des falaises au lever du soleil est inoubliable.</p>

  <h2>Location de Bateaux</h2>
  <p>De petits bateaux à moteur se louent sur la plage de Tamariu en été, ce qui permet d'explorer les criques cachées et les grottes marines du littoral au nord comme au sud — dont beaucoup sont inaccessibles à pied. Aucun permis n'est requis pour les embarcations de moins de 5 CV. Renseignez-vous sur place à votre arrivée pour les disponibilités.</p>

  <h2>Snorkeling</h2>
  <p>Les récifs rocheux juste devant la plage de Tamariu sont excellents pour le snorkeling, avec une bonne visibilité et une belle variété de poissons, poulpes et oursins. Les herbiers de posidonie au large sont un habitat protégé et le signe d'une qualité d'eau exceptionnelle. Apportez masque et palmes ou louez-les aux kiosques de la plage en été.</p>

  <h2>Plongée Sous-Marine</h2>
  <p>La Costa Brava est l'une des meilleures destinations de plongée de Méditerranée, avec un relief sous-marin spectaculaire, une excellente visibilité et une faune abondante. Nous recommandons particulièrement Stollis Dive Base, un centre de plongée réputé et de grande qualité dans la région.</p>

  <a href="https://stollis-divebase.com/en/index.html" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Stollis Dive Base</h4>
      <p>Centre de plongée professionnel proposant cours, plongées guidées et location de matériel sur la Costa Brava. Convient à tous les niveaux, du débutant au plongeur confirmé.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Kayak</h2>
  <p>Le kayak de mer sur cette portion de côte est exceptionnel — des excursions guidées partent de Tamariu vers le sud le long des falaises, à la découverte des grottes marines, des spots de snorkeling et des criques isolées. Kayaking Costa Brava propose une superbe excursion guidée d'une demi-journée au départ de Tamariu.</p>

  <a href="https://kayakingcostabrava.com/en/activities/guided-excursions/tamariu-south-half-day/" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Kayaking Costa Brava — Tamariu Sud, Demi-Journée</h4>
      <p>Excursion guidée en kayak de mer au départ de Tamariu vers le sud, le long d'un littoral spectaculaire. Comprend des arrêts snorkeling et l'exploration de grottes marines cachées. Accessible à tous.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Conseils en Mer</h2>
  <ul>
    <li>La mer à Tamariu est calme, mais vérifiez les conditions avant de partir — la Tramontane peut se lever rapidement</li>
    <li>Des chaussures d'eau sont utiles sur les entrées rocheuses de la baie</li>
    <li>La protection solaire est indispensable — le soleil méditerranéen tape fort, même avec la brise</li>
    <li>La plage est surveillée en été ; les drapeaux indiquent l'état de la mer</li>
    <li>Réservez les sorties kayak et plongée à l'avance en juillet et août</li>
  </ul>

</div>
""",
    },
    "nl": {
        "title": "Watersport — Tamariu Chalet",
        "desc": "Watersport bij Tamariu, Costa Brava — kajakken, duiken, snorkelen en suppen in de kristalheldere baaien van de Costa Brava.",
        "content": """
<div class="page-hero">
  <div class="page-hero-content">
    <p class="breadcrumb">Wat Te Doen → Watersport</p>
    <h1>Watersport &amp; Activiteiten op Zee</h1>
  </div>
</div>

<div class="content-page">

  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:30px;max-width:700px;">
    Door het heldere, kalme water is de Costa Brava een van de beste plekken in de Middellandse Zee
    voor watersport in alle vormen. De beschutte baai van Tamariu is een perfecte uitvalsbasis — de
    zee is hier opmerkelijk helder en de rotspunten net buiten de baai zitten vol zeeleven.
  </p>

  <h2>Suppen</h2>
  <p>Stand-up paddleboarding (SUP) is heerlijk in de kalme baai van Tamariu, vooral vroeg in de ochtend voordat er wind opsteekt. In de zomer kunt u boards huren op het strand. Bij zonsopgang langs de kliffen peddelen is onvergetelijk.</p>

  <h2>Bootverhuur</h2>
  <p>In de zomer zijn er kleine motorbootjes te huur op het strand van Tamariu, waarmee u de verborgen baaien en zeegrotten ten noorden en zuiden kunt verkennen — veel daarvan zijn te voet onbereikbaar. Voor vaartuigen onder 5 pk is geen vaarbewijs nodig. Informeer bij aankomst ter plaatse naar de actuele beschikbaarheid.</p>

  <h2>Snorkelen</h2>
  <p>De rotsriffen direct voor het strand van Tamariu zijn uitstekend om te snorkelen, met goed zicht en een grote variatie aan vissen, octopussen en zee-egels. De posidonia-zeegrasvelden vlak voor de kust zijn beschermd gebied en een teken van de uitzonderlijke waterkwaliteit. Neem uw eigen masker en vinnen mee of huur ze in de zomer bij de strandkiosken.</p>

  <h2>Duiken</h2>
  <p>De Costa Brava is een van de beste duikbestemmingen van de Middellandse Zee, met een spectaculair onderwaterlandschap, uitstekend zicht en volop zeeleven. Wij raden in het bijzonder Stollis Dive Base aan, een uitstekend en goed aangeschreven duikcentrum in de regio.</p>

  <a href="https://stollis-divebase.com/en/index.html" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Stollis Dive Base</h4>
      <p>Professioneel duikcentrum met cursussen, begeleide duiken en materiaalverhuur aan de Costa Brava. Geschikt voor alle niveaus, van beginners tot gevorderde duikers.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Kajakken</h2>
  <p>Zeekajakken langs dit stuk kust is uitzonderlijk — er vertrekken begeleide tochten vanuit Tamariu zuidwaarts langs de kliffen, waarbij zeegrotten, snorkelplekken en afgelegen baaien worden verkend. Kayaking Costa Brava biedt een prachtige begeleide halvedagtocht met vertrek vanuit Tamariu.</p>

  <a href="https://kayakingcostabrava.com/en/activities/guided-excursions/tamariu-south-half-day/" target="_blank" rel="noopener" class="external-link-card">
    <div>
      <h4>Kayaking Costa Brava — Tamariu Zuid, Halve Dag</h4>
      <p>Een begeleide zeekajaktocht vanuit Tamariu in zuidelijke richting langs de indrukwekkende kustlijn. Inclusief snorkelstops en het verkennen van verborgen zeegrotten. Geschikt voor alle niveaus.</p>
    </div>
    <span class="link-arrow">→</span>
  </a>

  <h2 style="margin-top:32px;">Tips voor op Zee</h2>
  <ul>
    <li>De zee bij Tamariu is kalm, maar controleer de omstandigheden voor u vertrekt — de Tramuntana-wind kan snel opsteken</li>
    <li>Waterschoenen zijn handig bij de rotsachtige instappunten rond de baai</li>
    <li>Zonbescherming is essentieel — de mediterrane zon is sterk, ook met een zeebries</li>
    <li>Het strand heeft in de zomer een strandwacht; vlaggen geven de zeecondities aan</li>
    <li>Boek kajak- en duiktochten in juli en augustus ruim van tevoren</li>
  </ul>

</div>
""",
    },
}

# ─────────────────────────────────────────────────────────────────────────────
# accommodation/shared-facilities.html
# {double}, {twin1}, {twin2} are resolved by the builder.
# ─────────────────────────────────────────────────────────────────────────────
_FAC_IMG = "../../images/facilities/"

PAGES["accommodation/shared-facilities.html"] = {
    "footer": FOOTER_FACILITIES,
    "es": {
        "title": "Baños y Cocina Compartidos — Tamariu Chalet",
        "desc": "Baños y cocina compartidos en Tamariu Chalet, Tamariu, Costa Brava — bien equipados y cuidados para todos los huéspedes de las habitaciones.",
        "content": """
<div class="page-hero">
  <div class="page-hero-content">
    <p class="breadcrumb">Alojamiento → Instalaciones Compartidas</p>
    <h1>Baños y Cocina Compartidos</h1>
  </div>
</div>

<div class="content-page">

  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:24px;max-width:700px;">
    Los huéspedes de la Habitación Doble, la Habitación Doble/Twin 1 y la Habitación Doble/Twin 2
    comparten dos baños bien equipados y una cocina compartida totalmente instalada. Todas las
    instalaciones se mantienen con un alto nivel de limpieza y tienen un tamaño holgado para el
    número de habitaciones a las que dan servicio.
  </p>

  <div class="facilities-note">
    Cada baño da servicio a un máximo de dos habitaciones. La cocina compartida está totalmente
    equipada con todo lo necesario para cocinar — desde una placa completa hasta cafetera,
    tostadora y toda la vajilla.
  </div>

  <h2 style="margin-bottom:24px;">Los Baños</h2>
  <div class="facilities-grid">

    <div class="facility-card">
      <div class="facility-card-img">
        <img src="{img}bathroom-1.jpg" alt="Baño 1">
      </div>
      <div class="facility-card-body">
        <h3>Baño 1</h3>
        <p>Un baño limpio y bien equipado con ducha de obra, lavabo, inodoro y todos los accesorios necesarios. Toallas incluidas.</p>
      </div>
    </div>

    <div class="facility-card">
      <div class="facility-card-img">
        <img src="{img}bathroom-2.jpg" alt="Baño 2">
      </div>
      <div class="facility-card-body">
        <h3>Baño 2</h3>
        <p>Un segundo baño luminoso con ducha, lavabo e inodoro. Se prepara con ropa limpia y se repone para cada grupo de huéspedes.</p>
      </div>
    </div>

  </div>

  <h2 style="margin-bottom:24px;">La Cocina</h2>
  <div class="facilities-grid-kitchen">

    <div class="facility-card">
      <div class="facility-card-img-wide">
        <img src="{img}kitchen-1.jpg" alt="Cocina compartida">
      </div>
      <div class="facility-card-body">
        <h3>Cocina Compartida</h3>
        <p>Totalmente equipada con placa, microondas, hervidor, tostadora, cafetera, vajilla y cubertería completas, vasos, ollas y sartenes. Todo lo necesario para una estancia cómoda cocinando por su cuenta.</p>
      </div>
    </div>

    <div class="facility-card">
      <div class="facility-card-img-wide">
        <img src="{img}kitchen-2.jpg" alt="Cocina compartida — segunda vista">
      </div>
      <div class="facility-card-body">
        <h3>Cocina Compartida</h3>
        <p>Otra vista de la cocina compartida, donde se aprecia toda la encimera, el almacenaje y los electrodomésticos disponibles para todos los huéspedes de las habitaciones de la casa principal.</p>
      </div>
    </div>

  </div>

  <h2 style="margin-bottom:16px;">Habitaciones que Usan estas Instalaciones</h2>
  <p style="color:var(--stone);font-size:0.9rem;margin-bottom:20px;">Las siguientes habitaciones comparten los baños y la cocina que se muestran arriba:</p>
  <div class="room-links">
    <a href="{double}">← Habitación Doble</a>
    <a href="{twin1}">← Habitación Doble/Twin 1</a>
    <a href="{twin2}">← Habitación Doble/Twin 2</a>
  </div>

</div>
""".replace("{img}", _FAC_IMG),
    },
    "ca": {
        "title": "Banys i Cuina Compartits — Tamariu Chalet",
        "desc": "Banys i cuina compartits a Tamariu Chalet, Tamariu, Costa Brava — ben equipats i cuidats per a tots els hostes de les habitacions.",
        "content": """
<div class="page-hero">
  <div class="page-hero-content">
    <p class="breadcrumb">Allotjament → Instal·lacions Compartides</p>
    <h1>Banys i Cuina Compartits</h1>
  </div>
</div>

<div class="content-page">

  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:24px;max-width:700px;">
    Els hostes de l'Habitació Doble, l'Habitació Doble/Twin 1 i l'Habitació Doble/Twin 2 comparteixen
    dos banys ben equipats i una cuina compartida totalment instal·lada. Totes les instal·lacions es
    mantenen amb un alt nivell de neteja i tenen una mida folgada per al nombre d'habitacions a què
    donen servei.
  </p>

  <div class="facilities-note">
    Cada bany dona servei a un màxim de dues habitacions. La cuina compartida està totalment
    equipada amb tot el que cal per cuinar — des d'una placa completa fins a cafetera, torradora
    i tota la vaixella.
  </div>

  <h2 style="margin-bottom:24px;">Els Banys</h2>
  <div class="facilities-grid">

    <div class="facility-card">
      <div class="facility-card-img">
        <img src="{img}bathroom-1.jpg" alt="Bany 1">
      </div>
      <div class="facility-card-body">
        <h3>Bany 1</h3>
        <p>Un bany net i ben equipat amb dutxa d'obra, lavabo, vàter i tots els accessoris necessaris. Tovalloles incloses.</p>
      </div>
    </div>

    <div class="facility-card">
      <div class="facility-card-img">
        <img src="{img}bathroom-2.jpg" alt="Bany 2">
      </div>
      <div class="facility-card-body">
        <h3>Bany 2</h3>
        <p>Un segon bany lluminós amb dutxa, lavabo i vàter. Es prepara amb roba neta i es reposa per a cada grup d'hostes.</p>
      </div>
    </div>

  </div>

  <h2 style="margin-bottom:24px;">La Cuina</h2>
  <div class="facilities-grid-kitchen">

    <div class="facility-card">
      <div class="facility-card-img-wide">
        <img src="{img}kitchen-1.jpg" alt="Cuina compartida">
      </div>
      <div class="facility-card-body">
        <h3>Cuina Compartida</h3>
        <p>Totalment equipada amb placa, microones, bullidor, torradora, cafetera, vaixella i coberteria completes, gots, olles i paelles. Tot el que cal per a una estada còmoda cuinant pel vostre compte.</p>
      </div>
    </div>

    <div class="facility-card">
      <div class="facility-card-img-wide">
        <img src="{img}kitchen-2.jpg" alt="Cuina compartida — segona vista">
      </div>
      <div class="facility-card-body">
        <h3>Cuina Compartida</h3>
        <p>Una altra vista de la cuina compartida, on es veu tot el taulell, l'emmagatzematge i els electrodomèstics disponibles per a tots els hostes de les habitacions de la casa principal.</p>
      </div>
    </div>

  </div>

  <h2 style="margin-bottom:16px;">Habitacions que Utilitzen aquestes Instal·lacions</h2>
  <p style="color:var(--stone);font-size:0.9rem;margin-bottom:20px;">Les habitacions següents comparteixen els banys i la cuina que es mostren a dalt:</p>
  <div class="room-links">
    <a href="{double}">← Habitació Doble</a>
    <a href="{twin1}">← Habitació Doble/Twin 1</a>
    <a href="{twin2}">← Habitació Doble/Twin 2</a>
  </div>

</div>
""".replace("{img}", _FAC_IMG),
    },
    "fr": {
        "title": "Salles de Bain &amp; Cuisine Partagées — Tamariu Chalet",
        "desc": "Salles de bain et cuisine partagées au Tamariu Chalet, Tamariu, Costa Brava — bien équipées et parfaitement entretenues pour tous les hôtes des chambres.",
        "content": """
<div class="page-hero">
  <div class="page-hero-content">
    <p class="breadcrumb">Hébergement → Équipements Partagés</p>
    <h1>Salles de Bain &amp; Cuisine Partagées</h1>
  </div>
</div>

<div class="content-page">

  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:24px;max-width:700px;">
    Les hôtes de la Chambre Double, de la Chambre Double/Lits Jumeaux 1 et de la Chambre
    Double/Lits Jumeaux 2 partagent deux salles de bain bien équipées et une cuisine commune
    entièrement aménagée. Tous les équipements sont tenus à un haut niveau de propreté et
    dimensionnés confortablement pour le nombre de chambres qu'ils desservent.
  </p>

  <div class="facilities-note">
    Chaque salle de bain ne dessert pas plus de deux chambres. La cuisine partagée est entièrement
    équipée de tout le nécessaire pour cuisiner — de la plaque de cuisson complète à la cafetière,
    au grille-pain et à toute la vaisselle.
  </div>

  <h2 style="margin-bottom:24px;">Les Salles de Bain</h2>
  <div class="facilities-grid">

    <div class="facility-card">
      <div class="facility-card-img">
        <img src="{img}bathroom-1.jpg" alt="Salle de bain 1">
      </div>
      <div class="facility-card-body">
        <h3>Salle de Bain 1</h3>
        <p>Une salle de bain propre et bien agencée avec douche à l'italienne, lavabo, WC et tous les accessoires nécessaires. Serviettes fournies.</p>
      </div>
    </div>

    <div class="facility-card">
      <div class="facility-card-img">
        <img src="{img}bathroom-2.jpg" alt="Salle de bain 2">
      </div>
      <div class="facility-card-body">
        <h3>Salle de Bain 2</h3>
        <p>Une seconde salle de bain lumineuse avec douche, lavabo et WC. Linge frais et réapprovisionnement à chaque nouvelle arrivée.</p>
      </div>
    </div>

  </div>

  <h2 style="margin-bottom:24px;">La Cuisine</h2>
  <div class="facilities-grid-kitchen">

    <div class="facility-card">
      <div class="facility-card-img-wide">
        <img src="{img}kitchen-1.jpg" alt="Cuisine partagée">
      </div>
      <div class="facility-card-body">
        <h3>Cuisine Partagée</h3>
        <p>Entièrement équipée : plaque de cuisson, micro-ondes, bouilloire, grille-pain, cafetière, vaisselle et couverts complets, verres, casseroles et poêles. Tout le nécessaire pour un séjour détendu en autonomie.</p>
      </div>
    </div>

    <div class="facility-card">
      <div class="facility-card-img-wide">
        <img src="{img}kitchen-2.jpg" alt="Cuisine partagée — seconde vue">
      </div>
      <div class="facility-card-body">
        <h3>Cuisine Partagée</h3>
        <p>Une autre vue de la cuisine partagée, montrant le plan de travail, les rangements et les équipements de cuisson à disposition de tous les hôtes des chambres de la maison principale.</p>
      </div>
    </div>

  </div>

  <h2 style="margin-bottom:16px;">Chambres Utilisant ces Équipements</h2>
  <p style="color:var(--stone);font-size:0.9rem;margin-bottom:20px;">Les chambres suivantes partagent les salles de bain et la cuisine présentées ci-dessus :</p>
  <div class="room-links">
    <a href="{double}">← Chambre Double</a>
    <a href="{twin1}">← Chambre Double/Lits Jumeaux 1</a>
    <a href="{twin2}">← Chambre Double/Lits Jumeaux 2</a>
  </div>

</div>
""".replace("{img}", _FAC_IMG),
    },
    "nl": {
        "title": "Gedeelde Badkamers &amp; Keuken — Tamariu Chalet",
        "desc": "Gedeelde badkamers en keuken in Tamariu Chalet, Tamariu, Costa Brava — goed uitgerust en fris onderhouden voor alle kamergasten.",
        "content": """
<div class="page-hero">
  <div class="page-hero-content">
    <p class="breadcrumb">Verblijf → Gedeelde Voorzieningen</p>
    <h1>Gedeelde Badkamers &amp; Keuken</h1>
  </div>
</div>

<div class="content-page">

  <p style="font-size:1.05rem;color:var(--stone);margin-bottom:24px;max-width:700px;">
    Gasten van de Tweepersoonskamer, Twee-/Tweepersoonskamer 1 en Twee-/Tweepersoonskamer 2 delen
    twee goed uitgeruste badkamers en een volledig ingerichte gemeenschappelijke keuken. Alle
    voorzieningen worden op een hoog niveau van properheid gehouden en zijn ruim bemeten voor het
    aantal kamers dat ze bedienen.
  </p>

  <div class="facilities-note">
    Elke badkamer bedient maximaal twee kamers. De gedeelde keuken is volledig uitgerust met alles
    wat u nodig hebt om zelf te koken — van een volwaardige kookplaat tot koffiezetapparaat,
    broodrooster en al het serviesgoed.
  </div>

  <h2 style="margin-bottom:24px;">De Badkamers</h2>
  <div class="facilities-grid">

    <div class="facility-card">
      <div class="facility-card-img">
        <img src="{img}bathroom-1.jpg" alt="Badkamer 1">
      </div>
      <div class="facility-card-body">
        <h3>Badkamer 1</h3>
        <p>Een schone, goed ingerichte badkamer met inloopdouche, wastafel, toilet en alle benodigde voorzieningen. Handdoeken aanwezig.</p>
      </div>
    </div>

    <div class="facility-card">
      <div class="facility-card-img">
        <img src="{img}bathroom-2.jpg" alt="Badkamer 2">
      </div>
      <div class="facility-card-body">
        <h3>Badkamer 2</h3>
        <p>Een tweede lichte badkamer met douche, wastafel en toilet. Voor elke nieuwe groep gasten voorzien van vers linnengoed en aangevuld.</p>
      </div>
    </div>

  </div>

  <h2 style="margin-bottom:24px;">De Keuken</h2>
  <div class="facilities-grid-kitchen">

    <div class="facility-card">
      <div class="facility-card-img-wide">
        <img src="{img}kitchen-1.jpg" alt="Gedeelde keuken">
      </div>
      <div class="facility-card-body">
        <h3>Gedeelde Keuken</h3>
        <p>Volledig uitgerust met kookplaat, magnetron, waterkoker, broodrooster, koffiezetapparaat, compleet servies en bestek, glazen, pannen en koekenpannen. Alles voor een ontspannen verblijf waarin u zelf kookt.</p>
      </div>
    </div>

    <div class="facility-card">
      <div class="facility-card-img-wide">
        <img src="{img}kitchen-2.jpg" alt="Gedeelde keuken — tweede aanzicht">
      </div>
      <div class="facility-card-body">
        <h3>Gedeelde Keuken</h3>
        <p>Nog een aanzicht van de gedeelde keuken, met het volledige werkblad, de opbergruimte en de kookvoorzieningen die beschikbaar zijn voor alle gasten van de kamers in het hoofdhuis.</p>
      </div>
    </div>

  </div>

  <h2 style="margin-bottom:16px;">Kamers die deze Voorzieningen Gebruiken</h2>
  <p style="color:var(--stone);font-size:0.9rem;margin-bottom:20px;">De volgende kamers delen de hierboven getoonde badkamers en keuken:</p>
  <div class="room-links">
    <a href="{double}">← Tweepersoonskamer</a>
    <a href="{twin1}">← Twee-/Tweepersoonskamer 1</a>
    <a href="{twin2}">← Twee-/Tweepersoonskamer 2</a>
  </div>

</div>
""".replace("{img}", _FAC_IMG),
    },
}
