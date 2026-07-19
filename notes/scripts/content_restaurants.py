#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
String table for things-to-do/restaurants.html.

Venue names, street addresses, phone numbers, websites, review counts and the
Catalan dish names (arròs mar i muntanya, arròs caldós de llagosta, tisana) are
deliberately absent from this table, so they pass through untranslated.
"""

from content_things_to_do import FOOTER_STD


def T(es, ca, fr, nl):
    return {"es": es, "ca": ca, "fr": fr, "nl": nl}


PAGES = {
    "things-to-do/restaurants.html": {
        "mode": "strings",
        "footer": FOOTER_STD,
        "meta": {
            "es": {"title": "Restaurantes y Bares en Tamariu — Tamariu Chalet",
                   "desc": "Dónde comer y beber en Tamariu, Costa Brava — bares, restaurantes de playa, cocina local, pizza para llevar y joyas gastronómicas cercanas. Nuestra guía personal para huéspedes."},
            "ca": {"title": "Restaurants i Bars a Tamariu — Tamariu Chalet",
                   "desc": "On menjar i beure a Tamariu, Costa Brava — bars, restaurants de platja, cuina local, pizza per emportar i joies gastronòmiques properes. La nostra guia personal per als hostes."},
            "fr": {"title": "Restaurants &amp; Bars à Tamariu — Tamariu Chalet",
                   "desc": "Où manger et boire à Tamariu, Costa Brava — bars, restaurants de plage, cuisine locale, pizzas à emporter et bonnes tables des environs. Notre guide personnel pour nos hôtes."},
            "nl": {"title": "Restaurants &amp; Bars in Tamariu — Tamariu Chalet",
                   "desc": "Waar u kunt eten en drinken in Tamariu, Costa Brava — bars, strandrestaurants, lokale eetadresjes, pizza om mee te nemen en pareltjes in de buurt. Onze persoonlijke gids voor gasten."},
        },
        "strings": {
            "Things To Do → Restaurants &amp; Bars": T(
                "Qué Hacer → Restaurantes y Bares", "Què Fer → Restaurants i Bars",
                "À Faire → Restaurants &amp; Bars", "Wat Te Doen → Restaurants &amp; Bars"),
            "Restaurants &amp; Bars in Tamariu": T(
                "Restaurantes y Bares en Tamariu", "Restaurants i Bars a Tamariu",
                "Restaurants &amp; Bars à Tamariu", "Restaurants &amp; Bars in Tamariu"),

            "Tamariu is a tiny village but it punches well above its weight when it comes to food and drink. The beachfront has some of the finest seafood on the Costa Brava, the evening bar scene is genuinely local, and a short drive opens up a string of outstanding Catalan restaurants. This is our personal guide — every place here we've eaten at and recommend.": T(
                "Tamariu es un pueblo diminuto, pero juega en una liga muy superior en lo que a comer y beber se refiere. El paseo marítimo reúne algunos de los mejores pescados y mariscos de la Costa Brava, el ambiente nocturno de los bares es auténticamente local y, a poca distancia en coche, se abre toda una serie de restaurantes catalanes excepcionales. Esta es nuestra guía personal — hemos comido en todos y cada uno de los sitios que aquí recomendamos.",
                "Tamariu és un poble diminut, però juga en una lliga molt superior pel que fa a menjar i beure. El passeig marítim aplega alguns dels millors peixos i mariscos de la Costa Brava, l'ambient nocturn dels bars és autènticament local i, a poca distància en cotxe, s'obre tota una sèrie de restaurants catalans excepcionals. Aquesta és la nostra guia personal — hem menjat en tots i cadascun dels llocs que hi recomanem.",
                "Tamariu est un village minuscule, mais il joue dans une tout autre catégorie dès qu'il s'agit de manger et de boire. Le front de mer propose certains des meilleurs produits de la mer de la Costa Brava, l'ambiance des bars le soir est authentiquement locale, et quelques minutes de voiture ouvrent sur une série de restaurants catalans remarquables. Voici notre guide personnel — nous avons mangé dans chacune des adresses recommandées ici.",
                "Tamariu is een piepklein dorp, maar op het gebied van eten en drinken speelt het ver boven zijn gewicht. Aan de boulevard vindt u enkele van de beste visgerechten van de Costa Brava, de avondlijke barscène is echt lokaal, en een klein stukje rijden opent een reeks uitstekende Catalaanse restaurants. Dit is onze persoonlijke gids — we hebben bij elk adres hier zelf gegeten en bevelen ze van harte aan."),

            "Drinks &amp; Evening": T("Copas y Noche", "Copes i Nit",
                                      "Boire un Verre &amp; Soirée", "Drankjes &amp; Avond"),
            "Bars in Tamariu": T("Bares en Tamariu", "Bars a Tamariu",
                                 "Bars à Tamariu", "Bars in Tamariu"),
            "Beach Bar": T("Bar de Playa", "Bar de Platja",
                           "Bar de Plage", "Strandbar"),
            "· 181 reviews": T("· 181 reseñas", "· 181 ressenyes",
                               "· 181 avis", "· 181 recensies"),
            "· 342 reviews · TripAdvisor": T(
                "· 342 reseñas · TripAdvisor", "· 342 ressenyes · TripAdvisor",
                "· 342 avis · TripAdvisor", "· 342 recensies · TripAdvisor"),
            "· 93 reviews": T("· 93 reseñas", "· 93 ressenyes",
                              "· 93 avis", "· 93 recensies"),
            "· 27 reviews (bravissima)": T(
                "· 27 reseñas (bravissima)", "· 27 ressenyes (bravissima)",
                "· 27 avis (bravissima)", "· 27 recensies (bravissima)"),

            "The liveliest spot on the beach edge — casual tables, good music and a crowd that mixes locals with visitors all evening. Great for bagels, sandwiches, burgers and tapas through the day, and cold beers and cocktails into the night.": T(
                "El sitio más animado junto a la playa — mesas informales, buena música y un público que mezcla a locales y visitantes durante toda la tarde. Ideal para bagels, bocadillos, hamburguesas y tapas durante el día, y cervezas frías y cócteles por la noche.",
                "El lloc més animat arran de platja — taules informals, bona música i un públic que barreja gent del poble i visitants durant tota la tarda. Ideal per a bagels, entrepans, hamburgueses i tapes durant el dia, i cerveses fredes i còctels a la nit.",
                "L'adresse la plus animée en bord de plage — tables décontractées, bonne musique et une clientèle qui mêle habitants et visiteurs toute la soirée. Parfait pour des bagels, sandwichs, burgers et tapas dans la journée, et des bières fraîches et cocktails le soir venu.",
                "De levendigste plek aan de rand van het strand — informele tafeltjes, goede muziek en een publiek van locals en bezoekers de hele avond door. Overdag prima voor bagels, broodjes, burgers en tapas, en 's avonds voor koude biertjes en cocktails."),
            "⏰ Daily — summer season": T(
                "⏰ Todos los días — temporada de verano",
                "⏰ Cada dia — temporada d'estiu",
                "⏰ Tous les jours — saison estivale",
                "⏰ Dagelijks — zomerseizoen"),
            "Restaurant &amp; Bar · Local Favourite": T(
                "Restaurante y Bar · Favorito de los Locales",
                "Restaurant i Bar · Preferit de la Gent del Poble",
                "Restaurant &amp; Bar · Le Préféré des Habitants",
                "Restaurant &amp; Bar · Favoriet bij Locals"),
            "The village's best-kept secret. A small, intimate place beloved by locals — known for outstanding sea-and-mountain rice (": T(
                "El secreto mejor guardado del pueblo. Un local pequeño e íntimo, muy querido por la gente de aquí — famoso por su extraordinario arroz de mar y montaña (",
                "El secret més ben guardat del poble. Un local petit i íntim, molt estimat per la gent d'aquí — famós pel seu extraordinari arròs de mar i muntanya (",
                "Le secret le mieux gardé du village. Un petit établissement intime, adoré des habitants — réputé pour son extraordinaire riz mer et montagne (",
                "Het best bewaarde geheim van het dorp. Een kleine, intieme zaak die geliefd is bij de locals — bekend om zijn uitstekende zee-en-bergrijst ("),
            "), gloriously homemade croquettes, and an atmosphere that carries on till 3am at weekends. Don't let the modest exterior fool you.": T(
                "), sus croquetas caseras gloriosas y un ambiente que los fines de semana se alarga hasta las 3 de la madrugada. No se deje engañar por su aspecto modesto.",
                "), les seves croquetes casolanes glorioses i un ambient que els caps de setmana s'allarga fins a les 3 de la matinada. No us deixeu enganyar pel seu aspecte modest.",
                "), ses croquettes maison somptueuses et une ambiance qui se prolonge jusqu'à 3 heures du matin le week-end. Ne vous fiez pas à la modestie de la façade.",
                "), zijn heerlijke huisgemaakte kroketten en een sfeer die in het weekend doorgaat tot drie uur 's nachts. Laat u niet misleiden door de bescheiden buitenkant."),
            "⏰ Fri–Sat 13:00–16:00 &amp; 20:30–23:00 · Sun 13:00–16:00": T(
                "⏰ Vie–Sáb 13:00–16:00 y 20:30–23:00 · Dom 13:00–16:00",
                "⏰ Dv–Ds 13:00–16:00 i 20:30–23:00 · Dg 13:00–16:00",
                "⏰ Ven–Sam 13h00–16h00 &amp; 20h30–23h00 · Dim 13h00–16h00",
                "⏰ Vr–Za 13:00–16:00 &amp; 20:30–23:00 · Zo 13:00–16:00"),
            "Local tip:": T("Consejo local:", "Consell local:",
                            "Conseil local :", "Lokale tip:"),
            "Mossec has very limited hours — if you want dinner there on a weekend, ask us to reserve for you when you arrive. It books up fast in July and August.": T(
                "Mossec tiene un horario muy limitado — si quiere cenar allí un fin de semana, pídanos que le reservemos al llegar. Se llena muy rápido en julio y agosto.",
                "Mossec té un horari molt limitat — si voleu sopar-hi un cap de setmana, demaneu-nos que us hi reservem en arribar. S'omple molt de pressa el juliol i l'agost.",
                "Mossec a des horaires très restreints — si vous souhaitez y dîner le week-end, demandez-nous de réserver à votre arrivée. L'établissement affiche vite complet en juillet et août.",
                "Mossec heeft zeer beperkte openingstijden — wilt u er in het weekend eten, vraag ons dan bij aankomst te reserveren. In juli en augustus is het snel volgeboekt."),

            "Seafood &amp; Views": T("Pescado y Vistas", "Peix i Vistes",
                                     "Fruits de Mer &amp; Panorama", "Vis &amp; Uitzicht"),
            "Beach &amp; Promenade Restaurants": T(
                "Restaurantes de Playa y Paseo Marítimo",
                "Restaurants de Platja i Passeig Marítim",
                "Restaurants de la Plage &amp; du Front de Mer",
                "Restaurants aan Strand &amp; Boulevard"),
            "Seafood · Promenade · Tamariu's Best": T(
                "Pescado y Marisco · Paseo Marítimo · Lo Mejor de Tamariu",
                "Peix i Marisc · Passeig Marítim · El Millor de Tamariu",
                "Fruits de Mer · Front de Mer · Le Meilleur de Tamariu",
                "Vis &amp; Zeevruchten · Boulevard · Beste van Tamariu"),
            "Highly Recommended": T("Muy Recomendado", "Molt Recomanat",
                                    "Vivement Recommandé", "Sterk Aanbevolen"),
            "Without question the star of the Tamariu seafront. Sit on the terrace right at the water's edge and order the paella or — if you're lucky enough to see it on the menu — the": T(
                "Sin duda la estrella del paseo marítimo de Tamariu. Siéntese en la terraza al borde del agua y pida la paella o — si tiene la suerte de verlo en la carta — el",
                "Sens dubte l'estrella del passeig marítim de Tamariu. Seieu a la terrassa arran d'aigua i demaneu la paella o — si teniu la sort de veure'l a la carta — l'",
                "Sans conteste la vedette du front de mer de Tamariu. Installez-vous en terrasse au bord de l'eau et commandez la paella ou — si vous avez la chance de le voir à la carte — l'",
                "Zonder twijfel de ster van de boulevard van Tamariu. Neem plaats op het terras aan het water en bestel de paella of — als u het geluk hebt dat het op de kaart staat — de"),
            "(lobster rice, broth-style). Possibly the best rice dish on the Costa Brava. Book ahead in summer.": T(
                "(arroz caldoso de langosta). Posiblemente el mejor arroz de la Costa Brava. Reserve con antelación en verano.",
                "(arròs caldós de llagosta). Possiblement el millor arròs de la Costa Brava. Reserveu amb antelació a l'estiu.",
                "(riz de homard en bouillon). Sans doute le meilleur plat de riz de la Costa Brava. Réservez à l'avance en été.",
                "(romige kreeftenrijst). Mogelijk het beste rijstgerecht van de Costa Brava. Reserveer in de zomer vooraf."),
            "📍 View on Google Maps": T(
                "📍 Ver en Google Maps", "📍 Veure a Google Maps",
                "📍 Voir sur Google Maps", "📍 Bekijk op Google Maps"),
            "Traditional Catalan · Promenade": T(
                "Cocina Catalana Tradicional · Paseo Marítimo",
                "Cuina Catalana Tradicional · Passeig Marítim",
                "Cuisine Catalane Traditionnelle · Front de Mer",
                "Traditioneel Catalaans · Boulevard"),
            "A reliable beachfront institution. The meat croquettes and mussels are the thing to order, and they do a proper family-sized paella that needs a day's notice. Friendly service, fair prices, right on the passeig.": T(
                "Una institución fiable del paseo marítimo. Hay que pedir las croquetas de carne y los mejillones, y preparan una paella familiar en condiciones que hay que encargar con un día de antelación. Servicio amable, precios justos, en pleno passeig.",
                "Una institució fiable del passeig marítim. Cal demanar les croquetes de carn i els musclos, i preparen una paella familiar com cal que s'ha d'encarregar amb un dia d'antelació. Servei amable, preus justos, en ple passeig.",
                "Une institution fiable du front de mer. Il faut commander les croquettes de viande et les moules, et l'on y prépare une vraie paella familiale à réserver un jour à l'avance. Service aimable, prix justes, en plein sur le passeig.",
                "Een betrouwbare instelling aan de boulevard. Bestel de vleeskroketten en de mosselen; ze maken ook een echte paella voor het hele gezin, die u een dag vooraf moet bestellen. Vriendelijke bediening, eerlijke prijzen, pal aan de passeig."),
            "Hotel Restaurant · Beach Views": T(
                "Restaurante de Hotel · Vistas a la Playa",
                "Restaurant d'Hotel · Vistes a la Platja",
                "Restaurant d'Hôtel · Vue sur la Plage",
                "Hotelrestaurant · Uitzicht op het Strand"),
            "The terrace of the Hotel Tamariu is one of the finest places to eat on the whole coast — right on the promenade with the whole bay laid out in front of you. The": T(
                "La terraza del Hotel Tamariu es uno de los mejores sitios para comer de toda la costa — en pleno paseo marítimo, con toda la bahía delante. El cóctel",
                "La terrassa de l'Hotel Tamariu és un dels millors llocs per menjar de tota la costa — en ple passeig marítim, amb tota la badia al davant. El còctel",
                "La terrasse de l'Hotel Tamariu est l'une des plus belles tables de toute la côte — en plein sur la promenade, avec toute la baie devant soi. Le cocktail",
                "Het terras van Hotel Tamariu is een van de mooiste eetplekken van de hele kust — pal aan de boulevard met de hele baai voor u. De"),
            "cocktail is a summer ritual. Good Catalan kitchen, excellent wine list.": T(
                "es un ritual de verano. Buena cocina catalana, excelente carta de vinos.",
                "és un ritual d'estiu. Bona cuina catalana, excel·lent carta de vins.",
                "est un rituel estival. Bonne cuisine catalane, excellente carte des vins.",
                "cocktail is een zomerritueel. Goede Catalaanse keuken, uitstekende wijnkaart."),
            "Family Run · Simple Catalan": T(
                "Negocio Familiar · Cocina Catalana Sencilla",
                "Negoci Familiar · Cuina Catalana Senzilla",
                "Affaire Familiale · Cuisine Catalane Simple",
                "Familiebedrijf · Eenvoudig Catalaans"),
            "A family-run spot with sea views and honest, unpretentious Catalan cooking. Fresh fish of the day, grilled to order, with good local wine. No frills — just good food at the water's edge. A favourite for a long, lazy lunch.": T(
                "Un local familiar con vistas al mar y cocina catalana honesta y sin pretensiones. Pescado fresco del día, a la plancha al momento, con buen vino de la zona. Sin florituras — solo buena comida al borde del agua. Un favorito para una comida larga y tranquila.",
                "Un local familiar amb vistes al mar i cuina catalana honesta i sense pretensions. Peix fresc del dia, a la planxa al moment, amb bon vi de la zona. Sense floritures — només bon menjar arran d'aigua. Un preferit per a un dinar llarg i tranquil.",
                "Une adresse familiale avec vue sur la mer et une cuisine catalane honnête et sans prétention. Poisson frais du jour grillé à la commande, accompagné d'un bon vin local. Sans chichis — juste de la bonne cuisine au bord de l'eau. Un incontournable pour un déjeuner long et paisible.",
                "Een familiezaak met zeezicht en eerlijke, pretentieloze Catalaanse keuken. Verse vis van de dag, à la minute gegrild, met goede lokale wijn. Geen poespas — gewoon lekker eten aan het water. Een favoriet voor een lange, luie lunch."),
            "⏰ Lunch &amp; dinner · summer season": T(
                "⏰ Comidas y cenas · temporada de verano",
                "⏰ Dinars i sopars · temporada d'estiu",
                "⏰ Déjeuner &amp; dîner · saison estivale",
                "⏰ Lunch &amp; diner · zomerseizoen"),

            "Village Dining": T("Comer en el Pueblo", "Menjar al Poble",
                                "Manger au Village", "Eten in het Dorp"),
            "Town &amp; Local Restaurants": T(
                "Restaurantes del Pueblo", "Restaurants del Poble",
                "Restaurants du Village", "Restaurants in het Dorp"),
            "Catalan Kitchen · Good Value": T(
                "Cocina Catalana · Buena Relación Calidad-Precio",
                "Cuina Catalana · Bona Relació Qualitat-Preu",
                "Cuisine Catalane · Bon Rapport Qualité-Prix",
                "Catalaanse Keuken · Goede Prijs-Kwaliteit"),
            "One of the better-value spots in the village — solidly good Catalan home cooking in a simple, honest setting. Locals eat here regularly, which is always a good sign. Great for a relaxed dinner without the beach price premium.": T(
                "Uno de los sitios con mejor relación calidad-precio del pueblo — buena cocina catalana casera en un entorno sencillo y honesto. La gente de aquí come aquí a menudo, lo que siempre es buena señal. Ideal para una cena tranquila sin el sobreprecio de la playa.",
                "Un dels llocs amb millor relació qualitat-preu del poble — bona cuina catalana casolana en un entorn senzill i honest. La gent d'aquí hi menja sovint, cosa que sempre és bon senyal. Ideal per a un sopar tranquil sense el sobrepreu de la platja.",
                "L'une des meilleures adresses en rapport qualité-prix du village — une solide cuisine catalane familiale dans un cadre simple et honnête. Les habitants y mangent régulièrement, ce qui est toujours bon signe. Parfait pour un dîner tranquille sans le supplément bord de mer.",
                "Een van de beste adresjes qua prijs-kwaliteit in het dorp — degelijke Catalaanse huiskeuken in een eenvoudige, eerlijke setting. Locals eten hier geregeld, altijd een goed teken. Prima voor een ontspannen diner zonder de strandtoeslag."),
            "📍 Tamariu village centre": T(
                "📍 Centro del pueblo de Tamariu", "📍 Centre del poble de Tamariu",
                "📍 Centre du village de Tamariu", "📍 Dorpscentrum van Tamariu"),
            "Pizza &amp; Pasta · Family Friendly": T(
                "Pizza y Pasta · Ideal para Familias",
                "Pizza i Pasta · Ideal per a Famílies",
                "Pizza &amp; Pâtes · Familial",
                "Pizza &amp; Pasta · Gezinsvriendelijk"),
            "Fresh wood-oven pizzas and pasta in a family-friendly setting — a solid choice when you want something simple and reliable. Relaxed atmosphere, good for children. The Nutella pizza for dessert has its fans.": T(
                "Pizzas recién hechas al horno de leña y pasta en un ambiente familiar — una opción segura cuando se quiere algo sencillo y fiable. Ambiente relajado, bien para niños. La pizza de Nutella de postre tiene sus incondicionales.",
                "Pizzes acabades de fer al forn de llenya i pasta en un ambient familiar — una opció segura quan es vol alguna cosa senzilla i fiable. Ambient relaxat, bé per a nens. La pizza de Nutella de postres té els seus incondicionals.",
                "Pizzas fraîches au feu de bois et pâtes dans un cadre familial — une valeur sûre quand on cherche simple et fiable. Ambiance détendue, adapté aux enfants. La pizza au Nutella en dessert a ses adeptes.",
                "Verse houtovenpizza's en pasta in een gezinsvriendelijke setting — een prima keuze als u iets eenvoudigs en betrouwbaars wilt. Ontspannen sfeer, geschikt voor kinderen. De Nutella-pizza als dessert heeft zijn liefhebbers."),
            "📍 Tamariu village": T("📍 Pueblo de Tamariu", "📍 Poble de Tamariu",
                                    "📍 Village de Tamariu", "📍 Dorp Tamariu"),
            "⏰ Evenings · summer season": T(
                "⏰ Noches · temporada de verano", "⏰ Vespres · temporada d'estiu",
                "⏰ Le soir · saison estivale", "⏰ 's Avonds · zomerseizoen"),
            "Grill &amp; Rotisserie · Among the Pines": T(
                "Parrilla y Asador · Entre los Pinos",
                "Graella i Rostidor · Entre els Pins",
                "Grill &amp; Rôtisserie · Au Milieu des Pins",
                "Grill &amp; Rotisserie · Tussen de Dennen"),
            "A wonderfully relaxed open-air grill on the edge of the village, tucked down a quiet dead-end street among the pines. The speciality is meat cooked over an oak-wood fire — spit-roasted chicken, veal, rabbit and lamb chops, served with chips and simple salads. Generous, honest cooking at fair prices, with a shady terrace that's made for a long, lazy family lunch. Reserve the roast chicken a day ahead, as it slow-cooks over the fire.": T(
                "Una parrilla al aire libre maravillosamente relajada en las afueras del pueblo, escondida en una calle sin salida tranquila entre los pinos. La especialidad es la carne al fuego de leña de encina — pollo al ast, ternera, conejo y chuletillas de cordero, servidos con patatas fritas y ensaladas sencillas. Cocina generosa y honesta a precios justos, con una terraza a la sombra hecha para una comida familiar larga y sin prisas. Encargue el pollo asado con un día de antelación, porque se hace lentamente al fuego.",
                "Una graella a l'aire lliure meravellosament relaxada a les afores del poble, amagada en un carrer sense sortida tranquil entre els pins. L'especialitat és la carn al foc de llenya d'alzina — pollastre a l'ast, vedella, conill i costelletes de xai, servits amb patates fregides i amanides senzilles. Cuina generosa i honesta a preus justos, amb una terrassa a l'ombra feta per a un dinar familiar llarg i sense presses. Encarregueu el pollastre rostit amb un dia d'antelació, perquè es fa lentament al foc.",
                "Un grill en plein air merveilleusement détendu en bordure du village, niché dans une impasse tranquille au milieu des pins. La spécialité, c'est la viande cuite au feu de bois de chêne — poulet à la broche, veau, lapin et côtelettes d'agneau, servis avec des frites et des salades simples. Cuisine généreuse et honnête à prix justes, avec une terrasse ombragée faite pour un long déjeuner de famille. Réservez le poulet rôti la veille, car il cuit lentement sur le feu.",
                "Een heerlijk ontspannen openluchtgrill aan de rand van het dorp, verscholen in een rustig doodlopend straatje tussen de dennen. De specialiteit is vlees boven een eikenhoutvuur — kip aan het spit, kalfsvlees, konijn en lamskoteletjes, geserveerd met friet en eenvoudige salades. Royale, eerlijke keuken tegen faire prijzen, met een schaduwrijk terras dat gemaakt is voor een lange, luie familielunch. Bestel de gebraden kip een dag vooruit, want die gaart langzaam boven het vuur."),
            "⏰ Summer season · approx. June–September": T(
                "⏰ Temporada de verano · aprox. junio–septiembre",
                "⏰ Temporada d'estiu · aprox. juny–setembre",
                "⏰ Saison estivale · env. juin–septembre",
                "⏰ Zomerseizoen · ca. juni–september"),

            "A Short Drive Away": T("A Poca Distancia en Coche", "A Poca Distància en Cotxe",
                                    "À Quelques Minutes en Voiture", "Op Korte Rijafstand"),
            "Worth the Drive": T("Merece el Viaje", "Val la Pena el Viatge",
                                 "Ça Vaut le Détour", "De Rit Waard"),
            "Farm Restaurant · Creative Catalan · Palau-Sator Area": T(
                "Restaurante de Masía · Cocina Catalana Creativa · Zona de Palau-Sator",
                "Restaurant de Masia · Cuina Catalana Creativa · Zona de Palau-Sator",
                "Restaurant à la Ferme · Cuisine Catalane Créative · Secteur de Palau-Sator",
                "Boerderijrestaurant · Creatief Catalaans · Omgeving Palau-Sator"),
            "A genuinely special experience — a creative Catalan restaurant set on a working farm in the countryside near Palafrugell. They grow much of what they serve, the wine list is outstanding, and the setting among the fields is like no other restaurant on the coast. Well worth the short drive inland. Booking essential.": T(
                "Una experiencia realmente especial — un restaurante catalán creativo instalado en una masía en activo en el campo cerca de Palafrugell. Cultivan buena parte de lo que sirven, la carta de vinos es extraordinaria y el entorno entre los campos no se parece a ningún otro restaurante de la costa. Merece de sobra el corto trayecto hacia el interior. Imprescindible reservar.",
                "Una experiència realment especial — un restaurant català creatiu instal·lat en una masia en actiu al camp a prop de Palafrugell. Cultiven bona part del que serveixen, la carta de vins és extraordinària i l'entorn entre els camps no s'assembla a cap altre restaurant de la costa. Val de sobres el curt trajecte cap a l'interior. Imprescindible reservar.",
                "Une expérience vraiment à part — un restaurant catalan créatif installé dans une ferme en activité, à la campagne près de Palafrugell. Ils cultivent une grande partie de ce qu'ils servent, la carte des vins est remarquable et le cadre au milieu des champs ne ressemble à aucun autre restaurant de la côte. Le court trajet vers l'intérieur en vaut largement la peine. Réservation indispensable.",
                "Een werkelijk bijzondere ervaring — een creatief Catalaans restaurant op een werkende boerderij op het platteland bij Palafrugell. Ze verbouwen veel van wat ze serveren, de wijnkaart is uitmuntend en de ligging tussen de velden is uniek aan deze kust. Het korte ritje landinwaarts meer dan waard. Reserveren is noodzakelijk."),
            "📍 Palau-Sator / Fontanilles area · approx. 15 min drive": T(
                "📍 Zona de Palau-Sator / Fontanilles · aprox. 15 min en coche",
                "📍 Zona de Palau-Sator / Fontanilles · aprox. 15 min en cotxe",
                "📍 Secteur Palau-Sator / Fontanilles · env. 15 min de route",
                "📍 Omgeving Palau-Sator / Fontanilles · ca. 15 min rijden"),
            "Fine Dining · Llafranc · 10 min": T(
                "Alta Cocina · Llafranc · 10 min", "Alta Cuina · Llafranc · 10 min",
                "Gastronomique · Llafranc · 10 min", "Fine Dining · Llafranc · 10 min"),
            "Perched on the lighthouse headland above Llafranc with extraordinary views down the coast. Creative modern Catalan cooking using the best local ingredients — a special-occasion restaurant. One of the finest settings on the Costa Brava.": T(
                "Encaramado en el promontorio del faro sobre Llafranc, con vistas extraordinarias a lo largo de la costa. Cocina catalana moderna y creativa con los mejores productos locales — un restaurante para ocasiones especiales. Uno de los emplazamientos más bonitos de la Costa Brava.",
                "Enfilat al promontori del far sobre Llafranc, amb vistes extraordinàries al llarg de la costa. Cuina catalana moderna i creativa amb els millors productes locals — un restaurant per a ocasions especials. Un dels emplaçaments més bonics de la Costa Brava.",
                "Perché sur le promontoire du phare au-dessus de Llafranc, avec des vues extraordinaires sur la côte. Cuisine catalane moderne et créative à partir des meilleurs produits locaux — une table pour les grandes occasions. L'un des plus beaux cadres de la Costa Brava.",
                "Hoog op de vuurtorenkaap boven Llafranc, met buitengewone uitzichten langs de kust. Creatieve moderne Catalaanse keuken met de beste lokale ingrediënten — een restaurant voor bijzondere gelegenheden. Een van de mooiste locaties van de Costa Brava."),
            "Classic Catalan · Calella · 15 min": T(
                "Cocina Catalana Clásica · Calella · 15 min",
                "Cuina Catalana Clàssica · Calella · 15 min",
                "Cuisine Catalane Classique · Calella · 15 min",
                "Klassiek Catalaans · Calella · 15 min"),
            "A Calella de Palafrugell institution — simple, honest Catalan cooking in a colourful setting. The rice dishes are outstanding. Long summer lunches here are a Costa Brava highlight. Very popular — booking strongly advised.": T(
                "Una institución de Calella de Palafrugell — cocina catalana sencilla y honesta en un local lleno de color. Los arroces son extraordinarios. Las largas comidas de verano aquí son uno de los grandes placeres de la Costa Brava. Muy popular — se recomienda encarecidamente reservar.",
                "Una institució de Calella de Palafrugell — cuina catalana senzilla i honesta en un local ple de color. Els arrossos són extraordinaris. Els llargs dinars d'estiu aquí són un dels grans plaers de la Costa Brava. Molt popular — es recomana molt reservar.",
                "Une institution de Calella de Palafrugell — cuisine catalane simple et honnête dans un cadre haut en couleur. Les plats de riz sont remarquables. Les longs déjeuners d'été ici comptent parmi les grands plaisirs de la Costa Brava. Très prisé — réservation fortement conseillée.",
                "Een instituut in Calella de Palafrugell — eenvoudige, eerlijke Catalaanse keuken in een kleurrijke setting. De rijstgerechten zijn uitstekend. Lange zomerse lunches hier zijn een hoogtepunt van de Costa Brava. Zeer populair — reserveren sterk aangeraden."),
            "Acclaimed · Palafrugell · 15 min": T(
                "Aclamado · Palafrugell · 15 min", "Aclamat · Palafrugell · 15 min",
                "Reconnu · Palafrugell · 15 min", "Veelgeprezen · Palafrugell · 15 min"),
            "One of the most acclaimed restaurants in the area — sophisticated Catalan cuisine in an intimate setting. The tasting menu is excellent value for the quality on offer. Book well in advance. A treat for a special evening.": T(
                "Uno de los restaurantes más aclamados de la zona — cocina catalana sofisticada en un espacio íntimo. El menú degustación tiene una relación calidad-precio excelente. Reserve con mucha antelación. Un capricho para una noche especial.",
                "Un dels restaurants més aclamats de la zona — cuina catalana sofisticada en un espai íntim. El menú de degustació té una relació qualitat-preu excel·lent. Reserveu amb molta antelació. Un caprici per a una nit especial.",
                "L'un des restaurants les plus salués de la région — cuisine catalane sophistiquée dans un cadre intime. Le menu dégustation offre un excellent rapport qualité-prix. Réservez bien à l'avance. Un plaisir pour une soirée particulière.",
                "Een van de meest geprezen restaurants in de omgeving — verfijnde Catalaanse keuken in een intieme setting. Het proefmenu biedt uitstekende waarde voor de geboden kwaliteit. Reserveer ruim van tevoren. Een traktatie voor een bijzondere avond."),
            "Creative Dining · Esclanyà, Begur · 20 min": T(
                "Cocina Creativa · Esclanyà, Begur · 20 min",
                "Cuina Creativa · Esclanyà, Begur · 20 min",
                "Cuisine Créative · Esclanyà, Begur · 20 min",
                "Creatieve Keuken · Esclanyà, Begur · 20 min"),
            "A stylish, intimate restaurant tucked away in the hamlet of Esclanyà, just outside Begur, with a lovely terrace and a short, creative menu of beautifully presented, Latin-influenced dishes. Attentive service and a real sense of occasion — one of the finest meals in the area. Open evenings, closed Tuesdays. Booking recommended.": T(
                "Un restaurante con estilo e íntimo escondido en el pueblecito de Esclanyà, a las afueras de Begur, con una terraza preciosa y una carta corta y creativa de platos bellamente presentados con influencia latina. Servicio atento y una verdadera sensación de ocasión especial — una de las mejores comidas de la zona. Abre por las noches, cierra los martes. Se recomienda reservar.",
                "Un restaurant amb estil i íntim amagat al llogaret d'Esclanyà, a tocar de Begur, amb una terrassa preciosa i una carta curta i creativa de plats bellament presentats amb influència llatina. Servei atent i una autèntica sensació d'ocasió especial — un dels millors àpats de la zona. Obre als vespres, tanca els dimarts. Es recomana reservar.",
                "Un restaurant élégant et intime niché dans le hameau d'Esclanyà, juste à la sortie de Begur, avec une jolie terrasse et une carte courte et créative de plats magnifiquement présentés aux influences latines. Service attentionné et vrai sentiment d'événement — l'un des meilleurs repas de la région. Ouvert le soir, fermé le mardi. Réservation conseillée.",
                "Een stijlvol, intiem restaurant verscholen in het gehucht Esclanyà, net buiten Begur, met een mooi terras en een korte, creatieve kaart met prachtig gepresenteerde gerechten met Latijns-Amerikaanse invloeden. Attente bediening en een echt gevoel van gelegenheid — een van de beste maaltijden in de omgeving. 's Avonds open, dinsdag gesloten. Reserveren aanbevolen."),
            "Street Food · Platja de Pals · 25 min": T(
                "Comida Callejera · Platja de Pals · 25 min",
                "Menjar de Carrer · Platja de Pals · 25 min",
                "Street Food · Platja de Pals · 25 min",
                "Streetfood · Platja de Pals · 25 min"),
            "A fun, buzzy street-food spot a few minutes from Pals beach — bold flavours from Mexico and Asia with tacos, Korean fried chicken, burgers and nachos, great cocktails and a relaxed terrace. Perfect for a livelier, informal evening; equally good for families, groups and a young crowd. It fills up fast, so book ahead.": T(
                "Un local de comida callejera divertido y animado a pocos minutos de la playa de Pals — sabores potentes de México y Asia con tacos, pollo frito coreano, hamburguesas y nachos, buenos cócteles y una terraza relajada. Perfecto para una noche informal y más animada; igual de bueno para familias, grupos y gente joven. Se llena rápido, así que reserve con antelación.",
                "Un local de menjar de carrer divertit i animat a pocs minuts de la platja de Pals — sabors potents de Mèxic i Àsia amb tacos, pollastre fregit coreà, hamburgueses i natxos, bons còctels i una terrassa relaxada. Perfecte per a una nit informal i més animada; igual de bo per a famílies, grups i gent jove. S'omple de pressa, així que reserveu amb antelació.",
                "Une adresse de street food conviviale et animée à quelques minutes de la plage de Pals — saveurs affirmées du Mexique et d'Asie avec tacos, poulet frit coréen, burgers et nachos, de bons cocktails et une terrasse décontractée. Parfait pour une soirée informelle et plus animée ; tout aussi bien pour les familles, les groupes et un public jeune. Ça se remplit vite, pensez à réserver.",
                "Een leuke, levendige streetfoodplek op een paar minuten van het strand van Pals — uitgesproken smaken uit Mexico en Azië met taco's, Koreaanse gefrituurde kip, burgers en nacho's, goede cocktails en een ontspannen terras. Perfect voor een levendigere, informele avond; net zo goed voor gezinnen, groepen en een jong publiek. Het loopt snel vol, dus reserveer vooraf."),

            "Pizza &amp; Takeaway": T("Pizza y Para Llevar", "Pizza i Per Emportar",
                                      "Pizza &amp; À Emporter", "Pizza &amp; Afhalen"),
            "Takeaway in Tamariu": T("Para Llevar en Tamariu", "Per Emportar a Tamariu",
                                     "À Emporter à Tamariu", "Afhalen in Tamariu"),
            "Pizza Takeaway · Artisan · Seasonal": T(
                "Pizza Para Llevar · Artesanal · De Temporada",
                "Pizza Per Emportar · Artesanal · De Temporada",
                "Pizza à Emporter · Artisanale · Saisonnier",
                "Pizza Afhalen · Ambachtelijk · Seizoensgebonden"),
            "Summer season only": T("Solo temporada de verano", "Només temporada d'estiu",
                                    "Saison estivale uniquement", "Alleen zomerseizoen"),
            "A brilliant little takeaway right in the village — artisan wood-fired pizzas and crepes, made fresh to order. Gluten-free bases available. Perfect for an evening on the terrace or beach. Small, so arrive early or expect a short wait — it's worth it. One of the village's genuine hidden gems.": T(
                "Un pequeño local para llevar estupendo en pleno pueblo — pizzas artesanales al horno de leña y crepes, hechas al momento. Hay bases sin gluten. Perfecto para una noche en la terraza o en la playa. Es pequeño, así que llegue temprano o cuente con una breve espera — vale la pena. Una de las joyas escondidas de verdad del pueblo.",
                "Un petit local per emportar estupend en ple poble — pizzes artesanals al forn de llenya i creps, fetes al moment. Hi ha bases sense gluten. Perfecte per a un vespre a la terrassa o a la platja. És petit, així que arribeu aviat o compteu amb una breu espera — val la pena. Una de les joies amagades de debò del poble.",
                "Un excellent petit comptoir à emporter en plein village — pizzas artisanales au feu de bois et crêpes, préparées à la commande. Pâtes sans gluten disponibles. Parfait pour une soirée en terrasse ou à la plage. C'est petit, alors venez tôt ou attendez-vous à patienter un peu — ça vaut le coup. L'un des vrais trésors cachés du village.",
                "Een geweldig afhaaladresje midden in het dorp — ambachtelijke houtovenpizza's en crêpes, vers bereid op bestelling. Glutenvrije bodems beschikbaar. Perfect voor een avond op het terras of aan het strand. Klein, dus kom vroeg of reken op korte wachttijd — het is het waard. Een van de echte verborgen pareltjes van het dorp."),
            "⏰ Evenings · summer season only (approx. June–September)": T(
                "⏰ Noches · solo temporada de verano (aprox. junio–septiembre)",
                "⏰ Vespres · només temporada d'estiu (aprox. juny–setembre)",
                "⏰ Le soir · saison estivale uniquement (env. juin–septembre)",
                "⏰ 's Avonds · alleen zomerseizoen (ca. juni–september)"),
            "Mediterranean Takeaway · Fresh &amp; Healthy": T(
                "Para Llevar Mediterráneo · Fresco y Saludable",
                "Per Emportar Mediterrani · Fresc i Saludable",
                "À Emporter Méditerranéen · Frais &amp; Sain",
                "Mediterraans Afhalen · Vers &amp; Gezond"),
            "A stylish little takeaway in the village with a fresh, modern Mediterranean menu — poke bowls, tartars and ceviches, plus brioches and delicate desserts, all matched with craft beer and wine. Healthy, colourful food to take back to the terrace or down to the beach. Their motto says it well: \"our food, your place.\"": T(
                "Un pequeño local para llevar con estilo en el pueblo, con una carta mediterránea fresca y moderna — poke bowls, tartares y ceviches, además de brioches y postres delicados, todo acompañado de cerveza artesana y vino. Comida sana y llena de color para llevar a la terraza o bajar a la playa. Su lema lo dice bien: «nuestra comida, tu sitio».",
                "Un petit local per emportar amb estil al poble, amb una carta mediterrània fresca i moderna — poke bowls, tàrtars i ceviches, a més de brioixos i postres delicades, tot acompanyat de cervesa artesana i vi. Menjar sa i ple de color per endur-vos a la terrassa o baixar a la platja. El seu lema ho diu bé: «el nostre menjar, el teu lloc».",
                "Un petit comptoir à emporter élégant au village, avec une carte méditerranéenne fraîche et moderne — poke bowls, tartares et ceviches, ainsi que brioches et desserts délicats, le tout accompagné de bière artisanale et de vin. Une cuisine saine et colorée à emporter en terrasse ou à la plage. Leur devise résume tout : « notre cuisine, chez vous ».",
                "Een stijlvol afhaaladresje in het dorp met een frisse, moderne mediterrane kaart — pokébowls, tartaars en ceviches, plus brioches en fijne desserts, alles gecombineerd met speciaalbier en wijn. Gezond, kleurrijk eten om mee te nemen naar het terras of het strand. Hun motto zegt het treffend: \"ons eten, jouw plek.\""),

            "Ask us for advice:": T("Pregúntenos:", "Pregunteu-nos:",
                                    "Demandez-nous conseil :", "Vraag ons om advies:"),
            "We're always happy to recommend somewhere specific or make a reservation on your behalf — just ask at check-in or drop us a message beforehand. And don't forget: in July and August, most restaurants need booking at least a day ahead.": T(
                "Siempre estaremos encantados de recomendarle un sitio concreto o de hacer una reserva por usted — solo tiene que pedírnoslo al llegar o escribirnos antes. Y no lo olvide: en julio y agosto, en la mayoría de restaurantes hay que reservar con al menos un día de antelación.",
                "Sempre estarem encantats de recomanar-vos un lloc concret o de fer una reserva per vosaltres — només cal que ens ho demaneu en arribar o que ens escriviu abans. I no ho oblideu: el juliol i l'agost, a la majoria de restaurants cal reservar amb almenys un dia d'antelació.",
                "Nous serons toujours ravis de vous recommander une adresse précise ou de réserver pour vous — demandez-nous simplement à votre arrivée ou écrivez-nous en amont. Et n'oubliez pas : en juillet et août, la plupart des restaurants demandent de réserver au moins la veille.",
                "We adviseren graag een specifiek adres of reserveren voor u — vraag het bij aankomst of stuur ons vooraf een bericht. En vergeet niet: in juli en augustus moet u bij de meeste restaurants minstens een dag van tevoren reserveren."),

            # alt text
            "Bar Ona beach bar, Tamariu": T(
                "Bar Ona, bar de playa en Tamariu", "Bar Ona, bar de platja a Tamariu",
                "Bar Ona, bar de plage à Tamariu", "Bar Ona, strandbar in Tamariu"),
            "Mossec restaurant, Tamariu": T(
                "Restaurante Mossec, Tamariu", "Restaurant Mossec, Tamariu",
                "Restaurant Mossec, Tamariu", "Restaurant Mossec, Tamariu"),
            "El Palanquí seafood restaurant on the Tamariu seafront": T(
                "El Palanquí, restaurante de pescado en el paseo marítimo de Tamariu",
                "El Palanquí, restaurant de peix al passeig marítim de Tamariu",
                "El Palanquí, restaurant de fruits de mer sur le front de mer de Tamariu",
                "El Palanquí, visrestaurant aan de boulevard van Tamariu"),
            "Royal Restaurant on the Tamariu promenade": T(
                "Royal Restaurant en el paseo marítimo de Tamariu",
                "Royal Restaurant al passeig marítim de Tamariu",
                "Royal Restaurant sur la promenade de Tamariu",
                "Royal Restaurant aan de boulevard van Tamariu"),
            "Hotel Tamariu beach restaurant": T(
                "Restaurante de playa del Hotel Tamariu",
                "Restaurant de platja de l'Hotel Tamariu",
                "Restaurant de plage de l'Hotel Tamariu",
                "Strandrestaurant van Hotel Tamariu"),
            "Es Dofí family restaurant, Tamariu": T(
                "Es Dofí, restaurante familiar en Tamariu",
                "Es Dofí, restaurant familiar a Tamariu",
                "Es Dofí, restaurant familial à Tamariu",
                "Es Dofí, familierestaurant in Tamariu"),
            "El Clot dels Mussols restaurant, Tamariu": T(
                "Restaurante El Clot dels Mussols, Tamariu",
                "Restaurant El Clot dels Mussols, Tamariu",
                "Restaurant El Clot dels Mussols, Tamariu",
                "Restaurant El Clot dels Mussols, Tamariu"),
            "La Pasta pizza and pasta, Tamariu": T(
                "La Pasta, pizza y pasta en Tamariu", "La Pasta, pizza i pasta a Tamariu",
                "La Pasta, pizzas et pâtes à Tamariu", "La Pasta, pizza en pasta in Tamariu"),
            "La Pineda open-air grill among the pines, Tamariu": T(
                "La Pineda, parrilla al aire libre entre los pinos, Tamariu",
                "La Pineda, graella a l'aire lliure entre els pins, Tamariu",
                "La Pineda, grill en plein air au milieu des pins, Tamariu",
                "La Pineda, openluchtgrill tussen de dennen, Tamariu"),
            "Mooma farm restaurant near Palafrugell": T(
                "Mooma, restaurante de masía cerca de Palafrugell",
                "Mooma, restaurant de masia a prop de Palafrugell",
                "Mooma, restaurant à la ferme près de Palafrugell",
                "Mooma, boerderijrestaurant bij Palafrugell"),
            "El Far hotel-restaurant above Llafranc": T(
                "El Far, hotel-restaurante sobre Llafranc",
                "El Far, hotel-restaurant sobre Llafranc",
                "El Far, hôtel-restaurant au-dessus de Llafranc",
                "El Far, hotel-restaurant boven Llafranc"),
            "La Malcontenta restaurant, Calella de Palafrugell": T(
                "Restaurante La Malcontenta, Calella de Palafrugell",
                "Restaurant La Malcontenta, Calella de Palafrugell",
                "Restaurant La Malcontenta, Calella de Palafrugell",
                "Restaurant La Malcontenta, Calella de Palafrugell"),
            "La Xicra restaurant, Palafrugell": T(
                "Restaurante La Xicra, Palafrugell", "Restaurant La Xicra, Palafrugell",
                "Restaurant La Xicra, Palafrugell", "Restaurant La Xicra, Palafrugell"),
            "Alfok restaurant, Esclanyà, Begur": T(
                "Restaurante Alfok, Esclanyà, Begur", "Restaurant Alfok, Esclanyà, Begur",
                "Restaurant Alfok, Esclanyà, Begur", "Restaurant Alfok, Esclanyà, Begur"),
            "Machete's street food, Platja de Pals": T(
                "Machete's, comida callejera en Platja de Pals",
                "Machete's, menjar de carrer a Platja de Pals",
                "Machete's, street food à Platja de Pals",
                "Machete's, streetfood op Platja de Pals"),
            "El Camí de Ronda pizza takeaway, Tamariu": T(
                "El Camí de Ronda, pizzas para llevar en Tamariu",
                "El Camí de Ronda, pizzes per emportar a Tamariu",
                "El Camí de Ronda, pizzas à emporter à Tamariu",
                "El Camí de Ronda, pizza-afhaal in Tamariu"),
            "Boleru Mediterranean takeaway, Tamariu": T(
                "Boleru, comida mediterránea para llevar en Tamariu",
                "Boleru, menjar mediterrani per emportar a Tamariu",
                "Boleru, cuisine méditerranéenne à emporter à Tamariu",
                "Boleru, mediterraans afhaaladres in Tamariu"),
        },
    }
}
