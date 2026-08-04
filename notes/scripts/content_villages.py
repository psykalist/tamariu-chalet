#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translations for things-to-do/villages-tour.html.

Strings mode: the English markup is the single source and only the words are
per language. Village names, place names, festival names, distances and drive
times are deliberately left out of the table, so they stay unchanged in every
language.
"""

from content_things_to_do import FOOTER_STD

PAGES = {}


def T(es, ca, fr, nl):
    return {"es": es, "ca": ca, "fr": fr, "nl": nl}


PAGES["things-to-do/villages-tour.html"] = {
    "mode": "strings",
    "footer": FOOTER_STD,
    "meta": {
        "es": {"title": "Ruta de los Pueblos Medievales — Tamariu Chalet",
               "desc": "Ruta autoguiada por seis pueblos medievales cerca de Tamariu Chalet — Begur, Pals, Palau-sator, Peratallada, Ullastret y Monells. Rutas, aparcamiento, qué ver, cafés, restaurantes y fiestas."},
        "ca": {"title": "Ruta dels Pobles Medievals — Tamariu Chalet",
               "desc": "Ruta autoguiada per sis pobles medievals a prop de Tamariu Chalet — Begur, Pals, Palau-sator, Peratallada, Ullastret i Monells. Rutes, aparcament, què veure, cafès, restaurants i festes."},
        "fr": {"title": "Circuit des Villages Médiévaux — Tamariu Chalet",
               "desc": "Circuit en autonomie de six villages médiévaux près du Tamariu Chalet — Begur, Pals, Palau-sator, Peratallada, Ullastret et Monells. Itinéraires, stationnement, à voir, cafés, restaurants et fêtes."},
        "nl": {"title": "Route langs de Middeleeuwse Dorpen — Tamariu Chalet",
               "desc": "Zelfstandige route langs zes middeleeuwse dorpen bij Tamariu Chalet — Begur, Pals, Palau-sator, Peratallada, Ullastret en Monells. Routes, parkeren, bezienswaardigheden, cafés, restaurants en feesten."},
    },
    "strings": {
        # ── Breadcrumb & title ──────────────────────────────────────────────
        "Things To Do → Villages Tour": T(
            "Qué Hacer → Ruta de los Pueblos", "Què Fer → Ruta dels Pobles",
            "À Faire → Circuit des Villages", "Wat Te Doen → Dorpenroute"),
        "A Tour of the Medieval Villages": T(
            "Una ruta por los pueblos medievales", "Una ruta pels pobles medievals",
            "Un circuit à travers les villages médiévaux", "Een route langs de middeleeuwse dorpen"),

        # ── Image captions ──────────────────────────────────────────────────
        "Begur and its hilltop castle, seen from above": T(
            "Begur y su castillo en lo alto, vistos desde arriba",
            "Begur i el seu castell dalt del turó, vistos des de dalt",
            "Begur et son château perché, vus d'en haut",
            "Begur en zijn kasteel op de heuvel, van bovenaf gezien"),
        "Pals rising above the Empordà rice fields": T(
            "Pals alzándose sobre los arrozales del Empordà",
            "Pals alçant-se sobre els arrossars de l'Empordà",
            "Pals dominant les rizières de l'Empordà",
            "Pals boven de rijstvelden van de Empordà"),
        "The tower and stone lanes of Palau-sator": T(
            "La torre y las callejuelas de piedra de Palau-sator",
            "La torre i els carrerons de pedra de Palau-sator",
            "La tour et les ruelles de pierre de Palau-sator",
            "De toren en stenen steegjes van Palau-sator"),
        "The rock-cut lanes and castle of Peratallada": T(
            "Las callejuelas excavadas en la roca y el castillo de Peratallada",
            "Els carrerons excavats a la roca i el castell de Peratallada",
            "Les ruelles taillées dans la roche et le château de Peratallada",
            "De in de rots uitgehakte steegjes en het kasteel van Peratallada"),
        "The fortified old quarter of Ullastret": T(
            "El casco antiguo fortificado de Ullastret",
            "El nucli antic fortificat d'Ullastret",
            "Le vieux quartier fortifié d'Ullastret",
            "De versterkte oude wijk van Ullastret"),
        "Plaça Jaume I, the arcaded square of Monells": T(
            "La Plaça Jaume I, la plaza porticada de Monells",
            "La Plaça Jaume I, la plaça porxada de Monells",
            "La Plaça Jaume I, la place à arcades de Monells",
            "Plaça Jaume I, het plein met arcades van Monells"),

        # ── Intro ───────────────────────────────────────────────────────────
        "Some of the most beautiful medieval villages in Catalonia sit on the plain just inland from Tamariu, close enough to string several together in a single, unhurried day. This self-guided tour runs as a natural loop — Begur, Pals, Palau-sator, Peratallada, Ullastret and Monells — with the driving time, parking, sights, and the best places for a coffee or a long lunch for each one.": T(
            "Algunos de los pueblos medievales más bonitos de Cataluña se encuentran en la llanura justo tierra adentro de Tamariu, lo bastante cerca como para enlazar varios en un solo día sin prisas. Esta ruta autoguiada forma un recorrido circular natural — Begur, Pals, Palau-sator, Peratallada, Ullastret y Monells — con el tiempo en coche, el aparcamiento, los lugares de interés y los mejores sitios para un café o un almuerzo largo en cada uno.",
            "Alguns dels pobles medievals més bonics de Catalunya es troben a la plana just terra endins de Tamariu, prou a prop com per enllaçar-ne uns quants en un sol dia sense presses. Aquesta ruta autoguiada forma un recorregut circular natural — Begur, Pals, Palau-sator, Peratallada, Ullastret i Monells — amb el temps en cotxe, l'aparcament, els llocs d'interès i els millors indrets per a un cafè o un dinar tranquil a cadascun.",
            "Parmi les plus beaux villages médiévaux de Catalogne, plusieurs se trouvent dans la plaine juste à l'intérieur des terres depuis Tamariu, assez proches pour en enchaîner plusieurs en une seule journée, sans se presser. Ce circuit en autonomie forme une boucle naturelle — Begur, Pals, Palau-sator, Peratallada, Ullastret et Monells — avec, pour chacun, le temps de route, le stationnement, les curiosités et les meilleures adresses pour un café ou un long déjeuner.",
            "Enkele van de mooiste middeleeuwse dorpen van Catalonië liggen op de vlakte net landinwaarts van Tamariu, dicht genoeg bij elkaar om er in één ontspannen dag meerdere aaneen te rijgen. Deze zelfstandige route vormt een natuurlijke lus — Begur, Pals, Palau-sator, Peratallada, Ullastret en Monells — met voor elk dorp de rijtijd, het parkeren, de bezienswaardigheden en de beste plekken voor een koffie of een lange lunch."),
        "A few practical notes. All the driving times below are approximate and measured by car from the chalet; add a little in July and August when the roads and car parks are busiest. The historic centre of each village is pedestrianised, so the pattern is always the same: park at the edge and walk in. Village car parks are generally free out of season and charged (a barrier ticket or a blue-bay meter) from roughly July to early September. Mornings are cool and quiet for wandering the lanes; the light in late afternoon is lovely for photographs.": T(
            "Unas notas prácticas. Todos los tiempos en coche que figuran abajo son aproximados y se miden desde el chalet; añada un poco en julio y agosto, cuando las carreteras y los aparcamientos están más concurridos. El centro histórico de cada pueblo es peatonal, así que la pauta es siempre la misma: aparcar en las afueras y entrar andando. Los aparcamientos de los pueblos suelen ser gratuitos fuera de temporada y de pago (con barrera o parquímetro de zona azul) desde aproximadamente julio hasta principios de septiembre. Las mañanas son frescas y tranquilas para pasear por las callejuelas; la luz de última hora de la tarde es preciosa para las fotos.",
            "Unes notes pràctiques. Tots els temps en cotxe que figuren a sota són aproximats i es mesuren des del xalet; afegiu-hi una mica al juliol i a l'agost, quan les carreteres i els aparcaments estan més concorreguts. El centre històric de cada poble és per als vianants, així que la pauta és sempre la mateixa: aparcar a fora i entrar-hi a peu. Els aparcaments dels pobles solen ser gratuïts fora de temporada i de pagament (amb barrera o parquímetre de zona blava) des d'aproximadament el juliol fins a principis de setembre. Els matins són frescos i tranquils per passejar pels carrerons; la llum de mitja tarda és preciosa per a les fotografies.",
            "Quelques remarques pratiques. Tous les temps de route ci-dessous sont approximatifs et mesurés en voiture depuis le chalet ; comptez un peu plus en juillet et août, quand les routes et les parkings sont les plus fréquentés. Le centre historique de chaque village est piéton : le principe est donc toujours le même, se garer à l'entrée et continuer à pied. Les parkings des villages sont en général gratuits hors saison et payants (barrière ou horodateur en zone bleue) de juillet à début septembre environ. Les matinées sont fraîches et calmes pour flâner dans les ruelles ; la lumière de fin d'après-midi est superbe pour les photos.",
            "Enkele praktische opmerkingen. Alle rijtijden hieronder zijn bij benadering en gemeten met de auto vanaf het chalet; tel er in juli en augustus wat bij op, wanneer de wegen en parkeerplaatsen het drukst zijn. Het historische centrum van elk dorp is autovrij, dus het patroon is altijd hetzelfde: parkeer aan de rand en loop naar binnen. De dorpsparkeerplaatsen zijn buiten het seizoen doorgaans gratis en betaald (een slagboomticket of een meter in de blauwe zone) van ongeveer juli tot begin september. De ochtenden zijn koel en rustig om door de steegjes te dwalen; het licht in de late namiddag is prachtig voor foto's."),

        # ── Reused section labels ───────────────────────────────────────────
        "Getting there &amp; parking": T(
            "Cómo llegar y aparcar", "Com arribar-hi i aparcar",
            "Y aller &amp; se garer", "Ernaartoe &amp; parkeren"),
        "What to see": T("Qué ver", "Què veure", "À voir", "Wat te zien"),
        "Coffee &amp; lunch": T(
            "Café y almuerzo", "Cafè i dinar", "Café &amp; déjeuner", "Koffie &amp; lunch"),
        "Festivals": T("Fiestas", "Festes", "Fêtes", "Feesten"),
        "Drive from Tamariu": T(
            "En coche desde Tamariu", "En cotxe des de Tamariu",
            "En voiture depuis Tamariu", "Rijden vanaf Tamariu"),
        "Distance": T("Distancia", "Distància", "Distance", "Afstand"),

        # ── Stop headers ────────────────────────────────────────────────────
        "Stop 1 — the hilltop town": T(
            "Parada 1 — el pueblo en lo alto", "Parada 1 — el poble dalt del turó",
            "Étape 1 — le village perché", "Stop 1 — het dorp op de heuvel"),
        "Stop 2 — the golden village": T(
            "Parada 2 — el pueblo dorado", "Parada 2 — el poble daurat",
            "Étape 2 — le village doré", "Stop 2 — het gouden dorp"),
        "Stop 3 — the quiet hamlets": T(
            "Parada 3 — las aldeas tranquilas", "Parada 3 — els llogarets tranquils",
            "Étape 3 — les hameaux paisibles", "Stop 3 — de stille gehuchten"),
        "Stop 4 — the fairytale village": T(
            "Parada 4 — el pueblo de cuento", "Parada 4 — el poble de conte",
            "Étape 4 — le village de conte de fées", "Stop 4 — het sprookjesdorp"),
        "Stop 5 — the ancient one": T(
            "Parada 5 — el más antiguo", "Parada 5 — el més antic",
            "Étape 5 — le plus ancien", "Stop 5 — de aloude"),
        "Stop 6 — the film-set square": T(
            "Parada 6 — la plaza de película", "Parada 6 — la plaça de pel·lícula",
            "Étape 6 — la place de cinéma", "Stop 6 — het filmplein"),

        # ── Begur ───────────────────────────────────────────────────────────
        "A hilltop town crowned by a ruined castle, famous for its grand \"Indianos\" mansions — showy houses built by locals who made their fortunes in nineteenth-century Cuba and returned home to build them.": T(
            "Un pueblo en lo alto coronado por un castillo en ruinas, célebre por sus grandes casas de \"indianos\" — mansiones ostentosas que construyeron los vecinos que hicieron fortuna en la Cuba del siglo XIX y regresaron a casa para levantarlas.",
            "Un poble dalt d'un turó coronat per un castell en ruïnes, cèlebre per les seves grans cases d'\"indians\" — mansions ostentoses que van construir els veïns que van fer fortuna a la Cuba del segle XIX i van tornar a casa per aixecar-les.",
            "Un village perché couronné par un château en ruine, célèbre pour ses grandes demeures d'« Indianos » — des maisons ostentatoires bâties par des habitants ayant fait fortune à Cuba au XIXe siècle avant de rentrer les construire.",
            "Een dorp op een heuvel, bekroond door een kasteelruïne en beroemd om zijn grote \"Indianos\"-huizen — opzichtige villa's, gebouwd door dorpelingen die in het negentiende-eeuwse Cuba fortuin maakten en terugkeerden om ze neer te zetten."),
        "The easy route runs inland through Palafrugell and Esclanyà, then up into Begur. The streets in the centre are narrow and steep, so use the car parks and blue metered bays on the edge of town; parking is only charged in July, August and early September. If the town is full, the car park on the road down to Sa Riera is a short walk back up.": T(
            "La ruta más fácil va tierra adentro por Palafrugell y Esclanyà, y luego sube a Begur. Las calles del centro son estrechas y empinadas, así que use los aparcamientos y las zonas azules de las afueras; solo se paga en julio, agosto y principios de septiembre. Si el pueblo está lleno, el aparcamiento de la carretera que baja a Sa Riera queda a un corto paseo cuesta arriba.",
            "La ruta més fàcil va terra endins per Palafrugell i Esclanyà, i després puja a Begur. Els carrers del centre són estrets i costeruts, així que feu servir els aparcaments i les zones blaves de fora; només es paga al juliol, agost i principis de setembre. Si el poble és ple, l'aparcament de la carretera que baixa a Sa Riera queda a un curt passeig costa amunt.",
            "L'itinéraire le plus simple passe par l'intérieur des terres via Palafrugell et Esclanyà, puis monte vers Begur. Les rues du centre sont étroites et pentues : utilisez les parkings et les places payantes en zone bleue en périphérie ; le stationnement n'est payant qu'en juillet, août et début septembre. Si le village est complet, le parking sur la route qui descend vers Sa Riera n'est qu'à quelques minutes de marche en remontant.",
            "De makkelijkste route loopt landinwaarts via Palafrugell en Esclanyà en dan omhoog naar Begur. De straten in het centrum zijn smal en steil, dus gebruik de parkeerterreinen en de blauwe zones aan de rand van het dorp; parkeren kost alleen in juli, augustus en begin september geld. Is het dorp vol, dan ligt de parkeerplaats aan de weg omlaag naar Sa Riera op een korte wandeling terug omhoog."),
        "The castle ruins above the town, for sweeping views over the coast": T(
            "Las ruinas del castillo sobre el pueblo, con amplias vistas de la costa",
            "Les ruïnes del castell sobre el poble, amb àmplies vistes de la costa",
            "Les ruines du château au-dessus du village, pour de vastes vues sur la côte",
            "De kasteelruïne boven het dorp, met weidse uitzichten over de kust"),
        "The grand Indianos mansions along the old streets": T(
            "Las grandes casas de indianos por las calles antiguas",
            "Les grans cases d'indians pels carrers antics",
            "Les grandes demeures d'Indianos le long des vieilles rues",
            "De grote Indianos-villa's langs de oude straten"),
        "The medieval watchtowers dotted around the old quarter": T(
            "Las torres de vigía medievales repartidas por el casco antiguo",
            "Les torres de guaita medievals repartides pel nucli antic",
            "Les tours de guet médiévales dispersées dans la vieille ville",
            "De middeleeuwse wachttorens verspreid door de oude wijk"),
        "The nearby coves of Sa Tuna and Sa Riera for a swim": T(
            "Las calas cercanas de Sa Tuna y Sa Riera para darse un baño",
            "Les cales properes de Sa Tuna i Sa Riera per fer un bany",
            "Les criques voisines de Sa Tuna et Sa Riera pour une baignade",
            "De nabijgelegen baaien Sa Tuna en Sa Riera voor een duik"),
        "The terraces around Plaça de la Vila and Plaça Esteve i Cruañas are the place for a mid-morning coffee under the plane trees. For lunch there is plenty of choice in the centre, from Catalan tavernas to modern Mediterranean cooking; in summer the beach restaurants at Sa Riera and Sa Tuna make a fine seaside alternative.": T(
            "Las terrazas de la Plaça de la Vila y la Plaça Esteve i Cruañas son el sitio para un café a media mañana bajo los plátanos. Para almorzar hay mucho donde elegir en el centro, desde tabernas catalanas hasta cocina mediterránea moderna; en verano, los restaurantes de playa de Sa Riera y Sa Tuna son una buena alternativa junto al mar.",
            "Les terrasses de la Plaça de la Vila i la Plaça Esteve i Cruañas són el lloc per a un cafè a mig matí sota els plàtans. Per dinar hi ha molt on triar al centre, des de tavernes catalanes fins a cuina mediterrània moderna; a l'estiu, els restaurants de platja de Sa Riera i Sa Tuna són una bona alternativa vora el mar.",
            "Les terrasses de la Plaça de la Vila et de la Plaça Esteve i Cruañas sont l'endroit idéal pour un café en milieu de matinée sous les platanes. Pour le déjeuner, le choix est large dans le centre, des tavernes catalanes à la cuisine méditerranéenne moderne ; en été, les restaurants de plage de Sa Riera et Sa Tuna offrent une belle alternative en bord de mer.",
            "De terrassen rond de Plaça de la Vila en de Plaça Esteve i Cruañas zijn dé plek voor een koffie halverwege de ochtend onder de platanen. Voor de lunch is er in het centrum volop keuze, van Catalaanse taverna's tot moderne mediterrane keuken; in de zomer vormen de strandrestaurants van Sa Riera en Sa Tuna een mooi alternatief aan zee."),
        "The Fira d'Indians, on the first weekend of September, is the big one — the town relives its Cuban connection with an overseas-produce market, Havanera singing and Caribbean music. In August there are open-air Havaneres gatherings in the square and down on Sa Riera beach.": T(
            "La Fira d'Indians, el primer fin de semana de septiembre, es la grande — el pueblo revive su vínculo cubano con un mercado de productos de ultramar, cantos de habaneras y música caribeña. En agosto hay encuentros de habaneras al aire libre en la plaza y en la playa de Sa Riera.",
            "La Fira d'Indians, el primer cap de setmana de setembre, és la gran — el poble reviu el seu vincle cubà amb un mercat de productes d'ultramar, cants d'havaneres i música caribenya. A l'agost hi ha trobades d'havaneres a l'aire lliure a la plaça i a la platja de Sa Riera.",
            "La Fira d'Indians, le premier week-end de septembre, est le grand rendez-vous — le village fait revivre son lien avec Cuba par un marché de produits d'outre-mer, des chants de havaneres et de la musique caribéenne. En août, des rassemblements de havaneres en plein air ont lieu sur la place et sur la plage de Sa Riera.",
            "De Fira d'Indians, het eerste weekend van september, is de grote — het dorp herbeleeft zijn Cubaanse band met een markt van overzeese producten, havanera-zang en Caribische muziek. In augustus zijn er openluchtbijeenkomsten met havaneres op het plein en op het strand van Sa Riera."),

        # ── Pals ────────────────────────────────────────────────────────────
        "A beautifully restored medieval quarter of honey-coloured stone, ringed by rice fields, with a Gothic tower and viewpoints that reach across the plain to the sea.": T(
            "Un barrio medieval magníficamente restaurado, de piedra color miel, rodeado de arrozales, con una torre gótica y miradores que se extienden por la llanura hasta el mar.",
            "Un barri medieval magníficament restaurat, de pedra color mel, envoltat d'arrossars, amb una torre gòtica i miradors que s'estenen per la plana fins al mar.",
            "Un quartier médiéval superbement restauré, en pierre couleur miel, entouré de rizières, avec une tour gothique et des belvédères qui portent le regard à travers la plaine jusqu'à la mer.",
            "Een prachtig gerestaureerde middeleeuwse wijk van honingkleurige steen, omringd door rijstvelden, met een gotische toren en uitzichtpunten die over de vlakte tot aan zee reiken."),
        "Leave the car in the free car parks below the old town, near the Torre de les Hores, then walk up into El Pedró, the historic centre. It gets busy in August, so it pays to arrive earlier in the day.": T(
            "Deje el coche en los aparcamientos gratuitos bajo el casco antiguo, cerca de la Torre de les Hores, y suba andando a El Pedró, el centro histórico. En agosto se llena, así que conviene llegar a primera hora.",
            "Deixeu el cotxe als aparcaments gratuïts sota el nucli antic, a prop de la Torre de les Hores, i pugeu a peu a El Pedró, el centre històric. A l'agost s'omple, així que val la pena arribar-hi d'hora.",
            "Laissez la voiture dans les parkings gratuits en contrebas de la vieille ville, près de la Torre de les Hores, puis montez à pied jusqu'à El Pedró, le centre historique. Il y a foule en août : mieux vaut arriver tôt.",
            "Zet de auto op de gratis parkeerplaatsen onder de oude stad, bij de Torre de les Hores, en loop omhoog naar El Pedró, het historische centrum. In augustus is het druk, dus het loont om vroeg te komen."),
        "El Pedró, the walled medieval quarter of stone lanes": T(
            "El Pedró, el barrio medieval amurallado de callejuelas de piedra",
            "El Pedró, el barri medieval emmurallat de carrerons de pedra",
            "El Pedró, le quartier médiéval fortifié aux ruelles de pierre",
            "El Pedró, de ommuurde middeleeuwse wijk met stenen steegjes"),
        "The Torre de les Hores, the village clock tower": T(
            "La Torre de les Hores, la torre del reloj del pueblo",
            "La Torre de les Hores, la torre del rellotge del poble",
            "La Torre de les Hores, la tour de l'horloge du village",
            "De Torre de les Hores, de klokkentoren van het dorp"),
        "The Mirador Josep Pla viewpoint over the rice fields": T(
            "El Mirador Josep Pla sobre los arrozales",
            "El Mirador Josep Pla sobre els arrossars",
            "Le belvédère Josep Pla sur les rizières",
            "Het uitzichtpunt Mirador Josep Pla over de rijstvelden"),
        "The craft and pottery shops tucked into the old houses": T(
            "Las tiendas de artesanía y cerámica escondidas en las casas antiguas",
            "Les botigues d'artesania i ceràmica amagades a les cases antigues",
            "Les boutiques d'artisanat et de poterie nichées dans les vieilles maisons",
            "De ambachts- en aardewerkwinkeltjes verscholen in de oude huizen"),
        "Café terraces cluster among the squares of the old town — pick one with a view down the valley. For lunch, Es Portal and Sol Blanc are both excellent, and La Vila serves traditional Catalan cooking; the local rice dishes are the thing to order here.": T(
            "Las terrazas de los cafés se agrupan en las plazas del casco antiguo — elija una con vistas al valle. Para almorzar, Es Portal y Sol Blanc son excelentes, y La Vila sirve cocina catalana tradicional; aquí lo que hay que pedir son los arroces de la zona.",
            "Les terrasses dels cafès s'apleguen a les places del nucli antic — trieu-ne una amb vistes a la vall. Per dinar, Es Portal i Sol Blanc són excel·lents, i La Vila serveix cuina catalana tradicional; aquí el que cal demanar són els arrossos de la zona.",
            "Les terrasses de café se regroupent sur les places de la vieille ville — choisissez-en une avec vue sur la vallée. Pour déjeuner, Es Portal et Sol Blanc sont tous deux excellents, et La Vila propose une cuisine catalane traditionnelle ; ici, ce sont les riz de la région qu'il faut commander.",
            "De caféterrassen scholen samen op de pleinen van de oude stad — kies er een met uitzicht over de vallei. Voor de lunch zijn Es Portal en Sol Blanc allebei uitstekend, en La Vila serveert traditionele Catalaanse gerechten; hier moet je de plaatselijke rijstgerechten bestellen."),
        "The Festa Major, in early August, fills the village with concerts, dancing and processions. In autumn the Fira de l'Arròs celebrates the local rice harvest with tastings and cultural events, and a wine, cava and cheese fair is held in the courtyard of Ca La Pruna.": T(
            "La Festa Major, a principios de agosto, llena el pueblo de conciertos, bailes y procesiones. En otoño, la Fira de l'Arròs celebra la cosecha local de arroz con degustaciones y actos culturales, y en el patio de Ca La Pruna se celebra una feria del vino, el cava y el queso.",
            "La Festa Major, a principis d'agost, omple el poble de concerts, balls i processons. A la tardor, la Fira de l'Arròs celebra la collita local d'arròs amb degustacions i actes culturals, i al pati de Ca La Pruna s'hi fa una fira del vi, el cava i el formatge.",
            "La Festa Major, début août, remplit le village de concerts, de danses et de processions. En automne, la Fira de l'Arròs célèbre la récolte locale du riz avec dégustations et animations culturelles, et une foire aux vins, cava et fromages se tient dans la cour de Ca La Pruna.",
            "De Festa Major, begin augustus, vult het dorp met concerten, dans en processies. In de herfst viert de Fira de l'Arròs de plaatselijke rijstoogst met proeverijen en culturele evenementen, en op de binnenplaats van Ca La Pruna wordt een wijn-, cava- en kaasbeurs gehouden."),

        # ── Palau-sator ─────────────────────────────────────────────────────
        "A tiny fortified village with a defensive tower, at the centre of a cluster of sleepy hamlets and known for its good country cooking.": T(
            "Un diminuto pueblo fortificado con una torre defensiva, en el centro de un grupo de aldeas apacibles y conocido por su buena cocina de payés.",
            "Un diminut poble fortificat amb una torre de defensa, al centre d'un grup de llogarets tranquils i conegut per la seva bona cuina de pagès.",
            "Un tout petit village fortifié doté d'une tour défensive, au cœur d'un ensemble de hameaux paisibles et réputé pour sa bonne cuisine du terroir.",
            "Een piepklein versterkt dorp met een verdedigingstoren, in het midden van een groepje slaperige gehuchten en bekend om zijn goede boerenkeuken."),
        "The lanes here are small and low-key. Park on the edge of the village by the road and walk in — rarely a problem outside the busiest weekends.": T(
            "Aquí las calles son estrechas y discretas. Aparque a la entrada del pueblo junto a la carretera y entre andando — rara vez es un problema salvo los fines de semana más concurridos.",
            "Aquí els carrers són estrets i discrets. Aparqueu a l'entrada del poble vora la carretera i entreu-hi a peu — poques vegades és un problema, tret dels caps de setmana més concorreguts.",
            "Ici, les ruelles sont étroites et discrètes. Garez-vous à l'entrée du village, le long de la route, et continuez à pied — rarement un problème en dehors des week-ends de forte affluence.",
            "De straatjes hier zijn smal en ingetogen. Parkeer aan de rand van het dorp langs de weg en loop naar binnen — buiten de drukste weekends zelden een probleem."),
        "The medieval gate tower and fortified core of the village": T(
            "La torre-portal medieval y el núcleo fortificado del pueblo",
            "La torre-portal medieval i el nucli fortificat del poble",
            "La tour-porte médiévale et le cœur fortifié du village",
            "De middeleeuwse poorttoren en de versterkte kern van het dorp"),
        "Sant Julià de Boada, one of Catalonia's oldest little churches": T(
            "Sant Julià de Boada, una de las iglesias pequeñas más antiguas de Cataluña",
            "Sant Julià de Boada, una de les esglésies petites més antigues de Catalunya",
            "Sant Julià de Boada, l'une des plus anciennes petites églises de Catalogne",
            "Sant Julià de Boada, een van de oudste kerkjes van Catalonië"),
        "Sant Feliu de Boada, a pretty stone hamlet with a fortified Gothic church": T(
            "Sant Feliu de Boada, una bonita aldea de piedra con una iglesia gótica fortificada",
            "Sant Feliu de Boada, un bonic llogaret de pedra amb una església gòtica fortificada",
            "Sant Feliu de Boada, un joli hameau de pierre doté d'une église gothique fortifiée",
            "Sant Feliu de Boada, een fraai stenen gehucht met een versterkte gotische kerk"),
        "This is a quiet corner, and the village restaurant terraces double as the coffee stop — part of the charm is how untouched it feels. For lunch the hamlets punch above their weight: Can Bach, in an eighteenth-century farmhouse, and Can Joan in Sant Feliu de Boada are both strong on traditional Empordà home cooking.": T(
            "Es un rincón tranquilo, y las terrazas de los restaurantes del pueblo hacen también de parada para el café — parte de su encanto está en lo poco alterado que se siente. Para almorzar, las aldeas rinden más de lo que parece: Can Bach, en una masía del siglo XVIII, y Can Joan, en Sant Feliu de Boada, destacan por su cocina casera tradicional del Empordà.",
            "És un racó tranquil, i les terrasses dels restaurants del poble fan també de parada per al cafè — part del seu encant està en com de poc alterat se sent. Per dinar, els llogarets ret més del que sembla: Can Bach, en una masia del segle XVIII, i Can Joan, a Sant Feliu de Boada, destaquen per la seva cuina casolana tradicional de l'Empordà.",
            "C'est un coin tranquille, et les terrasses des restaurants du village font aussi office de pause-café — une partie du charme tient à ce sentiment de lieu préservé. Pour le déjeuner, les hameaux valent bien mieux que leur taille : Can Bach, dans un mas du XVIIIe siècle, et Can Joan, à Sant Feliu de Boada, brillent par leur cuisine familiale traditionnelle de l'Empordà.",
            "Dit is een rustig hoekje, en de restaurantterrassen van het dorp doen tegelijk dienst als koffiestop — een deel van de charme zit in hoe onaangetast het aanvoelt. Voor de lunch presteren de gehuchten boven verwachting: Can Bach, in een achttiende-eeuwse boerderij, en Can Joan in Sant Feliu de Boada blinken allebei uit in traditionele huiselijke Empordà-keuken."),
        "The village keeps a traditional summer Festa Major in August — a low-key local affair of music and communal meals rather than the big medieval fairs of its neighbours.": T(
            "El pueblo mantiene una Festa Major de verano tradicional en agosto — un acontecimiento local sencillo, de música y comidas populares, más que las grandes ferias medievales de sus vecinos.",
            "El poble manté una Festa Major d'estiu tradicional a l'agost — un esdeveniment local senzill, de música i àpats populars, més que no pas les grans fires medievals dels seus veïns.",
            "Le village conserve une Festa Major estivale traditionnelle en août — un événement local sans prétention, fait de musique et de repas partagés, loin des grandes foires médiévales de ses voisins.",
            "Het dorp houdt in augustus een traditionele zomerse Festa Major — een ingetogen plaatselijk feest van muziek en gezamenlijke maaltijden, geen grote middeleeuwse markten zoals bij de buren."),

        # ── Peratallada ─────────────────────────────────────────────────────
        "Perhaps the most spectacular of them all — a village carved out of the rock, with a moat, a castle, an arcaded square and a maze of cobbled lanes.": T(
            "Quizá el más espectacular de todos — un pueblo excavado en la roca, con foso, castillo, una plaza porticada y un laberinto de callejuelas empedradas.",
            "Potser el més espectacular de tots — un poble excavat a la roca, amb fossat, castell, una plaça porxada i un laberint de carrerons empedrats.",
            "Peut-être le plus spectaculaire de tous — un village taillé dans la roche, avec des douves, un château, une place à arcades et un dédale de ruelles pavées.",
            "Misschien wel het meest spectaculaire van allemaal — een dorp uitgehakt in de rots, met een slotgracht, een kasteel, een plein met arcades en een doolhof van geplaveide steegjes."),
        "Three car parks ring the village; they are paid in summer and at weekends, and free in the quieter months. Park and walk the last few minutes into the centre.": T(
            "Tres aparcamientos rodean el pueblo; son de pago en verano y los fines de semana, y gratuitos en los meses más tranquilos. Aparque y recorra a pie los últimos minutos hasta el centro.",
            "Tres aparcaments envolten el poble; són de pagament a l'estiu i els caps de setmana, i gratuïts els mesos més tranquils. Aparqueu i feu a peu els darrers minuts fins al centre.",
            "Trois parkings entourent le village ; ils sont payants en été et le week-end, gratuits pendant les mois plus calmes. Garez-vous et parcourez à pied les dernières minutes jusqu'au centre.",
            "Drie parkeerterreinen omringen het dorp; ze zijn betaald in de zomer en in het weekend, en gratis in de rustigere maanden. Parkeer en loop de laatste paar minuten naar het centrum."),
        "The rock-cut moat and the castle at the heart of the village": T(
            "El foso excavado en la roca y el castillo en el corazón del pueblo",
            "El fossat excavat a la roca i el castell al cor del poble",
            "Les douves taillées dans la roche et le château au cœur du village",
            "De in de rots uitgehakte slotgracht en het kasteel in het hart van het dorp"),
        "Plaça de les Voltes, the arcaded main square": T(
            "La Plaça de les Voltes, la plaza mayor porticada",
            "La Plaça de les Voltes, la plaça major porxada",
            "La Plaça de les Voltes, la place principale à arcades",
            "Plaça de les Voltes, het hoofdplein met arcades"),
        "The clock tower, which you can climb free of charge for views to the Medes Islands": T(
            "La torre del reloj, que se puede subir gratis para ver las islas Medes",
            "La torre del rellotge, que es pot pujar gratis per veure les illes Medes",
            "La tour de l'horloge, que l'on peut gravir gratuitement pour la vue sur les îles Medes",
            "De klokkentoren, die je gratis kunt beklimmen voor uitzicht op de Medes-eilanden"),
        "Sant Esteve, the thirteenth-century Romanesque church just outside the walls": T(
            "Sant Esteve, la iglesia románica del siglo XIII justo fuera de las murallas",
            "Sant Esteve, l'església romànica del segle XIII just fora de les muralles",
            "Sant Esteve, l'église romane du XIIIe siècle juste à l'extérieur des remparts",
            "Sant Esteve, de dertiende-eeuwse romaanse kerk net buiten de muren"),
        "Carrer Major and its craft shops": T(
            "El Carrer Major y sus tiendas de artesanía",
            "El Carrer Major i les seves botigues d'artesania",
            "Le Carrer Major et ses boutiques d'artisanat",
            "Carrer Major en zijn ambachtswinkels"),
        "A vermouth or a coffee at Bar del Castell comes with a view of the castle, and the terraces under the arches of Plaça de les Voltes are the classic spot. For lunch, look out for arròs a la cassola, the casserole rice that is the local dish to try here.": T(
            "Un vermut o un café en el Bar del Castell vienen con vistas al castillo, y las terrazas bajo los arcos de la Plaça de les Voltes son el clásico. Para almorzar, busque el arròs a la cassola, el arroz de cazuela que es el plato local que hay que probar aquí.",
            "Un vermut o un cafè al Bar del Castell vénen amb vistes al castell, i les terrasses sota els arcs de la Plaça de les Voltes són el clàssic. Per dinar, busqueu l'arròs a la cassola, l'arròs de cassola que és el plat local que cal tastar aquí.",
            "Un vermouth ou un café au Bar del Castell s'accompagne d'une vue sur le château, et les terrasses sous les arcades de la Plaça de les Voltes sont l'adresse classique. Pour déjeuner, cherchez l'arròs a la cassola, le riz en cocotte, plat local à goûter ici.",
            "Een vermout of een koffie in Bar del Castell komt met uitzicht op het kasteel, en de terrassen onder de bogen van de Plaça de les Voltes zijn de klassieke plek. Zoek voor de lunch naar arròs a la cassola, de rijstschotel uit de pan die je hier moet proberen."),
        "The Fira Medieval de Peratallada, on the first weekend of October, turns the whole old town into a medieval market of jesters, craftsmen and costumed characters — one of the best in the region.": T(
            "La Fira Medieval de Peratallada, el primer fin de semana de octubre, convierte todo el casco antiguo en un mercado medieval de bufones, artesanos y personajes disfrazados — una de las mejores de la comarca.",
            "La Fira Medieval de Peratallada, el primer cap de setmana d'octubre, converteix tot el nucli antic en un mercat medieval de bufons, artesans i personatges disfressats — una de les millors de la comarca.",
            "La Fira Medieval de Peratallada, le premier week-end d'octobre, transforme toute la vieille ville en un marché médiéval de bouffons, d'artisans et de personnages costumés — l'une des plus belles de la région.",
            "De Fira Medieval de Peratallada, het eerste weekend van oktober, verandert de hele oude stad in een middeleeuwse markt van nar­ren, ambachtslieden en gekostumeerde figuren — een van de beste van de streek."),

        # ── Ullastret ───────────────────────────────────────────────────────
        "A walled medieval village with a remarkable bonus: on the hill just outside sits the largest Iberian settlement in Catalonia, more than two and a half thousand years old.": T(
            "Un pueblo medieval amurallado con un extra notable: en la colina justo a las afueras se alza el mayor poblado ibérico de Cataluña, de más de dos mil quinientos años.",
            "Un poble medieval emmurallat amb un extra notable: al turó just a les afores s'alça el poblat ibèric més gran de Catalunya, de més de dos mil cinc-cents anys.",
            "Un village médiéval fortifié avec un atout remarquable : sur la colline juste à la sortie se dresse le plus grand site ibère de Catalogne, vieux de plus de deux mille cinq cents ans.",
            "Een ommuurd middeleeuws dorp met een opmerkelijke bonus: op de heuvel er net buiten ligt de grootste Iberische nederzetting van Catalonië, ruim tweeënhalfduizend jaar oud."),
        "Park at the edge of the old village. The Iberian site, up the hill on the Puig de Sant Andreu, has its own car park a short drive away.": T(
            "Aparque a la entrada del pueblo antiguo. El yacimiento ibérico, en lo alto del Puig de Sant Andreu, tiene su propio aparcamiento a poca distancia en coche.",
            "Aparqueu a l'entrada del poble antic. El jaciment ibèric, dalt del Puig de Sant Andreu, té el seu propi aparcament a poca distància en cotxe.",
            "Garez-vous à l'entrée du vieux village. Le site ibère, en haut du Puig de Sant Andreu, dispose de son propre parking à quelques minutes en voiture.",
            "Parkeer aan de rand van het oude dorp. De Iberische vindplaats, boven op de Puig de Sant Andreu, heeft een eigen parkeerplaats op korte rijafstand."),
        "The Iberian settlement and its archaeology museum — the walls, houses and temples of the Indiketes people": T(
            "El poblado ibérico y su museo de arqueología — las murallas, casas y templos del pueblo indigete",
            "El poblat ibèric i el seu museu d'arqueologia — les muralles, cases i temples del poble indiget",
            "Le site ibère et son musée d'archéologie — les remparts, maisons et temples du peuple indigète",
            "De Iberische nederzetting en het archeologisch museum — de muren, huizen en tempels van het volk der Indiketen"),
        "The fortified old quarter of the village itself": T(
            "El casco antiguo fortificado del propio pueblo",
            "El nucli antic fortificat del mateix poble",
            "Le vieux quartier fortifié du village lui-même",
            "De versterkte oude wijk van het dorp zelf"),
        "The Romanesque church of Sant Pere": T(
            "La iglesia románica de Sant Pere", "L'església romànica de Sant Pere",
            "L'église romane de Sant Pere", "De romaanse kerk van Sant Pere"),
        "La Llotja, the Gothic square": T(
            "La Llotja, la plaza gótica", "La Llotja, la plaça gòtica",
            "La Llotja, la place gothique", "La Llotja, het gotische plein"),
        "A quiet village square with a bar terrace or two makes a peaceful pause after walking the ruins. A handful of restaurants in and around the village serve Empordà country cooking, which pairs well with a morning at the archaeological site.": T(
            "Una plaza tranquila con una o dos terrazas de bar es una pausa apacible tras recorrer las ruinas. Un puñado de restaurantes en el pueblo y sus alrededores sirven cocina de payés del Empordà, que combina bien con una mañana en el yacimiento.",
            "Una plaça tranquil·la amb una o dues terrasses de bar és una pausa plàcida després de recórrer les ruïnes. Un grapat de restaurants al poble i els voltants serveixen cuina de pagès de l'Empordà, que lliga bé amb un matí al jaciment.",
            "Une place de village tranquille avec une terrasse de bar ou deux offre une pause paisible après la visite des ruines. Quelques restaurants dans le village et alentour servent une cuisine du terroir de l'Empordà, qui se marie bien avec une matinée sur le site archéologique.",
            "Een rustig dorpsplein met een of twee barterrassen is een vredige pauze na een wandeling door de ruïnes. Een handvol restaurants in en rond het dorp serveert Empordà-boerenkeuken, die goed past bij een ochtend op de archeologische site."),
        "The Festa Major falls in early August, with music and local food. The Iberian site also runs popular theatrical \"living history\" visits that recreate Iberian life, with workshops and themed stalls.": T(
            "La Festa Major cae a principios de agosto, con música y comida local. El yacimiento ibérico también organiza populares visitas teatralizadas de \"historia viva\" que recrean la vida ibérica, con talleres y puestos temáticos.",
            "La Festa Major cau a principis d'agost, amb música i menjar local. El jaciment ibèric també organitza populars visites teatralitzades d'\"història viva\" que recreen la vida ibèrica, amb tallers i parades temàtiques.",
            "La Festa Major a lieu début août, avec musique et cuisine locale. Le site ibère propose aussi de populaires visites théâtralisées d'« histoire vivante » qui recréent la vie ibère, avec ateliers et stands thématiques.",
            "De Festa Major valt begin augustus, met muziek en streekgerechten. De Iberische vindplaats organiseert ook populaire theatrale \"living history\"-bezoeken die het Iberische leven naspelen, met workshops en themakraampjes."),

        # ── Monells ─────────────────────────────────────────────────────────
        "The most postcard-perfect square of the lot — a beautifully preserved arcaded plaça that has featured in Spanish films, yet stays wonderfully calm.": T(
            "La plaza más de postal de todas — una plaça porticada bellamente conservada que ha aparecido en películas españolas y, aun así, sigue maravillosamente tranquila.",
            "La plaça més de postal de totes — una plaça porxada bellament conservada que ha sortit en pel·lícules espanyoles i, tot i això, segueix meravellosament tranquil·la.",
            "La place la plus digne d'une carte postale — une plaça à arcades magnifiquement conservée, apparue dans des films espagnols et pourtant merveilleusement calme.",
            "Het meest ansichtkaartwaardige plein van allemaal — een prachtig bewaarde plaça met arcades die in Spaanse films te zien was en toch heerlijk rustig blijft."),
        "There is free parking on the edge of the village, and the centre is a short, flat walk away — usually the easiest of the six for parking.": T(
            "Hay aparcamiento gratuito a la entrada del pueblo, y el centro queda a un paseo corto y llano — normalmente el más fácil de los seis para aparcar.",
            "Hi ha aparcament gratuït a l'entrada del poble, i el centre queda a un passeig curt i pla — normalment el més fàcil dels sis per aparcar.",
            "Il y a un parking gratuit à l'entrée du village, et le centre est à quelques minutes de marche à plat — en général le plus facile des six pour se garer.",
            "Er is gratis parkeren aan de rand van het dorp, en het centrum ligt op een korte, vlakke wandeling — meestal het makkelijkste van de zes om te parkeren."),
        "Plaça Jaume I, the arcaded medieval square": T(
            "La Plaça Jaume I, la plaza medieval porticada",
            "La Plaça Jaume I, la plaça medieval porxada",
            "La Plaça Jaume I, la place médiévale à arcades",
            "Plaça Jaume I, het middeleeuwse plein met arcades"),
        "The stone archways, gates and old streets around it": T(
            "Los arcos de piedra, los portales y las calles antiguas de alrededor",
            "Els arcs de pedra, els portals i els carrers antics del voltant",
            "Les arches de pierre, les portes et les vieilles rues alentour",
            "De stenen bogen, poorten en oude straten eromheen"),
        "The church of Sant Genís": T(
            "La iglesia de Sant Genís", "L'església de Sant Genís",
            "L'église de Sant Genís", "De kerk van Sant Genís"),
        "The arcades of the main square are made for a slow coffee — one of the prettiest places to sit in the whole Empordà. The square and the surrounding lanes have well-regarded restaurants, and La Bisbal, five minutes away, adds more choice if you want it.": T(
            "Los soportales de la plaza mayor están hechos para un café sin prisa — uno de los sitios más bonitos para sentarse de todo el Empordà. La plaza y las calles de alrededor tienen restaurantes muy valorados, y La Bisbal, a cinco minutos, añade más opciones si le apetece.",
            "Els porxos de la plaça major estan fets per a un cafè sense presses — un dels llocs més bonics per seure de tot l'Empordà. La plaça i els carrers del voltant tenen restaurants molt valorats, i La Bisbal, a cinc minuts, afegeix més opcions si en voleu.",
            "Les arcades de la place principale sont faites pour un café sans hâte — l'un des plus jolis endroits où s'asseoir de tout l'Empordà. La place et les ruelles alentour comptent des restaurants bien notés, et La Bisbal, à cinq minutes, offre encore plus de choix si vous le souhaitez.",
            "De arcades van het hoofdplein zijn gemaakt voor een koffie op je gemak — een van de mooiste plekken om te zitten in heel de Empordà. Het plein en de omliggende straatjes hebben goed aangeschreven restaurants, en La Bisbal, op vijf minuten, biedt meer keuze als je wilt."),
        "The Festa Major de Sant Genís, in late August, is the village's traditional patron-saint celebration, with communal meals, music and dancing in the arcaded square.": T(
            "La Festa Major de Sant Genís, a finales de agosto, es la celebración tradicional del patrón del pueblo, con comidas populares, música y baile en la plaza porticada.",
            "La Festa Major de Sant Genís, a finals d'agost, és la celebració tradicional del patró del poble, amb àpats populars, música i ball a la plaça porxada.",
            "La Festa Major de Sant Genís, fin août, est la fête traditionnelle du saint patron du village, avec repas partagés, musique et danses sur la place à arcades.",
            "De Festa Major de Sant Genís, eind augustus, is het traditionele patroonheiligenfeest van het dorp, met gezamenlijke maaltijden, muziek en dans op het plein met arcades."),

        # ── Festival calendar ───────────────────────────────────────────────
        "Festival calendar at a glance": T(
            "Calendario de fiestas de un vistazo", "Calendari de festes d'un cop d'ull",
            "Le calendrier des fêtes en un coup d'œil", "Feestkalender in één oogopslag"),
        "Exact dates shift a little each year, so it is worth checking the village or Costa Brava tourism websites before you set out — but the months are reliable.": T(
            "Las fechas exactas cambian un poco cada año, así que conviene consultar las webs de turismo del pueblo o de la Costa Brava antes de salir — pero los meses son fiables.",
            "Les dates exactes canvien una mica cada any, així que val la pena consultar els webs de turisme del poble o de la Costa Brava abans de sortir — però els mesos són fiables.",
            "Les dates exactes varient un peu chaque année : mieux vaut vérifier les sites de tourisme du village ou de la Costa Brava avant de partir — mais les mois sont fiables.",
            "De exacte data verschuiven elk jaar een beetje, dus het loont om vóór vertrek de toeristische websites van het dorp of van de Costa Brava te raadplegen — maar de maanden kloppen."),
        "When": T("Cuándo", "Quan", "Quand", "Wanneer"),
        "Village": T("Pueblo", "Poble", "Village", "Dorp"),
        "Festival": T("Fiesta", "Festa", "Fête", "Feest"),
        "Early August": T("Principios de agosto", "Principis d'agost", "Début août", "Begin augustus"),
        "August": T("Agosto", "Agost", "Août", "Augustus"),
        "Late August": T("Finales de agosto", "Finals d'agost", "Fin août", "Eind augustus"),
        "First weekend of September": T(
            "Primer fin de semana de septiembre", "Primer cap de setmana de setembre",
            "Premier week-end de septembre", "Eerste weekend van september"),
        "First weekend of October": T(
            "Primer fin de semana de octubre", "Primer cap de setmana d'octubre",
            "Premier week-end d'octobre", "Eerste weekend van oktober"),
        "Autumn": T("Otoño", "Tardor", "Automne", "Herfst"),
        "Festa Major — concerts, dancing and processions": T(
            "Festa Major — conciertos, bailes y procesiones",
            "Festa Major — concerts, balls i processons",
            "Festa Major — concerts, danses et processions",
            "Festa Major — concerten, dans en processies"),
        "Festa Major and Iberian living-history visits": T(
            "Festa Major y visitas de historia viva ibérica",
            "Festa Major i visites d'història viva ibèrica",
            "Festa Major et visites d'histoire vivante ibère",
            "Festa Major en Iberische living-history-bezoeken"),
        "Festa Major, a traditional village celebration": T(
            "Festa Major, una celebración tradicional del pueblo",
            "Festa Major, una celebració tradicional del poble",
            "Festa Major, une fête villageoise traditionnelle",
            "Festa Major, een traditioneel dorpsfeest"),
        "Open-air Havaneres in the square and on Sa Riera beach": T(
            "Habaneras al aire libre en la plaza y en la playa de Sa Riera",
            "Havaneres a l'aire lliure a la plaça i a la platja de Sa Riera",
            "Havaneres en plein air sur la place et sur la plage de Sa Riera",
            "Havaneres in de openlucht op het plein en op het strand van Sa Riera"),
        "Festa Major de Sant Genís": T(
            "Festa Major de Sant Genís", "Festa Major de Sant Genís",
            "Festa Major de Sant Genís", "Festa Major de Sant Genís"),
        "Fira d'Indians, the Cuban-heritage fair": T(
            "Fira d'Indians, la feria de herencia cubana",
            "Fira d'Indians, la fira d'herència cubana",
            "Fira d'Indians, la foire de l'héritage cubain",
            "Fira d'Indians, de beurs van het Cubaanse erfgoed"),
        "Fira Medieval, the great medieval market": T(
            "Fira Medieval, el gran mercado medieval",
            "Fira Medieval, el gran mercat medieval",
            "Fira Medieval, le grand marché médiéval",
            "Fira Medieval, de grote middeleeuwse markt"),
        "Fira de l'Arròs and the wine and cheese fair": T(
            "Fira de l'Arròs y la feria del vino y el queso",
            "Fira de l'Arròs i la fira del vi i el formatge",
            "Fira de l'Arròs et la foire aux vins et fromages",
            "Fira de l'Arròs en de wijn- en kaasbeurs"),
    },
}
