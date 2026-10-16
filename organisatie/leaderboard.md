# Leaderboard — LAN-party 26

> ## ⚠️ Status: DEPRECATED — vervangen door het LAN-portaal
> De oorspronkelijke Python-leaderboard (zie `leaderboard/` in de repo) wordt **niet meer gebruikt**.
> **Kyell** heeft het uitgrown tot een volwaardig **LAN-portaal**:
> [**github.com/kyell182/lan-portaal**](https://github.com/kyell182/lan-portaal)
> (Docker, volledig offline; scoreboard + toernooien met live brackets, edities,
> zitplan, prijzen, Discord-meldingen, PWA). Dit document blijft de
> **oorspronkelijke opdracht- en scope-eisen** van de hoofdtak bewaren — de
> privacykaders (pseudoniem, lokaal bewaren, verwijdering binnen 1 week) blijven
> van toepassing op het portaal.

> De leaderboard was een van de twee hoofdtaken van ons project (naast de inrichting en uitvoering in Stuvo).

## 1. Doel

Een zichtbaar, live scoreboard waarop de spelresultaten van de deelnemers worden getoond. De leaderboard:

- motiveren: deelnemers zien hun stand en die van anderen;
- draagt bij aan de sfeer (projectie of scherm in het lokaal);
- de toernooirondes volgt, waar toernooien georganiseerd worden.

## 2. Scope (concept)

| Onderdeel | Beslissing | Status |
|---|---|---|
| Ondersteunde games | Dynamisch toevoegbaar (geen vaste lijst; de crew registreert welke games aan bod komen) | Concept |
| Toernooivorm | Gekoppelde rondes; regels en verantwoordelijke vast te leggen | Open |
| Invoer van resultaten | Handmatig door crew / vrijwilligers bij de servicedesk (eenvoudig, robuust) | Concept |
| Weergave | Een scherm in het lokaal; projectie waar mogelijk | Concept |
| Privacy | Alleen nickname of pseudoniem van de deelnemer; geen naam of e-mail | Vereist |
| Opslag | Lokaal op de eventhost; geen persoonsgegevens in de repo | Vereist |

## 3. Privacytoestemming

Volgens de opdracht mag een live scoreboard alleen met **expliciete privacytoestemming** van de deelnemer (zie opdrachtsectie *Could* en *Gedragscode*). De inschrijving verloopt via IEEE student branch Brugge; de privacytoestemming voor de leaderboard verwerkt daar in hun inschrijfformulier, terwijl wij de privacykaders aan onze kant documenteren:

- [ ] Privacytoestemming voor de leaderboard via het IEEE-inschrijfformulier (checkbox, expliciet) — af te stemmen met IEEE (contact: Kyell).
- [x] Alleen het pseudoniem tonen dat de deelnemer zelf kiest; de koppeling met de echte naam blijft lokaal en wordt na afloop verwijderd.
- [x] Deelnemer kan toestemming weigeren zonder dat dit zijn deelname belemmert.
- [x] Bewaartermijn: scoreboard-data wordt binnen 1 week na het event verwijderd.

## 4. Uitvoering (te specificeren)

De technische aanpak wordt gekozen op basis van wat met minimale infrastructuur haalbaar is in Stuvo. Opties (niet uitgewerkt):

1. **Lokale web-app** met een eenvoudige database (bijv. een statische front-end die een lokale API of bestand leest); resultaten worden door de crew ingevoerd.
2. **Bestaand toernooi-/scorebordtool** dat we lokaal draaien.
3. **Voorbeeldopstelling** in het netwerkontwerp: de leaderboard-server zit in VLAN 20 (Core Services), bereikbaar voor de crew, niet voor het open deelnemersnetwerk.

De keuze wordt vastgelegd in [overzicht.md](../netwerk/overzicht.md) zodra de services worden uitgewerkt.

## 5. Acceptatiecriteria (concept)

- [ ] De leaderboard toont minimaal een ranking van de deelnemers in de ondersteunde games.
- [ ] Resultaten kunnen door de crew worden bijgewerkt zonder onderbreking.
- [ ] Alleen pseudoniemen zijn zichtbaar; persoonsgegevens zijn niet zichtbaar en niet in de repo.
- [ ] De privacytoestemming is geregeld en geregistreerd via het IEEE-inschrijfformulier.
- [ ] De leaderboard draait lokaal en werkt offline (afhankelijk van de uplink is toegestaan maar niet vereist).
- [ ] Een draaiboek-punt in [05-bijlagen.md](../draaiboek/05-bijlagen.md) dekt op- en afschakeling van de leaderboard.

## 6. Status

| Veld | Waarde |
|---|---|
| Status | **DEPRECATED** — vervangen door het [LAN-portaal](https://github.com/kyell182/lan-portaal) van Kyell (Docker, offline). De Python-code blijft ter referentie. |
| Eigenaar | oorspr. Jules (back-up Kyell); portaal: Kyell |
| Verbonden gate | Gate 3 (Techniek) en Gate 4 (Communicatie) — beide vóór 20/10 |
| Datum | 2026-10-16 (deprecation: zie logboek) |
