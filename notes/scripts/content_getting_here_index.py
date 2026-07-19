#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Authored translations for getting-here/index.html (map & directions)."""

from content_getting_here import FOOTER

MAP_IFRAME = """  <iframe
    src="https://maps.google.com/maps?q=Carrer+de+la+Punta+De+L%27Estela+7,+Tamariu,+17212,+Spain&t=&z=15&ie=UTF8&iwloc=&output=embed"
    class="map-embed"
    allowfullscreen=""
    loading="lazy"
    title="{title}">
  </iframe>"""

PAGES = {}

PAGES["getting-here/index.html"] = {
    "footer": FOOTER,
    "es": {
        "title": "Cómo Llegar — Mapa y Direcciones — Tamariu Chalet",
        "desc": "Cómo llegar a Tamariu Chalet, Costa Brava — en coche desde Barcelona y Girona, en tren y autobús, y aeropuertos más cercanos.",
        "content": """
<div class="page-hero">
  <div class="page-hero-content">
    <p class="breadcrumb">Cómo Llegar → Mapa y Direcciones</p>
    <h1>Cómo Llegar a Tamariu Chalet</h1>
  </div>
</div>

<div class="content-page">

  <h2>Dónde Estamos</h2>
  <p style="color:var(--stone);margin-bottom:16px;">Estamos en el pueblo de Tamariu, dentro del municipio de Palafrugell, en la Costa Brava, Catalunya, España.</p>

""" + MAP_IFRAME.format(title="Mapa de ubicación de Tamariu Chalet") + """

  <a href="https://maps.app.goo.gl/mNMy1VPqRKun75PV8" target="_blank" rel="noopener" class="availability-btn" style="display:inline-flex;margin-bottom:40px;">
    📍 Abrir en Google Maps
  </a>

  <h2>En Coche</h2>
  <div class="transport-card">
    <h4>Desde Barcelona (aprox. 2 h)</h4>
    <p>Tome la autopista AP-7 en dirección norte hacia Girona. Salga por la salida 9 (Palamós / Palafrugell). Siga la C-31 hacia Palafrugell y después la GI-660 hasta Tamariu. El pueblo está señalizado desde Palafrugell.</p>
  </div>
  <div class="transport-card">
    <h4>Desde el Aeropuerto de Girona (aprox. 50 min)</h4>
    <p>Salga del aeropuerto y tome la C-65 en dirección sur hacia La Bisbal d'Empordà; después continúe por la C-31 hasta Palafrugell y la GI-660 hasta Tamariu. Hay alquiler de coches en el aeropuerto.</p>
  </div>
  <div class="transport-card">
    <h4>Desde el Aeropuerto de Barcelona (aprox. 2,5 h)</h4>
    <p>Tome la autopista AP-7 en dirección norte. Siga la misma ruta que desde el centro de Barcelona — unas 2,5 horas según el tráfico. Hay alquiler de coches en el aeropuerto.</p>
  </div>

  <h2>En Tren + Autobús</h2>
  <div class="transport-card">
    <h4>Tren hasta Girona o Flaçà</h4>
    <p>Los trenes de alta velocidad (AVE) van de Barcelona Sants a Girona en unos 40 minutos. Desde la estación de Girona, tome un autobús hasta Palafrugell (aprox. 1 hora) — <strong>Palafrugell es la población más cercana a Tamariu</strong>, a solo 6 km. Como alternativa, los trenes regionales paran en Flaçà, con un autobús directo a Palafrugell aunque menos frecuente.</p>
  </div>
  <div class="transport-card">
    <h4>Autobús a Palafrugell y de allí a Tamariu</h4>
    <p>Un servicio de autobús de temporada conecta Palafrugell con Tamariu durante los meses de verano. Puede consultar las rutas y horarios vigentes en el enlace de abajo. Para los últimos 6 km de Palafrugell a Tamariu, un taxi local es una opción rápida y cómoda — el trayecto dura unos 10 minutos.</p>
    <a href="https://compras.moventis.es/online/search" target="_blank" rel="noopener" class="btn-outline" style="display:inline-block;margin-top:12px;">🚌 Buscar Transporte en Autobús</a>
  </div>
  <div class="transport-card" style="border-left:3px solid var(--gold);background:var(--linen);">
    <h4>¿Necesita que le recojamos en Palafrugell?</h4>
    <p>Es posible que podamos organizar un traslado desde Palafrugell hasta la casa por un precio fijo de <strong>25 €</strong>. Solo tiene que mencionarlo al ponerse en contacto y haremos lo posible por ayudarle.</p>
    <a href="{contact}" class="btn-outline" style="display:inline-block;margin-top:12px;">Contáctenos para Organizarlo</a>
  </div>

  <h2>En Avión</h2>
  <ul>
    <li><strong>Aeropuerto de Girona–Costa Brava</strong> — 50 km (recomendado para vuelos europeos de corto radio)</li>
    <li><strong>Aeropuerto de Barcelona El Prat</strong> — 130 km (la mayoría de conexiones internacionales)</li>
    <li><strong>Aeropuerto de Reus</strong> — 130 km (base de Ryanair; algunas rutas europeas)</li>
  </ul>

  <div style="margin-top:30px;display:flex;gap:14px;flex-wrap:wrap;">
    <a href="https://compras.moventis.es/online/search" target="_blank" rel="noopener" class="btn-outline">🚌 Buscar Transporte en Autobús</a>
  </div>

</div>
""",
    },
    "ca": {
        "title": "Com Arribar — Mapa i Indicacions — Tamariu Chalet",
        "desc": "Com arribar a Tamariu Chalet, Costa Brava — amb cotxe des de Barcelona i Girona, amb tren i autobús, i aeroports més propers.",
        "content": """
<div class="page-hero">
  <div class="page-hero-content">
    <p class="breadcrumb">Com Arribar → Mapa i Indicacions</p>
    <h1>Com Arribar a Tamariu Chalet</h1>
  </div>
</div>

<div class="content-page">

  <h2>On Som</h2>
  <p style="color:var(--stone);margin-bottom:16px;">Som al poble de Tamariu, dins del municipi de Palafrugell, a la Costa Brava, Catalunya, Espanya.</p>

""" + MAP_IFRAME.format(title="Mapa d'ubicació de Tamariu Chalet") + """

  <a href="https://maps.app.goo.gl/mNMy1VPqRKun75PV8" target="_blank" rel="noopener" class="availability-btn" style="display:inline-flex;margin-bottom:40px;">
    📍 Obrir a Google Maps
  </a>

  <h2>Amb Cotxe</h2>
  <div class="transport-card">
    <h4>Des de Barcelona (aprox. 2 h)</h4>
    <p>Agafeu l'autopista AP-7 en direcció nord cap a Girona. Sortiu per la sortida 9 (Palamós / Palafrugell). Seguiu la C-31 cap a Palafrugell i després la GI-660 fins a Tamariu. El poble està senyalitzat des de Palafrugell.</p>
  </div>
  <div class="transport-card">
    <h4>Des de l'Aeroport de Girona (aprox. 50 min)</h4>
    <p>Sortiu de l'aeroport i agafeu la C-65 en direcció sud cap a La Bisbal d'Empordà; després continueu per la C-31 fins a Palafrugell i la GI-660 fins a Tamariu. Hi ha lloguer de cotxes a l'aeroport.</p>
  </div>
  <div class="transport-card">
    <h4>Des de l'Aeroport de Barcelona (aprox. 2,5 h)</h4>
    <p>Agafeu l'autopista AP-7 en direcció nord. Seguiu la mateixa ruta que des del centre de Barcelona — unes 2,5 hores segons el trànsit. Hi ha lloguer de cotxes a l'aeroport.</p>
  </div>

  <h2>Amb Tren + Autobús</h2>
  <div class="transport-card">
    <h4>Tren fins a Girona o Flaçà</h4>
    <p>Els trens d'alta velocitat (AVE) van de Barcelona Sants a Girona en uns 40 minuts. Des de l'estació de Girona, agafeu un autobús fins a Palafrugell (aprox. 1 hora) — <strong>Palafrugell és la població més propera a Tamariu</strong>, a només 6 km. Alternativament, els trens regionals paren a Flaçà, amb un autobús directe a Palafrugell tot i que menys freqüent.</p>
  </div>
  <div class="transport-card">
    <h4>Autobús a Palafrugell i d'allà a Tamariu</h4>
    <p>Un servei d'autobús de temporada connecta Palafrugell amb Tamariu durant els mesos d'estiu. Podeu consultar les rutes i els horaris vigents a l'enllaç de sota. Per als darrers 6 km de Palafrugell a Tamariu, un taxi local és una opció ràpida i còmoda — el trajecte dura uns 10 minuts.</p>
    <a href="https://compras.moventis.es/online/search" target="_blank" rel="noopener" class="btn-outline" style="display:inline-block;margin-top:12px;">🚌 Cercar Transport en Autobús</a>
  </div>
  <div class="transport-card" style="border-left:3px solid var(--gold);background:var(--linen);">
    <h4>Necessiteu que us recollim a Palafrugell?</h4>
    <p>És possible que puguem organitzar un trasllat des de Palafrugell fins a la casa per un preu fix de <strong>25 €</strong>. Només cal que ho mencioneu quan us poseu en contacte i farem el possible per ajudar-vos.</p>
    <a href="{contact}" class="btn-outline" style="display:inline-block;margin-top:12px;">Contacteu-nos per Organitzar-ho</a>
  </div>

  <h2>Amb Avió</h2>
  <ul>
    <li><strong>Aeroport de Girona–Costa Brava</strong> — 50 km (recomanat per a vols europeus de curt radi)</li>
    <li><strong>Aeroport de Barcelona El Prat</strong> — 130 km (la majoria de connexions internacionals)</li>
    <li><strong>Aeroport de Reus</strong> — 130 km (base de Ryanair; algunes rutes europees)</li>
  </ul>

  <div style="margin-top:30px;display:flex;gap:14px;flex-wrap:wrap;">
    <a href="https://compras.moventis.es/online/search" target="_blank" rel="noopener" class="btn-outline">🚌 Cercar Transport en Autobús</a>
  </div>

</div>
""",
    },
    "fr": {
        "title": "Comment Venir — Carte &amp; Itinéraire — Tamariu Chalet",
        "desc": "Comment rejoindre le Tamariu Chalet, Costa Brava — en voiture depuis Barcelone et Gérone, en train et en bus, et aéroports les plus proches.",
        "content": """
<div class="page-hero">
  <div class="page-hero-content">
    <p class="breadcrumb">Comment Venir → Carte &amp; Itinéraire</p>
    <h1>Rejoindre le Tamariu Chalet</h1>
  </div>
</div>

<div class="content-page">

  <h2>Où Nous Trouver</h2>
  <p style="color:var(--stone);margin-bottom:16px;">Nous sommes situés dans le village de Tamariu, sur la commune de Palafrugell, sur la côte de la Costa Brava, en Catalogne, Espagne.</p>

""" + MAP_IFRAME.format(title="Carte de localisation du Tamariu Chalet") + """

  <a href="https://maps.app.goo.gl/mNMy1VPqRKun75PV8" target="_blank" rel="noopener" class="availability-btn" style="display:inline-flex;margin-bottom:40px;">
    📍 Ouvrir dans Google Maps
  </a>

  <h2>En Voiture</h2>
  <div class="transport-card">
    <h4>Depuis Barcelone (environ 2 h)</h4>
    <p>Prenez l'autoroute AP-7 vers le nord en direction de Gérone. Sortez à la sortie 9 (Palamós / Palafrugell). Suivez la C-31 vers Palafrugell, puis la GI-660 jusqu'à Tamariu. Le village est signalisé depuis Palafrugell.</p>
  </div>
  <div class="transport-card">
    <h4>Depuis l'aéroport de Gérone (environ 50 min)</h4>
    <p>À la sortie de l'aéroport, prenez la C-65 vers le sud en direction de La Bisbal d'Empordà, puis continuez sur la C-31 jusqu'à Palafrugell et la GI-660 jusqu'à Tamariu. Location de voitures disponible à l'aéroport.</p>
  </div>
  <div class="transport-card">
    <h4>Depuis l'aéroport de Barcelone (environ 2 h 30)</h4>
    <p>Prenez l'autoroute AP-7 vers le nord. Suivez le même itinéraire que depuis le centre de Barcelone — environ 2 h 30 selon le trafic. Location de voitures disponible à l'aéroport.</p>
  </div>

  <h2>En Train + Bus</h2>
  <div class="transport-card">
    <h4>Train jusqu'à Gérone ou Flaçà</h4>
    <p>Les trains à grande vitesse (AVE) relient Barcelona Sants à Gérone en environ 40 minutes. Depuis la gare de Gérone, prenez un bus jusqu'à Palafrugell (environ 1 heure) — <strong>Palafrugell est la ville la plus proche de Tamariu</strong>, à seulement 6 km. Les trains régionaux s'arrêtent également à Flaçà, d'où part un bus direct pour Palafrugell, moins fréquent.</p>
  </div>
  <div class="transport-card">
    <h4>Bus jusqu'à Palafrugell, puis vers Tamariu</h4>
    <p>Un service de bus saisonnier relie Palafrugell à Tamariu pendant les mois d'été. Vous pouvez consulter les itinéraires et horaires en vigueur via le lien ci-dessous. Pour les 6 derniers kilomètres entre Palafrugell et Tamariu, le taxi local est une solution rapide et pratique — le trajet dure une dizaine de minutes.</p>
    <a href="https://compras.moventis.es/online/search" target="_blank" rel="noopener" class="btn-outline" style="display:inline-block;margin-top:12px;">🚌 Rechercher un Bus</a>
  </div>
  <div class="transport-card" style="border-left:3px solid var(--gold);background:var(--linen);">
    <h4>Besoin d'être récupéré à Palafrugell ?</h4>
    <p>Nous pouvons éventuellement organiser un transfert de Palafrugell jusqu'à la maison pour un tarif fixe de <strong>25 €</strong>. Mentionnez-le simplement lors de votre prise de contact et nous ferons de notre mieux.</p>
    <a href="{contact}" class="btn-outline" style="display:inline-block;margin-top:12px;">Nous Contacter pour l'Organiser</a>
  </div>

  <h2>En Avion</h2>
  <ul>
    <li><strong>Aéroport de Gérone–Costa Brava</strong> — 50 km (recommandé pour les vols européens court-courriers)</li>
    <li><strong>Aéroport de Barcelone El Prat</strong> — 130 km (la plupart des correspondances internationales)</li>
    <li><strong>Aéroport de Reus</strong> — 130 km (base Ryanair ; quelques lignes européennes)</li>
  </ul>

  <div style="margin-top:30px;display:flex;gap:14px;flex-wrap:wrap;">
    <a href="https://compras.moventis.es/online/search" target="_blank" rel="noopener" class="btn-outline">🚌 Rechercher un Bus</a>
  </div>

</div>
""",
    },
    "nl": {
        "title": "Hoe Te Bereiken — Kaart &amp; Routebeschrijving — Tamariu Chalet",
        "desc": "Zo bereikt u Tamariu Chalet, Costa Brava — met de auto vanuit Barcelona en Girona, met trein en bus, en de dichtstbijzijnde luchthavens.",
        "content": """
<div class="page-hero">
  <div class="page-hero-content">
    <p class="breadcrumb">Hoe Te Bereiken → Kaart &amp; Routebeschrijving</p>
    <h1>Tamariu Chalet Bereiken</h1>
  </div>
</div>

<div class="content-page">

  <h2>Waar U Ons Vindt</h2>
  <p style="color:var(--stone);margin-bottom:16px;">Wij liggen in het dorp Tamariu, in de gemeente Palafrugell, aan de kust van de Costa Brava in Catalonië, Spanje.</p>

""" + MAP_IFRAME.format(title="Locatiekaart van Tamariu Chalet") + """

  <a href="https://maps.app.goo.gl/mNMy1VPqRKun75PV8" target="_blank" rel="noopener" class="availability-btn" style="display:inline-flex;margin-bottom:40px;">
    📍 Openen in Google Maps
  </a>

  <h2>Met de Auto</h2>
  <div class="transport-card">
    <h4>Vanuit Barcelona (ongeveer 2 uur)</h4>
    <p>Neem de snelweg AP-7 noordwaarts richting Girona. Neem afrit 9 (Palamós / Palafrugell). Volg de C-31 richting Palafrugell en daarna de GI-660 naar Tamariu. Het dorp is vanaf Palafrugell bewegwijzerd.</p>
  </div>
  <div class="transport-card">
    <h4>Vanaf luchthaven Girona (ongeveer 50 min)</h4>
    <p>Verlaat de luchthaven en neem de C-65 zuidwaarts richting La Bisbal d'Empordà, vervolg dan over de C-31 naar Palafrugell en de GI-660 naar Tamariu. Op de luchthaven is autoverhuur beschikbaar.</p>
  </div>
  <div class="transport-card">
    <h4>Vanaf luchthaven Barcelona (ongeveer 2,5 uur)</h4>
    <p>Neem de snelweg AP-7 noordwaarts. Volg dezelfde route als vanuit het centrum van Barcelona — ongeveer 2,5 uur, afhankelijk van het verkeer. Op de luchthaven is autoverhuur beschikbaar.</p>
  </div>

  <h2>Met Trein + Bus</h2>
  <div class="transport-card">
    <h4>Trein naar Girona of Flaçà</h4>
    <p>Hogesnelheidstreinen (AVE) rijden van Barcelona Sants naar Girona in ongeveer 40 minuten. Neem vanaf station Girona een bus naar Palafrugell (ongeveer 1 uur) — <strong>Palafrugell is de dichtstbijzijnde plaats bij Tamariu</strong>, op slechts 6 km. Regionale treinen stoppen ook in Flaçà, met een directe maar minder frequente bus naar Palafrugell.</p>
  </div>
  <div class="transport-card">
    <h4>Bus naar Palafrugell en verder naar Tamariu</h4>
    <p>Een seizoensgebonden busdienst verbindt Palafrugell in de zomermaanden met Tamariu. Actuele routes en dienstregelingen vindt u via onderstaande link. Voor de laatste 6 km van Palafrugell naar Tamariu is een lokale taxi snel en eenvoudig — de rit duurt ongeveer 10 minuten.</p>
    <a href="https://compras.moventis.es/online/search" target="_blank" rel="noopener" class="btn-outline" style="display:inline-block;margin-top:12px;">🚌 Busvervoer Zoeken</a>
  </div>
  <div class="transport-card" style="border-left:3px solid var(--gold);background:var(--linen);">
    <h4>Wilt u opgehaald worden in Palafrugell?</h4>
    <p>Wij kunnen mogelijk een transfer van Palafrugell naar het huis regelen voor een vast bedrag van <strong>€25</strong>. Vermeld het gewoon wanneer u contact opneemt, dan doen we ons best om te helpen.</p>
    <a href="{contact}" class="btn-outline" style="display:inline-block;margin-top:12px;">Neem Contact Op om Dit te Regelen</a>
  </div>

  <h2>Met het Vliegtuig</h2>
  <ul>
    <li><strong>Luchthaven Girona–Costa Brava</strong> — 50 km (aanbevolen voor Europese korteafstandsvluchten)</li>
    <li><strong>Luchthaven Barcelona El Prat</strong> — 130 km (de meeste internationale verbindingen)</li>
    <li><strong>Luchthaven Reus</strong> — 130 km (Ryanair-basis; enkele Europese routes)</li>
  </ul>

  <div style="margin-top:30px;display:flex;gap:14px;flex-wrap:wrap;">
    <a href="https://compras.moventis.es/online/search" target="_blank" rel="noopener" class="btn-outline">🚌 Busvervoer Zoeken</a>
  </div>

</div>
""",
    },
}
