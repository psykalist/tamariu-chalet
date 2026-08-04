#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
String table for getting-here/bus-timetables.html (tabbed timetable page).

Strings-mode page: the English markup is the single source and only the words
differ per language (see strings_mode.py / build_translations.py). German is
supplied inline here too, so merge_german leaves this page untouched.

Proper nouns (place, cove, street and operator names — Palafrugell, Llafranc,
Calella, Aiguablava, Sa Tuna, Sa Riera, Cap Roig, Moventis, Sarfa, Julivia,
Estació, Pl. d'Europa, camí de ronda...), clock times, dates' numerals, prices
and arrows are deliberately left unchanged.
"""


def T(es, ca, fr, nl, de):
    return {"es": es, "ca": ca, "fr": fr, "nl": nl, "de": de}


# The interactive route-map on this page is the same widget as on
# things-to-do/tamariu-by-foot.html and uses the identical set of JS strings
# (Leaflet popups, tab descriptions, stop labels). Reuse that translation table
# rather than duplicating it.
from content_tamariu_by_foot import PAGES as _FOOT_PAGES  # noqa: E402

_MAP_SCRIPT_STRINGS = _FOOT_PAGES["things-to-do/tamariu-by-foot.html"]["script_only"]


PAGES = {
    "getting-here/bus-timetables.html": {
        "mode": "strings",
        "meta": {
            "es": {"title": "Horarios de Autobús a y desde Tamariu — Tamariu Chalet",
                   "desc": "Horarios de autobús verano 2026 para Tamariu, Costa Brava — el Bus 60 y el bus turístico Julivia hacia y desde Tamariu, más el Bus 30 y el bus de playas de Begur. Horas de llegada a Tamariu destacadas."},
            "ca": {"title": "Horaris d'Autobús cap a i des de Tamariu — Tamariu Chalet",
                   "desc": "Horaris d'autobús estiu 2026 per a Tamariu, Costa Brava — el Bus 60 i el bus turístic Julivia cap a i des de Tamariu, més el Bus 30 i el bus de platges de Begur. Hores d'arribada a Tamariu destacades."},
            "fr": {"title": "Horaires de Bus vers et depuis Tamariu — Tamariu Chalet",
                   "desc": "Horaires de bus été 2026 pour Tamariu, Costa Brava — le Bus 60 et le bus touristique Julivia vers et depuis Tamariu, plus le Bus 30 et la navette des plages de Begur. Heures d'arrivée à Tamariu en surbrillance."},
            "nl": {"title": "Busdienstregelingen van en naar Tamariu — Tamariu Chalet",
                   "desc": "Busdienstregelingen zomer 2026 voor Tamariu, Costa Brava — Bus 60 en de toeristenbus Julivia van en naar Tamariu, plus Bus 30 en de strandbus van Begur. Aankomsttijden in Tamariu gemarkeerd."},
            "de": {"title": "Busfahrpläne von und nach Tamariu — Tamariu Chalet",
                   "desc": "Busfahrpläne Sommer 2026 für Tamariu, Costa Brava — Bus 60 und der Touristenbus Julivia von und nach Tamariu, dazu Bus 30 und der Strandbus von Begur. Ankunftszeiten in Tamariu hervorgehoben."},
        },
        "strings": {
            "Getting Here → Bus Timetables": T(
                "Cómo Llegar → Horarios de Autobús", "Com Arribar → Horaris d'Autobús",
                "Venir → Horaires de Bus", "Bereikbaarheid → Busdienstregelingen",
                "Anreise → Busfahrpläne"),
            "Bus Timetables to &amp; from Tamariu": T(
                "Horarios de Autobús a y desde Tamariu", "Horaris d'Autobús cap a i des de Tamariu",
                "Horaires de Bus vers et depuis Tamariu", "Busdienstregelingen van en naar Tamariu",
                "Busfahrpläne von und nach Tamariu"),
            "Summer 2026 timetables for the four bus services around Tamariu, reproduced from the operators so you can plan without hunting for a PDF.": T(
                "Horarios de verano 2026 de los cuatro servicios de autobús de la zona de Tamariu, reproducidos de los operadores para que pueda planificar sin buscar un PDF.",
                "Horaris d'estiu 2026 dels quatre serveis d'autobús de la zona de Tamariu, reproduïts dels operadors perquè pugueu planificar sense buscar cap PDF.",
                "Horaires été 2026 des quatre lignes de bus autour de Tamariu, reproduits d'après les opérateurs pour planifier sans chercher de PDF.",
                "Zomerdienstregelingen 2026 van de vier buslijnen rond Tamariu, overgenomen van de vervoerders zodat u kunt plannen zonder naar een PDF te zoeken.",
                "Sommerfahrpläne 2026 der vier Buslinien rund um Tamariu, von den Betreibern übernommen, damit Sie ohne PDF-Suche planen können."),
            "The times the bus is actually in Tamariu are highlighted in gold.": T(
                "Las horas en que el autobús está realmente en Tamariu se destacan en dorado.",
                "Les hores en què l'autobús és realment a Tamariu es destaquen en daurat.",
                "Les heures où le bus est effectivement à Tamariu sont surlignées en doré.",
                "De tijden waarop de bus daadwerkelijk in Tamariu is, zijn goudkleurig gemarkeerd.",
                "Die Zeiten, zu denen der Bus tatsächlich in Tamariu ist, sind golden hervorgehoben."),
            "Operators do revise these mid-season, so the official source is linked under every table.": T(
                "Los operadores los revisan a mitad de temporada, por lo que bajo cada tabla se enlaza la fuente oficial.",
                "Els operadors els revisen a mitja temporada, per això sota cada taula s'enllaça la font oficial.",
                "Les opérateurs les révisent en cours de saison ; la source officielle est donc indiquée sous chaque tableau.",
                "Vervoerders passen deze halverwege het seizoen aan, dus onder elke tabel staat de officiële bron.",
                "Die Betreiber ändern sie mitten in der Saison, daher ist unter jeder Tabelle die offizielle Quelle verlinkt."),
            "✓ Stops in Tamariu": T(
                "✓ Para en Tamariu", "✓ Para a Tamariu", "✓ S'arrête à Tamariu",
                "✓ Stopt in Tamariu", "✓ Hält in Tamariu"),
            "— Palafrugell ⇄ Llafranc ⇄ Tamariu, summer only.": T(
                "— Palafrugell ⇄ Llafranc ⇄ Tamariu, solo en verano.",
                "— Palafrugell ⇄ Llafranc ⇄ Tamariu, només a l'estiu.",
                "— Palafrugell ⇄ Llafranc ⇄ Tamariu, en été uniquement.",
                "— Palafrugell ⇄ Llafranc ⇄ Tamariu, alleen in de zomer.",
                "— Palafrugell ⇄ Llafranc ⇄ Tamariu, nur im Sommer."),
            "— the hop-on hop-off tourist loop, summer only.": T(
                "— el circuito turístico de subir y bajar, solo en verano.",
                "— el circuit turístic de pujar i baixar, només a l'estiu.",
                "— la boucle touristique à montée et descente libres, en été uniquement.",
                "— de hop-on hop-off toeristenlus, alleen in de zomer.",
                "— die Hop-on-Hop-off-Touristenschleife, nur im Sommer."),
            "✗ Does not reach Tamariu": T(
                "✗ No llega a Tamariu", "✗ No arriba a Tamariu", "✗ Ne dessert pas Tamariu",
                "✗ Bereikt Tamariu niet", "✗ Erreicht Tamariu nicht"),
            "— loops Palafrugell ⇄ Calella ⇄ Llafranc only.": T(
                "— solo circula entre Palafrugell ⇄ Calella ⇄ Llafranc.",
                "— només fa el circuit Palafrugell ⇄ Calella ⇄ Llafranc.",
                "— fait seulement la boucle Palafrugell ⇄ Calella ⇄ Llafranc.",
                "— rijdt alleen de lus Palafrugell ⇄ Calella ⇄ Llafranc.",
                "— fährt nur die Schleife Palafrugell ⇄ Calella ⇄ Llafranc."),
            "— serves Begur's own coves (Sa Riera, Aiguablava, Sa Tuna).": T(
                "— sirve las calas propias de Begur (Sa Riera, Aiguablava, Sa Tuna).",
                "— serveix les cales pròpies de Begur (Sa Riera, Aiguablava, Sa Tuna).",
                "— dessert les criques de Begur (Sa Riera, Aiguablava, Sa Tuna).",
                "— bedient de eigen baaien van Begur (Sa Riera, Aiguablava, Sa Tuna).",
                "— bedient die Buchten von Begur (Sa Riera, Aiguablava, Sa Tuna)."),
            "Gold rows are the Tamariu times — where the bus arrives at, and departs from, the Tamariu stop.": T(
                "Las filas doradas son las horas de Tamariu — cuando el autobús llega y sale de la parada de Tamariu.",
                "Les files daurades són les hores de Tamariu — quan l'autobús arriba i surt de la parada de Tamariu.",
                "Les lignes dorées correspondent aux heures de Tamariu — l'arrivée et le départ à l'arrêt de Tamariu.",
                "De goudkleurige rijen zijn de Tamariu-tijden — waar de bus aankomt bij en vertrekt van de halte van Tamariu.",
                "Die goldenen Zeilen sind die Tamariu-Zeiten — wann der Bus an der Haltestelle Tamariu ankommt und abfährt."),
            "Begur beach bus": T(
                "Bus de playas de Begur", "Bus de platges de Begur", "Navette des plages de Begur",
                "Strandbus van Begur", "Strandbus von Begur"),
            "Begur beach bus →": T(
                "Bus de playas de Begur →", "Bus de platges de Begur →", "Navette des plages de Begur →",
                "Strandbus van Begur →", "Strandbus von Begur →"),
            "Girona": T("Girona", "Girona", "Gérone", "Girona", "Girona"),
            "07:30, 11:30 and 17:00": T(
                "07:30, 11:30 y 17:00", "07:30, 11:30 i 17:00", "07:30, 11:30 et 17:00",
                "07:30, 11:30 en 17:00", "07:30, 11:30 und 17:00"),
            "Onward to Girona →": T(
                "Continuar a Girona →", "Continuar a Girona →", "Continuer vers Gérone →",
                "Verder naar Girona →", "Weiter nach Girona →"),
            "Where the buses actually stop": T(
                "Dónde paran realmente los autobuses", "On paren realment els autobusos",
                "Où les bus s'arrêtent réellement", "Waar de bussen echt stoppen",
                "Wo die Busse tatsächlich halten"),
            "Four services, four different networks. Use the tabs to focus on one route at a time, or see them all together. Routes follow the roads; for the operators' own definitive maps and exact stops, use the official links under each table.": T(
                "Cuatro servicios, cuatro redes distintas. Use las pestañas para centrarse en una ruta cada vez, o véalas todas juntas. Las rutas siguen las carreteras; para los mapas definitivos de los operadores y las paradas exactas, use los enlaces oficiales bajo cada tabla.",
                "Quatre serveis, quatre xarxes diferents. Feu servir les pestanyes per centrar-vos en una ruta cada cop, o vegeu-les totes juntes. Les rutes segueixen les carreteres; per als mapes definitius dels operadors i les parades exactes, feu servir els enllaços oficials sota cada taula.",
                "Quatre lignes, quatre réseaux différents. Utilisez les onglets pour vous concentrer sur un itinéraire à la fois, ou voyez-les tous ensemble. Les tracés suivent les routes ; pour les cartes définitives des opérateurs et les arrêts exacts, utilisez les liens officiels sous chaque tableau.",
                "Vier lijnen, vier verschillende netwerken. Gebruik de tabbladen om op één route tegelijk te focussen, of bekijk ze allemaal samen. De routes volgen de wegen; gebruik voor de definitieve kaarten van de vervoerders en de exacte haltes de officiële links onder elke tabel.",
                "Vier Linien, vier verschiedene Netze. Nutzen Sie die Reiter, um sich auf eine Route zu konzentrieren, oder sehen Sie alle zusammen. Die Verläufe folgen den Straßen; für die verbindlichen Karten der Betreiber und die genauen Haltestellen nutzen Sie die offiziellen Links unter jeder Tabelle."),
            "Overview": T("Vista general", "Vista general", "Vue d'ensemble",
                          "Overzicht", "Übersicht"),
            "All the networks together. The southern cluster (Julivia, Bus 30′ and Bus 60′) is largely walkable; the Begur coves in the north are separate spokes with no cove-to-cove link.": T(
                "Todas las redes juntas. El grupo sur (Julivia, Bus 30′ y Bus 60′) es en gran parte accesible a pie; las calas de Begur, al norte, son ramales separados sin enlace directo entre calas.",
                "Totes les xarxes juntes. El grup sud (Julivia, Bus 30′ i Bus 60′) és en gran part accessible a peu; les cales de Begur, al nord, són ramals separats sense enllaç directe entre cales.",
                "Tous les réseaux réunis. Le groupe sud (Julivia, Bus 30′ et Bus 60′) est en grande partie accessible à pied ; les criques de Begur, au nord, sont des antennes séparées sans liaison de crique à crique.",
                "Alle netwerken samen. Het zuidelijke cluster (Julivia, Bus 30′ en Bus 60′) is grotendeels te belopen; de baaien van Begur in het noorden zijn losse takken zonder verbinding tussen de baaien onderling.",
                "Alle Netze zusammen. Das südliche Cluster (Julivia, Bus 30′ und Bus 60′) ist weitgehend zu Fuß erschließbar; die Buchten von Begur im Norden sind einzelne Stichlinien ohne Verbindung von Bucht zu Bucht."),
            "Routes are drawn along the roads from the stop list; for the operators' definitive maps and exact kerbside stops, use the official links under each table below.": T(
                "Las rutas se trazan por las carreteras a partir de la lista de paradas; para los mapas definitivos de los operadores y las paradas exactas en calzada, use los enlaces oficiales bajo cada tabla.",
                "Les rutes es tracen per les carreteres a partir de la llista de parades; per als mapes definitius dels operadors i les parades exactes a la vorera, feu servir els enllaços oficials sota cada taula.",
                "Les tracés suivent les routes d'après la liste des arrêts ; pour les cartes définitives des opérateurs et les arrêts exacts en bordure, utilisez les liens officiels sous chaque tableau.",
                "De routes zijn langs de wegen getekend op basis van de haltelijst; gebruik voor de definitieve kaarten van de vervoerders en de exacte haltes langs de weg de officiële links onder elke tabel.",
                "Die Verläufe folgen den Straßen anhand der Haltestellenliste; für die verbindlichen Karten der Betreiber und die genauen Haltestellen am Straßenrand nutzen Sie die offiziellen Links unter jeder Tabelle."),
            "Bus 60′ — Palafrugell ⇄ Llafranc ⇄ Tamariu": T(
                "Bus 60′ — Palafrugell ⇄ Llafranc ⇄ Tamariu", "Bus 60′ — Palafrugell ⇄ Llafranc ⇄ Tamariu",
                "Bus 60′ — Palafrugell ⇄ Llafranc ⇄ Tamariu", "Bus 60′ — Palafrugell ⇄ Llafranc ⇄ Tamariu",
                "Bus 60′ — Palafrugell ⇄ Llafranc ⇄ Tamariu"),
            "1 July – 31 August 2026 · €2 single (free under 4) · T-10 €6.40 via ATM Girona · operated by Moventis": T(
                "1 julio – 31 agosto 2026 · €2 sencillo (gratis menores de 4) · T-10 €6,40 vía ATM Girona · operado por Moventis",
                "1 juliol – 31 agost 2026 · €2 senzill (gratis menors de 4) · T-10 €6,40 via ATM Girona · operat per Moventis",
                "1er juillet – 31 août 2026 · €2 aller simple (gratuit moins de 4 ans) · T-10 €6,40 via ATM Girona · exploité par Moventis",
                "1 juli – 31 augustus 2026 · €2 enkeltje (gratis onder de 4) · T-10 €6,40 via ATM Girona · uitgevoerd door Moventis",
                "1. Juli – 31. August 2026 · €2 Einzelfahrt (unter 4 gratis) · T-10 €6,40 über ATM Girona · betrieben von Moventis"),
            "The most useful service for guests: a direct link between Tamariu, Llafranc and Palafrugell town.": T(
                "El servicio más útil para los huéspedes: un enlace directo entre Tamariu, Llafranc y el pueblo de Palafrugell.",
                "El servei més útil per als hostes: un enllaç directe entre Tamariu, Llafranc i el poble de Palafrugell.",
                "La ligne la plus utile pour les hôtes : une liaison directe entre Tamariu, Llafranc et la ville de Palafrugell.",
                "De handigste lijn voor gasten: een directe verbinding tussen Tamariu, Llafranc en het stadje Palafrugell.",
                "Die nützlichste Linie für Gäste: eine Direktverbindung zwischen Tamariu, Llafranc und der Stadt Palafrugell."),
            "The bus reaches Tamariu exactly 30 minutes after leaving Palafrugell station, then turns straight round": T(
                "El autobús llega a Tamariu exactamente 30 minutos después de salir de la estación de Palafrugell y da la vuelta enseguida",
                "L'autobús arriba a Tamariu exactament 30 minuts després de sortir de l'estació de Palafrugell i tot seguit gira",
                "Le bus arrive à Tamariu exactement 30 minutes après avoir quitté la gare de Palafrugell, puis repart aussitôt",
                "De bus komt precies 30 minuten na vertrek van het station van Palafrugell in Tamariu aan en keert meteen terug",
                "Der Bus erreicht Tamariu genau 30 Minuten nach Abfahrt vom Bahnhof Palafrugell und wendet sofort"),
            "— so each Tamariu time below is both when it arrives from Palafrugell and when you board it for the trip back.": T(
                "— así que cada hora de Tamariu de abajo es a la vez cuando llega desde Palafrugell y cuando lo toma para volver.",
                "— així que cada hora de Tamariu de sota és alhora quan arriba des de Palafrugell i quan el preneu per tornar.",
                "— chaque heure de Tamariu ci-dessous correspond donc à la fois à l'arrivée depuis Palafrugell et au départ pour le retour.",
                "— elke Tamariu-tijd hieronder is dus zowel de aankomst vanuit Palafrugell als het moment waarop u instapt voor de terugreis.",
                "— jede Tamariu-Zeit unten ist also zugleich die Ankunft aus Palafrugell und der Zeitpunkt, zu dem Sie für die Rückfahrt einsteigen."),
            "At the Tamariu stop": T(
                "En la parada de Tamariu", "A la parada de Tamariu", "À l'arrêt de Tamariu",
                "Bij de halte van Tamariu", "An der Haltestelle Tamariu"),
            "At Tamariu": T("En Tamariu", "A Tamariu", "À Tamariu", "In Tamariu", "In Tamariu"),
            "Heading to": T("Con destino a", "En direcció a", "En direction de",
                            "Richting", "In Richtung"),
            "Arrives": T("Llega", "Arriba", "Arrivée", "Aankomst", "Ankunft"),
            "— via Llafranc": T("— vía Llafranc", "— via Llafranc", "— via Llafranc",
                                "— via Llafranc", "— über Llafranc"),
            "last bus": T("último bus", "últim bus", "dernier bus", "laatste bus", "letzter Bus"),
            "Tamariu is the end of the line, so every Bus 60′ here is heading back to": T(
                "Tamariu es el final de la línea, así que cada Bus 60′ de aquí vuelve hacia",
                "Tamariu és el final de la línia, així que cada Bus 60′ d'aquí torna cap a",
                "Tamariu est le terminus, donc chaque Bus 60′ ici repart vers",
                "Tamariu is het eindpunt, dus elke Bus 60′ hier gaat terug naar",
                "Tamariu ist die Endstation, daher fährt jeder Bus 60′ hier zurück nach"),
            "via Llafranc, reaching the station 30 minutes later. Each bus reached Tamariu 30 minutes after leaving Palafrugell (departures 07:00–11:00 and 15:30–19:30); there is no service between 11:00 and 15:30.": T(
                "vía Llafranc, llegando a la estación 30 minutos después. Cada bus llegaba a Tamariu 30 minutos después de salir de Palafrugell (salidas 07:00–11:00 y 15:30–19:30); no hay servicio entre las 11:00 y las 15:30.",
                "via Llafranc, arribant a l'estació 30 minuts després. Cada bus arribava a Tamariu 30 minuts després de sortir de Palafrugell (sortides 07:00–11:00 i 15:30–19:30); no hi ha servei entre les 11:00 i les 15:30.",
                "via Llafranc, atteignant la gare 30 minutes plus tard. Chaque bus arrivait à Tamariu 30 minutes après avoir quitté Palafrugell (départs 07:00–11:00 et 15:30–19:30) ; il n'y a pas de service entre 11:00 et 15:30.",
                "via Llafranc, 30 minuten later bij het station. Elke bus kwam 30 minuten na vertrek uit Palafrugell in Tamariu aan (vertrek 07:00–11:00 en 15:30–19:30); tussen 11:00 en 15:30 rijdt er geen bus.",
                "über Llafranc und erreicht den Bahnhof 30 Minuten später. Jeder Bus erreichte Tamariu 30 Minuten nach Abfahrt aus Palafrugell (Abfahrten 07:00–11:00 und 15:30–19:30); zwischen 11:00 und 15:30 fährt kein Bus."),
            "Early July": T("Principios de julio", "Principis de juliol", "Début juillet",
                            "Begin juli", "Anfang Juli"),
            "(1–3, 6–10, 13–16) there are only three a day — at Tamariu": T(
                "(1–3, 6–10, 13–16) solo hay tres al día — en Tamariu",
                "(1–3, 6–10, 13–16) només n'hi ha tres al dia — a Tamariu",
                "(1–3, 6–10, 13–16) il n'y en a que trois par jour — à Tamariu",
                "(1–3, 6–10, 13–16) rijden er slechts drie per dag — in Tamariu",
                "(1.–3., 6.–10., 13.–16.) fahren nur drei pro Tag — in Tamariu"),
            ". Out of July and August the service does not run.": T(
                ". Fuera de julio y agosto el servicio no funciona.",
                ". Fora de juliol i agost el servei no funciona.",
                ". En dehors de juillet et août, la ligne ne circule pas.",
                ". Buiten juli en augustus rijdt de lijn niet.",
                ". Außerhalb von Juli und August verkehrt die Linie nicht."),
            "Full route:": T("Ruta completa:", "Ruta completa:", "Itinéraire complet :",
                             "Volledige route:", "Vollständige Route:"),
            "→ and back the same way.": T(
                "→ y de vuelta por el mismo camino.", "→ i tornada pel mateix camí.",
                "→ et retour par le même chemin.", "→ en dezelfde weg terug.",
                "→ und auf demselben Weg zurück."),
            "Official Bus 30′ &amp; 60′ timetable (PDF)": T(
                "Horario oficial Bus 30′ y 60′ (PDF)", "Horari oficial Bus 30′ i 60′ (PDF)",
                "Horaire officiel Bus 30′ &amp; 60′ (PDF)", "Officiële dienstregeling Bus 30′ &amp; 60′ (PDF)",
                "Offizieller Fahrplan Bus 30′ &amp; 60′ (PDF)"),
            "Visit Palafrugell": T("Visitar Palafrugell", "Visitar Palafrugell",
                                   "Visiter Palafrugell", "Bezoek Palafrugell", "Palafrugell besuchen"),
            "Julivia — hop-on hop-off tourist bus": T(
                "Julivia — bus turístico de subir y bajar", "Julivia — bus turístic de pujar i baixar",
                "Julivia — bus touristique à montée et descente libres", "Julivia — hop-on hop-off toeristenbus",
                "Julivia — Hop-on-Hop-off-Touristenbus"),
            "25 July – 20 September 2026 · €6.50 adult, €3 child 4–12 · all-day ticket": T(
                "25 julio – 20 septiembre 2026 · €6,50 adulto, €3 niño 4–12 · billete de todo el día",
                "25 juliol – 20 setembre 2026 · €6,50 adult, €3 nen 4–12 · bitllet de tot el dia",
                "25 juillet – 20 septembre 2026 · €6,50 adulte, €3 enfant 4–12 · billet journée",
                "25 juli – 20 september 2026 · €6,50 volwassene, €3 kind 4–12 · dagkaart",
                "25. Juli – 20. September 2026 · €6,50 Erwachsene, €3 Kind 4–12 · Tagesticket"),
            "A single all-day ticket, bought on board, valid for as many loops as you like. Best used as a shuttle between Tamariu, the Sant Sebastià lighthouse, Llafranc, Calella (Port Bo) and the Cap Roig gardens. Unlike Bus 60′, the Julivia is a one-way loop — so at Tamariu it runs in two directions.": T(
                "Un único billete de todo el día, comprado a bordo, válido para tantas vueltas como quiera. Se aprovecha mejor como lanzadera entre Tamariu, el faro de Sant Sebastià, Llafranc, Calella (Port Bo) y los jardines de Cap Roig. A diferencia del Bus 60′, la Julivia es un circuito de sentido único — así que en Tamariu pasa en dos direcciones.",
                "Un únic bitllet de tot el dia, comprat a bord, vàlid per a tantes voltes com vulgueu. S'aprofita millor com a llançadora entre Tamariu, el far de Sant Sebastià, Llafranc, Calella (Port Bo) i els jardins de Cap Roig. A diferència del Bus 60′, la Julivia és un circuit de sentit únic — així que a Tamariu passa en dues direccions.",
                "Un seul billet journée, acheté à bord, valable pour autant de boucles que vous voulez. À utiliser de préférence comme navette entre Tamariu, le phare de Sant Sebastià, Llafranc, Calella (Port Bo) et les jardins de Cap Roig. Contrairement au Bus 60′, la Julivia est une boucle à sens unique — à Tamariu, elle passe donc dans deux directions.",
                "Eén dagkaart, aan boord gekocht, geldig voor zoveel rondes als u wilt. Het best te gebruiken als pendel tussen Tamariu, de vuurtoren van Sant Sebastià, Llafranc, Calella (Port Bo) en de tuinen van Cap Roig. Anders dan Bus 60′ is de Julivia een eenrichtingslus — bij Tamariu rijdt hij dus in twee richtingen.",
                "Ein einziges Tagesticket, an Bord gekauft, gültig für beliebig viele Runden. Am besten als Pendelverbindung zwischen Tamariu, dem Leuchtturm Sant Sebastià, Llafranc, Calella (Port Bo) und den Gärten von Cap Roig. Anders als Bus 60′ ist die Julivia eine Einbahnschleife — in Tamariu fährt sie daher in zwei Richtungen."),
            "→ El Far, Llafranc, Calella &amp;": T(
                "→ El Far, Llafranc, Calella y", "→ El Far, Llafranc, Calella i",
                "→ El Far, Llafranc, Calella &amp;", "→ El Far, Llafranc, Calella &amp;",
                "→ El Far, Llafranc, Calella &amp;"),
            "outbound, along the beaches": T(
                "de ida, por las playas", "d'anada, per les platges", "à l'aller, le long des plages",
                "heenreis, langs de stranden", "hinwärts, entlang der Strände"),
            "(town) — then loops straight back out along the beaches": T(
                "(pueblo) — luego vuelve a salir enseguida por las playas",
                "(poble) — després torna a sortir de seguida per les platges",
                "(ville) — puis repart aussitôt le long des plages",
                "(dorp) — draait dan meteen weer terug langs de stranden",
                "(Ort) — dreht dann sofort wieder hinaus entlang der Strände"),
            "(town) — last loop before the midday break": T(
                "(pueblo) — última vuelta antes del descanso del mediodía",
                "(poble) — última volta abans del descans del migdia",
                "(ville) — dernière boucle avant la pause de midi",
                "(dorp) — laatste ronde vóór de middagpauze",
                "(Ort) — letzte Runde vor der Mittagspause"),
            "(town) — final loop of the day, ends in town": T(
                "(pueblo) — última vuelta del día, termina en el pueblo",
                "(poble) — última volta del dia, acaba al poble",
                "(ville) — dernière boucle de la journée, se termine en ville",
                "(dorp) — laatste ronde van de dag, eindigt in het dorp",
                "(Ort) — letzte Runde des Tages, endet im Ort"),
            "Because it is a hop-on hop-off ticket, you can ride out on one loop and come back on a later one. Full stop-by-stop times below.": T(
                "Como es un billete de subir y bajar, puede ir en una vuelta y volver en otra posterior. Horas parada por parada más abajo.",
                "Com que és un bitllet de pujar i baixar, podeu anar en una volta i tornar en una de posterior. Hores parada per parada més avall.",
                "Comme c'est un billet à montée et descente libres, vous pouvez partir sur une boucle et revenir sur une autre plus tard. Horaires arrêt par arrêt ci-dessous.",
                "Omdat het een hop-on hop-off kaartje is, kunt u op de ene ronde heen en op een latere terug. Tijden halte voor halte hieronder.",
                "Da es ein Hop-on-Hop-off-Ticket ist, können Sie auf einer Runde hin- und auf einer späteren zurückfahren. Zeiten Haltestelle für Haltestelle unten."),
            "Stop": T("Parada", "Parada", "Arrêt", "Halte", "Haltestelle"),
            "lighthouse": T("faro", "far", "phare", "vuurtoren", "Leuchtturm"),
            "gardens": T("jardines", "jardins", "jardins", "tuinen", "Gärten"),
            "return": T("vuelta", "tornada", "retour", "terug", "zurück"),
            "Mind the midday gap:": T(
                "Cuidado con el paréntesis del mediodía:", "Compte amb el parèntesi del migdia:",
                "Attention à la coupure de midi :", "Let op de middagonderbreking:",
                "Achtung, Mittagslücke:"),
            "leave Tamariu on the 12:46 and the next bus out is not until 16:16.": T(
                "salga de Tamariu en el de las 12:46 y el siguiente bus de salida no es hasta las 16:16.",
                "sortiu de Tamariu amb el de les 12:46 i el següent bus de sortida no és fins a les 16:16.",
                "partez de Tamariu à 12:46 et le prochain bus au départ n'est qu'à 16:16.",
                "vertrek uit Tamariu met die van 12:46 en de volgende bus terug is pas om 16:16.",
                "verlassen Sie Tamariu um 12:46, und der nächste Bus hinaus fährt erst um 16:16."),
            "Official Julivia 2026 timetable (PDF)": T(
                "Horario oficial Julivia 2026 (PDF)", "Horari oficial Julivia 2026 (PDF)",
                "Horaire officiel Julivia 2026 (PDF)", "Officiële dienstregeling Julivia 2026 (PDF)",
                "Offizieller Julivia-Fahrplan 2026 (PDF)"),
            "More about the Julivia bus": T(
                "Más sobre el bus Julivia", "Més sobre el bus Julivia", "En savoir plus sur le bus Julivia",
                "Meer over de Julivia-bus", "Mehr über den Julivia-Bus"),
            "Bus 30′ — Palafrugell ⇄ Calella ⇄ Llafranc": T(
                "Bus 30′ — Palafrugell ⇄ Calella ⇄ Llafranc", "Bus 30′ — Palafrugell ⇄ Calella ⇄ Llafranc",
                "Bus 30′ — Palafrugell ⇄ Calella ⇄ Llafranc", "Bus 30′ — Palafrugell ⇄ Calella ⇄ Llafranc",
                "Bus 30′ — Palafrugell ⇄ Calella ⇄ Llafranc"),
            "1 July – 31 August 2026 · €2 single · daily · operated by Moventis": T(
                "1 julio – 31 agosto 2026 · €2 sencillo · diario · operado por Moventis",
                "1 juliol – 31 agost 2026 · €2 senzill · diari · operat per Moventis",
                "1er juillet – 31 août 2026 · €2 aller simple · tous les jours · exploité par Moventis",
                "1 juli – 31 augustus 2026 · €2 enkeltje · dagelijks · uitgevoerd door Moventis",
                "1. Juli – 31. August 2026 · €2 Einzelfahrt · täglich · betrieben von Moventis"),
            "This service does not reach Tamariu": T(
                "Este servicio no llega a Tamariu", "Aquest servei no arriba a Tamariu",
                "Cette ligne ne dessert pas Tamariu", "Deze lijn bereikt Tamariu niet",
                "Diese Linie erreicht Tamariu nicht"),
            "— it loops between Palafrugell, Calella de Palafrugell and Llafranc. It is handy for combining a town morning with a beach afternoon at Calella or Llafranc. Departures leave Palafrugell (Pl. d'Europa)": T(
                "— circula entre Palafrugell, Calella de Palafrugell y Llafranc. Es práctico para combinar una mañana de pueblo con una tarde de playa en Calella o Llafranc. Las salidas parten de Palafrugell (Pl. d'Europa)",
                "— fa el circuit entre Palafrugell, Calella de Palafrugell i Llafranc. És pràctic per combinar un matí de poble amb una tarda de platja a Calella o Llafranc. Les sortides surten de Palafrugell (Pl. d'Europa)",
                "— il fait la boucle entre Palafrugell, Calella de Palafrugell et Llafranc. Pratique pour combiner une matinée en ville et un après-midi plage à Calella ou Llafranc. Les départs partent de Palafrugell (Pl. d'Europa)",
                "— hij rijdt de lus tussen Palafrugell, Calella de Palafrugell en Llafranc. Handig om een ochtend in de stad te combineren met een strandmiddag in Calella of Llafranc. De ritten vertrekken uit Palafrugell (Pl. d'Europa)",
                "— er fährt die Schleife zwischen Palafrugell, Calella de Palafrugell und Llafranc. Praktisch, um einen Vormittag in der Stadt mit einem Strandnachmittag in Calella oder Llafranc zu verbinden. Die Abfahrten starten in Palafrugell (Pl. d'Europa)"),
            "every 30 minutes from 07:30 to 21:30": T(
                "cada 30 minutos de 07:30 a 21:30", "cada 30 minuts de 07:30 a 21:30",
                "toutes les 30 minutes de 07:30 à 21:30", "elke 30 minuten van 07:30 tot 21:30",
                "alle 30 Minuten von 07:30 bis 21:30"),
            "; the table below shows how many minutes after that departure the bus reaches each stop.": T(
                "; la tabla de abajo muestra cuántos minutos después de esa salida llega el bus a cada parada.",
                "; la taula de sota mostra quants minuts després d'aquesta sortida arriba el bus a cada parada.",
                "; le tableau ci-dessous indique combien de minutes après ce départ le bus atteint chaque arrêt.",
                "; de tabel hieronder toont hoeveel minuten na dat vertrek de bus elke halte bereikt.",
                "; die Tabelle unten zeigt, wie viele Minuten nach dieser Abfahrt der Bus jede Haltestelle erreicht."),
            "Minutes after departure": T(
                "Minutos tras la salida", "Minuts després de la sortida", "Minutes après le départ",
                "Minuten na vertrek", "Minuten nach Abfahrt"),
            "First": T("Primero", "Primer", "Premier", "Eerste", "Erster"),
            "Last": T("Último", "Últim", "Dernier", "Laatste", "Letzter"),
            "departs": T("sale", "surt", "départ", "vertrek", "Abfahrt"),
            "C. Barris i Buixó (centre)": T(
                "C. Barris i Buixó (centro)", "C. Barris i Buixó (centre)", "C. Barris i Buixó (centre)",
                "C. Barris i Buixó (centrum)", "C. Barris i Buixó (Zentrum)"),
            "So a bus leaves Palafrugell at 07:30, 08:00, 08:30 … through to 21:30, each reaching Calella about 10 minutes later and Llafranc about 15 minutes later.": T(
                "Así, un bus sale de Palafrugell a las 07:30, 08:00, 08:30 … hasta las 21:30, y cada uno llega a Calella unos 10 minutos después y a Llafranc unos 15 minutos después.",
                "Així, un bus surt de Palafrugell a les 07:30, 08:00, 08:30 … fins a les 21:30, i cadascun arriba a Calella uns 10 minuts després i a Llafranc uns 15 minuts després.",
                "Ainsi un bus part de Palafrugell à 07:30, 08:00, 08:30 … jusqu'à 21:30, chacun atteignant Calella environ 10 minutes plus tard et Llafranc environ 15 minutes plus tard.",
                "Zo vertrekt er een bus uit Palafrugell om 07:30, 08:00, 08:30 … tot 21:30, die telkens ongeveer 10 minuten later in Calella en ongeveer 15 minuten later in Llafranc is.",
                "So fährt ein Bus in Palafrugell um 07:30, 08:00, 08:30 … bis 21:30 ab und erreicht Calella jeweils etwa 10 Minuten und Llafranc etwa 15 Minuten später."),
            "13 June – 13 September 2026 · €1.50 single, €3 day pass, €1 under-16s, under-6 free": T(
                "13 junio – 13 septiembre 2026 · €1,50 sencillo, €3 abono de día, €1 menores de 16, menores de 6 gratis",
                "13 juny – 13 setembre 2026 · €1,50 senzill, €3 abonament de dia, €1 menors de 16, menors de 6 gratis",
                "13 juin – 13 septembre 2026 · €1,50 aller simple, €3 pass journée, €1 moins de 16 ans, moins de 6 ans gratuit",
                "13 juni – 13 september 2026 · €1,50 enkeltje, €3 dagpas, €1 onder de 16, onder de 6 gratis",
                "13. Juni – 13. September 2026 · €1,50 Einzelfahrt, €3 Tagespass, €1 unter 16, unter 6 gratis"),
            "This bus is based in Begur, not Tamariu": T(
                "Este autobús tiene su base en Begur, no en Tamariu", "Aquest autobús té la base a Begur, no a Tamariu",
                "Ce bus part de Begur, pas de Tamariu", "Deze bus vertrekt vanuit Begur, niet Tamariu",
                "Dieser Bus hat seine Basis in Begur, nicht in Tamariu"),
            "— it shuttles from Plaça Forgas in Begur out to Begur's own coves. Reaching it means driving to Begur first (about 15 minutes from Tamariu). Every route starts and ends at Plaça Forgas, so there is no direct hop between coves.": T(
                "— hace de lanzadera desde la Plaça Forgas de Begur hasta las calas propias de Begur. Para tomarlo hay que ir primero en coche a Begur (unos 15 minutos desde Tamariu). Todas las rutas empiezan y terminan en la Plaça Forgas, así que no hay salto directo entre calas.",
                "— fa de llançadora des de la Plaça Forgas de Begur fins a les cales pròpies de Begur. Per prendre'l cal anar primer en cotxe a Begur (uns 15 minuts des de Tamariu). Totes les rutes comencen i acaben a la Plaça Forgas, així que no hi ha salt directe entre cales.",
                "— il fait la navette depuis la Plaça Forgas de Begur vers les criques de Begur. Pour le prendre, il faut d'abord rejoindre Begur en voiture (environ 15 minutes depuis Tamariu). Chaque trajet part et se termine à la Plaça Forgas, il n'y a donc pas de saut direct d'une crique à l'autre.",
                "— hij pendelt vanaf de Plaça Forgas in Begur naar de eigen baaien van Begur. Om er te komen moet u eerst naar Begur rijden (ongeveer 15 minuten vanuit Tamariu). Elke route begint en eindigt op de Plaça Forgas, dus er is geen directe overstap tussen de baaien.",
                "— er pendelt von der Plaça Forgas in Begur zu den Buchten von Begur. Um ihn zu erreichen, muss man zuerst nach Begur fahren (etwa 15 Minuten von Tamariu). Jede Route beginnt und endet an der Plaça Forgas, daher gibt es keinen direkten Sprung zwischen den Buchten."),
            "red": T("rojo", "vermell", "rouge", "rood", "rot"),
            "blue": T("azul", "blau", "bleu", "blauw", "blau"),
            "green": T("verde", "verd", "vert", "groen", "grün"),
            "from Begur": T("desde Begur", "des de Begur", "depuis Begur", "vanuit Begur", "ab Begur"),
            "from Sa Riera": T("desde Sa Riera", "des de Sa Riera", "depuis Sa Riera",
                               "vanuit Sa Riera", "ab Sa Riera"),
            "from Aiguablava": T("desde Aiguablava", "des de Aiguablava", "depuis Aiguablava",
                                 "vanuit Aiguablava", "ab Aiguablava"),
            "from Sa Tuna": T("desde Sa Tuna", "des de Sa Tuna", "depuis Sa Tuna",
                              "vanuit Sa Tuna", "ab Sa Tuna"),
            "* Connections from/to Esclanyà. Times shown in": T(
                "* Conexiones desde/hacia Esclanyà. Las horas en",
                "* Connexions des de/cap a Esclanyà. Les hores en",
                "* Correspondances depuis/vers Esclanyà. Les heures en",
                "* Aansluitingen van/naar Esclanyà. De tijden in",
                "* Anschlüsse von/nach Esclanyà. Die Zeiten in"),
            "orange": T("naranja", "taronja", "orange", "oranje", "Orange"),
            "are the last of the day on that route.": T(
                "son las últimas del día en esa ruta.", "són les últimes del dia en aquella ruta.",
                "sont les dernières de la journée sur cet itinéraire.", "zijn de laatste van de dag op die route.",
                "sind die letzten des Tages auf dieser Route."),
            "Begur shuttle bus timetable": T(
                "Horario del bus lanzadera de Begur", "Horari del bus llançadora de Begur",
                "Horaire de la navette de Begur", "Dienstregeling pendelbus Begur",
                "Fahrplan des Begur-Pendelbusses"),
            "More about the Begur beach bus": T(
                "Más sobre el bus de playas de Begur", "Més sobre el bus de platges de Begur",
                "En savoir plus sur la navette des plages de Begur", "Meer over de strandbus van Begur",
                "Mehr über den Strandbus von Begur"),
            "Girona → Palafrugell — getting home": T(
                "Girona → Palafrugell — volver a casa", "Girona → Palafrugell — tornar a casa",
                "Gérone → Palafrugell — le retour", "Girona → Palafrugell — naar huis",
                "Girona → Palafrugell — nach Hause"),
            "Moventis (Sarfa) line 42, direct via La Bisbal · daily 1 July – 31 August 2026 · journey ~1 h 10": T(
                "Moventis (Sarfa) línea 42, directo vía La Bisbal · diario 1 julio – 31 agosto 2026 · trayecto ~1 h 10",
                "Moventis (Sarfa) línia 42, directe via La Bisbal · diari 1 juliol – 31 agost 2026 · trajecte ~1 h 10",
                "Moventis (Sarfa) ligne 42, direct via La Bisbal · tous les jours 1er juillet – 31 août 2026 · trajet ~1 h 10",
                "Moventis (Sarfa) lijn 42, direct via La Bisbal · dagelijks 1 juli – 31 augustus 2026 · reistijd ~1 u 10",
                "Moventis (Sarfa) Linie 42, direkt über La Bisbal · täglich 1. Juli – 31. August 2026 · Fahrt ~1 Std. 10"),
            "There is no direct bus between Tamariu and Girona — you travel in two legs. Coming home you take": T(
                "No hay autobús directo entre Tamariu y Girona — se viaja en dos tramos. Para volver se toma",
                "No hi ha autobús directe entre Tamariu i Girona — es viatja en dos trams. Per tornar es pren",
                "Il n'y a pas de bus direct entre Tamariu et Gérone — le trajet se fait en deux étapes. Au retour, vous prenez",
                "Er is geen directe bus tussen Tamariu en Girona — u reist in twee etappes. Voor de terugreis neemt u",
                "Es gibt keinen Direktbus zwischen Tamariu und Girona — die Fahrt erfolgt in zwei Etappen. Für die Rückfahrt nehmen Sie"),
            "line 42": T("la línea 42", "la línia 42", "la ligne 42", "lijn 42", "die Linie 42"),
            "(Girona → La Bisbal → Palafrugell), then the": T(
                "(Girona → La Bisbal → Palafrugell), y después el", "(Girona → La Bisbal → Palafrugell), i després el",
                "(Gérone → La Bisbal → Palafrugell), puis le", "(Girona → La Bisbal → Palafrugell), en daarna de",
                "(Girona → La Bisbal → Palafrugell), dann den"),
            "for the last stretch to Tamariu. The table shows every line 42 departure from Girona and when it reaches Palafrugell station;": T(
                "para el último tramo hasta Tamariu. La tabla muestra cada salida de la línea 42 desde Girona y cuándo llega a la estación de Palafrugell;",
                "per a l'últim tram fins a Tamariu. La taula mostra cada sortida de la línia 42 des de Girona i quan arriba a l'estació de Palafrugell;",
                "pour le dernier tronçon jusqu'à Tamariu. Le tableau indique chaque départ de la ligne 42 depuis Gérone et l'heure d'arrivée à la gare de Palafrugell ;",
                "voor het laatste stuk naar Tamariu. De tabel toont elk vertrek van lijn 42 uit Girona en wanneer die het station van Palafrugell bereikt;",
                "für das letzte Stück nach Tamariu. Die Tabelle zeigt jede Abfahrt der Linie 42 aus Girona und wann sie den Bahnhof Palafrugell erreicht;"),
            "gold rows": T("las filas doradas", "les files daurades", "les lignes dorées",
                           "de goudkleurige rijen", "die goldenen Zeilen"),
            "are the ones that land in time for a Bus 60′ home.": T(
                "son las que llegan a tiempo para un Bus 60′ de vuelta a casa.",
                "són les que arriben a temps per a un Bus 60′ de tornada a casa.",
                "sont celles qui arrivent à temps pour un Bus 60′ vers la maison.",
                "zijn degene die op tijd aankomen voor een Bus 60′ naar huis.",
                "sind diejenigen, die rechtzeitig für einen Bus 60′ nach Hause ankommen."),
            "Estació, departs": T("Estació, sale", "Estació, surt", "Estació, départ",
                                  "Estació, vertrek", "Estació, Abfahrt"),
            "arrives": T("llega", "arriba", "arrivée", "aankomst", "Ankunft"),
            "Onward Bus 60′ → Tamariu": T(
                "Enlace Bus 60′ → Tamariu", "Enllaç Bus 60′ → Tamariu", "Correspondance Bus 60′ → Tamariu",
                "Aansluiting Bus 60′ → Tamariu", "Anschluss Bus 60′ → Tamariu"),
            "09:00 → Tamariu 09:30": T("09:00 → Tamariu 09:30", "09:00 → Tamariu 09:30",
                                       "09:00 → Tamariu 09:30", "09:00 → Tamariu 09:30", "09:00 → Tamariu 09:30"),
            "tight, 5 min at the station": T(
                "justo, 5 min en la estación", "just, 5 min a l'estació", "juste, 5 min à la gare",
                "krap, 5 min op het station", "knapp, 5 Min. am Bahnhof"),
            "10:00 → Tamariu 10:30": T("10:00 → Tamariu 10:30", "10:00 → Tamariu 10:30",
                                       "10:00 → Tamariu 10:30", "10:00 → Tamariu 10:30", "10:00 → Tamariu 10:30"),
            "tight, 5 min": T("justo, 5 min", "just, 5 min", "juste, 5 min", "krap, 5 min", "knapp, 5 Min."),
            "11:00 → Tamariu 11:30": T("11:00 → Tamariu 11:30", "11:00 → Tamariu 11:30",
                                       "11:00 → Tamariu 11:30", "11:00 → Tamariu 11:30", "11:00 → Tamariu 11:30"),
            "tight; last before the midday gap": T(
                "justo; el último antes del paréntesis del mediodía", "just; l'últim abans del parèntesi del migdia",
                "juste ; le dernier avant la coupure de midi", "krap; de laatste vóór de middagonderbreking",
                "knapp; der letzte vor der Mittagslücke"),
            "15:30 → Tamariu 16:00": T("15:30 → Tamariu 16:00", "15:30 → Tamariu 16:00",
                                       "15:30 → Tamariu 16:00", "15:30 → Tamariu 16:00", "15:30 → Tamariu 16:00"),
            "long midday wait": T("larga espera al mediodía", "llarga espera al migdia",
                                  "longue attente à midi", "lange middagwachttijd", "lange Mittagswartezeit"),
            "long wait": T("larga espera", "llarga espera", "longue attente", "lange wachttijd", "lange Wartezeit"),
            "16:30 → Tamariu 17:00": T("16:30 → Tamariu 17:00", "16:30 → Tamariu 17:00",
                                       "16:30 → Tamariu 17:00", "16:30 → Tamariu 17:00", "16:30 → Tamariu 17:00"),
            "17:30 → Tamariu 18:00": T("17:30 → Tamariu 18:00", "17:30 → Tamariu 18:00",
                                       "17:30 → Tamariu 18:00", "17:30 → Tamariu 18:00", "17:30 → Tamariu 18:00"),
            "18:30 → Tamariu 19:00": T("18:30 → Tamariu 19:00", "18:30 → Tamariu 19:00",
                                       "18:30 → Tamariu 19:00", "18:30 → Tamariu 19:00", "18:30 → Tamariu 19:00"),
            "19:30 → Tamariu 20:00": T("19:30 → Tamariu 20:00", "19:30 → Tamariu 20:00",
                                       "19:30 → Tamariu 20:00", "19:30 → Tamariu 20:00", "19:30 → Tamariu 20:00"),
            "the last Bus 60′ of the day": T(
                "el último Bus 60′ del día", "l'últim Bus 60′ del dia", "le dernier Bus 60′ de la journée",
                "de laatste Bus 60′ van de dag", "der letzte Bus 60′ des Tages"),
            "— no Bus 60′ left · taxi (~€15–20)": T(
                "— ya no queda Bus 60′ · taxi (~€15–20)", "— ja no queda cap Bus 60′ · taxi (~€15–20)",
                "— plus de Bus 60′ · taxi (~€15–20)", "— geen Bus 60′ meer · taxi (~€15–20)",
                "— kein Bus 60′ mehr · Taxi (~€15–20)"),
            "— no Bus 60′ · taxi": T(
                "— sin Bus 60′ · taxi", "— sense Bus 60′ · taxi", "— pas de Bus 60′ · taxi",
                "— geen Bus 60′ · taxi", "— kein Bus 60′ · Taxi"),
            "Mind the midday gap.": T(
                "Cuidado con el paréntesis del mediodía.", "Compte amb el parèntesi del migdia.",
                "Attention à la coupure de midi.", "Let op de middagonderbreking.",
                "Achtung, Mittagslücke."),
            "Bus 60′ has no service between 11:00 and 15:30, so a line 42 arriving 11:55–13:55 means a wait in Palafrugell (nice enough for a long lunch) or a taxi. The safe evening connections are the 13:45–17:45 departures from Girona.": T(
                "El Bus 60′ no circula entre las 11:00 y las 15:30, así que una línea 42 que llegue entre 11:55 y 13:55 supone esperar en Palafrugell (lo bastante agradable para una comida larga) o un taxi. Los enlaces seguros de la tarde son las salidas de 13:45–17:45 desde Girona.",
                "El Bus 60′ no circula entre les 11:00 i les 15:30, així que una línia 42 que arribi entre 11:55 i 13:55 vol dir esperar a Palafrugell (prou agradable per a un dinar llarg) o un taxi. Els enllaços segurs de la tarda són les sortides de 13:45–17:45 des de Girona.",
                "Le Bus 60′ ne circule pas entre 11:00 et 15:30, donc une ligne 42 arrivant entre 11:55 et 13:55 signifie une attente à Palafrugell (assez agréable pour un long déjeuner) ou un taxi. Les correspondances sûres du soir sont les départs de 13:45–17:45 depuis Gérone.",
                "Bus 60′ rijdt niet tussen 11:00 en 15:30, dus een lijn 42 die tussen 11:55 en 13:55 aankomt betekent wachten in Palafrugell (aangenaam genoeg voor een lange lunch) of een taxi. De veilige avondaansluitingen zijn de vertrektijden 13:45–17:45 uit Girona.",
                "Bus 60′ verkehrt zwischen 11:00 und 15:30 nicht, daher bedeutet eine Linie 42, die zwischen 11:55 und 13:55 ankommt, Warten in Palafrugell (angenehm genug für ein langes Mittagessen) oder ein Taxi. Die sicheren Abendanschlüsse sind die Abfahrten 13:45–17:45 aus Girona."),
            "(1–3, 6–10, 13–16) Bus 60′ runs only three times a day — into Tamariu at 07:30, 11:30 and 17:00 — so plan around those instead.": T(
                "(1–3, 6–10, 13–16) el Bus 60′ solo circula tres veces al día — llegando a Tamariu a las 07:30, 11:30 y 17:00 — así que planifique en torno a esas horas.",
                "(1–3, 6–10, 13–16) el Bus 60′ només circula tres cops al dia — arribant a Tamariu a les 07:30, 11:30 i 17:00 — així que planifiqueu al voltant d'aquestes hores.",
                "(1–3, 6–10, 13–16) le Bus 60′ ne circule que trois fois par jour — arrivée à Tamariu à 07:30, 11:30 et 17:00 — planifiez donc autour de ces horaires.",
                "(1–3, 6–10, 13–16) rijdt Bus 60′ slechts driemaal per dag — in Tamariu om 07:30, 11:30 en 17:00 — plan dus rond die tijden.",
                "(1.–3., 6.–10., 13.–16.) fährt Bus 60′ nur dreimal täglich — in Tamariu um 07:30, 11:30 und 17:00 — planen Sie also danach."),
            "Getting there in the morning": T(
                "Ir por la mañana", "Anar-hi al matí", "S'y rendre le matin",
                "'s Ochtends heen", "Die Hinfahrt am Morgen"),
            "is the same in reverse: Bus 60′ or the Julivia to Palafrugell, then line 42 on to Girona (roughly hourly). Full timetable on the operator's PDF below.": T(
                "es lo mismo a la inversa: Bus 60′ o la Julivia hasta Palafrugell, y después la línea 42 hasta Girona (aproximadamente cada hora). Horario completo en el PDF del operador más abajo.",
                "és el mateix a la inversa: Bus 60′ o la Julivia fins a Palafrugell, i després la línia 42 fins a Girona (aproximadament cada hora). Horari complet al PDF de l'operador més avall.",
                "c'est l'inverse : Bus 60′ ou la Julivia jusqu'à Palafrugell, puis la ligne 42 jusqu'à Gérone (environ toutes les heures). Horaire complet sur le PDF de l'opérateur ci-dessous.",
                "is hetzelfde omgekeerd: Bus 60′ of de Julivia naar Palafrugell, dan lijn 42 door naar Girona (ongeveer elk uur). Volledige dienstregeling in de PDF van de vervoerder hieronder.",
                "ist dasselbe umgekehrt: Bus 60′ oder die Julivia nach Palafrugell, dann Linie 42 weiter nach Girona (etwa stündlich). Vollständiger Fahrplan im PDF des Betreibers unten."),
            "Official Moventis line 42 timetable": T(
                "Horario oficial Moventis línea 42", "Horari oficial Moventis línia 42",
                "Horaire officiel Moventis ligne 42", "Officiële dienstregeling Moventis lijn 42",
                "Offizieller Moventis-Fahrplan Linie 42"),
            "Our guide to visiting Girona": T(
                "Nuestra guía para visitar Girona", "La nostra guia per visitar Girona",
                "Notre guide pour visiter Gérone", "Onze gids voor een bezoek aan Girona",
                "Unser Leitfaden für einen Besuch in Girona"),
            "Planning a car-free day around these buses? See": T(
                "¿Planea un día sin coche en torno a estos buses? Vea",
                "Planifiqueu un dia sense cotxe al voltant d'aquests busos? Vegeu",
                "Vous préparez une journée sans voiture autour de ces bus ? Voir",
                "Plant u een autoloze dag rond deze bussen? Zie",
                "Planen Sie einen autofreien Tag rund um diese Busse? Siehe"),
            "Tamariu by Foot — seven car-free days out": T(
                "Tamariu a Pie — siete días sin coche", "Tamariu a Peu — set dies sense cotxe",
                "Tamariu à Pied — sept journées sans voiture", "Tamariu te Voet — zeven autoloze dagen",
                "Tamariu zu Fuß — sieben autofreie Tage"),
            ", which builds full itineraries around the Bus 60, the Julivia and the coastal footpaths.": T(
                ", que construye itinerarios completos en torno al Bus 60, la Julivia y los senderos costeros.",
                ", que construeix itineraris complets al voltant del Bus 60, la Julivia i els camins costaners.",
                ", qui bâtit des itinéraires complets autour du Bus 60, de la Julivia et des sentiers côtiers.",
                ", die volledige routes opbouwt rond Bus 60, de Julivia en de kustpaden.",
                ", das vollständige Routen rund um Bus 60, die Julivia und die Küstenpfade aufbaut."),
            "Choose a bus route": T(
                "Elija una línea de autobús", "Trieu una línia d'autobús", "Choisissez une ligne de bus",
                "Kies een buslijn", "Buslinie wählen"),
        },
        "script_only": _MAP_SCRIPT_STRINGS,
    }
}
