#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
things-to-do/local-beaches.html — prose translations.

Short field labels live in content_beaches_labels.py. Beach names, restaurant
names, street addresses, Catalan dish names (arròs de Pals, gambes de Palamós)
and the phrase camí de ronda are deliberately left untranslated.
"""

from content_things_to_do import FOOTER_STD
from content_beaches_labels import LABELS


def T(es, ca, fr, nl):
    return {"es": es, "ca": ca, "fr": fr, "nl": nl}


PROSE = {
    "One of the great luxuries of staying in Tamariu is that you are not limited to one beach. Within half an hour's drive there are a dozen quite different stretches of coast — hidden coves reached only on foot, long pine-backed sands you could lose a family on, and pretty fishing villages where lunch is served a few metres from the water. Here is our honest guide to each of them: what it's like, where to eat, and how far it is from the chalet.": T(
        "Uno de los grandes lujos de alojarse en Tamariu es que no está limitado a una sola playa. A menos de media hora en coche hay una docena de tramos de costa bien distintos — calas escondidas a las que solo se llega a pie, largos arenales entre pinos donde se pierde a la familia, y bonitos pueblos pesqueros donde se come a unos metros del agua. Esta es nuestra guía honesta de cada uno: cómo son, dónde comer y a qué distancia están de la casa.",
        "Un dels grans luxes d'allotjar-se a Tamariu és que no esteu limitats a una sola platja. A menys de mitja hora en cotxe hi ha una dotzena de trams de costa ben diferents — cales amagades on només s'arriba a peu, llargs arenals entre pins on es perd la família, i bonics pobles pescadors on es menja a pocs metres de l'aigua. Aquesta és la nostra guia honesta de cadascun: com són, on menjar i a quina distància són de la casa.",
        "L'un des grands luxes d'un séjour à Tamariu, c'est de n'être pas limité à une seule plage. À moins d'une demi-heure de route s'étendent une douzaine de littoraux bien différents — criques cachées accessibles seulement à pied, longues plages bordées de pins où l'on perdrait une famille, et jolis villages de pêcheurs où l'on déjeune à quelques mètres de l'eau. Voici notre guide honnête de chacune : à quoi elles ressemblent, où manger, et à quelle distance elles se trouvent de la maison.",
        "Een van de grote luxes van een verblijf in Tamariu is dat u niet gebonden bent aan één strand. Binnen een half uur rijden liggen een dozijn heel verschillende stukken kust — verborgen baaien die alleen te voet bereikbaar zijn, lange zandstranden met dennen erachter waar u een heel gezin kwijtraakt, en mooie vissersdorpjes waar u een paar meter van het water eet. Dit is onze eerlijke gids voor elk daarvan: hoe het er is, waar u kunt eten, en hoe ver het is vanaf het huis."),

    "Three beaches you can reach from the chalet without ever starting the car — one at the bottom of the hill, two along the coastal footpath.": T(
        "Tres playas a las que puede llegar desde la casa sin arrancar el coche — una al pie de la cuesta y dos por el camino de ronda.",
        "Tres platges a les quals podeu arribar des de la casa sense engegar el cotxe — una al peu del turó i dues pel camí de ronda.",
        "Trois plages accessibles depuis la maison sans jamais démarrer la voiture — une en bas de la côte, deux par le chemin de ronde.",
        "Drie stranden die u vanaf het huis bereikt zonder de auto te starten — één onder aan de heuvel, twee via het kustpad."),

    # ── Tamariu ──────────────────────────────────────────────────────────
    "A perfect crescent of pale sand about 175 metres long, held between two pine-covered headlands and lined with a low, unhurried promenade. Tamariu has never been allowed to grow — there are no high-rise blocks, no traffic on the front, and the fishing boats are still pulled up at the north end. The water is exceptionally clear and shelves gently, which makes it one of the safest family beaches on this stretch of coast.": T(
        "Una media luna perfecta de arena clara de unos 175 metros, encajada entre dos puntas cubiertas de pinos y bordeada por un paseo bajo y sin prisas. A Tamariu nunca se le ha permitido crecer — no hay bloques altos, no hay tráfico en el frente marítimo y las barcas de pesca siguen varadas en el extremo norte. El agua es excepcionalmente clara y entra en pendiente suave, lo que la convierte en una de las playas más seguras para familias de este tramo de costa.",
        "Una mitja lluna perfecta de sorra clara d'uns 175 metres, encaixada entre dues puntes cobertes de pins i vorejada per un passeig baix i sense presses. A Tamariu mai se li ha permès créixer — no hi ha blocs alts, no hi ha trànsit al front marítim i les barques de pesca continuen varades a l'extrem nord. L'aigua és excepcionalment clara i entra amb pendent suau, cosa que la converteix en una de les platges més segures per a famílies d'aquest tram de costa.",
        "Un croissant parfait de sable clair d'environ 175 mètres, serti entre deux pointes couvertes de pins et bordé d'une promenade basse et paisible. Tamariu n'a jamais eu le droit de grandir — pas d'immeubles, pas de circulation sur le front de mer, et les barques de pêche sont toujours tirées au sec à l'extrémité nord. L'eau est d'une clarté exceptionnelle et descend en pente douce, ce qui en fait l'une des plages les plus sûres pour les familles sur cette portion de côte.",
        "Een perfecte sikkel van bleek zand van zo'n 175 meter, ingeklemd tussen twee met dennen begroeide landtongen en omzoomd door een lage, ontspannen boulevard. Tamariu heeft nooit mogen groeien — er zijn geen hoogbouwflats, geen verkeer aan de boulevard, en de vissersboten liggen nog steeds op het noordelijke uiteinde. Het water is uitzonderlijk helder en loopt geleidelijk af, wat dit tot een van de veiligste gezinsstranden van deze kuststrook maakt."),

    "It faces east, so mornings are bright and sheltered and the afternoons fall pleasantly into shade under the cliffs. Snorkelling around the rocks at either end is superb — you'll find wrasse, octopus and the occasional cuttlefish within a few metres of the sand. Sunbeds, kayaks and paddleboards can be hired on the beach in season, and there's a small diving centre.": T(
        "Mira al este, así que las mañanas son luminosas y resguardadas y las tardes caen agradablemente en sombra bajo los acantilados. El snorkel alrededor de las rocas de ambos extremos es magnífico — encontrará tordos, pulpos y alguna sepia a pocos metros de la arena. En temporada se alquilan hamacas, kayaks y tablas de paddle en la playa, y hay un pequeño centro de buceo.",
        "Mira a llevant, així que els matins són lluminosos i arrecerats i les tardes cauen agradablement a l'ombra sota els penya-segats. El snorkel al voltant de les roques dels dos extrems és magnífic — hi trobareu tords, pops i alguna sípia a pocs metres de la sorra. En temporada es lloguen gandules, caiacs i taules de paddle a la platja, i hi ha un petit centre de submarinisme.",
        "Elle est exposée à l'est : les matinées y sont lumineuses et abritées, et les après-midis basculent agréablement à l'ombre des falaises. Le snorkeling autour des rochers, aux deux extrémités, est superbe — vous verrez des labres, des poulpes et parfois une seiche à quelques mètres du sable. Transats, kayaks et paddles se louent sur la plage en saison, et il y a un petit centre de plongée.",
        "Het strand ligt op het oosten, dus de ochtenden zijn helder en beschut en in de middag valt het aangenaam in de schaduw onder de kliffen. Snorkelen bij de rotsen aan beide uiteinden is prachtig — u vindt lipvissen, octopussen en af en toe een zeekat op enkele meters van het zand. In het seizoen kunt u op het strand ligbedden, kajaks en supboards huren, en er is een klein duikcentrum."),

    "The seafront and the streets immediately behind the beach are": T(
        "El paseo marítimo y las calles justo detrás de la playa son",
        "El passeig marítim i els carrers just darrere de la platja són",
        "Le front de mer et les rues juste derrière la plage sont en",
        "De boulevard en de straten direct achter het strand zijn"),
    "(paid) from roughly June to September, and there is a small manned car park by the beach. Spaces near the sand are gone by mid-morning in July and August.": T(
        "(de pago) aproximadamente de junio a septiembre, y hay un pequeño aparcamiento vigilado junto a la playa. En julio y agosto las plazas cercanas a la arena se agotan a media mañana.",
        "(de pagament) aproximadament de juny a setembre, i hi ha un petit aparcament vigilat vora la platja. El juliol i l'agost les places properes a la sorra s'esgoten a mig matí.",
        "(payante) de juin à septembre environ, et il y a un petit parking surveillé près de la plage. En juillet et août, les places proches du sable sont prises dès la fin de matinée.",
        "(betaald) van ongeveer juni tot september, en er is een kleine bewaakte parkeerplaats bij het strand. In juli en augustus zijn de plekken bij het zand halverwege de ochtend bezet."),
    "park higher up on the road climbing out of the village towards Aiguablava and walk down — five to ten minutes, and free all year. Outside the summer months the blue zone is free too.": T(
        "aparque más arriba, en la carretera que sube del pueblo hacia Aiguablava, y baje andando — cinco o diez minutos, y gratuito todo el año. Fuera de los meses de verano la zona azul también es gratuita.",
        "aparqueu més amunt, a la carretera que puja del poble cap a Aiguablava, i baixeu a peu — cinc o deu minuts, i gratuït tot l'any. Fora dels mesos d'estiu la zona blava també és gratuïta.",
        "garez-vous plus haut, sur la route qui monte du village vers Aiguablava, et descendez à pied — cinq à dix minutes, gratuit toute l'année. Hors des mois d'été, la zone bleue est gratuite elle aussi.",
        "parkeer hogerop aan de weg die het dorp uit klimt richting Aiguablava en loop naar beneden — vijf tot tien minuten, en het hele jaar gratis. Buiten de zomermaanden is de blauwe zone ook gratis."),
    "— the star of the seafront. Terrace at the water's edge; order the paella or the lobster rice. Book ahead in summer.": T(
        "— la estrella del paseo marítimo. Terraza al borde del agua; pida la paella o el arroz de langosta. Reserve con antelación en verano.",
        "— l'estrella del passeig marítim. Terrassa arran d'aigua; demaneu la paella o l'arròs de llagosta. Reserveu amb antelació a l'estiu.",
        "— la vedette du front de mer. Terrasse au bord de l'eau ; commandez la paella ou le riz au homard. Réservez à l'avance en été.",
        "— de ster van de boulevard. Terras aan het water; bestel de paella of de kreeftenrijst. Reserveer in de zomer vooraf."),
    "— a reliable beachfront institution; excellent croquettes and mussels, family paella with a day's notice.": T(
        "— una institución fiable del paseo; croquetas y mejillones excelentes, paella familiar avisando con un día.",
        "— una institució fiable del passeig; croquetes i musclos excel·lents, paella familiar avisant amb un dia.",
        "— une institution fiable du front de mer ; excellentes croquettes et moules, paella familiale à commander la veille.",
        "— een betrouwbare instelling aan het strand; uitstekende kroketten en mosselen, familiepaella op bestelling een dag vooraf."),
    "— the liveliest spot at the beach edge, all day from breakfast to cocktails.": T(
        "— el sitio más animado junto a la playa, todo el día del desayuno a los cócteles.",
        "— el lloc més animat arran de platja, tot el dia de l'esmorzar als còctels.",
        "— l'adresse la plus animée en bord de plage, du petit-déjeuner aux cocktails.",
        "— de levendigste plek aan de rand van het strand, de hele dag van ontbijt tot cocktails."),
    "— the village's best-kept secret, loved by locals for its": T(
        "— el secreto mejor guardado del pueblo, querido por la gente de aquí por su",
        "— el secret més ben guardat del poble, estimat per la gent d'aquí pel seu",
        "— le secret le mieux gardé du village, adoré des habitants pour son",
        "— het best bewaarde geheim van het dorp, geliefd bij locals om zijn"),

    # ── Cala Pedrosa ─────────────────────────────────────────────────────
    "The reward at the end of the finest short walk in the area. Cala Pedrosa cannot be reached by road at all — you get there along the": T(
        "La recompensa al final del mejor paseo corto de la zona. A Cala Pedrosa no se llega por carretera de ninguna manera — se accede por el",
        "La recompensa al final de la millor passejada curta de la zona. A Cala Pedrosa no s'hi arriba per carretera de cap manera — s'hi accedeix pel",
        "La récompense au bout de la plus belle courte randonnée du secteur. Cala Pedrosa n'est pas accessible par la route — on y arrive par le",
        "De beloning aan het eind van de mooiste korte wandeling in de omgeving. Cala Pedrosa is helemaal niet per weg bereikbaar — u komt er via het"),
    "heading south out of Tamariu, a narrow path that climbs through pine and holm oak with the sea flashing below, then drops down a steep final scramble into a tiny shingle cove hemmed in by cliffs.": T(
        "hacia el sur desde Tamariu, un sendero estrecho que sube entre pinos y encinas con el mar destellando abajo, y luego baja en un último tramo empinado hasta una diminuta cala de grava encajada entre acantilados.",
        "cap al sud des de Tamariu, un camí estret que puja entre pins i alzines amb el mar espurnejant a sota, i després baixa en un darrer tram costerut fins a una diminuta cala de grava encaixada entre penya-segats.",
        "vers le sud depuis Tamariu, un sentier étroit qui grimpe entre pins et chênes verts, la mer scintillant en contrebas, avant de plonger par une dernière descente raide dans une minuscule crique de galets enserrée par les falaises.",
        "zuidwaarts vanuit Tamariu, een smal pad dat door dennen en steeneiken omhoog klimt met de zee glinsterend beneden, en daarna via een steile laatste afdaling uitkomt in een piepkleine grindbaai ingesloten door kliffen."),
    "It is small, quiet and dazzlingly clear — a favourite of snorkellers and of boats that anchor just offshore. There is no sand to speak of, so bring a mat, and wear proper shoes for the descent; the last section is genuinely steep and unsuitable for young children or anyone unsteady. Go early, take water, and you may well have it almost to yourself.": T(
        "Es pequeña, tranquila y de una transparencia deslumbrante — favorita de quienes hacen snorkel y de las barcas que fondean justo enfrente. No hay arena propiamente dicha, así que lleve una esterilla, y calce zapato adecuado para la bajada; el último tramo es realmente empinado y no apto para niños pequeños ni para quien no vaya seguro. Vaya temprano, lleve agua y es muy probable que la tenga casi para usted solo.",
        "És petita, tranquil·la i d'una transparència enlluernadora — preferida de qui fa snorkel i de les barques que fondegen just al davant. No hi ha sorra pròpiament dita, així que porteu una estora, i calceu sabata adequada per a la baixada; el darrer tram és realment costerut i no apte per a nens petits ni per a qui no vagi segur. Aneu-hi aviat, porteu aigua i és molt probable que la tingueu gairebé per a vosaltres sols.",
        "Elle est petite, tranquille et d'une clarté éblouissante — la préférée des amateurs de snorkeling et des bateaux qui mouillent au large. Il n'y a pas vraiment de sable : prévoyez un tapis, et de vraies chaussures pour la descente ; la dernière portion est franchement raide et déconseillée aux jeunes enfants comme à qui manque d'assurance. Venez tôt, emportez de l'eau, et vous l'aurez sans doute presque pour vous.",
        "Hij is klein, rustig en oogverblindend helder — een favoriet van snorkelaars en van boten die er vlak voor de kust ankeren. Er is nauwelijks zand, dus neem een matje mee, en trek stevige schoenen aan voor de afdaling; het laatste stuk is echt steil en niet geschikt voor jonge kinderen of voor wie onvast ter been is. Ga vroeg, neem water mee, en de kans is groot dat u hem bijna voor uzelf hebt."),
    "There is no parking at Cala Pedrosa — the cove is reached only on foot along the camí de ronda.": T(
        "No hay aparcamiento en Cala Pedrosa — a la cala solo se llega a pie por el camí de ronda.",
        "No hi ha aparcament a Cala Pedrosa — a la cala només s'hi arriba a peu pel camí de ronda.",
        "Il n'y a pas de stationnement à Cala Pedrosa — on n'y accède qu'à pied par le camí de ronda.",
        "Er is geen parkeergelegenheid bij Cala Pedrosa — de baai is alleen te voet bereikbaar via het camí de ronda."),
    "leave the car in Tamariu (upper village streets) and walk the coastal path south, about 35–40 minutes. From the Llafranc side, park free near the Far de Sant Sebastià approach and walk north.": T(
        "deje el coche en Tamariu (calles de la parte alta) y siga el camino de ronda hacia el sur, unos 35–40 minutos. Desde el lado de Llafranc, aparque gratis cerca del acceso al Far de Sant Sebastià y camine hacia el norte.",
        "deixeu el cotxe a Tamariu (carrers de la part alta) i seguiu el camí de ronda cap al sud, uns 35–40 minuts. Des del costat de Llafranc, aparqueu gratis a prop de l'accés al Far de Sant Sebastià i camineu cap al nord.",
        "laissez la voiture à Tamariu (rues du haut du village) et suivez le chemin côtier vers le sud, 35 à 40 minutes environ. Côté Llafranc, garez-vous gratuitement près de l'accès au Far de Sant Sebastià et marchez vers le nord.",
        "laat de auto in Tamariu staan (straten in het hoger gelegen deel) en loop het kustpad zuidwaarts, ongeveer 35–40 minuten. Vanaf de kant van Llafranc parkeert u gratis bij de toegang naar de Far de Sant Sebastià en loopt u noordwaarts."),
    "sometimes operates at the cove in high season — charming, but don't rely on it. Check locally before setting off.": T(
        "a veces funciona en la cala en plena temporada — encantador, pero no cuente con ello. Compruébelo antes de salir.",
        "de vegades funciona a la cala en plena temporada — encantador, però no hi compteu. Comproveu-ho abans de sortir.",
        "fonctionne parfois à la crique en haute saison — charmant, mais n'y comptez pas. Renseignez-vous avant de partir.",
        "is in het hoogseizoen soms open bij de baai — charmant, maar reken er niet op. Informeer voor u vertrekt."),
    "— the obvious plan is to walk out in the morning and come back for a long late lunch at El Palanquí or Royal.": T(
        "— el plan evidente es ir andando por la mañana y volver para una comida larga y tardía en El Palanquí o Royal.",
        "— el pla evident és anar-hi a peu al matí i tornar per a un dinar llarg i tardà a El Palanquí o Royal.",
        "— le plan évident : y aller à pied le matin et revenir pour un long déjeuner tardif à El Palanquí ou Royal.",
        "— het voor de hand liggende plan is 's ochtends heen lopen en terugkomen voor een lange, late lunch bij El Palanquí of Royal."),

    # ── Aiguablava ───────────────────────────────────────────────────────
    '"Blue water", and it earns the name — a short, sheltered bay of pale sand where the sea turns an almost implausible turquoise over the light seabed. It is the most celebrated cove on this stretch of coast and appears on half the postcards in the region, with pine-covered slopes and white villas rising steeply on either side.': T(
        "«Agua azul», y se gana el nombre — una bahía corta y resguardada de arena clara donde el mar se vuelve de un turquesa casi inverosímil sobre el fondo claro. Es la cala más célebre de este tramo de costa y aparece en la mitad de las postales de la comarca, con laderas de pinos y villas blancas que suben empinadas a ambos lados.",
        "«Aigua blava», i es guanya el nom — una badia curta i arrecerada de sorra clara on el mar es torna d'un turquesa gairebé inversemblant sobre el fons clar. És la cala més cèlebre d'aquest tram de costa i surt a la meitat de les postals de la comarca, amb vessants de pins i vil·les blanques que pugen costerudes a banda i banda.",
        "« Eau bleue », et elle mérite son nom — une baie courte et abritée de sable clair où la mer prend un turquoise presque invraisemblable sur le fond clair. C'est la crique la plus célèbre de cette portion de côte, présente sur la moitié des cartes postales de la région, avec des pentes couvertes de pins et des villas blanches qui s'élèvent de part et d'autre.",
        "\"Blauw water\", en die naam is verdiend — een korte, beschutte baai met bleek zand waar de zee boven de lichte bodem een bijna ongelooflijk turquoise aanneemt. Het is de beroemdste baai van deze kuststrook en staat op de helft van de ansichtkaarten in de regio, met met dennen begroeide hellingen en witte villa's die aan weerszijden steil oprijzen."),
    "The main beach is compact and gets very full in August, but the water is calm and shallow, ideal for children and for snorkelling around the edges. Next door, the smaller inlet of": T(
        "La playa principal es compacta y se llena mucho en agosto, pero el agua es tranquila y poco profunda, ideal para niños y para hacer snorkel por los bordes. Al lado, la ensenada más pequeña de",
        "La platja principal és compacta i s'omple molt a l'agost, però l'aigua és tranquil·la i poc profunda, ideal per a nens i per fer snorkel pels vorals. Al costat, la cala més petita de",
        "La plage principale est compacte et se remplit beaucoup en août, mais l'eau est calme et peu profonde, idéale pour les enfants et pour le snorkeling sur les bords. Juste à côté, la plus petite anse de",
        "Het hoofdstrand is compact en loopt in augustus flink vol, maar het water is kalm en ondiep, ideaal voor kinderen en om langs de randen te snorkelen. Ernaast heeft de kleinere inham"),
    "has a tiny harbour and its own charm, and the state-run Parador hotel occupies the headland above with a spectacular outlook. Boat trips run from here along the coast in summer.": T(
        "tiene un puertecito y su propio encanto, y el Parador estatal ocupa la punta de arriba con unas vistas espectaculares. En verano salen de aquí paseos en barco por la costa.",
        "té un portet i el seu propi encant, i el Parador estatal ocupa la punta de dalt amb unes vistes espectaculars. A l'estiu surten d'aquí passejades en barca per la costa.",
        "possède un petit port et un charme propre, et le Parador d'État occupe la pointe au-dessus avec un panorama spectaculaire. Des sorties en bateau partent d'ici le long de la côte en été.",
        "een haventje en zijn eigen charme, en het staatshotel Parador ligt op de landtong erboven met een spectaculair uitzicht. In de zomer vertrekken hier boottochten langs de kust."),
    "A small pay-and-display car park sits at the entrance to the cove, under 100 m from the sand. In July and August it is full between 09:00 and 10:00.": T(
        "Hay un pequeño aparcamiento de pago con tique a la entrada de la cala, a menos de 100 m de la arena. En julio y agosto se llena entre las 09:00 y las 10:00.",
        "Hi ha un petit aparcament de pagament amb tiquet a l'entrada de la cala, a menys de 100 m de la sorra. El juliol i l'agost s'omple entre les 09:00 i les 10:00.",
        "Un petit parking payant se trouve à l'entrée de la crique, à moins de 100 m du sable. En juillet et août, il est plein entre 9h00 et 10h00.",
        "Bij de ingang van de baai ligt een kleine betaalde parkeerplaats, op minder dan 100 m van het zand. In juli en augustus is die tussen 09:00 en 10:00 vol."),
    "there is limited free roadside parking on the approach above Fornells — arrive early. Otherwise Begur runs a €1 beach shuttle from the town car parks to Aiguablava, Sa Riera and Sa Tuna through the summer.": T(
        "hay aparcamiento gratuito limitado en el arcén del acceso sobre Fornells — llegue temprano. Si no, Begur ofrece en verano una lanzadera de playa de 1 € desde los aparcamientos del pueblo hasta Aiguablava, Sa Riera y Sa Tuna.",
        "hi ha aparcament gratuït limitat al voral de l'accés sobre Fornells — arribeu-hi aviat. Si no, Begur ofereix a l'estiu una llançadora de platja d'1 € des dels aparcaments del poble fins a Aiguablava, Sa Riera i Sa Tuna.",
        "il y a un stationnement gratuit limité en bord de route sur l'accès au-dessus de Fornells — arrivez tôt. Sinon, Begur propose en été une navette de plage à 1 € depuis les parkings du village vers Aiguablava, Sa Riera et Sa Tuna.",
        "er is beperkt gratis parkeren langs de weg op de aanrijroute boven Fornells — kom vroeg. Anders rijdt Begur in de zomer een strandpendel van €1 vanaf de parkeerplaatsen van het stadje naar Aiguablava, Sa Riera en Sa Tuna."),
    "— right on the sand at Aiguablava and something of a legend: fish and seafood grilled over oak charcoal, rice dishes finished in a wood oven. You can even arrive by boat. Book well ahead.": T(
        "— en plena arena de Aiguablava y ya casi una leyenda: pescado y marisco a la brasa de encina, arroces acabados en horno de leña. Incluso se puede llegar en barca. Reserve con mucha antelación.",
        "— en plena sorra d'Aiguablava i ja gairebé una llegenda: peix i marisc a la brasa d'alzina, arrossos acabats al forn de llenya. Fins i tot s'hi pot arribar amb barca. Reserveu amb molta antelació.",
        "— les pieds dans le sable à Aiguablava et déjà une légende : poissons et fruits de mer grillés au charbon de chêne, riz terminés au four à bois. On peut même y arriver en bateau. Réservez bien à l'avance.",
        "— pal op het zand van Aiguablava en inmiddels bijna een legende: vis en zeevruchten gegrild op eikenhoutskool, rijstgerechten afgemaakt in een houtoven. U kunt er zelfs per boot komen. Reserveer ruim vooraf."),
    "— relaxed terrace dining just above the bay.": T(
        "— comida relajada en terraza justo encima de la bahía.",
        "— àpat relaxat en terrassa just damunt de la badia.",
        "— repas détendu en terrasse juste au-dessus de la baie.",
        "— ontspannen eten op het terras net boven de baai."),
    "— on the headland, with an unmatched panorama; good for a drink at sunset even if you don't eat.": T(
        "— en la punta, con una panorámica insuperable; buen sitio para una copa al atardecer aunque no coma.",
        "— a la punta, amb una panoràmica insuperable; bon lloc per a una copa a la posta de sol encara que no hi mengeu.",
        "— sur la pointe, avec un panorama inégalé ; parfait pour un verre au coucher du soleil, même sans y manger.",
        "— op de landtong, met een weergaloos panorama; ook zonder te eten een goede plek voor een drankje bij zonsondergang."),

    # ── Aigua Xelida ─────────────────────────────────────────────────────
    'The name means "chilled water" in old Catalan, after the cold freshwater springs that seep into the bay — and it is noticeably cooler than the beaches either side of it. Aigua Xelida is really a cluster of tiny pebble inlets and flat rock platforms just north of Tamariu, backed by a scatter of low white villas and a great many pines. There is a small slipway and a handful of moored boats, and that is about the extent of the development.': T(
        "El nombre significa «agua helada» en catalán antiguo, por los manantiales fríos de agua dulce que se filtran en la cala — y se nota más fresca que las playas de al lado. Aigua Xelida es en realidad un conjunto de diminutas calas de cantos y plataformas de roca lisa justo al norte de Tamariu, con unas pocas villas blancas bajas detrás y muchísimos pinos. Hay una pequeña rampa y un puñado de barcas amarradas, y ahí acaba prácticamente la urbanización.",
        "El nom significa «aigua gelada» en català antic, pels brolladors freds d'aigua dolça que s'infiltren a la cala — i es nota més fresca que les platges del costat. Aigua Xelida és en realitat un conjunt de diminutes cales de còdols i plataformes de roca llisa just al nord de Tamariu, amb unes poques vil·les blanques baixes al darrere i moltíssims pins. Hi ha una petita rampa i un grapat de barques amarrades, i aquí s'acaba pràcticament la urbanització.",
        "Le nom signifie « eau glacée » en vieux catalan, à cause des sources d'eau douce froide qui s'infiltrent dans la baie — et l'eau y est nettement plus fraîche que sur les plages voisines. Aigua Xelida est en réalité un chapelet de minuscules anses de galets et de plateformes rocheuses plates juste au nord de Tamariu, avec quelques villas blanches basses en arrière-plan et beaucoup de pins. Il y a une petite cale de mise à l'eau et quelques bateaux au mouillage, et c'est à peu près tout.",
        "De naam betekent \"gekoeld water\" in het oud-Catalaans, naar de koude zoetwaterbronnen die in de baai sijpelen — en het water is merkbaar frisser dan op de stranden ernaast. Aigua Xelida is eigenlijk een groepje piepkleine kiezelinhammen en vlakke rotsplateaus net ten noorden van Tamariu, met daarachter een handvol lage witte villa's en heel veel dennen. Er is een kleine botenhelling en een paar afgemeerde bootjes, en daar houdt de bebouwing zo ongeveer op."),
    "There are no facilities at all, which is exactly the point. Come with a towel, a mask and a picnic, claim a rock, and swim in some of the clearest water on the coast. Parking is limited to a few roadside spaces so arrive early or walk in. Best in the morning; the light on the water here at around 9am is remarkable.": T(
        "No hay ningún servicio, que es justamente la gracia. Venga con toalla, gafas y picnic, ocupe una roca y báñese en una de las aguas más claras de la costa. El aparcamiento se limita a unas pocas plazas en el arcén, así que llegue temprano o venga andando. Mejor por la mañana; la luz sobre el agua aquí hacia las 9 es extraordinaria.",
        "No hi ha cap servei, que és justament la gràcia. Veniu amb tovallola, ulleres i pícnic, ocupeu una roca i banyeu-vos en una de les aigües més clares de la costa. L'aparcament es limita a unes poques places al voral, així que arribeu-hi aviat o veniu a peu. Millor al matí; la llum sobre l'aigua aquí cap a les 9 és extraordinària.",
        "Il n'y a aucun service, et c'est précisément l'intérêt. Venez avec une serviette, un masque et un pique-nique, prenez possession d'un rocher, et baignez-vous dans l'une des eaux les plus claires de la côte. Le stationnement se limite à quelques places en bord de route : arrivez tôt ou venez à pied. Le matin de préférence ; la lumière sur l'eau vers 9 h y est remarquable.",
        "Er zijn helemaal geen voorzieningen, en dat is precies de bedoeling. Kom met een handdoek, een duikbril en een picknick, claim een rots, en zwem in een van de helderste wateren van de kust. Parkeren beperkt zich tot een paar plekken langs de weg, dus kom vroeg of te voet. Het mooist in de ochtend; het licht op het water rond negen uur is hier bijzonder."),
    "and the surrounding streets of the Aigua Xelida urbanisation, then a five to ten minute walk down steps to the cove.": T(
        "y las calles de alrededor de la urbanización de Aigua Xelida, y después cinco o diez minutos bajando escaleras hasta la cala.",
        "i els carrers del voltant de la urbanització d'Aigua Xelida, i després cinc o deu minuts baixant escales fins a la cala.",
        "et les rues alentour du lotissement d'Aigua Xelida, puis cinq à dix minutes de descente par des escaliers jusqu'à la crique.",
        "en de omliggende straten van de wijk Aigua Xelida, daarna vijf tot tien minuten trappen af naar de baai."),
    "Spaces are few and unsupervised — in summer aim to arrive before 09:30. There is no other parking closer.": T(
        "Las plazas son pocas y sin vigilancia — en verano procure llegar antes de las 09:30. No hay otro aparcamiento más cerca.",
        "Les places són poques i sense vigilància — a l'estiu mireu d'arribar-hi abans de les 09:30. No hi ha cap altre aparcament més a prop.",
        "Les places sont rares et non surveillées — en été, essayez d'arriver avant 9h30. Il n'y a pas de stationnement plus proche.",
        "Er zijn weinig plekken en geen toezicht — probeer in de zomer voor 09:30 te arriveren. Dichterbij is er geen parkeergelegenheid."),
    "— bring a picnic, or plan lunch elsewhere.": T(
        "— lleve un picnic o planee comer en otro sitio.",
        "— porteu-hi un pícnic o planegeu dinar en un altre lloc.",
        "— prévoyez un pique-nique, ou déjeunez ailleurs.",
        "— neem een picknick mee of plan de lunch elders."),
    "— El Palanquí, Royal, Bar Ona, or a pizza from El Camí de Ronda to take back with you.": T(
        "— El Palanquí, Royal, Bar Ona, o una pizza de El Camí de Ronda para llevar.",
        "— El Palanquí, Royal, Bar Ona, o una pizza d'El Camí de Ronda per emportar.",
        "— El Palanquí, Royal, Bar Ona, ou une pizza d'El Camí de Ronda à emporter.",
        "— El Palanquí, Royal, Bar Ona, of een pizza van El Camí de Ronda om mee te nemen."),
    "— the natural pairing if you want a proper lunch after a morning swim here.": T(
        "— la combinación natural si quiere comer bien después de un baño matinal aquí.",
        "— la combinació natural si voleu dinar bé després d'un bany matinal aquí.",
        "— l'association naturelle si vous voulez un vrai déjeuner après une baignade matinale ici.",
        "— de logische combinatie als u na een ochtendduik hier goed wilt lunchen."),
    "Almost every cove on this coast has far less parking than it has admirers. In July and August the golden rule is simple — arrive before 10am or after 4pm, or take the seasonal beach buses. We're happy to advise on the day.": T(
        "Casi todas las calas de esta costa tienen mucho menos aparcamiento que admiradores. En julio y agosto la regla de oro es sencilla — llegue antes de las 10:00 o después de las 16:00, o tome los buses de playa de temporada. Con mucho gusto le aconsejamos el mismo día.",
        "Gairebé totes les cales d'aquesta costa tenen molt menys aparcament que admiradors. El juliol i l'agost la regla d'or és senzilla — arribeu abans de les 10:00 o després de les 16:00, o agafeu els busos de platja de temporada. Us aconsellem de gust el mateix dia.",
        "Presque chaque crique de cette côte compte bien moins de places que d'admirateurs. En juillet et août, la règle d'or est simple — arrivez avant 10h ou après 16h, ou prenez les bus de plage saisonniers. Nous vous conseillons volontiers le jour même.",
        "Bijna elke baai aan deze kust heeft veel minder parkeerplaatsen dan bewonderaars. In juli en augustus is de gouden regel eenvoudig — kom voor 10:00 of na 16:00 uur, of neem de seizoensstrandbussen. We adviseren graag op de dag zelf."),

    # ── Llafranc / Calella intro ─────────────────────────────────────────
    "Tamariu's two sister villages and the wild little cove between them. All three are linked to Tamariu by the": T(
        "Los dos pueblos hermanos de Tamariu y la pequeña cala salvaje que hay entre ellos. Los tres están unidos a Tamariu por el",
        "Els dos pobles germans de Tamariu i la petita cala salvatge que hi ha entremig. Tots tres estan units a Tamariu pel",
        "Les deux villages jumeaux de Tamariu et la petite crique sauvage entre les deux. Tous trois sont reliés à Tamariu par le",
        "De twee zusterdorpen van Tamariu en het wilde baaitje ertussen. Alle drie zijn met Tamariu verbonden via het"),
    ", so you can walk one way and take a taxi or the bus back.": T(
        ", así que puede ir andando y volver en taxi o en autobús.",
        ", així que podeu anar-hi a peu i tornar en taxi o en autobús.",
        ", vous pouvez donc faire l'aller à pied et rentrer en taxi ou en bus.",
        ", dus u kunt heen lopen en met taxi of bus terugkeren."),
    "The grandest of the three Palafrugell villages — a wide, gently curving bay of soft golden sand with a broad palm-lined promenade behind it and a small marina at the western end. Llafranc feels a touch more polished than Tamariu: white awnings, ice-cream terraces, yachts swinging at anchor, and a long line of restaurants where you can sit over lunch and watch the whole bay.": T(
        "El más señorial de los tres pueblos de Palafrugell — una bahía amplia y de curva suave, de arena dorada y fina, con un ancho paseo de palmeras detrás y un pequeño puerto deportivo en el extremo oeste. Llafranc se siente algo más pulido que Tamariu: toldos blancos, terrazas de helados, yates fondeados y una larga hilera de restaurantes donde sentarse a comer viendo toda la bahía.",
        "El més senyorial dels tres pobles de Palafrugell — una badia àmplia i de corba suau, de sorra daurada i fina, amb un ample passeig de palmeres al darrere i un petit port esportiu a l'extrem oest. Llafranc se sent una mica més polit que Tamariu: tendals blancs, terrasses de gelats, iots fondejats i una llarga filera de restaurants on seure a dinar mirant tota la badia.",
        "Le plus élégant des trois villages de Palafrugell — une large baie doucement incurvée de sable doré, avec une vaste promenade bordée de palmiers derrière et un petit port de plaisance à l'extrémité ouest. Llafranc paraît un peu plus soigné que Tamariu : stores blancs, terrasses à glaces, yachts au mouillage, et une longue enfilade de restaurants où l'on déjeune face à toute la baie.",
        "Het statigste van de drie dorpen van Palafrugell — een brede, licht gebogen baai met zacht goudkleurig zand, met daarachter een brede, met palmen omzoomde boulevard en een kleine jachthaven aan de westkant. Llafranc voelt net iets verzorgder dan Tamariu: witte zonneschermen, ijsterrasjes, jachten voor anker, en een lange rij restaurants waar u kunt lunchen met uitzicht over de hele baai."),
    "It's a fine beach for swimming and for children, with plenty of space even in August, and it's the best local base for sailing, windsurfing and paddleboarding. Above the village sits the Sant Sebastià lighthouse — the drive or walk up is worth it for one of the great views of the Costa Brava, and there's a bar and restaurant at the top.": T(
        "Es una buena playa para nadar y para niños, con espacio de sobra incluso en agosto, y es la mejor base de la zona para vela, windsurf y paddle surf. Sobre el pueblo está el faro de Sant Sebastià — subir en coche o a pie merece la pena por una de las grandes vistas de la Costa Brava, y arriba hay bar y restaurante.",
        "És una bona platja per nedar i per a nens, amb espai de sobres fins i tot a l'agost, i és la millor base de la zona per a vela, windsurf i paddle surf. Sobre el poble hi ha el far de Sant Sebastià — pujar-hi amb cotxe o a peu val la pena per una de les grans vistes de la Costa Brava, i a dalt hi ha bar i restaurant.",
        "C'est une belle plage pour nager et pour les enfants, avec de la place même en août, et la meilleure base du secteur pour la voile, la planche à voile et le paddle. Au-dessus du village se dresse le phare de Sant Sebastià — la montée, en voiture ou à pied, vaut le détour pour l'une des plus belles vues de la Costa Brava, et il y a un bar-restaurant au sommet.",
        "Het is een fijn strand om te zwemmen en voor kinderen, met ruimte genoeg zelfs in augustus, en het is de beste uitvalsbasis in de omgeving voor zeilen, windsurfen en suppen. Boven het dorp staat de vuurtoren van Sant Sebastià — de rit of wandeling omhoog is de moeite waard voor een van de mooiste uitzichten van de Costa Brava, en bovenaan zijn een bar en restaurant."),
    "The blue zone along the seafront is paid from June to September. There is also a paid car park about two minutes' walk from the beach.": T(
        "La zona azul del paseo marítimo es de pago de junio a septiembre. También hay un aparcamiento de pago a unos dos minutos a pie de la playa.",
        "La zona blava del passeig marítim és de pagament de juny a setembre. També hi ha un aparcament de pagament a uns dos minuts a peu de la platja.",
        "La zone bleue le long du front de mer est payante de juin à septembre. Il y a aussi un parking payant à environ deux minutes à pied de la plage.",
        "De blauwe zone langs de boulevard is betaald van juni tot september. Er is ook een betaalde parkeerplaats op ongeveer twee minuten lopen van het strand."),
    ", plus free street parking on Carrer de la Sirena and the streets above. Outside June–September the blue zone is free.": T(
        ", además de aparcamiento libre en Carrer de la Sirena y las calles de arriba. Fuera de junio–septiembre la zona azul es gratuita.",
        ", a més d'aparcament lliure al Carrer de la Sirena i els carrers de dalt. Fora de juny–setembre la zona blava és gratuïta.",
        ", ainsi que du stationnement gratuit sur le Carrer de la Sirena et les rues au-dessus. Hors juin–septembre, la zone bleue est gratuite.",
        ", plus gratis parkeren aan de Carrer de la Sirena en de straten daarboven. Buiten juni–september is de blauwe zone gratis."),
    "— Michelin-starred, on the hillside above the bay. Refined modern Catalan cooking with a stunning terrace view. Reserve well ahead.": T(
        "— con estrella Michelin, en la ladera sobre la bahía. Cocina catalana moderna y refinada con una vista de terraza impresionante. Reserve con mucha antelación.",
        "— amb estrella Michelin, al vessant sobre la badia. Cuina catalana moderna i refinada amb una vista de terrassa impressionant. Reserveu amb molta antelació.",
        "— étoilé au Michelin, à flanc de colline au-dessus de la baie. Cuisine catalane moderne et raffinée, vue de terrasse saisissante. Réservez bien à l'avance.",
        "— met Michelinster, tegen de helling boven de baai. Verfijnde moderne Catalaanse keuken met een adembenemend terrasuitzicht. Reserveer ruim vooraf."),
    "— long-established seafront dining room; classic rice dishes and fresh fish.": T(
        "— comedor de toda la vida en el paseo; arroces clásicos y pescado fresco.",
        "— menjador de tota la vida al passeig; arrossos clàssics i peix fresc.",
        "— salle à manger de longue date sur le front de mer ; riz classiques et poisson frais.",
        "— een gevestigd restaurant aan de boulevard; klassieke rijstgerechten en verse vis."),
    "— a Llafranc institution just off the front, popular for grilled meats and generous Catalan plates.": T(
        "— una institución de Llafranc a un paso del paseo, popular por las carnes a la brasa y los platos catalanes generosos.",
        "— una institució de Llafranc a tocar del passeig, popular per les carns a la brasa i els plats catalans generosos.",
        "— une institution de Llafranc juste derrière le front de mer, réputée pour ses grillades et ses généreuses assiettes catalanes.",
        "— een instituut in Llafranc net achter de boulevard, populair om het gegrilde vlees en de royale Catalaanse gerechten."),
    "— perfect for a vermut before lunch or a gin and tonic at dusk.": T(
        "— perfecto para un vermut antes de comer o un gin-tonic al anochecer.",
        "— perfecte per a un vermut abans de dinar o un gin-tònic al capvespre.",
        "— parfait pour un vermouth avant le déjeuner ou un gin tonic au crépuscule.",
        "— perfect voor een vermout voor de lunch of een gin-tonic in de schemering."),
    "— restaurant and bar at the lighthouse; go for the panorama.": T(
        "— restaurante y bar en el faro; vaya por la panorámica.",
        "— restaurant i bar al far; aneu-hi per la panoràmica.",
        "— restaurant et bar au phare ; allez-y pour le panorama.",
        "— restaurant en bar bij de vuurtoren; ga erheen voor het panorama."),

    # ── Calella ──────────────────────────────────────────────────────────
    "The image most people carry away from the Costa Brava: whitewashed fishermen's houses with arched arcades (": T(
        "La imagen que la mayoría se lleva de la Costa Brava: casas de pescadores encaladas con arcadas (",
        "La imatge que la majoria s'emporta de la Costa Brava: cases de pescadors emblanquinades amb arcades (",
        "L'image que la plupart des gens gardent de la Costa Brava : maisons de pêcheurs blanchies à la chaux et arcades (",
        "Het beeld dat de meeste mensen van de Costa Brava meenemen: witgekalkte vissershuizen met booggalerijen ("),
    ") standing directly over the water at Port Bo, boats drawn up on the shingle, and a string of small sandy coves connected by little tunnels and stepped alleyways. It is genuinely beautiful and, remarkably, has been kept almost entirely free of modern building.": T(
        ") justo sobre el agua en Port Bo, barcas varadas en la grava y un rosario de pequeñas calas de arena unidas por túneles y callejones con escaleras. Es de verdad hermoso y, notablemente, se ha mantenido casi por completo libre de construcción moderna.",
        ") just damunt de l'aigua a Port Bo, barques varades a la grava i un reguitzell de petites cales de sorra unides per túnels i carrerons amb escales. És de debò bonic i, notablement, s'ha mantingut gairebé del tot lliure de construcció moderna.",
        ") donnant directement sur l'eau à Port Bo, des barques tirées sur les galets, et un chapelet de petites criques sableuses reliées par de petits tunnels et des ruelles en escalier. C'est réellement beau et, chose remarquable, presque entièrement préservé de toute construction moderne.",
        ") die pal boven het water staan bij Port Bo, boten op het grind getrokken, en een reeks kleine zandbaaien verbonden door tunneltjes en trapsteegjes. Het is werkelijk mooi en is opmerkelijk genoeg vrijwel geheel gevrijwaard gebleven van moderne bebouwing."),
    "Rather than one beach, Calella is a series of them —": T(
        "Más que una playa, Calella es una serie de ellas —",
        "Més que una platja, Calella és una sèrie de platges —",
        "Plutôt qu'une plage, Calella en est une série —",
        "Calella is niet één strand maar een reeks —"),
    "is the biggest and best for sand and space,": T(
        "es la más grande y la mejor en arena y espacio,",
        "és la més gran i la millor en sorra i espai,",
        "est la plus grande et la meilleure pour le sable et l'espace,",
        "is de grootste en de beste qua zand en ruimte,"),
    "the prettiest and most photographed,": T(
        "la más bonita y la más fotografiada,",
        "la més bonica i la més fotografiada,",
        "la plus jolie et la plus photographiée,",
        "de mooiste en meest gefotografeerde,"),
    "quieter with good rocks for snorkelling. In early July the arcades host the": T(
        "más tranquila y con buenas rocas para el snorkel. A principios de julio las arcadas acogen la",
        "més tranquil·la i amb bones roques per al snorkel. A primers de juliol les arcades acullen la",
        "plus tranquille, avec de bons rochers pour le snorkeling. Début juillet, les arcades accueillent la",
        "rustiger met goede rotsen om te snorkelen. Begin juli vindt onder de arcades de"),
    ", a night of sea shanties and burnt rum that is one of the highlights of the Catalan summer. Don't miss the Cap Roig botanical gardens on the headland above.": T(
        ", una noche de canciones marineras y ron quemado que es uno de los momentos culminantes del verano catalán. No se pierda los jardines botánicos de Cap Roig, en la punta de arriba.",
        ", una nit de cançons marineres i rom cremat que és un dels moments culminants de l'estiu català. No us perdeu els jardins botànics de Cap Roig, a la punta de dalt.",
        ", une soirée de chants de marins et de rhum brûlé qui est l'un des temps forts de l'été catalan. Ne manquez pas les jardins botaniques de Cap Roig, sur la pointe au-dessus.",
        " plaats, een avond vol zeemansliederen en gebrande rum die tot de hoogtepunten van de Catalaanse zomer behoort. Mis de botanische tuinen van Cap Roig op de landtong erboven niet."),
    "The car park nearest the beach has fewer than 100 spaces and the streets closest to the water are blue zone (paid).": T(
        "El aparcamiento más cercano a la playa tiene menos de 100 plazas y las calles más próximas al agua son zona azul (de pago).",
        "L'aparcament més proper a la platja té menys de 100 places i els carrers més propers a l'aigua són zona blava (de pagament).",
        "Le parking le plus proche de la plage compte moins de 100 places et les rues les plus proches de l'eau sont en zone bleue (payante).",
        "De parkeerplaats het dichtst bij het strand heeft minder dan 100 plekken en de straten het dichtst bij het water zijn blauwe zone (betaald)."),
    "free street parking higher up the road towards Canadell — generally a 5–10 minute walk back down. Palafrugell also runs a large free car park at": T(
        "aparcamiento libre más arriba en la carretera hacia Canadell — normalmente 5–10 minutos bajando a pie. Palafrugell también tiene un gran aparcamiento gratuito en",
        "aparcament lliure més amunt a la carretera cap a Canadell — normalment 5–10 minuts baixant a peu. Palafrugell també té un gran aparcament gratuït a",
        "stationnement gratuit plus haut sur la route vers Canadell — généralement 5 à 10 minutes de descente à pied. Palafrugell dispose aussi d'un grand parking gratuit à",
        "gratis parkeren hogerop aan de weg richting Canadell — meestal 5–10 minuten naar beneden lopen. Palafrugell heeft ook een grote gratis parkeerplaats bij"),
    "(P11 'Autovia'), about 10 minutes away by car.": T(
        "(P11 «Autovia»), a unos 10 minutos en coche.",
        "(P11 «Autovia»), a uns 10 minuts en cotxe.",
        "(P11 « Autovia »), à environ 10 minutes en voiture.",
        "(P11 'Autovia'), op ongeveer 10 minuten met de auto."),
    "— right on the sand at El Canadell; modern seafood and superb rice dishes with your feet almost in the water. Book ahead.": T(
        "— en plena arena de El Canadell; marisco moderno y arroces magníficos casi con los pies en el agua. Reserve con antelación.",
        "— en plena sorra d'El Canadell; marisc modern i arrossos magnífics gairebé amb els peus a l'aigua. Reserveu amb antelació.",
        "— les pieds dans le sable à El Canadell ; fruits de mer modernes et riz superbes, presque les pieds dans l'eau. Réservez à l'avance.",
        "— pal op het zand van El Canadell; moderne visgerechten en fantastische rijstgerechten met uw voeten bijna in het water. Reserveer vooraf."),
    "— seafront terrace at Port Bo with a lovely outlook over the arches and boats.": T(
        "— terraza junto al mar en Port Bo con una vista preciosa de los arcos y las barcas.",
        "— terrassa arran de mar a Port Bo amb una vista preciosa dels arcs i les barques.",
        "— terrasse en bord de mer à Port Bo avec une jolie vue sur les arches et les barques.",
        "— terras aan zee bij Port Bo met een mooi uitzicht op de bogen en de boten."),
    "— the hotel restaurant on the cliff, with arguably the finest terrace view in Calella.": T(
        "— el restaurante del hotel en el acantilado, posiblemente con la mejor vista de terraza de Calella.",
        "— el restaurant de l'hotel al penya-segat, possiblement amb la millor vista de terrassa de Calella.",
        "— le restaurant de l'hôtel sur la falaise, avec sans doute la plus belle vue en terrasse de Calella.",
        "— het hotelrestaurant op de klif, met misschien wel het mooiste terrasuitzicht van Calella."),
    "— a leafy, long-standing garden restaurant a little back from the front; classic Empordà cooking.": T(
        "— un restaurante ajardinado de toda la vida, un poco retirado del paseo; cocina clásica del Empordà.",
        "— un restaurant enjardinat de tota la vida, una mica retirat del passeig; cuina clàssica de l'Empordà.",
        "— un restaurant de jardin verdoyant et de longue date, un peu en retrait du front de mer ; cuisine classique de l'Empordà.",
        "— een groen, al lang bestaand tuinrestaurant iets van de boulevard af; klassieke Empordà-keuken."),

    # ── El Golfet ────────────────────────────────────────────────────────
    'Tucked beneath the red cliffs of Cap Roig at the southern end of Calella, El Golfet is the wilder alternative to its polished neighbours. A flight of steps drops down through pine woods to a small cove of coarse sand and shingle backed by dramatic rust-coloured rock — the "red cape" that gives the headland its name.': T(
        "Escondida bajo los acantilados rojos de Cap Roig, en el extremo sur de Calella, El Golfet es la alternativa salvaje a sus vecinas pulidas. Un tramo de escaleras baja entre pinares hasta una pequeña cala de arena gruesa y grava con espectacular roca color óxido detrás — el «cabo rojo» que da nombre a la punta.",
        "Amagada sota els penya-segats vermells de Cap Roig, a l'extrem sud de Calella, El Golfet és l'alternativa salvatge a les seves veïnes polides. Un tram d'escales baixa entre pinedes fins a una petita cala de sorra gruixuda i grava amb espectacular roca color òxid al darrere — el «cap roig» que dona nom a la punta.",
        "Nichée sous les falaises rouges de Cap Roig, à l'extrémité sud de Calella, El Golfet est l'alternative sauvage à ses voisines soignées. Un escalier descend à travers les pinèdes vers une petite crique de sable grossier et de galets, adossée à une roche spectaculaire couleur rouille — le « cap rouge » qui donne son nom à la pointe.",
        "Verscholen onder de rode kliffen van Cap Roig aan de zuidkant van Calella is El Golfet het wildere alternatief voor zijn verzorgde buren. Een trap daalt door dennenbossen af naar een kleine baai met grof zand en grind, met daarachter spectaculaire roestkleurige rots — de \"rode kaap\" die de landtong zijn naam geeft."),
    "There are no sunbeds, no bars and no music, just clear deep water that's excellent for swimming and snorkelling, and a good deal of shade in the afternoon. Because of the steps it stays quieter than Calella even in August. Combine it with a morning at the Cap Roig gardens directly above, whose terraced grounds and clifftop views are one of the great sights of the coast.": T(
        "No hay hamacas, ni bares, ni música, solo agua clara y profunda excelente para nadar y hacer snorkel, y bastante sombra por la tarde. Por las escaleras se mantiene más tranquila que Calella incluso en agosto. Combínela con una mañana en los jardines de Cap Roig, justo encima, cuyos aterrazamientos y vistas desde el acantilado son uno de los grandes atractivos de la costa.",
        "No hi ha gandules, ni bars, ni música, només aigua clara i profunda excel·lent per nedar i fer snorkel, i força ombra a la tarda. Per les escales es manté més tranquil·la que Calella fins i tot a l'agost. Combineu-la amb un matí als jardins de Cap Roig, just a sobre, els terraplens i vistes des del penya-segat dels quals són un dels grans atractius de la costa.",
        "Pas de transats, pas de bars, pas de musique, seulement une eau claire et profonde, excellente pour nager et faire du snorkeling, et beaucoup d'ombre l'après-midi. À cause des escaliers, elle reste plus tranquille que Calella même en août. Associez-la à une matinée aux jardins de Cap Roig juste au-dessus, dont les terrasses et les vues du haut de la falaise comptent parmi les grands spectacles de la côte.",
        "Er zijn geen ligbedden, geen bars en geen muziek, alleen helder diep water dat uitstekend is om te zwemmen en te snorkelen, en 's middags veel schaduw. Door de trappen blijft het er zelfs in augustus rustiger dan in Calella. Combineer het met een ochtend in de tuinen van Cap Roig direct erboven, waarvan de terrassen en uitzichten vanaf de klif tot de mooiste van de kust behoren."),
    "Free parking in the Cala El Golfet urbanisation around": T(
        "Aparcamiento gratuito en la urbanización Cala El Golfet, alrededor de",
        "Aparcament gratuït a la urbanització Cala El Golfet, al voltant de",
        "Stationnement gratuit dans le lotissement Cala El Golfet, autour de",
        "Gratis parkeren in de wijk Cala El Golfet, rond"),
    ", then down a flight of steps to the beach. It is roadside parking rather than a proper car park, and it fills early in high season.": T(
        ", y después un tramo de escaleras hasta la playa. Es aparcamiento en el arcén más que un aparcamiento propiamente dicho, y se llena pronto en plena temporada.",
        ", i després un tram d'escales fins a la platja. És aparcament al voral més que un aparcament pròpiament dit, i s'omple aviat en plena temporada.",
        ", puis un escalier jusqu'à la plage. Il s'agit de stationnement en bord de route plutôt que d'un vrai parking, et il se remplit tôt en haute saison.",
        ", daarna een trap af naar het strand. Het is parkeren langs de weg in plaats van een echte parkeerplaats, en in het hoogseizoen loopt het vroeg vol."),
    "the free Cap Roig car park, or park in Calella and walk the camí de ronda (about 20 minutes).": T(
        "el aparcamiento gratuito de Cap Roig, o aparque en Calella y venga por el camí de ronda (unos 20 minutos).",
        "l'aparcament gratuït de Cap Roig, o aparqueu a Calella i veniu pel camí de ronda (uns 20 minuts).",
        "le parking gratuit de Cap Roig, ou garez-vous à Calella et venez par le camí de ronda (environ 20 minutes).",
        "de gratis parkeerplaats van Cap Roig, of parkeer in Calella en loop het camí de ronda (ongeveer 20 minuten)."),
    "— a short walk up; drinks and light lunch with a view over the cove.": T(
        "— a poca distancia subiendo; bebidas y comida ligera con vistas a la cala.",
        "— a poca distància pujant; begudes i menjar lleuger amb vistes a la cala.",
        "— à quelques minutes en montant ; boissons et déjeuner léger avec vue sur la crique.",
        "— een klein stukje omhoog; drankjes en een lichte lunch met uitzicht over de baai."),
    "— Tragamar, La Blava and the rest are all within easy reach.": T(
        "— Tragamar, La Blava y el resto quedan todos a mano.",
        "— Tragamar, La Blava i la resta queden tots a mà.",
        "— Tragamar, La Blava et les autres sont tous à portée.",
        "— Tragamar, La Blava en de rest zijn allemaal goed bereikbaar."),

    # ── Begur intro / Sa Riera / Sa Tuna ─────────────────────────────────
    "North of Tamariu the coast breaks into a run of small, dramatic bays below the town of Begur. These are among the most photographed spots in Catalunya — and, in high summer, among the busiest. Go early.": T(
        "Al norte de Tamariu la costa se rompe en una sucesión de bahías pequeñas y espectaculares bajo el pueblo de Begur. Están entre los lugares más fotografiados de Catalunya — y, en pleno verano, entre los más concurridos. Vaya temprano.",
        "Al nord de Tamariu la costa es trenca en una successió de badies petites i espectaculars sota la vila de Begur. Són dels llocs més fotografiats de Catalunya — i, en ple estiu, dels més concorreguts. Aneu-hi aviat.",
        "Au nord de Tamariu, la côte se découpe en une succession de petites baies spectaculaires sous le village de Begur. Ce sont parmi les endroits les plus photographiés de Catalogne — et, en plein été, parmi les plus fréquentés. Venez tôt.",
        "Ten noorden van Tamariu breekt de kust op in een reeks kleine, indrukwekkende baaien onder het stadje Begur. Ze behoren tot de meest gefotografeerde plekken van Catalonië — en in het hoogzomer tot de drukste. Ga vroeg."),
    "The biggest and most practical of Begur's beaches — an old fishing cove that has grown into a small resort without losing its shape. There's a decent expanse of sand, boats hauled up at one end, a slipway, showers, sunbed hire and a proper handful of restaurants, which makes it the easiest of the Begur coves for a full day out with a family.": T(
        "La más grande y práctica de las playas de Begur — una antigua cala de pescadores que ha crecido hasta ser un pequeño centro turístico sin perder su forma. Hay una buena extensión de arena, barcas varadas en un extremo, rampa, duchas, alquiler de hamacas y un puñado de restaurantes en condiciones, lo que la convierte en la más cómoda de las calas de Begur para un día completo en familia.",
        "La més gran i pràctica de les platges de Begur — una antiga cala de pescadors que ha crescut fins a ser un petit centre turístic sense perdre la seva forma. Hi ha una bona extensió de sorra, barques varades en un extrem, rampa, dutxes, lloguer de gandules i un grapat de restaurants com cal, cosa que la converteix en la més còmoda de les cales de Begur per a un dia complet en família.",
        "La plus grande et la plus pratique des plages de Begur — une ancienne crique de pêcheurs devenue une petite station sans perdre sa forme. Il y a une belle étendue de sable, des barques tirées au sec à une extrémité, une cale, des douches, de la location de transats et une vraie poignée de restaurants, ce qui en fait la plus commode des criques de Begur pour une journée en famille.",
        "Het grootste en praktischste van de stranden van Begur — een oude vissersbaai die is uitgegroeid tot een kleine badplaats zonder haar vorm te verliezen. Er is een flinke strook zand, boten op het droge aan één kant, een botenhelling, douches, ligbedverhuur en een behoorlijk aantal restaurants, wat het de makkelijkste van de Begur-baaien maakt voor een hele dag met het gezin."),
    "The water is clear and the bay reasonably sheltered, though it can pick up a swell in an easterly. Walk north around the headland and you reach": T(
        "El agua es clara y la bahía está razonablemente resguardada, aunque puede coger oleaje con viento de levante. Caminando al norte rodeando la punta se llega a",
        "L'aigua és clara i la badia està raonablement arrecerada, tot i que pot agafar onatge amb vent de llevant. Caminant cap al nord vorejant la punta s'arriba a",
        "L'eau est claire et la baie assez abritée, même si elle peut prendre de la houle par vent d'est. En marchant vers le nord autour de la pointe, on atteint",
        "Het water is helder en de baai redelijk beschut, al kan er bij oostenwind deining staan. Loop noordwaarts om de landtong heen en u komt bij"),
    ", a strikingly beautiful red-rock cove that is one of the coast's best-known naturist beaches, and beyond it the long sands of Pals.": T(
        ", una cala de roca roja de una belleza sorprendente que es una de las playas nudistas más conocidas de la costa, y más allá los largos arenales de Pals.",
        ", una cala de roca vermella d'una bellesa sorprenent que és una de les platges nudistes més conegudes de la costa, i més enllà els llargs arenals de Pals.",
        ", une crique de roche rouge d'une beauté saisissante, l'une des plages naturistes les plus connues de la côte, et au-delà les longues plages de Pals.",
        ", een opvallend mooie baai met rode rotsen die een van de bekendste naaktstranden van de kust is, en daarachter de lange zandstranden van Pals."),
    "The car park above the beach is paid and small — roughly €3 an hour — and the approach road is narrow. Come early or late in the day.": T(
        "El aparcamiento sobre la playa es de pago y pequeño — unos 3 € la hora — y la carretera de acceso es estrecha. Venga temprano o al final del día.",
        "L'aparcament sobre la platja és de pagament i petit — uns 3 € l'hora — i la carretera d'accés és estreta. Veniu aviat o al final del dia.",
        "Le parking au-dessus de la plage est payant et petit — environ 3 € l'heure — et la route d'accès est étroite. Venez tôt ou en fin de journée.",
        "De parkeerplaats boven het strand is betaald en klein — ongeveer €3 per uur — en de toegangsweg is smal. Kom vroeg of laat op de dag."),
    "use the free car parks on the edge of Begur town and take the €1 beach shuttle down (roughly June to September).": T(
        "use los aparcamientos gratuitos a las afueras de Begur y baje con la lanzadera de playa de 1 € (aproximadamente de junio a septiembre).",
        "feu servir els aparcaments gratuïts a les afores de Begur i baixeu amb la llançadora de platja d'1 € (aproximadament de juny a setembre).",
        "utilisez les parkings gratuits en bordure de Begur et descendez avec la navette de plage à 1 € (de juin à septembre environ).",
        "gebruik de gratis parkeerplaatsen aan de rand van Begur en neem de strandpendel van €1 naar beneden (ongeveer juni tot september)."),
    "— traditional seafood and rice a few steps from the sand.": T(
        "— marisco y arroces tradicionales a unos pasos de la arena.",
        "— marisc i arrossos tradicionals a unes passes de la sorra.",
        "— fruits de mer et riz traditionnels à quelques pas du sable.",
        "— traditionele visgerechten en rijst op een paar stappen van het zand."),
    "— terrace lunches with a view over the bay.": T(
        "— comidas en terraza con vistas a la bahía.",
        "— dinars en terrassa amb vistes a la badia.",
        "— déjeuners en terrasse avec vue sur la baie.",
        "— lunchen op het terras met uitzicht over de baai."),
    "— a couple of summer bars on the sand for drinks and something quick.": T(
        "— un par de chiringuitos de verano en la arena para tomar algo rápido.",
        "— un parell de xiringuitos d'estiu a la sorra per prendre alguna cosa ràpida.",
        "— deux bars d'été sur le sable pour boire un verre ou manger sur le pouce.",
        "— een paar zomerbarretjes op het zand voor een drankje en iets snels."),
    "Many people's favourite cove on the whole Costa Brava, and it's easy to see why. Sa Tuna is a tiny horseshoe of smooth pebbles enclosed by a tight ring of old white fishermen's houses, with a single waterfront hostal-restaurant, a scatter of boats and almost nothing else. The scale of it is what charms — everything is within thirty paces of the water.": T(
        "Para mucha gente, la cala favorita de toda la Costa Brava, y es fácil ver por qué. Sa Tuna es una diminuta herradura de cantos pulidos cerrada por un anillo apretado de viejas casas blancas de pescadores, con un único hostal-restaurante frente al agua, unas cuantas barcas y casi nada más. Lo que encanta es la escala — todo está a treinta pasos del agua.",
        "Per a molta gent, la cala preferida de tota la Costa Brava, i és fàcil veure per què. Sa Tuna és una diminuta ferradura de còdols polits tancada per un anell atapeït de velles cases blanques de pescadors, amb un únic hostal-restaurant arran d'aigua, unes quantes barques i gairebé res més. El que encanta és l'escala — tot és a trenta passes de l'aigua.",
        "La crique préférée de bien des gens sur toute la Costa Brava, et l'on comprend pourquoi. Sa Tuna est un minuscule fer à cheval de galets lisses enserré par un anneau serré de vieilles maisons blanches de pêcheurs, avec un unique hostal-restaurant en bord d'eau, quelques barques et presque rien d'autre. C'est l'échelle qui séduit — tout se trouve à trente pas de l'eau.",
        "Voor veel mensen de mooiste baai van de hele Costa Brava, en het is makkelijk te zien waarom. Sa Tuna is een piepklein hoefijzer van gladde kiezels, omsloten door een strakke ring oude witte vissershuizen, met één hostal-restaurant aan het water, een paar boten en vrijwel niets anders. De schaal is wat betovert — alles ligt binnen dertig passen van het water."),
    "The swimming is excellent: deep, clear and immediately good for snorkelling around the rocky sides. Bring water shoes if you're tender-footed, as it's pebble rather than sand. Parking is genuinely difficult — there is a car park above the cove and a steep walk down, and in August it fills early. A short walk round the point brings you to the even smaller": T(
        "El baño es excelente: profundo, claro y estupendo para hacer snorkel enseguida por los lados rocosos. Lleve escarpines si tiene los pies delicados, porque es de cantos y no de arena. El aparcamiento es realmente complicado — hay un aparcamiento sobre la cala y una bajada empinada, y en agosto se llena pronto. Un corto paseo rodeando la punta lleva a la aún más pequeña",
        "El bany és excel·lent: profund, clar i estupend per fer snorkel de seguida pels costats rocosos. Porteu escarpins si teniu els peus delicats, perquè és de còdols i no de sorra. L'aparcament és realment complicat — hi ha un aparcament sobre la cala i una baixada costeruda, i a l'agost s'omple aviat. Una curta passejada vorejant la punta porta a l'encara més petita",
        "La baignade y est excellente : eau profonde, claire et immédiatement propice au snorkeling le long des bords rocheux. Prévoyez des chaussons si vous avez les pieds sensibles, car ce sont des galets et non du sable. Le stationnement est vraiment difficile — il y a un parking au-dessus de la crique et une descente raide, et en août il se remplit tôt. Une courte marche autour de la pointe mène à la plus petite encore",
        "Het zwemmen is uitstekend: diep, helder en meteen goed om te snorkelen langs de rotsige randen. Neem waterschoenen mee als u gevoelige voeten hebt, want het is kiezel en geen zand. Parkeren is echt lastig — er is een parkeerplaats boven de baai en een steile afdaling, en in augustus loopt die vroeg vol. Een korte wandeling om de punt brengt u bij het nog kleinere"),
    ", all rock platforms and diving-board swimming.": T(
        ", todo plataformas de roca y baños de trampolín.",
        ", tot plataformes de roca i banys de trampolí.",
        ", tout en plateformes rocheuses et plongeons.",
        ", helemaal rotsplateaus en zwemmen als vanaf een duikplank."),
    "The road down is narrow and winding with very few spaces, all paid. In summer you may simply not find a spot.": T(
        "La carretera de bajada es estrecha y con curvas, con muy pocas plazas, todas de pago. En verano puede sencillamente no encontrar sitio.",
        "La carretera de baixada és estreta i amb corbes, amb molt poques places, totes de pagament. A l'estiu podeu senzillament no trobar-hi lloc.",
        "La route qui descend est étroite et sinueuse, avec très peu de places, toutes payantes. En été, vous risquez simplement de ne pas trouver de place.",
        "De weg naar beneden is smal en bochtig met heel weinig plekken, allemaal betaald. In de zomer vindt u mogelijk gewoon geen plek."),
    "park free in Begur town and take the €1 beach shuttle — for Sa Tuna this is much the easier choice.": T(
        "aparque gratis en el pueblo de Begur y tome la lanzadera de playa de 1 € — para Sa Tuna es con diferencia la opción más fácil.",
        "aparqueu gratis al poble de Begur i agafeu la llançadora de platja d'1 € — per a Sa Tuna és de bon tros l'opció més fàcil.",
        "garez-vous gratuitement dans le village de Begur et prenez la navette de plage à 1 € — pour Sa Tuna, c'est de loin le plus simple.",
        "parkeer gratis in Begur en neem de strandpendel van €1 — voor Sa Tuna is dat verreweg de makkelijkste keuze."),
    "— the only place at the cove and all the better for it: tapas, paella and seafood on a rustic terrace directly above the beach. Reserve in season.": T(
        "— el único sitio de la cala y mejor por ello: tapas, paella y marisco en una terraza rústica justo encima de la playa. Reserve en temporada.",
        "— l'únic lloc de la cala i millor per això: tapes, paella i marisc en una terrassa rústica just damunt de la platja. Reserveu en temporada.",
        "— la seule adresse de la crique, et c'est tant mieux : tapas, paella et fruits de mer sur une terrasse rustique juste au-dessus de la plage. Réservez en saison.",
        "— de enige zaak bij de baai, en des te beter: tapas, paella en zeevruchten op een rustiek terras pal boven het strand. Reserveer in het seizoen."),
    "— a good choice of restaurants around the castle and the old streets if you want dinner after a swim.": T(
        "— buena oferta de restaurantes alrededor del castillo y las calles antiguas si quiere cenar después del baño.",
        "— bona oferta de restaurants al voltant del castell i els carrers antics si voleu sopar després del bany.",
        "— un bon choix de restaurants autour du château et dans les vieilles rues si vous voulez dîner après la baignade.",
        "— een goede keuze aan restaurants rond het kasteel en de oude straten als u na het zwemmen wilt dineren."),

    # ── Long sands: Pals / Castell / La Fosca ────────────────────────────
    "When you want room to walk, throw a ball, or swim without company, head a little further out. These are the wide beaches — two north towards the Empordà plain, one south beyond Palamós.": T(
        "Cuando quiera espacio para caminar, jugar a la pelota o nadar sin compañía, aléjese un poco más. Estas son las playas amplias — dos al norte hacia la llanura del Empordà, una al sur pasado Palamós.",
        "Quan vulgueu espai per caminar, jugar a pilota o nedar sense companyia, allunyeu-vos una mica més. Aquestes són les platges àmplies — dues al nord cap a la plana de l'Empordà, una al sud passat Palamós.",
        "Quand vous voulez de la place pour marcher, jouer au ballon ou nager sans personne autour, éloignez-vous un peu. Voici les grandes plages — deux au nord vers la plaine de l'Empordà, une au sud au-delà de Palamós.",
        "Wilt u ruimte om te wandelen, te ballen of te zwemmen zonder gezelschap, ga dan wat verder. Dit zijn de brede stranden — twee noordwaarts richting de vlakte van de Empordà, één zuidwaarts voorbij Palamós."),
    "A complete change of character from the coves — nearly three kilometres of open golden sand backed by umbrella pines and low dunes, running north towards the mouth of the River Ter. On a clear day you can see the Medes Islands and the great sweep of the Bay of Roses. There is always space here, even at the height of August.": T(
        "Un cambio total de carácter respecto a las calas — casi tres kilómetros de arena dorada abierta con pinos piñoneros y dunas bajas detrás, en dirección norte hacia la desembocadura del Ter. En un día claro se ven las islas Medes y la gran curva de la bahía de Roses. Aquí siempre hay sitio, incluso en pleno agosto.",
        "Un canvi total de caràcter respecte a les cales — gairebé tres quilòmetres de sorra daurada oberta amb pins pinyers i dunes baixes al darrere, en direcció nord cap a la desembocadura del Ter. En un dia clar es veuen les illes Medes i la gran corba de la badia de Roses. Aquí sempre hi ha lloc, fins i tot en ple agost.",
        "Un changement complet par rapport aux criques — près de trois kilomètres de sable doré ouvert, bordés de pins parasols et de dunes basses, s'étirant vers le nord jusqu'à l'embouchure du Ter. Par temps clair, on aperçoit les îles Medes et la grande courbe de la baie de Roses. Il y a toujours de la place ici, même au plus fort du mois d'août.",
        "Een compleet ander karakter dan de baaien — bijna drie kilometer open goudkleurig zand met parasoldennen en lage duinen erachter, noordwaarts richting de monding van de rivier de Ter. Op een heldere dag ziet u de Medes-eilanden en de weidse boog van de Golf van Roses. Hier is altijd ruimte, zelfs op het hoogtepunt van augustus."),
    "The openness means more wind and more surf than the sheltered bays, which makes Pals the local centre for windsurfing, kitesurfing and paddleboarding, and a fine place for a long barefoot walk at either end of the day. Combine it with the medieval hill town of": T(
        "Al estar tan abierta hay más viento y más olas que en las bahías resguardadas, lo que hace de Pals el centro local del windsurf, el kitesurf y el paddle surf, y un buen sitio para un largo paseo descalzo a primera o última hora. Combínela con el pueblo medieval en alto de",
        "En ser tan oberta hi ha més vent i més onatge que a les badies arrecerades, cosa que fa de Pals el centre local del windsurf, el kitesurf i el paddle surf, i un bon lloc per a una llarga passejada descalç a primera o última hora. Combineu-la amb el poble medieval enlairat de",
        "Cette ouverture signifie plus de vent et plus de vagues que dans les baies abritées, ce qui fait de Pals le centre local de la planche à voile, du kitesurf et du paddle, et un bel endroit pour une longue marche pieds nus en début ou en fin de journée. Associez-la au village médiéval perché de",
        "Door die openheid staat er meer wind en meer branding dan in de beschutte baaien, waardoor Pals het lokale centrum is voor windsurfen, kitesurfen en suppen, en een fijne plek voor een lange blotevoetenwandeling aan het begin of eind van de dag. Combineer het met het middeleeuwse heuveldorp"),
    "itself, five minutes inland — one of the most beautifully preserved villages in Catalunya — or with the golf courses just behind the beach.": T(
        "en sí, a cinco minutos tierra adentro — uno de los pueblos mejor conservados de Catalunya — o con los campos de golf justo detrás de la playa.",
        "mateix, a cinc minuts cap a l'interior — un dels pobles més ben conservats de Catalunya — o amb els camps de golf just darrere de la platja.",
        "même, à cinq minutes dans les terres — l'un des villages les mieux préservés de Catalogne — ou avec les golfs juste derrière la plage.",
        "zelf, vijf minuten landinwaarts — een van de best bewaarde dorpen van Catalonië — of met de golfbanen vlak achter het strand."),
    "Free parking areas serve the beach, with additional free spaces in the lower part of Pals near the sports pavilion.": T(
        "Zonas de aparcamiento gratuito dan servicio a la playa, con plazas gratuitas adicionales en la parte baja de Pals, cerca del pabellón deportivo.",
        "Zones d'aparcament gratuït donen servei a la platja, amb places gratuïtes addicionals a la part baixa de Pals, a prop del pavelló esportiu.",
        "Des zones de stationnement gratuit desservent la plage, avec des places gratuites supplémentaires dans le bas de Pals, près du pavillon sportif.",
        "Gratis parkeerzones bedienen het strand, met extra gratis plekken in het lager gelegen deel van Pals bij de sporthal."),
    "The beach is long and there are several access points — the further north you go, the easier parking tends to be.": T(
        "La playa es larga y hay varios accesos — cuanto más al norte, más fácil suele ser aparcar.",
        "La platja és llarga i hi ha diversos accessos — com més al nord, més fàcil sol ser aparcar.",
        "La plage est longue et compte plusieurs accès — plus vous allez vers le nord, plus il est facile de se garer.",
        "Het strand is lang en er zijn meerdere toegangen — hoe verder noordwaarts, hoe makkelijker het parkeren doorgaans is."),
    "— the smart choice, in gardens near the southern end of the beach; polished market cuisine and a large poolside terrace.": T(
        "— la opción elegante, entre jardines cerca del extremo sur de la playa; cocina de mercado cuidada y una gran terraza junto a la piscina.",
        "— l'opció elegant, entre jardins a prop de l'extrem sud de la platja; cuina de mercat acurada i una gran terrassa vora la piscina.",
        "— le choix élégant, dans un jardin près de l'extrémité sud de la plage ; cuisine de marché soignée et grande terrasse au bord de la piscine.",
        "— de chique keuze, in tuinen bij het zuidelijke uiteinde van het strand; verzorgde marktkeuken en een groot terras bij het zwembad."),
    "— several along the sand in season for grilled fish, salads and cold beer, feet in the sand.": T(
        "— varios a lo largo de la arena en temporada para pescado a la brasa, ensaladas y cerveza fría, con los pies en la arena.",
        "— diversos al llarg de la sorra en temporada per a peix a la brasa, amanides i cervesa freda, amb els peus a la sorra.",
        "— plusieurs le long du sable en saison pour du poisson grillé, des salades et une bière fraîche, les pieds dans le sable.",
        "— meerdere langs het zand in het seizoen voor gegrilde vis, salades en koud bier, met de voeten in het zand."),
    "— excellent restaurants in the old stone streets; the local rice,": T(
        "— excelentes restaurantes en las viejas calles de piedra; el arroz local,",
        "— excel·lents restaurants als vells carrers de pedra; l'arròs local,",
        "— d'excellents restaurants dans les vieilles rues de pierre ; le riz local,",
        "— uitstekende restaurants in de oude stenen straatjes; de lokale rijst,"),
    "Something of a local legend. In 1994 the people of Palamós voted in a referendum to stop this bay being built on, and Castell remains the last major undeveloped beach on the Costa Brava — a broad half-moon of fine sand with pine woods and open farmland behind it and not a single apartment block in sight. Walking onto it feels like stepping back forty years.": T(
        "Toda una leyenda local. En 1994 los vecinos de Palamós votaron en referéndum para impedir que se urbanizara esta bahía, y Castell sigue siendo la última gran playa sin urbanizar de la Costa Brava — una amplia media luna de arena fina con pinares y campos abiertos detrás y ni un solo bloque de apartamentos a la vista. Pisarla es como retroceder cuarenta años.",
        "Tota una llegenda local. El 1994 els veïns de Palamós van votar en referèndum per impedir que s'urbanitzés aquesta badia, i Castell continua sent l'última gran platja sense urbanitzar de la Costa Brava — una àmplia mitja lluna de sorra fina amb pinedes i camps oberts al darrere i ni un sol bloc d'apartaments a la vista. Trepitjar-la és com retrocedir quaranta anys.",
        "Une véritable légende locale. En 1994, les habitants de Palamós ont voté par référendum pour empêcher la construction sur cette baie, et Castell reste la dernière grande plage non bâtie de la Costa Brava — un large croissant de sable fin avec pinèdes et champs ouverts derrière, et pas un seul immeuble en vue. Y poser le pied, c'est remonter quarante ans en arrière.",
        "Bijna een lokale legende. In 1994 stemden de inwoners van Palamós in een referendum tegen bebouwing van deze baai, en Castell is nog altijd het laatste grote onbebouwde strand van de Costa Brava — een brede halve maan van fijn zand met dennenbossen en open landbouwgrond erachter en geen enkel appartementenblok in zicht. Het betreden voelt als veertig jaar teruggaan in de tijd."),
    "The water is clean and shallow, there's plenty of room, and the whole area is now protected. On the headland at the northern end sit the excavated remains of an": T(
        "El agua es limpia y poco profunda, hay espacio de sobra y toda la zona está ahora protegida. En la punta del extremo norte están los restos excavados de un",
        "L'aigua és neta i poc profunda, hi ha espai de sobres i tota la zona està ara protegida. A la punta de l'extrem nord hi ha les restes excavades d'un",
        "L'eau est propre et peu profonde, la place ne manque pas, et toute la zone est aujourd'hui protégée. Sur la pointe à l'extrémité nord se trouvent les vestiges fouillés d'un",
        "Het water is schoon en ondiep, er is ruimte in overvloed, en het hele gebied is nu beschermd. Op de landtong aan de noordkant liggen de opgegraven resten van een"),
    "dating from the 6th century BC, well worth the ten-minute climb for the ruins and the view. Continue on the coastal path and you reach the tiny, exquisite": T(
        "del siglo VI a. C., que bien merece la subida de diez minutos por las ruinas y la vista. Siguiendo el camino de ronda se llega a la diminuta y exquisita",
        "del segle VI aC, que bé val la pujada de deu minuts per les ruïnes i la vista. Seguint el camí de ronda s'arriba a la diminuta i exquisida",
        "datant du VIe siècle av. J.-C., qui vaut bien les dix minutes de montée pour les ruines et la vue. En continuant sur le chemin côtier, on atteint la minuscule et exquise",
        "uit de 6e eeuw v.Chr., de klim van tien minuten meer dan waard voor de ruïnes en het uitzicht. Volg het kustpad verder en u komt bij het piepkleine, prachtige"),
    "with its coloured fishermen's huts.": T(
        "con sus casetas de pescadores de colores.",
        "amb les seves casetes de pescadors de colors.",
        "avec ses cabanes de pêcheurs colorées.",
        "met zijn gekleurde vissershutjes."),
    "A large car park with around 600 spaces sits behind the beach, a few minutes' walk from the sand. In summer it is paid: €5 for the day, €3 from 14:00, €1 from 18:00.": T(
        "Detrás de la playa hay un gran aparcamiento con unas 600 plazas, a pocos minutos a pie de la arena. En verano es de pago: 5 € el día, 3 € desde las 14:00, 1 € desde las 18:00.",
        "Darrere de la platja hi ha un gran aparcament amb unes 600 places, a pocs minuts a peu de la sorra. A l'estiu és de pagament: 5 € el dia, 3 € des de les 14:00, 1 € des de les 18:00.",
        "Un grand parking d'environ 600 places se trouve derrière la plage, à quelques minutes à pied du sable. En été il est payant : 5 € la journée, 3 € à partir de 14h00, 1 € à partir de 18h00.",
        "Achter het strand ligt een grote parkeerplaats met zo'n 600 plekken, op een paar minuten lopen van het zand. In de zomer is die betaald: €5 voor de dag, €3 vanaf 14:00, €1 vanaf 18:00."),
    "outside high season the same car park is free. There is no closer alternative — the beach is protected and undeveloped, which is exactly its charm.": T(
        "fuera de temporada alta ese mismo aparcamiento es gratuito. No hay alternativa más cercana — la playa está protegida y sin urbanizar, que es justamente su encanto.",
        "fora de temporada alta aquest mateix aparcament és gratuït. No hi ha alternativa més propera — la platja està protegida i sense urbanitzar, que és justament el seu encant.",
        "hors haute saison, ce même parking est gratuit. Il n'y a pas d'alternative plus proche — la plage est protégée et non bâtie, et c'est précisément son charme.",
        "buiten het hoogseizoen is diezelfde parkeerplaats gratis. Er is geen dichterbij alternatief — het strand is beschermd en onbebouwd, en dat is precies de charme."),
    "— the beach bar on the sand; fresh fish and seafood, good bread and coffee, in a setting that's hard to beat. Summer only.": T(
        "— el chiringuito en la arena; pescado y marisco frescos, buen pan y café, en un entorno difícil de superar. Solo en verano.",
        "— el xiringuito a la sorra; peix i marisc frescos, bon pa i cafè, en un entorn difícil de superar. Només a l'estiu.",
        "— la paillote sur le sable ; poisson et fruits de mer frais, bon pain et bon café, dans un cadre difficile à égaler. L'été seulement.",
        "— het strandtentje op het zand; verse vis en zeevruchten, goed brood en koffie, in een setting die moeilijk te overtreffen is. Alleen in de zomer."),
    "— the second beach bar, with a wide menu and a very friendly welcome. Summer only.": T(
        "— el segundo chiringuito, con una carta amplia y una acogida muy amable. Solo en verano.",
        "— el segon xiringuito, amb una carta àmplia i una acollida molt amable. Només a l'estiu.",
        "— la seconde paillote, avec une carte étendue et un accueil très chaleureux. L'été seulement.",
        "— het tweede strandtentje, met een uitgebreide kaart en een heel vriendelijk onthaal. Alleen in de zomer."),
    "— the fishing port is famous for its": T(
        "— el puerto pesquero es famoso por sus",
        "— el port pesquer és famós per les seves",
        "— le port de pêche est célèbre pour ses",
        "— de vissershaven is beroemd om zijn"),
    ", the finest prawns in Catalunya. Worth a dedicated trip.": T(
        ", las mejores gambas de Catalunya. Merecen un viaje solo por ellas.",
        ", les millors gambes de Catalunya. Mereixen un viatge només per elles.",
        ", les meilleures gambas de Catalogne. Elles valent le déplacement à elles seules.",
        ", de beste garnalen van Catalonië. Een aparte rit waard."),
    "A wide, gently shelving bay just north of Palamós, and probably the most child-friendly beach in the area. The water stays shallow a long way out and is usually flat calm, protected by the headland — you can let small children paddle without watching every second. There's a proper little seafront with bars, sunbeds, pedalos and easy parking behind.": T(
        "Una bahía amplia y de pendiente suave justo al norte de Palamós, y probablemente la playa más apta para niños de la zona. El agua sigue siendo poco profunda mucho mar adentro y suele estar en calma total, resguardada por la punta — puede dejar chapotear a los pequeños sin vigilar cada segundo. Tiene un pequeño paseo marítimo en condiciones con bares, hamacas, patines y aparcamiento fácil detrás.",
        "Una badia àmplia i de pendent suau just al nord de Palamós, i probablement la platja més apta per a nens de la zona. L'aigua continua sent poc profunda molt mar endins i sol estar en calma total, arrecerada per la punta — podeu deixar xipollejar els petits sense vigilar cada segon. Té un petit passeig marítim com cal amb bars, gandules, patins i aparcament fàcil al darrere.",
        "Une baie large et à pente douce juste au nord de Palamós, et probablement la plage la plus adaptée aux enfants du secteur. L'eau reste peu profonde très loin et est généralement d'un calme plat, protégée par la pointe — on peut laisser les petits barboter sans surveiller chaque seconde. Il y a un vrai petit front de mer avec bars, transats, pédalos et un stationnement facile derrière.",
        "Een brede, geleidelijk aflopende baai net ten noorden van Palamós, en waarschijnlijk het meest kindvriendelijke strand in de omgeving. Het water blijft tot ver ondiep en is meestal spiegelglad, beschut door de landtong — u kunt kleine kinderen laten pootjebaden zonder elke seconde te hoeven kijken. Er is een echte kleine boulevard met bars, ligbedden, waterfietsen en makkelijk parkeren erachter."),
    "At the northern end stand the romantic ruins of the": T(
        "En el extremo norte se alzan las románticas ruinas del",
        "A l'extrem nord s'alcen les romàntiques ruïnes del",
        "À l'extrémité nord se dressent les ruines romantiques du",
        "Aan de noordkant staan de romantische ruïnes van het"),
    "on its rocky point, and beyond that the path continues to": T(
        "en su punta rocosa, y más allá el camino continúa hasta",
        "a la seva punta rocosa, i més enllà el camí continua fins a",
        "sur sa pointe rocheuse, et au-delà le sentier continue vers",
        "op de rotspunt, en daarachter loopt het pad door naar"),
    "and on to Castell — a lovely and easy hour's coastal walk. It's a busy, cheerful, family sort of beach rather than a wild one, and on the right day that's exactly what you want.": T(
        "y sigue hasta Castell — un paseo costero precioso y fácil de una hora. Es una playa animada, alegre y familiar más que salvaje, y en el día adecuado es exactamente lo que se busca.",
        "i continua fins a Castell — una passejada costanera preciosa i fàcil d'una hora. És una platja animada, alegre i familiar més que no pas salvatge, i el dia adequat és exactament el que es busca.",
        "puis jusqu'à Castell — une belle et facile heure de marche côtière. C'est une plage animée, gaie et familiale plutôt que sauvage, et le bon jour, c'est exactement ce qu'on cherche.",
        "en verder naar Castell — een mooie en makkelijke kustwandeling van een uur. Het is een druk, vrolijk gezinsstrand in plaats van een wild strand, en op de juiste dag is dat precies wat u wilt."),
    "A free car park with around 100 spaces sits roughly 200 m from the cove, plus free street parking on the roads around the bay.": T(
        "Hay un aparcamiento gratuito de unas 100 plazas a unos 200 m de la cala, además de aparcamiento libre en las calles de alrededor de la bahía.",
        "Hi ha un aparcament gratuït d'unes 100 places a uns 200 m de la cala, a més d'aparcament lliure als carrers del voltant de la badia.",
        "Un parking gratuit d'environ 100 places se trouve à quelque 200 m de la crique, en plus du stationnement gratuit dans les rues autour de la baie.",
        "Op ongeveer 200 m van de baai ligt een gratis parkeerplaats met zo'n 100 plekken, plus gratis parkeren in de straten rond de baai."),
    "It fills by about 10:00 in August — arrive early or plan on a slightly longer walk in from the streets behind.": T(
        "En agosto se llena hacia las 10:00 — llegue temprano o cuente con caminar un poco más desde las calles de detrás.",
        "A l'agost s'omple cap a les 10:00 — arribeu aviat o compteu amb caminar una mica més des dels carrers del darrere.",
        "En août, il est plein vers 10h00 — arrivez tôt ou prévoyez un peu plus de marche depuis les rues derrière.",
        "In augustus is die rond 10:00 vol — kom vroeg of houd rekening met een iets langere wandeling vanaf de straten erachter."),
    "— a good row of them facing the sand, doing paella, grilled fish and generous menus del dia.": T(
        "— una buena hilera de ellos frente a la arena, con paella, pescado a la brasa y menús del día generosos.",
        "— una bona filera d'ells davant de la sorra, amb paella, peix a la brasa i menús del dia generosos.",
        "— une belle rangée face au sable, avec paella, poisson grillé et généreux menus du jour.",
        "— een mooie rij ervan met uitzicht op het zand, met paella, gegrilde vis en royale dagmenu's."),
    "— several on the sand in season for a drink or a light lunch without moving.": T(
        "— varios en la arena en temporada para tomar algo o comer ligero sin moverse.",
        "— diversos a la sorra en temporada per prendre alguna cosa o menjar lleuger sense moure's.",
        "— plusieurs sur le sable en saison pour un verre ou un déjeuner léger sans bouger.",
        "— meerdere op het zand in het seizoen voor een drankje of lichte lunch zonder u te verplaatsen."),
    "— the fish market and the excellent seafood restaurants around the port; try the famous local prawns.": T(
        "— la lonja y los excelentes restaurantes de marisco alrededor del puerto; pruebe las famosas gambas locales.",
        "— la llotja i els excel·lents restaurants de marisc al voltant del port; proveu les famoses gambes locals.",
        "— la criée et les excellents restaurants de fruits de mer autour du port ; goûtez les fameuses gambas locales.",
        "— de visafslag en de uitstekende visrestaurants rond de haven; probeer de beroemde lokale garnalen."),

    # ── closing ──────────────────────────────────────────────────────────
    "Driving distances and times are approximate and measured from Tamariu village. Allow considerably longer in July and August, when parking rather than driving is the real constraint.": T(
        "Las distancias y tiempos en coche son aproximados y están medidos desde el pueblo de Tamariu. Cuente bastante más en julio y agosto, cuando la verdadera limitación es aparcar y no conducir.",
        "Les distàncies i temps en cotxe són aproximats i estan mesurats des del poble de Tamariu. Compteu-hi força més el juliol i l'agost, quan la veritable limitació és aparcar i no pas conduir.",
        "Les distances et durées en voiture sont approximatives et mesurées depuis le village de Tamariu. Comptez nettement plus en juillet et août, où la vraie contrainte est le stationnement, pas la conduite.",
        "Rijafstanden en -tijden zijn bij benadering en gemeten vanaf het dorp Tamariu. Reken in juli en augustus op aanzienlijk meer tijd, wanneer parkeren en niet rijden de echte beperking is."),
    "Every beach here has a day when it's at its best — wind direction, time of year and time of day all matter more on this coast than people expect. Tell us what you're after, whether that's a calm swim, a long lunch or a beach the children can run on, and we'll point you at the right one for that day.": T(
        "Cada playa de aquí tiene su día bueno — la dirección del viento, la época del año y la hora importan en esta costa más de lo que la gente espera. Díganos qué busca, ya sea un baño tranquilo, una comida larga o una playa donde los niños puedan correr, y le indicaremos la adecuada para ese día.",
        "Cada platja d'aquí té el seu dia bo — la direcció del vent, l'època de l'any i l'hora hi compten més del que la gent espera. Digueu-nos què busqueu, ja sigui un bany tranquil, un dinar llarg o una platja on els nens puguin córrer, i us indicarem la adequada per a aquell dia.",
        "Chaque plage ici a son jour de gloire — la direction du vent, la saison et l'heure comptent sur cette côte bien plus qu'on ne l'imagine. Dites-nous ce que vous cherchez — une baignade calme, un long déjeuner ou une plage où les enfants peuvent courir — et nous vous indiquerons la bonne pour ce jour-là.",
        "Elk strand hier heeft een dag waarop het op zijn best is — windrichting, seizoen en tijdstip tellen aan deze kust zwaarder dan mensen verwachten. Vertel ons wat u zoekt, of dat nu een rustige duik, een lange lunch of een strand is waar de kinderen kunnen rennen, en we wijzen u het juiste aan voor die dag."),

    ", is the thing to order.": T(
        ", es lo que hay que pedir.", ", és el que cal demanar.",
        ", c'est ce qu'il faut commander.", ", is wat u moet bestellen."),
    "~1 hr": T("~1 h", "~1 h", "~1 h", "~1 uur"),

    # ── image alt text ───────────────────────────────────────────────────
    "Platja de Tamariu, a sheltered sandy bay with fishing boats and pine-covered headlands, Costa Brava": T(
        "Platja de Tamariu, una bahía de arena resguardada con barcas de pesca y puntas cubiertas de pinos, Costa Brava",
        "Platja de Tamariu, una badia de sorra arrecerada amb barques de pesca i puntes cobertes de pins, Costa Brava",
        "Platja de Tamariu, une baie de sable abritée avec barques de pêche et pointes couvertes de pins, Costa Brava",
        "Platja de Tamariu, een beschutte zandbaai met vissersboten en met dennen begroeide landtongen, Costa Brava"),
    "Cala Pedrosa, a tiny pebble cove south of Tamariu reachable only on foot or by boat": T(
        "Cala Pedrosa, una diminuta cala de cantos al sur de Tamariu a la que solo se llega a pie o en barca",
        "Cala Pedrosa, una diminuta cala de còdols al sud de Tamariu on només s'arriba a peu o amb barca",
        "Cala Pedrosa, une minuscule crique de galets au sud de Tamariu, accessible seulement à pied ou en bateau",
        "Cala Pedrosa, een piepkleine kiezelbaai ten zuiden van Tamariu, alleen te voet of per boot bereikbaar"),
    "Platja d'Aiguablava, brilliant turquoise water in a sheltered bay backed by pines, Begur": T(
        "Platja d'Aiguablava, agua turquesa brillante en una bahía resguardada con pinos detrás, Begur",
        "Platja d'Aiguablava, aigua turquesa brillant en una badia arrecerada amb pins al darrere, Begur",
        "Platja d'Aiguablava, eau turquoise éclatante dans une baie abritée bordée de pins, Begur",
        "Platja d'Aiguablava, schitterend turquoise water in een beschutte baai met dennen erachter, Begur"),
    "Aigua Xelida, a small rocky cove with turquoise water between Tamariu and Aiguablava": T(
        "Aigua Xelida, una pequeña cala rocosa de agua turquesa entre Tamariu y Aiguablava",
        "Aigua Xelida, una petita cala rocosa d'aigua turquesa entre Tamariu i Aiguablava",
        "Aigua Xelida, une petite crique rocheuse aux eaux turquoise entre Tamariu et Aiguablava",
        "Aigua Xelida, een kleine rotsachtige baai met turquoise water tussen Tamariu en Aiguablava"),
    "Platja de Llafranc, a broad sandy bay with a palm-lined promenade and yachts at anchor": T(
        "Platja de Llafranc, una amplia bahía de arena con paseo de palmeras y yates fondeados",
        "Platja de Llafranc, una àmplia badia de sorra amb passeig de palmeres i iots fondejats",
        "Platja de Llafranc, une large baie de sable avec promenade bordée de palmiers et yachts au mouillage",
        "Platja de Llafranc, een brede zandbaai met een met palmen omzoomde boulevard en jachten voor anker"),
    "Calella de Palafrugell, white fishermen's houses and arched arcades above small sandy coves": T(
        "Calella de Palafrugell, casas blancas de pescadores y arcadas sobre pequeñas calas de arena",
        "Calella de Palafrugell, cases blanques de pescadors i arcades sobre petites cales de sorra",
        "Calella de Palafrugell, maisons blanches de pêcheurs et arcades au-dessus de petites criques sableuses",
        "Calella de Palafrugell, witte vissershuizen en booggalerijen boven kleine zandbaaien"),
    "Cala del Golfet, a small cove below red cliffs and pine woods near Cap Roig": T(
        "Cala del Golfet, una pequeña cala bajo acantilados rojos y pinares cerca de Cap Roig",
        "Cala del Golfet, una petita cala sota penya-segats vermells i pinedes a prop de Cap Roig",
        "Cala del Golfet, une petite crique sous des falaises rouges et des pinèdes près de Cap Roig",
        "Cala del Golfet, een kleine baai onder rode kliffen en dennenbossen bij Cap Roig"),
    "Sa Riera beach at Begur, a sandy bay with fishing boats and white houses on the hillside": T(
        "Playa de Sa Riera en Begur, una bahía de arena con barcas de pesca y casas blancas en la ladera",
        "Platja de Sa Riera a Begur, una badia de sorra amb barques de pesca i cases blanques al vessant",
        "Plage de Sa Riera à Begur, une baie de sable avec barques de pêche et maisons blanches à flanc de colline",
        "Strand Sa Riera bij Begur, een zandbaai met vissersboten en witte huizen tegen de helling"),
    "Sa Tuna cove at Begur, white houses around a small pebble beach with a waterfront restaurant": T(
        "Cala de Sa Tuna en Begur, casas blancas alrededor de una pequeña playa de cantos con restaurante junto al agua",
        "Cala de Sa Tuna a Begur, cases blanques al voltant d'una petita platja de còdols amb restaurant arran d'aigua",
        "Crique de Sa Tuna à Begur, maisons blanches autour d'une petite plage de galets avec un restaurant au bord de l'eau",
        "Baai Sa Tuna bij Begur, witte huizen rond een klein kiezelstrand met een restaurant aan het water"),
    "Platja de Pals, a long open sandy beach backed by pine woods with the Medes Islands on the horizon": T(
        "Platja de Pals, una larga playa de arena abierta con pinares detrás y las islas Medes en el horizonte",
        "Platja de Pals, una llarga platja de sorra oberta amb pinedes al darrere i les illes Medes a l'horitzó",
        "Platja de Pals, une longue plage de sable ouverte bordée de pinèdes avec les îles Medes à l'horizon",
        "Platja de Pals, een lang open zandstrand met dennenbossen erachter en de Medes-eilanden aan de horizon"),
    "Platja de Castell near Palamós, an undeveloped sandy bay backed by pine woods and farmland": T(
        "Platja de Castell cerca de Palamós, una bahía de arena sin urbanizar con pinares y campos detrás",
        "Platja de Castell a prop de Palamós, una badia de sorra sense urbanitzar amb pinedes i camps al darrere",
        "Platja de Castell près de Palamós, une baie de sable non bâtie bordée de pinèdes et de terres agricoles",
        "Platja de Castell bij Palamós, een onbebouwde zandbaai met dennenbossen en landbouwgrond erachter"),
    "La Fosca beach at Palamós, a sheltered sandy bay with shallow calm water": T(
        "Playa de La Fosca en Palamós, una bahía de arena resguardada con agua tranquila y poco profunda",
        "Platja de La Fosca a Palamós, una badia de sorra arrecerada amb aigua tranquil·la i poc profunda",
        "Plage de La Fosca à Palamós, une baie de sable abritée aux eaux calmes et peu profondes",
        "Strand La Fosca bij Palamós, een beschutte zandbaai met ondiep, rustig water"),
}

STRINGS = dict(LABELS)
STRINGS.update(PROSE)

PAGES = {
    "things-to-do/local-beaches.html": {
        "mode": "strings",
        "footer": FOOTER_STD,
        "meta": {
            "es": {"title": "Playas y Calas Locales — Tamariu Chalet",
                   "desc": "Guía honesta de las playas cerca de Tamariu, Costa Brava — 12 playas y calas con distancias, aparcamiento, dónde comer y para qué va bien cada una."},
            "ca": {"title": "Platges i Cales Locals — Tamariu Chalet",
                   "desc": "Guia honesta de les platges a prop de Tamariu, Costa Brava — 12 platges i cales amb distàncies, aparcament, on menjar i per a què va bé cadascuna."},
            "fr": {"title": "Plages &amp; Criques Locales — Tamariu Chalet",
                   "desc": "Guide honnête des plages près de Tamariu, Costa Brava — 12 plages et criques avec distances, stationnement, où manger et à quoi chacune convient."},
            "nl": {"title": "Lokale Stranden &amp; Baaien — Tamariu Chalet",
                   "desc": "Eerlijke gids voor de stranden bij Tamariu, Costa Brava — 12 stranden en baaien met afstanden, parkeren, waar te eten en waarvoor elk geschikt is."},
        },
        "strings": STRINGS,
    }
}
