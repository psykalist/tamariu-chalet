#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
String tables for the structured guide pages.

These pages use "strings" mode: the English markup is the single source and only
the words are per language (see strings_mode.py). Route names, place names,
restaurant names, phone numbers, addresses, ratings and distances are
deliberately absent from the tables, which leaves them untouched.
"""

from content_things_to_do import FOOTER_STD, FOOTER_WATER

PAGES = {}


def T(es, ca, fr, nl):
    return {"es": es, "ca": ca, "fr": fr, "nl": nl}


# ─────────────────────────────────────────────────────────────────────────────
# things-to-do/cycling.html
# ─────────────────────────────────────────────────────────────────────────────
PAGES["things-to-do/cycling.html"] = {
    "mode": "strings",
    "footer": FOOTER_WATER,
    "meta": {
        "es": {"title": "Ciclismo — Tamariu Chalet",
               "desc": "Rutas ciclistas cerca de Tamariu, Costa Brava — carreteras panorámicas y caminos de ronda de la zona de Palafrugell, desde Tamariu Chalet."},
        "ca": {"title": "Ciclisme — Tamariu Chalet",
               "desc": "Rutes ciclistes a prop de Tamariu, Costa Brava — carreteres panoràmiques i camins de ronda de la zona de Palafrugell, des de Tamariu Chalet."},
        "fr": {"title": "Cyclisme — Tamariu Chalet",
               "desc": "Itinéraires cyclables près de Tamariu, Costa Brava — routes panoramiques et chemins côtiers de la région de Palafrugell, au départ du Tamariu Chalet."},
        "nl": {"title": "Fietsen — Tamariu Chalet",
               "desc": "Fietsroutes bij Tamariu, Costa Brava — schilderachtige wegen en kustpaden rond Palafrugell, vanaf Tamariu Chalet."},
    },
    "strings": {
        "Things To Do → Cycling": T(
            "Qué Hacer → Ciclismo", "Què Fer → Ciclisme",
            "À Faire → Cyclisme", "Wat Te Doen → Fietsen"),
        "Cycling the Costa Brava": T(
            "Ciclismo por la Costa Brava", "Ciclisme per la Costa Brava",
            "Le Cyclisme sur la Costa Brava", "Fietsen op de Costa Brava"),
        "Popular Routes from Tamariu": T(
            "Rutas Populares desde Tamariu", "Rutes Populars des de Tamariu",
            "Itinéraires Populaires au Départ de Tamariu",
            "Populaire Routes vanuit Tamariu"),
        "(37 km | Difficult)": T("(37 km | Difícil)", "(37 km | Difícil)",
                                 "(37 km | Difficile)", "(37 km | Zwaar)"),
        "(64 km | Easy, e-bike)": T("(64 km | Fácil, e-bike)", "(64 km | Fàcil, e-bike)",
                                    "(64 km | Facile, vélo électrique)",
                                    "(64 km | Makkelijk, e-bike)"),
        "(82 km | Easy, road)": T("(82 km | Fácil, carretera)", "(82 km | Fàcil, carretera)",
                                  "(82 km | Facile, route)", "(82 km | Makkelijk, racefiets)"),
        "(84 km | Difficult)": T("(84 km | Difícil)", "(84 km | Difícil)",
                                 "(84 km | Difficile)", "(84 km | Zwaar)"),
        "Bike Hire": T("Alquiler de Bicicletas", "Lloguer de Bicicletes",
                       "Location de Vélos", "Fietsverhuur"),
        "— Our Recommendation": T("— Nuestra Recomendación", "— La Nostra Recomanació",
                                  "— Notre Recommandation", "— Onze Aanrader"),
        "Website →": T("Sitio web →", "Lloc web →", "Site web →", "Website →"),

        "The Costa Brava and surrounding Empordà plain make for exceptional cycling territory.\n    Whether you're after gentle coastal rollers or challenging climbs into the Gavarres hills,\n    there's a route for every rider — and the roads are quiet, well-surfaced and stunningly scenic.": T(
            "La Costa Brava y la llanura del Empordà que la rodea son un territorio excepcional para el ciclismo. Tanto si busca suaves toboganes junto al mar como subidas exigentes hacia las Gavarres, hay una ruta para cada ciclista — y las carreteras son tranquilas, están en buen estado y son de una belleza extraordinaria.",
            "La Costa Brava i la plana de l'Empordà que l'envolta són un territori excepcional per al ciclisme. Tant si busqueu suaus tobogans arran de mar com pujades exigents cap a les Gavarres, hi ha una ruta per a cada ciclista — i les carreteres són tranquil·les, en bon estat i d'una bellesa extraordinària.",
            "La Costa Brava et la plaine de l'Empordà qui l'entoure forment un territoire cyclable exceptionnel. Que vous cherchiez de douces ondulations le long de la côte ou des ascensions exigeantes vers les collines des Gavarres, il y a un itinéraire pour chaque cycliste — et les routes sont calmes, bien revêtues et magnifiques.",
            "De Costa Brava en de omliggende vlakte van de Empordà vormen uitzonderlijk fietsgebied. Of u nu zoekt naar zacht glooiende kustwegen of pittige klimmen de Gavarres-heuvels in, er is een route voor elke fietser — en de wegen zijn rustig, goed van kwaliteit en adembenemend mooi."),

        "A varied and rewarding mountain bike loop starting from Calella de Palafrugell, through Tamariu and inland via Mas Batllia, Regencós, Quermany and Pals before returning through Esclanyà. Mostly rideable trails with a mix of forest tracks and singletrack. Rated 4.7/5 on Wikiloc.": T(
            "Un circuito de BTT variado y gratificante que sale de Calella de Palafrugell, pasa por Tamariu y se adentra tierra adentro por Mas Batllia, Regencós, Quermany y Pals antes de volver por Esclanyà. Senderos mayoritariamente ciclables, con mezcla de pistas forestales y singletrack. Valorado con 4,7/5 en Wikiloc.",
            "Un circuit de BTT variat i gratificant que surt de Calella de Palafrugell, passa per Tamariu i s'endinsa cap a l'interior per Mas Batllia, Regencós, Quermany i Pals abans de tornar per Esclanyà. Camins majoritàriament ciclables, amb barreja de pistes forestals i singletrack. Valorat amb 4,7/5 a Wikiloc.",
            "Une boucle VTT variée et gratifiante au départ de Calella de Palafrugell, passant par Tamariu puis dans les terres via Mas Batllia, Regencós, Quermany et Pals avant de revenir par Esclanyà. Sentiers roulants pour l'essentiel, mêlant pistes forestières et singletrack. Noté 4,7/5 sur Wikiloc.",
            "Een gevarieerde en lonende mountainbikeroute vanaf Calella de Palafrugell, door Tamariu en het binnenland in via Mas Batllia, Regencós, Quermany en Pals, met een terugweg door Esclanyà. Grotendeels goed berijdbare paden met een mix van bosbanen en singletrack. Beoordeeld met 4,7/5 op Wikiloc."),

        "A long circular e-bike route from Tamariu taking in Ermedàs Church, the Aubi Stream bridge, Pi d'en Xana, the Eiffel Bridge, Calonge Castle, Coll de la Ganga, the Carmen Amaya Viewpoint and Esclanyà Castle. Gentle gradients throughout, well suited to an e-bike given the distance.": T(
            "Una larga ruta circular en bicicleta eléctrica desde Tamariu que pasa por la iglesia de Ermedàs, el puente sobre la riera Aubi, el Pi d'en Xana, el Puente Eiffel, el castillo de Calonge, el Coll de la Ganga, el mirador de Carmen Amaya y el castillo de Esclanyà. Pendientes suaves durante todo el recorrido, muy apropiada para e-bike dada la distancia.",
            "Una llarga ruta circular en bicicleta elèctrica des de Tamariu que passa per l'església d'Ermedàs, el pont sobre la riera Aubi, el Pi d'en Xana, el Pont Eiffel, el castell de Calonge, el Coll de la Ganga, el mirador de Carmen Amaya i el castell d'Esclanyà. Pendents suaus durant tot el recorregut, molt apropiada per a e-bike atesa la distància.",
            "Un long circuit en vélo électrique au départ de Tamariu passant par l'église d'Ermedàs, le pont sur le ruisseau Aubi, le Pi d'en Xana, le pont Eiffel, le château de Calonge, le Coll de la Ganga, le belvédère Carmen Amaya et le château d'Esclanyà. Pentes douces sur tout le parcours, bien adapté au vélo électrique vu la distance.",
            "Een lange rondrit op de e-bike vanuit Tamariu langs de kerk van Ermedàs, de brug over de Aubi-beek, de Pi d'en Xana, de Eiffelbrug, het kasteel van Calonge, de Coll de la Ganga, het uitzichtpunt Carmen Amaya en het kasteel van Esclanyà. Overal flauwe hellingen, gezien de afstand goed geschikt voor een e-bike."),

        "A full-day road cycling loop starting and finishing in Castell-Platja d'Aro, taking in Palamós, Palafrugell, Tamariu and Begur before a lunch stop at Els Masos de Pals and a visit to the medieval castle at Peratallada. The return leg winds inland via La Bisbal de l'Empordà and Calonge on quiet roads. A great mix of coastline, countryside and culture — worth timing for an ice cream stop in Peratallada.": T(
            "Una ruta de carretera de día completo que sale y termina en Castell-Platja d'Aro, pasando por Palamós, Palafrugell, Tamariu y Begur antes de la parada para comer en Els Masos de Pals y la visita al castillo medieval de Peratallada. La vuelta serpentea tierra adentro por La Bisbal de l'Empordà y Calonge por carreteras tranquilas. Una gran mezcla de costa, campo y cultura — merece la pena calcular el tiempo para parar a tomar un helado en Peratallada.",
            "Una ruta de carretera de dia complet que surt i acaba a Castell-Platja d'Aro, passant per Palamós, Palafrugell, Tamariu i Begur abans de la parada per dinar a Els Masos de Pals i la visita al castell medieval de Peratallada. La tornada serpenteja cap a l'interior per La Bisbal de l'Empordà i Calonge per carreteres tranquil·les. Una gran barreja de costa, camp i cultura — val la pena calcular el temps per parar a prendre un gelat a Peratallada.",
            "Une boucle sur route à la journée au départ et à l'arrivée de Castell-Platja d'Aro, par Palamós, Palafrugell, Tamariu et Begur, avec pause déjeuner à Els Masos de Pals et visite du château médiéval de Peratallada. Le retour serpente dans les terres via La Bisbal de l'Empordà et Calonge sur des routes tranquilles. Un beau mélange de littoral, de campagne et de culture — prévoyez l'arrêt glace à Peratallada.",
            "Een racefietsroute van een hele dag met start en finish in Castell-Platja d'Aro, via Palamós, Palafrugell, Tamariu en Begur, met een lunchstop in Els Masos de Pals en een bezoek aan het middeleeuwse kasteel van Peratallada. De terugweg kronkelt landinwaarts via La Bisbal de l'Empordà en Calonge over rustige wegen. Een mooie mix van kust, platteland en cultuur — plan er een ijsstop in Peratallada bij in."),

        "A demanding full-day mountain bike loop from Golf d'Aro along the coast via Platja d'Aro, Palamós, Calella de Palafrugell and the Sant Sebastià lighthouse, through Tamariu, Aiguablava, Sa Tuna and Begur, before heading inland into the Gavarres massif — passing Mines d'en Bernat, Castell de Vila Romà and the Eiffel Bridge — and back to Golf d'Aro. Nearly 2,000m of climbing; for strong, experienced riders.": T(
            "Un exigente circuito de BTT de día completo desde Golf d'Aro siguiendo la costa por Platja d'Aro, Palamós, Calella de Palafrugell y el faro de Sant Sebastià, pasando por Tamariu, Aiguablava, Sa Tuna y Begur, antes de adentrarse en el macizo de les Gavarres — pasando por les Mines d'en Bernat, el Castell de Vila Romà y el Puente Eiffel — y volver a Golf d'Aro. Casi 2.000 m de desnivel positivo; para ciclistas fuertes y experimentados.",
            "Un exigent circuit de BTT de dia complet des de Golf d'Aro seguint la costa per Platja d'Aro, Palamós, Calella de Palafrugell i el far de Sant Sebastià, passant per Tamariu, Aiguablava, Sa Tuna i Begur, abans d'endinsar-se al massís de les Gavarres — passant per les Mines d'en Bernat, el Castell de Vila Romà i el Pont Eiffel — i tornar a Golf d'Aro. Gairebé 2.000 m de desnivell positiu; per a ciclistes forts i experimentats.",
            "Une boucle VTT exigeante à la journée depuis Golf d'Aro, longeant la côte par Platja d'Aro, Palamós, Calella de Palafrugell et le phare de Sant Sebastià, traversant Tamariu, Aiguablava, Sa Tuna et Begur, avant de s'enfoncer dans le massif des Gavarres — en passant par les Mines d'en Bernat, le Castell de Vila Romà et le pont Eiffel — puis retour à Golf d'Aro. Près de 2 000 m de dénivelé positif ; pour cyclistes aguerris.",
            "Een zware mountainbikeroute van een hele dag vanaf Golf d'Aro langs de kust via Platja d'Aro, Palamós, Calella de Palafrugell en de vuurtoren van Sant Sebastià, door Tamariu, Aiguablava, Sa Tuna en Begur, om daarna het Gavarres-massief in te trekken — langs Mines d'en Bernat, Castell de Vila Romà en de Eiffelbrug — en terug naar Golf d'Aro. Bijna 2.000 hoogtemeters; voor sterke, ervaren fietsers."),

        "Several bike hire providers operate in the area. We recommend booking in advance during summer.": T(
            "En la zona operan varias empresas de alquiler de bicicletas. Recomendamos reservar con antelación en verano.",
            "A la zona hi operen diverses empreses de lloguer de bicicletes. Recomanem reservar amb antelació a l'estiu.",
            "Plusieurs loueurs de vélos sont présents dans la région. Nous conseillons de réserver à l'avance en été.",
            "In de omgeving zijn verschillende fietsverhuurders actief. In de zomer raden wij aan vooraf te reserveren."),

        "Ask us when you book — we can recommend the current best local hire options and provide route maps.\n    The house has a secure covered area for storing bikes overnight.": T(
            "Pregúntenos al reservar — podemos recomendarle las mejores opciones de alquiler del momento y facilitarle mapas de rutas. La casa dispone de una zona cubierta y segura para guardar las bicicletas por la noche.",
            "Pregunteu-nos en reservar — us podem recomanar les millors opcions de lloguer del moment i facilitar-vos mapes de rutes. La casa disposa d'una zona coberta i segura per guardar-hi les bicicletes a la nit.",
            "Demandez-nous au moment de réserver — nous pouvons vous indiquer les meilleures options de location du moment et vous fournir des cartes d'itinéraires. La maison dispose d'un espace couvert et sécurisé pour ranger les vélos la nuit.",
            "Vraag het ons bij het boeken — wij kunnen de op dat moment beste lokale verhuuropties aanbevelen en routekaarten meegeven. Het huis heeft een afgesloten overdekte ruimte om fietsen 's nachts te stallen."),

        "4.8 (288) · Bicycle hire shop · Palafrugell, Spain · +34 972 30 58 55": T(
            "4,8 (288) · Tienda de alquiler de bicicletas · Palafrugell, España · +34 972 30 58 55",
            "4,8 (288) · Botiga de lloguer de bicicletes · Palafrugell, Espanya · +34 972 30 58 55",
            "4,8 (288) · Magasin de location de vélos · Palafrugell, Espagne · +34 972 30 58 55",
            "4,8 (288) · Fietsverhuur · Palafrugell, Spanje · +34 972 30 58 55"),
        "5.0 (245) · Bicycle hire shop · Spain · +34 637 65 30 47": T(
            "5,0 (245) · Tienda de alquiler de bicicletas · España · +34 637 65 30 47",
            "5,0 (245) · Botiga de lloguer de bicicletes · Espanya · +34 637 65 30 47",
            "5,0 (245) · Magasin de location de vélos · Espagne · +34 637 65 30 47",
            "5,0 (245) · Fietsverhuur · Spanje · +34 637 65 30 47"),
        "4.4 (74) · Bicycle hire shop · Palafrugell, Spain · +34 972 61 07 09": T(
            "4,4 (74) · Tienda de alquiler de bicicletas · Palafrugell, España · +34 972 61 07 09",
            "4,4 (74) · Botiga de lloguer de bicicletes · Palafrugell, Espanya · +34 972 61 07 09",
            "4,4 (74) · Magasin de location de vélos · Palafrugell, Espagne · +34 972 61 07 09",
            "4,4 (74) · Fietsverhuur · Palafrugell, Spanje · +34 972 61 07 09"),
        "Closed · Opens 8 am Thu · Delivery": T(
            "Cerrado · Abre jue 8:00 · Entrega a domicilio",
            "Tancat · Obre dj. 8:00 · Lliurament a domicili",
            "Fermé · Ouvre jeu. 8h00 · Livraison",
            "Gesloten · Opent do. 8:00 · Bezorging"),
        "Closed · Opens 9 am Thu · On-site services": T(
            "Cerrado · Abre jue 9:00 · Servicios in situ",
            "Tancat · Obre dj. 9:00 · Serveis in situ",
            "Fermé · Ouvre jeu. 9h00 · Services sur place",
            "Gesloten · Opent do. 9:00 · Diensten ter plaatse"),
        "Closed · Opens 9 am Thu": T(
            "Cerrado · Abre jue 9:00", "Tancat · Obre dj. 9:00",
            "Fermé · Ouvre jeu. 9h00", "Gesloten · Opent do. 9:00"),
    },
}

# ─────────────────────────────────────────────────────────────────────────────
# things-to-do/walking.html
# ─────────────────────────────────────────────────────────────────────────────
PAGES["things-to-do/walking.html"] = {
    "mode": "strings",
    "footer": FOOTER_STD,
    "meta": {
        "es": {"title": "Senderismo — Tamariu Chalet",
               "desc": "Rutas a pie cerca de Tamariu, Costa Brava — el camino de ronda GR-92 y paseos por el interior desde Tamariu Chalet."},
        "ca": {"title": "Senderisme — Tamariu Chalet",
               "desc": "Rutes a peu a prop de Tamariu, Costa Brava — el camí de ronda GR-92 i passejades per l'interior des de Tamariu Chalet."},
        "fr": {"title": "Randonnée — Tamariu Chalet",
               "desc": "Itinéraires de randonnée près de Tamariu, Costa Brava — le sentier côtier GR-92 et les balades dans l'arrière-pays au départ du Tamariu Chalet."},
        "nl": {"title": "Wandelen — Tamariu Chalet",
               "desc": "Wandelroutes bij Tamariu, Costa Brava — het kustpad GR-92 en wandelingen door het achterland vanaf Tamariu Chalet."},
    },
    "strings": {
        "Things To Do → Walking": T(
            "Qué Hacer → Senderismo", "Què Fer → Senderisme",
            "À Faire → Randonnée", "Wat Te Doen → Wandelen"),
        "Walking in the Area": T(
            "Senderismo en la Zona", "Senderisme a la Zona",
            "Randonner dans la Région", "Wandelen in de Omgeving"),
        "Featured Walks": T("Rutas Destacadas", "Rutes Destacades",
                            "Randonnées à la Une", "Uitgelichte Wandelingen"),
        "Walking Tips": T("Consejos para Caminar", "Consells per Caminar",
                          "Conseils de Randonnée", "Wandeltips"),
        "▶ Animate route": T("▶ Animar ruta", "▶ Animar ruta",
                             "▶ Animer l'itinéraire", "▶ Route afspelen"),
        "↺ Reset": T("↺ Reiniciar", "↺ Reiniciar", "↺ Réinitialiser", "↺ Opnieuw"),
        "Speed": T("Velocidad", "Velocitat", "Vitesse", "Snelheid"),

        "The coastline and hinterland around Tamariu offer superb walking for all abilities — from gentle\n    strolls between coves to longer hikes through the cork oak forests of the Gavarres. The famous\n    GR-92 coastal path passes right through the village.": T(
            "La costa y el interior alrededor de Tamariu ofrecen un senderismo magnífico para todos los niveles — desde paseos suaves entre calas hasta caminatas más largas por los alcornocales de les Gavarres. El famoso camino de ronda GR-92 pasa por el mismo pueblo.",
            "La costa i l'interior al voltant de Tamariu ofereixen un senderisme magnífic per a tots els nivells — des de passejades suaus entre cales fins a caminades més llargues per les suredes de les Gavarres. El famós camí de ronda GR-92 passa pel mateix poble.",
            "Le littoral et l'arrière-pays autour de Tamariu offrent de superbes randonnées pour tous les niveaux — de la promenade tranquille entre les criques aux marches plus longues dans les forêts de chênes-lièges des Gavarres. Le célèbre sentier côtier GR-92 traverse le village.",
            "De kust en het achterland rond Tamariu bieden schitterende wandelingen voor elk niveau — van rustige tochtjes tussen de baaien tot langere trektochten door de kurkeikbossen van de Gavarres. Het beroemde kustpad GR-92 loopt dwars door het dorp."),

        "Walk to the Beach — 3&nbsp;km Circular from Tamariu Chalet": T(
            "Paseo a la Playa — Circular de 3 km desde Tamariu Chalet",
            "Passejada a la Platja — Circular de 3 km des de Tamariu Chalet",
            "Balade jusqu'à la Plage — Boucle de 3 km depuis le Tamariu Chalet",
            "Wandeling naar het Strand — Rondje van 3 km vanaf Tamariu Chalet"),
        "A gentle 3&nbsp;km loop from the chalet down to Aigua Xelida beach and back &mdash; about 90 minutes round trip.": T(
            "Un circuito suave de 3 km desde la casa hasta la playa de Aigua Xelida y vuelta — unos 90 minutos ida y vuelta.",
            "Un circuit suau de 3 km des de la casa fins a la platja d'Aigua Xelida i tornada — uns 90 minuts anada i tornada.",
            "Une boucle facile de 3 km depuis la maison jusqu'à la plage d'Aigua Xelida et retour — environ 90 minutes aller-retour.",
            "Een rustige lus van 3 km vanaf het huis naar het strand van Aigua Xelida en terug — ongeveer 90 minuten heen en terug."),

        "Walk 1 — Tamariu Chalet to Aigua Xelida Coastal Circuit": T(
            "Ruta 1 — Circuito costero de Tamariu Chalet a Aigua Xelida",
            "Ruta 1 — Circuit costaner de Tamariu Chalet a Aigua Xelida",
            "Randonnée 1 — Circuit côtier du Tamariu Chalet à Aigua Xelida",
            "Wandeling 1 — Kustroute van Tamariu Chalet naar Aigua Xelida"),
        "A classic coastal walk  along the costal path. Approximately 3.2km one way. Easy–moderate.": T(
            "Un clásico paseo costero por el camino de ronda. Aproximadamente 3,2 km solo ida. Fácil–moderado.",
            "Una clàssica passejada costanera pel camí de ronda. Aproximadament 3,2 km només anada. Fàcil–moderat.",
            "Une classique balade côtière sur le chemin de ronde. Environ 3,2 km à l'aller. Facile à modéré.",
            "Een klassieke kustwandeling over het kustpad. Ongeveer 3,2 km enkele reis. Makkelijk tot gemiddeld."),

        "Walk 2 — Tamariu to Ses Falugues": T(
            "Ruta 2 — De Tamariu a Ses Falugues", "Ruta 2 — De Tamariu a Ses Falugues",
            "Randonnée 2 — De Tamariu à Ses Falugues", "Wandeling 2 — Van Tamariu naar Ses Falugues"),
        "A circular climb to the summit of Ses Falugues with an exceptional viewpoint, pausing at the Aigua Xelida lookout before dropping down past Sa Roncadora and its small coves — a final stretch with plenty of steps. 8 km, loop. Moderate.": T(
            "Una subida circular hasta la cima de Ses Falugues, con un mirador excepcional, con parada en el mirador de Aigua Xelida antes de bajar pasando por Sa Roncadora y sus pequeñas calas — un tramo final con bastantes escaleras. 8 km, circular. Moderada.",
            "Una pujada circular fins al cim de Ses Falugues, amb un mirador excepcional, amb parada al mirador d'Aigua Xelida abans de baixar passant per Sa Roncadora i les seves petites cales — un tram final amb força escales. 8 km, circular. Moderada.",
            "Une montée en boucle jusqu'au sommet de Ses Falugues, avec un point de vue exceptionnel, en marquant une pause au belvédère d'Aigua Xelida avant de redescendre par Sa Roncadora et ses petites criques — une dernière portion comportant beaucoup de marches. 8 km, boucle. Modérée.",
            "Een rondwandeling omhoog naar de top van Ses Falugues met een uitzonderlijk uitzichtpunt, met een pauze bij het uitkijkpunt van Aigua Xelida voordat u afdaalt langs Sa Roncadora en de kleine baaien — een laatste stuk met veel trappen. 8 km, rondje. Gemiddeld."),

        "Walk 3 — Tamariu to Aiguafreda &amp; Sa Riera": T(
            "Ruta 3 — De Tamariu a Aiguafreda y Sa Riera",
            "Ruta 3 — De Tamariu a Aiguafreda i Sa Riera",
            "Randonnée 3 — De Tamariu à Aiguafreda &amp; Sa Riera",
            "Wandeling 3 — Van Tamariu naar Aiguafreda &amp; Sa Riera"),
        "Head north along the coast from Tamariu towards the unspoiled coves of Aiguafreda and Sa Riera. About  km. Moderate.": T(
            "Siga la costa hacia el norte desde Tamariu en dirección a las calas vírgenes de Aiguafreda y Sa Riera. Unos km. Moderada.",
            "Seguiu la costa cap al nord des de Tamariu en direcció a les cales verges d'Aiguafreda i Sa Riera. Uns km. Moderada.",
            "Longez la côte vers le nord depuis Tamariu en direction des criques préservées d'Aiguafreda et Sa Riera. Environ km. Modérée.",
            "Volg de kust noordwaarts vanaf Tamariu richting de ongerepte baaien Aiguafreda en Sa Riera. Ongeveer km. Gemiddeld."),

        "Walk 4 — Circular Palafrugell: Tamariu, Far Sant Sebastià, Llafranc &amp; Calella": T(
            "Ruta 4 — Circular de Palafrugell: Tamariu, Far de Sant Sebastià, Llafranc y Calella",
            "Ruta 4 — Circular de Palafrugell: Tamariu, Far de Sant Sebastià, Llafranc i Calella",
            "Randonnée 4 — Boucle de Palafrugell : Tamariu, phare de Sant Sebastià, Llafranc &amp; Calella",
            "Wandeling 4 — Rondje Palafrugell: Tamariu, Far Sant Sebastià, Llafranc &amp; Calella"),
        "A scenic loop from Palafrugell down to Tamariu, along the coast to the Sant Sebastià lighthouse, then on through Llafranc and Calella before returning inland to Palafrugell. 21.5 km, loop. Difficult.": T(
            "Un circuito panorámico desde Palafrugell bajando a Tamariu, siguiendo la costa hasta el faro de Sant Sebastià y continuando por Llafranc y Calella antes de volver tierra adentro a Palafrugell. 21,5 km, circular. Difícil.",
            "Un circuit panoràmic des de Palafrugell baixant a Tamariu, seguint la costa fins al far de Sant Sebastià i continuant per Llafranc i Calella abans de tornar cap a l'interior a Palafrugell. 21,5 km, circular. Difícil.",
            "Une boucle panoramique de Palafrugell jusqu'à Tamariu, le long de la côte jusqu'au phare de Sant Sebastià, puis par Llafranc et Calella avant de rentrer dans les terres à Palafrugell. 21,5 km, boucle. Difficile.",
            "Een schilderachtige rondwandeling van Palafrugell omlaag naar Tamariu, langs de kust naar de vuurtoren van Sant Sebastià en verder door Llafranc en Calella, met een terugweg landinwaarts naar Palafrugell. 21,5 km, rondje. Zwaar."),

        "Walk 5 — Tamariu to El Far de Sant Sebastià": T(
            "Ruta 5 — De Tamariu al Far de Sant Sebastià",
            "Ruta 5 — De Tamariu al Far de Sant Sebastià",
            "Randonnée 5 — De Tamariu au Far de Sant Sebastià",
            "Wandeling 5 — Van Tamariu naar El Far de Sant Sebastià"),
        "A loop out to the Sant Sebastià lighthouse on interior trails, returning to Tamariu along the scenic coastal path (camí de ronda). 9 km, loop. Easy.": T(
            "Un circuito hasta el faro de Sant Sebastià por senderos del interior, con vuelta a Tamariu por el precioso camí de ronda. 9 km, circular. Fácil.",
            "Un circuit fins al far de Sant Sebastià per camins de l'interior, amb tornada a Tamariu pel preciós camí de ronda. 9 km, circular. Fàcil.",
            "Une boucle jusqu'au phare de Sant Sebastià par les sentiers de l'intérieur, avec retour à Tamariu par le magnifique chemin de ronde. 9 km, boucle. Facile.",
            "Een rondwandeling naar de vuurtoren van Sant Sebastià over binnenlandse paden, met een terugweg naar Tamariu over het schilderachtige kustpad (camí de ronda). 9 km, rondje. Makkelijk."),

        "The coastal path can be rocky and uneven — proper walking shoes are recommended": T(
            "El camino de ronda puede ser pedregoso e irregular — se recomienda calzado de montaña",
            "El camí de ronda pot ser pedregós i irregular — es recomana calçat de muntanya",
            "Le chemin côtier peut être rocheux et irrégulier — de vraies chaussures de marche sont recommandées",
            "Het kustpad kan rotsachtig en oneffen zijn — stevige wandelschoenen worden aangeraden"),
        "Carry water — there are few water sources on the coastal path": T(
            "Lleve agua — hay pocas fuentes en el camino de ronda",
            "Porteu aigua — hi ha poques fonts al camí de ronda",
            "Emportez de l'eau — les points d'eau sont rares sur le chemin côtier",
            "Neem water mee — er zijn weinig waterpunten langs het kustpad"),
        "Start early in summer to avoid the heat — paths are shaded in the Gavarres but fully exposed on the coast": T(
            "En verano salga temprano para evitar el calor — los senderos de les Gavarres tienen sombra, pero la costa está totalmente expuesta",
            "A l'estiu sortiu aviat per evitar la calor — els camins de les Gavarres tenen ombra, però la costa està totalment exposada",
            "En été, partez tôt pour éviter la chaleur — les sentiers des Gavarres sont ombragés, mais la côte est totalement exposée",
            "Vertrek in de zomer vroeg om de hitte te vermijden — de paden in de Gavarres liggen in de schaduw, maar de kust is volledig onbeschut"),
        "The GR-92 is marked with red and white paint blazes on rocks and trees": T(
            "El GR-92 está señalizado con marcas de pintura roja y blanca en rocas y árboles",
            "El GR-92 està senyalitzat amb marques de pintura vermella i blanca a roques i arbres",
            "Le GR-92 est balisé de marques de peinture rouge et blanche sur les rochers et les arbres",
            "De GR-92 is gemarkeerd met rood-witte verfstrepen op rotsen en bomen"),
        "Several coves along the way are swimmable — pack a towel and snorkel": T(
            "En varias calas del recorrido se puede nadar — lleve toalla y gafas de bucear",
            "En diverses cales del recorregut s'hi pot nedar — porteu tovallola i ulleres de bussejar",
            "On peut se baigner dans plusieurs criques du parcours — prévoyez serviette et masque",
            "In verschillende baaien onderweg kunt u zwemmen — neem een handdoek en snorkel mee"),
    },
    # Strings that live only inside the map script, not in the page markup.
    "script_only": {
        "Start": T("Inicio", "Inici", "Départ", "Start"),
        "Finish": T("Final", "Final", "Arrivée", "Einde"),
        "Beach": T("Playa", "Platja", "Plage", "Strand"),
        "Viewpoint": T("Mirador", "Mirador", "Belvédère", "Uitzichtpunt"),
        "High path": T("Camino alto", "Camí alt", "Chemin haut", "Hoog pad"),
        "Village lanes": T("Calles del pueblo", "Carrers del poble",
                           "Ruelles du village", "Dorpsstraatjes"),
        "Tamariu Chalet — head downhill towards the village": T(
            "Tamariu Chalet — baje hacia el pueblo",
            "Tamariu Chalet — baixeu cap al poble",
            "Tamariu Chalet — descendez vers le village",
            "Tamariu Chalet — loop omlaag richting het dorp"),
        "Quiet shaded lanes wind down through the village": T(
            "Calles tranquilas y sombreadas bajan serpenteando por el pueblo",
            "Carrers tranquils i ombrejats baixen serpentejant pel poble",
            "Des ruelles calmes et ombragées descendent en serpentant dans le village",
            "Rustige, schaduwrijke straatjes kronkelen omlaag door het dorp"),
        "Tamariu Beach — time for a swim or lunch!": T(
            "Playa de Tamariu — ¡hora de un baño o de comer!",
            "Platja de Tamariu — hora d'un bany o de dinar!",
            "Plage de Tamariu — l'heure de la baignade ou du déjeuner !",
            "Strand van Tamariu — tijd voor een duik of de lunch!"),
        "A pause here gives lovely views over the bay": T(
            "Una parada aquí regala unas vistas preciosas de la bahía",
            "Una parada aquí regala unes vistes precioses de la badia",
            "Une pause ici offre de très belles vues sur la baie",
            "Even pauzeren hier geeft een prachtig uitzicht over de baai"),
        "The return route climbs gently above the bay": T(
            "La vuelta sube suavemente por encima de la bahía",
            "La tornada puja suaument per damunt de la badia",
            "Le retour grimpe doucement au-dessus de la baie",
            "De terugweg klimt geleidelijk boven de baai uit"),
        "Back to Tamariu Chalet": T(
            "De vuelta a Tamariu Chalet", "De tornada a Tamariu Chalet",
            "Retour au Tamariu Chalet", "Terug bij Tamariu Chalet"),
    },
}
