#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""String table for things-to-do/girona.html (carousel + lightbox page)."""

from content_things_to_do import FOOTER_STD


def T(es, ca, fr, nl):
    return {"es": es, "ca": ca, "fr": fr, "nl": nl}


PAGES = {
    "things-to-do/girona.html": {
        "mode": "strings",
        "footer": FOOTER_STD,
        "meta": {
            "es": {"title": "Visitar Girona — Tamariu Chalet",
                   "desc": "Guía de excursión a Girona desde Tamariu Chalet — el casco antiguo medieval, la catedral y el call judío de la capital cultural de la Costa Brava."},
            "ca": {"title": "Visitar Girona — Tamariu Chalet",
                   "desc": "Guia d'excursió a Girona des de Tamariu Chalet — el Barri Vell medieval, la catedral i el call jueu de la capital cultural de la Costa Brava."},
            "fr": {"title": "Visiter Gérone — Tamariu Chalet",
                   "desc": "Guide d'excursion à Gérone depuis le Tamariu Chalet — la vieille ville médiévale, la cathédrale et le quartier juif de la capitale culturelle de la Costa Brava."},
            "nl": {"title": "Bezoek Girona — Tamariu Chalet",
                   "desc": "Dagtripgids naar Girona vanaf Tamariu Chalet — de middeleeuwse oude stad, de kathedraal en de Joodse wijk van de culturele hoofdstad van de Costa Brava."},
        },
        "strings": {
            "Things To Do → Visit Girona": T(
                "Qué Hacer → Visitar Girona", "Què Fer → Visitar Girona",
                "À Faire → Visiter Gérone", "Wat Te Doen → Bezoek Girona"),
            "A Day Trip to Girona": T(
                "Una Excursión a Girona", "Una Excursió a Girona",
                "Une Journée à Gérone", "Een Dagje Girona"),

            "Girona is one of Catalonia's most captivating cities — a place where ancient Roman walls,\n    a medieval Jewish quarter and a magnificent Gothic cathedral sit alongside a thriving\n    contemporary food culture. From Tamariu, it's just 40 minutes by car.": T(
                "Girona es una de las ciudades más cautivadoras de Cataluña — un lugar donde las antiguas murallas romanas, un call judío medieval y una magnífica catedral gótica conviven con una cultura gastronómica contemporánea en plena efervescencia. Desde Tamariu, está a solo 40 minutos en coche.",
                "Girona és una de les ciutats més captivadores de Catalunya — un lloc on les antigues muralles romanes, un call jueu medieval i una magnífica catedral gòtica conviuen amb una cultura gastronòmica contemporània en plena efervescència. Des de Tamariu, és a només 40 minuts en cotxe.",
                "Gérone est l'une des villes les plus captivantes de Catalogne — un lieu où d'anciennes murailles romaines, un quartier juif médiéval et une magnifique cathédrale gothique côtoient une scène gastronomique contemporaine florissante. Depuis Tamariu, elle n'est qu'à 40 minutes en voiture.",
                "Girona is een van de meest betoverende steden van Catalonië — een plek waar oude Romeinse muren, een middeleeuwse Joodse wijk en een schitterende gotische kathedraal samengaan met een bloeiende hedendaagse eetcultuur. Vanuit Tamariu is het slechts 40 minuten rijden."),

            "Distance from Tamariu": T("Distancia desde Tamariu", "Distància des de Tamariu",
                                       "Distance depuis Tamariu", "Afstand vanaf Tamariu"),
            "Drive time": T("Tiempo en coche", "Temps en cotxe",
                            "Temps de trajet", "Rijtijd"),
            "By train from Flaçà": T("En tren desde Flaçà", "En tren des de Flaçà",
                                     "En train depuis Flaçà", "Met de trein vanaf Flaçà"),
            "~40 minutes": T("~40 minutos", "~40 minuts", "~40 minutes", "~40 minuten"),
            "~20 minutes": T("~20 minutos", "~20 minuts", "~20 minutes", "~20 minuten"),

            "Top Things to Do": T("Qué No Perderse", "Què No Us Podeu Perdre",
                                  "À Ne Pas Manquer", "Hoogtepunten"),
            "🏛 The Cathedral &amp; Old Town": T(
                "🏛 La Catedral y el Casco Antiguo", "🏛 La Catedral i el Barri Vell",
                "🏛 La Cathédrale &amp; la Vieille Ville", "🏛 De Kathedraal &amp; Oude Stad"),
            "Girona's cathedral is a masterpiece of Catalan Gothic architecture — its single nave is the widest Gothic vault in the world. Climb the famous flight of 86 steps for a view across the city's terracotta rooftops. The surrounding Barri Vell (Old Town) is a maze of narrow lanes, stone arches and hidden squares.": T(
                "La catedral de Girona es una obra maestra del gótico catalán — su nave única es la bóveda gótica más ancha del mundo. Suba los famosos 86 escalones para contemplar los tejados de terracota de la ciudad. El Barri Vell que la rodea es un laberinto de callejuelas, arcos de piedra y plazas escondidas.",
                "La catedral de Girona és una obra mestra del gòtic català — la seva nau única és la volta gòtica més ampla del món. Pugeu els famosos 86 esglaons per contemplar les teulades de terracota de la ciutat. El Barri Vell que l'envolta és un laberint de carrerons, arcs de pedra i places amagades.",
                "La cathédrale de Gérone est un chef-d'œuvre du gothique catalan — sa nef unique est la plus large voûte gothique du monde. Gravissez les célèbres 86 marches pour admirer les toits de terre cuite de la ville. Le Barri Vell alentour est un dédale de ruelles étroites, d'arcs de pierre et de places cachées.",
                "De kathedraal van Girona is een meesterwerk van Catalaanse gotiek — het eenbeukige schip vormt het breedste gotische gewelf ter wereld. Beklim de beroemde 86 treden voor uitzicht over de terracotta daken van de stad. De omliggende Barri Vell (oude stad) is een doolhof van smalle steegjes, stenen bogen en verborgen pleintjes."),

            "🕍 The Jewish Quarter (El Call)": T(
                "🕍 El Call Judío", "🕍 El Call Jueu",
                "🕍 Le Quartier Juif (El Call)", "🕍 De Joodse Wijk (El Call)"),
            "One of the best-preserved medieval Jewish quarters in Europe, El Call dates from the 9th century. The Museum of Jewish History (Museu d'Història dels Jueus) tells the story of Girona's Jewish community, expelled in 1492. The lanes are hauntingly beautiful and largely unchanged from the Middle Ages.": T(
                "Uno de los barrios judíos medievales mejor conservados de Europa, el Call se remonta al siglo IX. El Museu d'Història dels Jueus cuenta la historia de la comunidad judía de Girona, expulsada en 1492. Las callejuelas tienen una belleza sobrecogedora y apenas han cambiado desde la Edad Media.",
                "Un dels barris jueus medievals més ben conservats d'Europa, el Call es remunta al segle IX. El Museu d'Història dels Jueus explica la història de la comunitat jueva de Girona, expulsada el 1492. Els carrerons tenen una bellesa corprenedora i gairebé no han canviat des de l'edat mitjana.",
                "L'un des quartiers juifs médiévaux les mieux conservés d'Europe, El Call remonte au IXe siècle. Le Musée d'histoire des Juifs (Museu d'Història dels Jueus) retrace l'histoire de la communauté juive de Gérone, expulsée en 1492. Les ruelles sont d'une beauté saisissante et quasiment inchangées depuis le Moyen Âge.",
                "El Call is een van de best bewaarde middeleeuwse Joodse wijken van Europa en gaat terug tot de 9e eeuw. Het Museu d'Història dels Jueus vertelt het verhaal van de Joodse gemeenschap van Girona, in 1492 verdreven. De steegjes zijn aangrijpend mooi en sinds de middeleeuwen nauwelijks veranderd."),

            "🌉 The Coloured Houses (Onyar Riverbank)": T(
                "🌉 Las Casas de Colores (Orillas del Onyar)",
                "🌉 Les Cases de Colors (Vores de l'Onyar)",
                "🌉 Les Maisons Colorées (Bords de l'Onyar)",
                "🌉 De Gekleurde Huizen (Oevers van de Onyar)"),
            "Girona's postcard image — a row of vividly coloured houses reflected in the River Onyar. Walk across the iron footbridges (designed by Gustave Eiffel) for the classic view, then explore the boutiques and cafés lining the riverbanks on both sides.": T(
                "La imagen de postal de Girona — una hilera de casas de colores vivos reflejadas en el río Onyar. Cruce las pasarelas de hierro (diseñadas por Gustave Eiffel) para la vista clásica y después descubra las tiendas y cafeterías de ambas orillas.",
                "La imatge de postal de Girona — una filera de cases de colors vius reflectides al riu Onyar. Travesseu les passarel·les de ferro (dissenyades per Gustave Eiffel) per a la vista clàssica i després descobriu les botigues i cafeteries de totes dues ribes.",
                "L'image de carte postale de Gérone — une rangée de maisons aux couleurs vives se reflétant dans l'Onyar. Traversez les passerelles métalliques (conçues par Gustave Eiffel) pour la vue classique, puis explorez les boutiques et cafés qui bordent les deux rives.",
                "Het ansichtkaartbeeld van Girona — een rij felgekleurde huizen weerspiegeld in de rivier de Onyar. Loop over de ijzeren voetbruggen (ontworpen door Gustave Eiffel) voor het klassieke uitzicht en verken daarna de winkeltjes en cafés langs beide oevers."),

            "🏰 The Arab Baths (Banys Àrabs)": T(
                "🏰 Los Baños Árabes (Banys Àrabs)", "🏰 Els Banys Àrabs",
                "🏰 Les Bains Arabes (Banys Àrabs)", "🏰 De Arabische Baden (Banys Àrabs)"),
            "A remarkably well-preserved 12th-century bathhouse built in the Romanesque style, inspired by earlier Moorish and Roman bathing traditions. The central skylit pool room is particularly beautiful.": T(
                "Unos baños del siglo XII notablemente bien conservados, construidos en estilo románico e inspirados en las tradiciones termales árabes y romanas anteriores. La sala central de la piscina, con su lucernario, es especialmente bella.",
                "Uns banys del segle XII notablement ben conservats, construïts en estil romànic i inspirats en les tradicions termals àrabs i romanes anteriors. La sala central de la piscina, amb el seu lluernari, és especialment bella.",
                "Des bains du XIIe siècle remarquablement conservés, bâtis dans le style roman et inspirés des traditions thermales mauresques et romaines antérieures. La salle centrale du bassin, éclairée par un lanterneau, est particulièrement belle.",
                "Een opmerkelijk goed bewaard badhuis uit de 12e eeuw in romaanse stijl, geïnspireerd op eerdere Moorse en Romeinse badtradities. De centrale badzaal met bovenlicht is bijzonder mooi."),

            "🌿 The City Walls": T("🌿 Las Murallas", "🌿 Les Muralles",
                                   "🌿 Les Remparts", "🌿 De Stadsmuren"),
            "Walk a section of Girona's ancient Roman walls for sweeping views over the city and surrounding plains. The walk is free and the panorama on a clear day stretches all the way to the Pyrenees.": T(
                "Recorra un tramo de las antiguas murallas romanas de Girona para disfrutar de amplias vistas sobre la ciudad y la llanura circundante. El paseo es gratuito y, en un día despejado, la panorámica llega hasta los Pirineos.",
                "Recorreu un tram de les antigues muralles romanes de Girona per gaudir d'àmplies vistes sobre la ciutat i la plana del voltant. La passejada és gratuïta i, en un dia clar, la panoràmica arriba fins als Pirineus.",
                "Parcourez une portion des anciennes murailles romaines de Gérone pour de vastes vues sur la ville et la plaine alentour. La promenade est gratuite et, par temps clair, le panorama s'étend jusqu'aux Pyrénées.",
                "Loop een stuk over de oude Romeinse stadsmuren van Girona voor weidse uitzichten over de stad en de omliggende vlakte. De wandeling is gratis en op een heldere dag reikt het panorama tot aan de Pyreneeën."),

            "Girona in Pictures": T("Girona en Imágenes", "Girona en Imatges",
                                    "Gérone en Images", "Girona in Beeld"),
            "Click any image to view full size &mdash; use arrows to browse": T(
                "Haga clic en cualquier imagen para verla a tamaño completo &mdash; use las flechas para navegar",
                "Feu clic en qualsevol imatge per veure-la a mida completa &mdash; feu servir les fletxes per navegar",
                "Cliquez sur une image pour l'afficher en grand &mdash; utilisez les flèches pour naviguer",
                "Klik op een afbeelding voor volledige weergave &mdash; gebruik de pijlen om te bladeren"),

            # Carousel captions (also appear in the lightbox script)
            "The Cathedral": T("La Catedral", "La Catedral",
                               "La Cathédrale", "De Kathedraal"),
            "The Jewish Quarter (El Call)": T(
                "El Call Judío", "El Call Jueu",
                "Le Quartier Juif (El Call)", "De Joodse Wijk (El Call)"),
            "River Onyar &mdash; Coloured Houses": T(
                "Río Onyar &mdash; Casas de Colores", "Riu Onyar &mdash; Cases de Colors",
                "L'Onyar &mdash; Maisons Colorées", "Rivier de Onyar &mdash; Gekleurde Huizen"),
            "The Arab Baths (Banys &Agrave;rabs)": T(
                "Los Baños Árabes (Banys &Agrave;rabs)", "Els Banys &Agrave;rabs",
                "Les Bains Arabes (Banys &Agrave;rabs)", "De Arabische Baden (Banys &Agrave;rabs)"),
            "The City Walls": T("Las Murallas", "Les Muralles",
                                "Les Remparts", "De Stadsmuren"),
            "Girona Old Town Map": T(
                "Mapa del Casco Antiguo de Girona", "Mapa del Barri Vell de Girona",
                "Plan de la Vieille Ville de Gérone", "Plattegrond Oude Stad Girona"),

            # alt text
            "Girona Cathedral": T("Catedral de Girona", "Catedral de Girona",
                                  "Cathédrale de Gérone", "Kathedraal van Girona"),
            "The Jewish Quarter, Girona": T(
                "El call judío, Girona", "El call jueu, Girona",
                "Le quartier juif, Gérone", "De Joodse wijk, Girona"),
            "Coloured houses on the River Onyar, Girona": T(
                "Casas de colores en el río Onyar, Girona",
                "Cases de colors al riu Onyar, Girona",
                "Maisons colorées sur l'Onyar, Gérone",
                "Gekleurde huizen aan de Onyar, Girona"),
            "Pujada de Sant Martí, Girona": T(
                "Pujada de Sant Martí, Girona", "Pujada de Sant Martí, Girona",
                "Pujada de Sant Martí, Gérone", "Pujada de Sant Martí, Girona"),
            "The Arab Baths, Girona": T(
                "Los baños árabes, Girona", "Els banys àrabs, Girona",
                "Les bains arabes, Gérone", "De Arabische baden, Girona"),
            "The City Walls, Girona": T(
                "Las murallas, Girona", "Les muralles, Girona",
                "Les remparts, Gérone", "De stadsmuren, Girona"),
            "Map of Girona old town": T(
                "Mapa del casco antiguo de Girona", "Mapa del Barri Vell de Girona",
                "Plan de la vieille ville de Gérone", "Plattegrond van de oude stad van Girona"),

            "Previous": T("Anterior", "Anterior", "Précédent", "Vorige"),
            "Next": T("Siguiente", "Següent", "Suivant", "Volgende"),
            "Close": T("Cerrar", "Tancar", "Fermer", "Sluiten"),

            "Recommended Restaurants in Girona": T(
                "Restaurantes Recomendados en Girona",
                "Restaurants Recomanats a Girona",
                "Restaurants Recommandés à Gérone",
                "Aanbevolen Restaurants in Girona"),
            "One of the world's greatest restaurants, run by the three Roca brothers. Booking is essential — often months in advance. A once-in-a-lifetime dining experience combining technical brilliance with deep Catalan roots.": T(
                "Uno de los mejores restaurantes del mundo, dirigido por los tres hermanos Roca. Es imprescindible reservar — a menudo con meses de antelación. Una experiencia gastronómica irrepetible que combina brillantez técnica con hondas raíces catalanas.",
                "Un dels millors restaurants del món, dirigit pels tres germans Roca. És imprescindible reservar — sovint amb mesos d'antelació. Una experiència gastronòmica irrepetible que combina brillantor tècnica amb arrels catalanes profundes.",
                "L'un des plus grands restaurants du monde, tenu par les trois frères Roca. La réservation est indispensable — souvent des mois à l'avance. Une expérience gastronomique unique, alliant virtuosité technique et profondes racines catalanes.",
                "Een van de beste restaurants ter wereld, gerund door de drie gebroeders Roca. Reserveren is noodzakelijk — vaak maanden vooruit. Een eenmalige eetervaring die technische virtuositeit combineert met diepe Catalaanse wortels."),
            "An excellent wine bar and restaurant in the Old Town, with an outstanding selection of Catalan and Spanish wines paired with creative tapas and small plates. Relaxed atmosphere, great value.": T(
                "Un excelente bar de vinos y restaurante en el casco antiguo, con una selección extraordinaria de vinos catalanes y españoles acompañados de tapas creativas y platillos. Ambiente relajado y muy buena relación calidad-precio.",
                "Un excel·lent bar de vins i restaurant al Barri Vell, amb una selecció extraordinària de vins catalans i espanyols acompanyats de tapes creatives i platets. Ambient relaxat i molt bona relació qualitat-preu.",
                "Un excellent bar à vins et restaurant de la vieille ville, avec une sélection remarquable de vins catalans et espagnols accompagnés de tapas créatives et de petites assiettes. Ambiance détendue, excellent rapport qualité-prix.",
                "Een uitstekende wijnbar annex restaurant in de oude stad, met een prachtige selectie Catalaanse en Spaanse wijnen bij creatieve tapas en kleine gerechten. Ontspannen sfeer, goede prijs-kwaliteitverhouding."),
            "Modern Catalan cooking in a stylish setting near the cathedral. The tasting menu showcases the best local produce — great for a special dinner before heading back to Tamariu.": T(
                "Cocina catalana moderna en un espacio con estilo cerca de la catedral. El menú degustación luce lo mejor del producto local — ideal para una cena especial antes de volver a Tamariu.",
                "Cuina catalana moderna en un espai amb estil a prop de la catedral. El menú de degustació llueix el millor del producte local — ideal per a un sopar especial abans de tornar a Tamariu.",
                "Cuisine catalane moderne dans un cadre élégant près de la cathédrale. Le menu dégustation met en valeur les meilleurs produits locaux — parfait pour un dîner d'exception avant de rentrer à Tamariu.",
                "Moderne Catalaanse keuken in een stijlvolle setting vlak bij de kathedraal. Het proefmenu laat de beste lokale producten zien — ideaal voor een bijzonder diner voordat u terugkeert naar Tamariu."),
            "A charming, informal bistro in the Jewish Quarter — ideal for a long lunch of salads, open sandwiches and simple Catalan dishes. Popular with locals at lunchtime.": T(
                "Un bistró encantador e informal en el call judío — ideal para una comida larga a base de ensaladas, tostas y platos catalanes sencillos. Muy popular entre los locales al mediodía.",
                "Un bistró encantador i informal al call jueu — ideal per a un dinar llarg a base d'amanides, torrades i plats catalans senzills. Molt popular entre la gent del país al migdia.",
                "Un bistrot charmant et informel dans le quartier juif — idéal pour un long déjeuner de salades, tartines et plats catalans simples. Très prisé des habitants le midi.",
                "Een charmante, informele bistro in de Joodse wijk — ideaal voor een lange lunch met salades, belegde boterhammen en eenvoudige Catalaanse gerechten. Populair bij de lokale bevolking tijdens de lunch."),
            "Famous for its creative montaditos (small open sandwiches) and warm, buzzy atmosphere. Expect a queue at peak times — worth every minute.": T(
                "Famoso por sus montaditos creativos y su ambiente cálido y bullicioso. Espere cola en las horas punta — merece cada minuto.",
                "Famós pels seus montaditos creatius i pel seu ambient càlid i bulliciós. Espereu cua a les hores punta — val cada minut.",
                "Réputé pour ses montaditos créatifs et son ambiance chaleureuse et animée. Attendez-vous à faire la queue aux heures de pointe — cela en vaut la peine.",
                "Beroemd om zijn creatieve montaditos en warme, levendige sfeer. Reken op een rij tijdens piekuren — elke minuut waard."),
        },
    }
}
