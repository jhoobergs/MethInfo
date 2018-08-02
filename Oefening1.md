# 1. Backtracking

William het konijn is onderweg naar huis. Hij is een beetje een vreemde vogel en kan enkel sprongen van 60cm en 1m10 maken.
Hij zou willen weten welke mogelijke opeenvolgingen van sprongen (bv een sprong van 60cm, nog één van 60cm en dan één van 1m10 om 2m30 af te leggen) hij kan doen om thuis te geraken.

## Opgave 1.1

Schrijf een functie `william_find_all(distance)` (in een file genaamd `oef1_1.py`) die gegeven een afstand, alle mogelijke opeenvolgingen van sprongen geeft die William kan doen om exact de gevraagde afstand af te leggen. Het resultaat van de functie moet een lijst van opeenvolgingen zijn. Een opeenvolging is zelf een lijst van de afstanden die elke sprong aflegt. Het resultaat moet dus een lijst van lijsten zijn. Voor een afstand van 2m30 moet de oplossing gelijk zijn aan `[[110, 60, 60], [60, 110, 60], [60, 60, 110]]`. Run `assertions_oef1_1.py` om te testen of de code correct is.

### Opmerking: Zorg ervoor dat je code makkelijk aangepast kan worden in het geval dat Willam andere afstanden en/of meer verschillende afstanden kan springen.

### Opmerking 2: Gebruik cm's also eenheid.

## Opgave 1.2

Schrijf nu een functie `william_find_amount(distance)` (in een file genaamd `oef1_2.py`) die gegeven een afstand, het aantal verschillende opeenvolgingen berekent (ipv wat de exacte opeenvolgingen zijn). Run `assertions_oef1_2.py` om te testen of de code correct is.

### Opmerking: Neem niet gewoon de lengte van het resultaat van de functie van vorige oefening.

### Opmerking 2: De code zal hard lijken op die van vorige oefening.

## Opgave 1.3

William wilt meestal in zo weinig mogelijk sprongen ergens geraken. Schrijf nu een functie `william_find_shortest(distance)` (in een file genaamd `oef1_3.py`) die gegeven een afstand, de opeenvolging met de minste sprongen geeft. Als twee opeenvolgingen even veel sprongen hebben, wilt hij degene die kleiner is volgens de python `<` operator. Als er geen opeenvolging bestaat, geef dan `None` terug. Run `assertions_oef1_3.py` om te testen of de code correct is.

### Opmerking: Neem niet gewoon de kortste uit het resultaat van de functie van de eerste oefening.

### Opmerking 2: De code zal hard lijken op die van vorige oefeningen.

## Opgave 1.4

William moet soms ook op bezoek bij zijn schoonmoeder. In dat geval wilt hij zo veel mogelijk sprongen doen, om zo weinig mogelijk tijd met haar te moeten doorbrengen. Schrijf nu een functie `william_find_longest(distance)` (in een file genaamd `oef1_4.py`) die gegeven een afstand, de opeenvolging met de meeste sprongen geeft. Als twee opeenvolgingen even veel sprongen hebben, wilt hij degene die groter is volgens de python `>` operator. Als er geen opeenvolging bestaat, geef dan `None` terug. Run `assertions_oef1_4.py` om te testen of de code correct is.

### Opmerking: Neem niet gewoon de langste uit het resultaat van de functie van de eerste oefening.

### Opmerking 2: De code zal hard lijken op die van vorige oefeningen.
