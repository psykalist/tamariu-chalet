#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shared parking snippets for the "things to do" guide pages.

The recommended places (villages tour, markets, Girona, worth-the-drive
restaurants, local beaches) each carry a compact one-line parking note:

    🅿 Parking: <cost phrase> — Google Maps pin ↗

Only three kinds of text node are translatable — the "Parking:" label, the
cost phrase, and the "Google Maps pin ↗" link text — and each is isolated in
its own element so strings-mode substitutes it cleanly (whole-node match).
Car-park map pins are language-neutral URLs, so they never change.

Usage:
  * strings-mode pages (villages, girona, restaurants, beaches):
        from content_parking import PARKING_STRINGS
        PAGES[logical]["strings"].update(PARKING_STRINGS)
    German is picked up automatically because each entry already carries "de".
  * the English HTML line is produced by html_line() so the visible text always
    matches the PARKING_STRINGS keys exactly (see insert_parking.py).
  * markets is full-content mode; it writes the same phrases inline per language
    (see content_things_to_do / de_pages), reusing COST/label wording below.
"""


def _t(es, ca, fr, nl, de):
    return {"es": es, "ca": ca, "fr": fr, "nl": nl, "de": de}


LABEL_EN = "Parking:"
PIN_EN = "Google Maps pin ↗"

# key -> English cost phrase (each is one isolated text node)
COSTS = {
    "free": "Free.",
    "village_summer": "Free out of season; blue-zone charge in summer (about €1–2/hour).",
    "peratallada": "Blue zone — first 30 min free, then about €1–2/hour; free in low season.",
    "beach_paid": "Paid in summer (about €10/day), free the rest of the year.",
    "llafranc": "Free car parks at the village edge; central blue-zone bays charge in summer.",
    "girona": "Free beside the Devesa park (Av. Ramon Folch); central car parks about €15–22/day.",
    "big_free": "Large free car park by the beach (about 600 spaces).",
    "calella": "Mostly free street parking; blue zone in the centre from mid-June to mid-September.",
    "onsite": "Free parking on site.",
    "town_free": "Free car parks a few minutes' walk from the centre.",
    "tamariu": "Small paid car park by the beach in summer; free the rest of the year.",
    "sa_riera": "Paid by the beach in summer; a few free spaces up the access road — arrive early.",
    "sa_tuna": "Very limited paid parking — come early or take the summer beach bus.",
    "castell": "Paid car park in summer (about €10/day), then a short walk through the pines.",
    "palamos": "Free car park behind the beach; seafront bays paid in summer (about €10/day).",
}

# English source string -> {es, ca, fr, nl, de}
PARKING_STRINGS = {
    LABEL_EN: _t("Aparcamiento:", "Aparcament:", "Stationnement :", "Parkeren:", "Parken:"),
    PIN_EN: _t(
        "Ubicación en Google Maps ↗", "Ubicació a Google Maps ↗",
        "Emplacement Google Maps ↗", "Locatie op Google Maps ↗",
        "Standort auf Google Maps ↗"),

    COSTS["free"]: _t("Gratis.", "Gratuït.", "Gratuit.", "Gratis.", "Kostenlos."),

    COSTS["village_summer"]: _t(
        "Gratis fuera de temporada; zona azul en verano (aprox. 1–2 €/hora).",
        "Gratuït fora de temporada; zona blava a l'estiu (aprox. 1–2 €/hora).",
        "Gratuit hors saison ; zone bleue en été (env. 1–2 €/heure).",
        "Buiten het seizoen gratis; blauwe zone in de zomer (ca. €1–2/uur).",
        "Außerhalb der Saison kostenlos; blaue Zone im Sommer (ca. 1–2 €/Stunde)."),

    COSTS["peratallada"]: _t(
        "Zona azul — primera media hora gratis, después aprox. 1–2 €/hora; gratis en temporada baja.",
        "Zona blava — primera mitja hora gratis, després aprox. 1–2 €/hora; gratis a temporada baixa.",
        "Zone bleue — première demi-heure gratuite, puis env. 1–2 €/heure ; gratuit en basse saison.",
        "Blauwe zone — eerste half uur gratis, daarna ca. €1–2/uur; buiten het seizoen gratis.",
        "Blaue Zone — erste 30 Min. kostenlos, dann ca. 1–2 €/Stunde; in der Nebensaison kostenlos."),

    COSTS["beach_paid"]: _t(
        "De pago en verano (aprox. 10 €/día), gratis el resto del año.",
        "De pagament a l'estiu (aprox. 10 €/dia), gratuït la resta de l'any.",
        "Payant en été (env. 10 €/jour), gratuit le reste de l'année.",
        "Betaald in de zomer (ca. €10/dag), de rest van het jaar gratis.",
        "Im Sommer kostenpflichtig (ca. 10 €/Tag), sonst kostenlos."),

    COSTS["llafranc"]: _t(
        "Aparcamientos gratuitos a las afueras; zona azul en el centro en verano.",
        "Aparcaments gratuïts a les afores; zona blava al centre a l'estiu.",
        "Parkings gratuits en périphérie ; zone bleue au centre en été.",
        "Gratis parkeerplaatsen aan de rand; blauwe zone in het centrum in de zomer.",
        "Kostenlose Parkplätze am Ortsrand; blaue Zone im Zentrum im Sommer."),

    COSTS["girona"]: _t(
        "Gratis junto al parque de la Devesa (Av. Ramon Folch); parkings del centro aprox. 15–22 €/día.",
        "Gratis vora el parc de la Devesa (Av. Ramon Folch); pàrquings del centre aprox. 15–22 €/dia.",
        "Gratuit le long du parc de la Devesa (Av. Ramon Folch) ; parkings du centre env. 15–22 €/jour.",
        "Gratis langs het Devesa-park (Av. Ramon Folch); parkeergarages in het centrum ca. €15–22/dag.",
        "Kostenlos am Devesa-Park (Av. Ramon Folch); Parkhäuser im Zentrum ca. 15–22 €/Tag."),

    COSTS["big_free"]: _t(
        "Gran aparcamiento gratuito junto a la playa (unas 600 plazas).",
        "Gran aparcament gratuït vora la platja (unes 600 places).",
        "Grand parking gratuit près de la plage (environ 600 places).",
        "Grote gratis parkeerplaats bij het strand (ongeveer 600 plaatsen).",
        "Großer kostenloser Parkplatz am Strand (etwa 600 Plätze)."),

    COSTS["calella"]: _t(
        "Aparcamiento en la calle mayormente gratuito; zona azul en el centro de mediados de junio a mediados de septiembre.",
        "Aparcament al carrer majoritàriament gratuït; zona blava al centre de mitjan juny a mitjan setembre.",
        "Stationnement de rue en grande partie gratuit ; zone bleue au centre de mi-juin à mi-septembre.",
        "Grotendeels gratis parkeren op straat; blauwe zone in het centrum van half juni tot half september.",
        "Straßenparken größtenteils kostenlos; blaue Zone im Zentrum von Mitte Juni bis Mitte September."),

    COSTS["onsite"]: _t(
        "Aparcamiento gratuito en el propio restaurante.",
        "Aparcament gratuït al mateix restaurant.",
        "Stationnement gratuit sur place.",
        "Gratis parkeren bij het restaurant.",
        "Kostenloses Parken direkt am Restaurant."),

    COSTS["town_free"]: _t(
        "Aparcamientos gratuitos a pocos minutos a pie del centro.",
        "Aparcaments gratuïts a pocs minuts a peu del centre.",
        "Parkings gratuits à quelques minutes à pied du centre.",
        "Gratis parkeerplaatsen op een paar minuten lopen van het centrum.",
        "Kostenlose Parkplätze wenige Gehminuten vom Zentrum."),

    COSTS["tamariu"]: _t(
        "Pequeño aparcamiento de pago junto a la playa en verano; gratis el resto del año.",
        "Petit aparcament de pagament vora la platja a l'estiu; gratuït la resta de l'any.",
        "Petit parking payant près de la plage en été ; gratuit le reste de l'année.",
        "Kleine betaalde parkeerplaats bij het strand in de zomer; de rest van het jaar gratis.",
        "Kleiner kostenpflichtiger Parkplatz am Strand im Sommer; sonst kostenlos."),

    COSTS["sa_riera"]: _t(
        "De pago junto a la playa en verano; algunas plazas gratuitas subiendo por la carretera de acceso — llegue temprano.",
        "De pagament vora la platja a l'estiu; algunes places gratuïtes pujant per la carretera d'accés — arribeu aviat.",
        "Payant près de la plage en été ; quelques places gratuites en remontant la route d'accès — arrivez tôt.",
        "Betaald bij het strand in de zomer; enkele gratis plaatsen langs de toegangsweg — kom vroeg.",
        "Am Strand im Sommer kostenpflichtig; einige kostenlose Plätze die Zufahrtsstraße hinauf — früh kommen."),

    COSTS["sa_tuna"]: _t(
        "Aparcamiento de pago muy limitado — llegue muy temprano o use el bus de playa de verano.",
        "Aparcament de pagament molt limitat — arribeu molt aviat o feu servir el bus de platja d'estiu.",
        "Stationnement payant très limité — arrivez très tôt ou prenez la navette de plage estivale.",
        "Zeer beperkt betaald parkeren — kom heel vroeg of neem de zomerse strandbus.",
        "Sehr begrenztes kostenpflichtiges Parken — sehr früh kommen oder den Sommer-Strandbus nehmen."),

    COSTS["castell"]: _t(
        "Aparcamiento de pago en verano (aprox. 10 €/día) y luego un corto paseo entre los pinos.",
        "Aparcament de pagament a l'estiu (aprox. 10 €/dia) i després un curt passeig entre els pins.",
        "Parking payant en été (env. 10 €/jour), puis une courte marche à travers les pins.",
        "Betaalde parkeerplaats in de zomer (ca. €10/dag), daarna een korte wandeling door de dennen.",
        "Kostenpflichtiger Parkplatz im Sommer (ca. 10 €/Tag), dann ein kurzer Weg durch die Pinien."),

    COSTS["palamos"]: _t(
        "Aparcamiento gratuito detrás de la playa; plazas del paseo marítimo de pago en verano (aprox. 10 €/día).",
        "Aparcament gratuït darrere la platja; places del passeig marítim de pagament a l'estiu (aprox. 10 €/dia).",
        "Parking gratuit derrière la plage ; places du front de mer payantes en été (env. 10 €/jour).",
        "Gratis parkeerplaats achter het strand; plaatsen aan de boulevard betaald in de zomer (ca. €10/dag).",
        "Kostenloser Parkplatz hinter dem Strand; Plätze an der Strandpromenade im Sommer kostenpflichtig (ca. 10 €/Tag)."),
}


def inline_line(lang: str, cost_key: str, maps_url: str) -> str:
    """A fully-translated parking line for full-content pages (e.g. markets)."""
    if lang == "en":
        label, cost, pin = LABEL_EN, COSTS[cost_key], PIN_EN
    else:
        label = PARKING_STRINGS[LABEL_EN][lang]
        cost = PARKING_STRINGS[COSTS[cost_key]][lang]
        pin = PARKING_STRINGS[PIN_EN][lang]
    return (
        f'<p class="parking-note" style="{PARKING_STYLE}">🅿 '
        f'<strong>{label}</strong> <span>{cost}</span> '
        f'— <a href="{maps_url}" target="_blank" rel="noopener" '
        f'style="color:var(--deep-blue);font-weight:600;white-space:nowrap;">{pin}</a></p>'
    )


def pin_line(maps_url: str) -> str:
    """Just the Google Maps pin link (for pages that already state cost)."""
    return (
        f'<p class="parking-pin" style="margin:8px 0 0;font-size:0.92rem;">'
        f'📍 <a href="{maps_url}" target="_blank" rel="noopener" '
        f'style="color:var(--deep-blue);font-weight:600;">{PIN_EN}</a></p>'
    )


def html_line(cost_key: str, maps_url: str) -> str:
    """The exact English parking line to embed on an English page.

    Text nodes isolated so strings-mode matches each whole node:
    "Parking:", the cost phrase, and "Google Maps pin ↗".
    """
    cost = COSTS[cost_key]
    return (
        f'<p class="parking-note" style="{PARKING_STYLE}">🅿 '
        f'<strong>{LABEL_EN}</strong> <span>{cost}</span> '
        f'— <a href="{maps_url}" target="_blank" rel="noopener" '
        f'style="color:var(--deep-blue);font-weight:600;white-space:nowrap;">{PIN_EN}</a></p>'
    )


# Inline so no site-wide CSS / cache-buster bump is needed; copied verbatim into
# every translated page.
PARKING_STYLE = (
    "margin:12px 0 0;padding:9px 13px;background:#eef5f8;"
    "border-left:3px solid var(--deep-blue);border-radius:5px;"
    "font-size:0.95rem;line-height:1.55;"
)
