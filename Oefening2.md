# 2. Backtracking

William is een konijn en de planten zich natuurlijk voort als konijnen. William heeft dus een aantal kinderen. Elk konijn heeft een naam, leeftijd, kinderen, linkeroor en rechteroor. De oren van een konijn hebben een bepaalde lengte, breedte en oppervlakte.

# Opgave 2.1

Denk even na over de mogelijke klasses die je hier kan maken en welke attributen deze klassen dan zouden hebben.
Schrijf dit even op.

# Opgave 2.2

- Maak een klasse genaamd 'KonijnenOor' (in een file `oef2_2.py`) en voeg een constructor toe met als parameters: `lengte`, `breedte` en `oppervlakte`.
  - De oppervlakte is een optionele parameter. (zorg er dus voor dat dit ook zo is)
  - Als de oppervlakte niet gegeven is, mag je aannemen dat het oor rechthoekig is. `oppervlakte = lengte * breedte`
- Maak de methodes `getLengte()`, `getBreedte()` en `getOppervlakte()`
- Voeg de mogelijkheid toe om de lengte aan te passen via `setLengte(lengte)`. Een aanpassing van de lengte past de oppervlakte NIET aan.
- Run `assertions_oef2_2.py` om te testen of de code correct is.

# Opgave 2.3

- Pas de klasse aan (in een file `oef2_3.py`) zodat het enkel getallen (`int`) accepteert als waarden voor de breedte, hoogte en oppervlakte. Als een andere waarde wordt meegegeven, zet de waarde dan op volgende standaardwaarden: 12 voor lengte, 6 voor breedte, 67 voor oppervlakte.
- Run `assertions_oef2_3.py` om te testen of de code correct is.

# Opgave 2.4

- Maak een klasse Konijn (in een file `oef2_4.py` die ook de KonijnenOor klasse bevat) met een constructor met als parameters: `naam` (string), `leeftijd` (getal), `linkerOor` (KonijnenOor) en `rechterOor` (KonijnenOor)
- Controleer of de parameters een waarde van het juiste type hebben en zet de waarde op `None` als het type fout is
- Voeg de methodes `getNaam()`, `getLeeftijd()`, `getLinkerOor()`, `getRechterOor()` toe
- Voeg de methodes `addKind(kind)` en `getKinderen()` (geeft lijst van kinderen terug) toe
- Run `assertions_oef2_4.py` om te testen of de code correct is.

# Opgave 2.5

- Voeg de methode `getJongsteKind()` toe (in een file `oef2_5.py`) die het jongste kind van een konijn teruggeeft. Bij gelijke leeftijd, neem degene met de kleinste naam volgens de `<` operator. None als het konijn geen kinderen heeft.
- Bespreek de tijdscomplexiteit
- Run `assertions_oef2_5.py` om te testen of de code correct is.

# Opgave 2.6

- Zorg ervoor (in een file `oef2_6.py`) dat als je een konijn object print, hij het volgende print: `Hallo ik ben <naam> en ik ben <leeftijd> jaar oud. Ik heb <aantal_kinderen> kinderen. De afmetingen van mijn linkeroor zijn: <lengte_linkeroor> <breedte_linkeroor> <oppervlakte_linkeroor> en van mijn rechteroor: <lengte_rechteroor> <breedte_rechteroor> <oppervlakte_rechteroor>.`
- Run `assertions_oef2_6.py` om te testen of de code correct is.
