# Conceptnota — LAN-party 26

> Conceptnota voor het evenement "LAN-party 26". Deze nota vormt de basis voor **Gate 1: Concept akkoord**. Datum (22/10/2026) en locatie (Stuvo) zijn vastgelegd; de deelnemerscapaciteit wordt door de IEEE student branch Brugge bepaald (de inschrijving verloopt via IEEE; de eigen studentenbevraging is afgevoerd).

## 1. Doel

Een veilige, inclusieve en technisch sterke LAN-party organiseren voor studenten, waarin zij samen kunnen gamen in een stabiele en beheersbare omgeving. Het project toont het volledige traject van concept tot uitvoering, inclusief goedkeuringen, netwerkontwerp, caching, support, veiligheid en evaluatie.

## 2. Probleem en behoefte

Studenten willen een georganiseerd evenement waarin ze samen kunnen gamen. Zonder voorafgaande voorbereiding bestaan risico's rond netwerkbelasting, stroom, veiligheid, privacy, ondersteuning en communicatie. Een gestructureerde aanpak zorgt voor een stabiel netwerk, een veilige omgeving en een goede deelnemersexperience.

## 3. Doelgroep

- Studenten van de campus als hoofddoelgroep.
- Deelnemers variëren van casual gamers tot competitieve spelers.
- Deelnemers die niet meespelen, krijgen inclusieve nevenactiviteiten (boardgames, RetroPie, Arduino-entertainment).

De definitieve doelgroepomvang wordt bepaald op basis van de inschrijving via IEEE student branch Brugge en de capaciteit van Stuvo.

## 4. Concept en kenmerken

| Onderdeel | Concept | Status |
|---|---|---|
| Speelopstelling | Bekabelde LAN-opstelling met beheerde switches; eigen DHCP/AP alleen na IT-goedkeuring | Concept |
| Caching | LANCache voor toegelaten platformen (o.a. Steam); getest op opslag, hitratio, DNS-impact en fallback | Concept |
| Lokale gameservers | Pico 4 LAN-concept met Quake3Quest en mogelijke casting; overige lokale servers waar licenties dit toelaten | Concept |
| RetroPie | RetroPie op minipc voor klassieke games; handleiding en setup door Kyell | Concept |
| Arduino-controller | Ontdekking van mogelijkheden voor een Arduino-gebaseerde controller of entertainmentelement | Concept |
| Boardgames / Spellenlab | Inclusieve nevenactiviteit via Spellenlab voor niet-meespelende deelnemers | Concept |
| Leaderboard | Live scoreboard dat spelresultaten van de deelnemers toont; hoofdtaken van ons project (zie [leaderboard.md](leaderboard.md)) | Concept |
| Inschrijving | Minimale gegevensverwerking met privacytekst, bewaartermijn en gedragscode | Concept |
| Support | Servicedesk met triage, gekende problemen, reservekabels en escalatiepad | Concept |

## 5. Datumopties en timing

| Optie | Datum | Opmerking |
|---|---|---|
| 1 | Donderdag 22 oktober 2026, 18:00–24:00 | Vastgelegd |

De LAN-party vindt plaats op **donderdag 22 oktober 2026, van 18:00 tot 24:00**. Het evenement is een eenmalig dag-event.

## 6. Locatie en capaciteit (concept)

De LAN-party vindt plaats in **Stuvo**, het kleine gebouw op de campus. De overkoepelende organisatie wordt gedaan door **IEEE student branch Brugge** (aanspreekpunt: Jonas Rollier); ons project is verantwoordelijk voor de inrichting en uitvoering in Stuvo en voor de leaderboard.

| Aspect | Concept | Status |
|---|---|---|
| Locatie | Stuvo (klein gebouw op campus), 18:00–24:00 | Vastgelegd |
| Capaciteit deelnemers | Te bevestigen via IEEE (inschrijving) en Stuvo | Open |
| Tafels / werkplekken | Aantal en indeling te bepalen | Open |
| Stroom | Aantal en verdeling stroompunten te bepalen | Open |
| Evacuatie en toegankelijkheid | In overleg met preventie | Open |
| Sanitair en toezicht | In overleg met gebouwbeheer | Open |

## 7. Technische uitgangspunten

- Het netwerkontwerp bouwt op de door IT goedgekeurde uplink en diensten.
- Een eigen DHCP-server, router, NAT-oplossing of access point wordt niet gebruikt zonder expliciete toestemming.
- Caching wordt alleen ingezet voor toegelaten platformen en na testen van opslag, hitratio, DNS-impact en fallback.
- Deelnemersverkeer wordt niet inhoudelijk geïnspecteerd.
- Er worden geen illegale gamebestanden gedownload of gedistribueerd.
- Alle technische scenario's worden getest in een toegelaten proefopstelling vóór het evenement.

## 8. Budget (concept)

Het volledige evenement wordt financieel gedragen door de **IEEE student branch Brugge**; de posten hieronder zijn alleen de posten waarvoor wij direct eigenaar zijn (Stuvo-inrichting en leaderboard).

| Categorie | Eigenaar | Opmerking |
|---|---|---|
| Materialen (kabels, labels, verbruiksmateriaal) | Kyell / Jules | Via IEEE-budget |
| Technische middelen (switches, cachinghardware) | Kyell | Via IEEE-budget |
| Leaderboard (software en eventuele hardware) | Jules | Via IEEE-budget |
| Communicatie (aankondiging, drukwerk indien nodig) | Jules | Via IEEE-budget |
| Reserve / onvoorziene kosten | Kyell | Via IEEE-budget |

De eindverantwoordelijkheid voor het totaalbudget ligt bij IEEE; de posten worden bij de budgeteigenaar afstemmen (contact: Kyell, vóór Gate 1).

## 9. Risico's (kern)

| Risico | Impact | Mitigatie |
|---|---|---|
| Geen goedkeuring van Stuvo/IT | Event kan niet doorgaan | Tabletop-oefening en goedgekeurde dry-run als alternatief |
| Capaciteit netwerk of stroom onvoldoende | Degradatie of storing | Capaciteitsplan vooraf; monitoring en fallback |
| Locatie niet beschikbaar of onvoldoende | Concept moet worden aangepast | Alternatieve datumoptie; vroege aanvraag |
| Privacy of gegevensverwerking niet conform | Juridisch risico | Minimale gegevensverwerking; privacytekst; bewaartermijn |
| Technisch falen van caching of gameserver | Ervaringsverlies | Fallback-test; scenario-7 en scenario-8 |

Voor de volledige risicoanalyse wordt verwezen naar [risicoanalyse.md](risicoanalyse.md).

## 10. Succescriteria (concept)

- Alle vijf de go/no-go-gates zijn goedgekeurd vóór het evenement.
- Alle acht verplichte technische scenario's zijn getest en geslaagd, of voorzien van een gedocumenteerde beperking.
- De deelnemerscapaciteit en opkomst komen binnen de afgesproken grenzen.
- Mediane latency en packet loss blijven binnen de vooraf bepaalde drempelwaarden.
- Geen vermijdbaar veiligheids- of netwerkincident.
- Opbouw en afbraak binnen het afgesproken tijdsvenster.
- Deelnemersfeedback is verzameld en verwerkt; gegevens zijn verwijderd na de bewaartermijn.

## 11. Gate 1 — Concept akkoord

Deze conceptnota is de basis voor de formele **Gate 1: Concept akkoord**. De **Gate 1-bespreking met Leroy is gepland op vrijdag 16/10**; alle vijf de gates moeten vóór 20/10 gesloten zijn. De volgende punten moeten bevestigd zijn:

- [ ] Doel en doelgroep zijn geformuleerd en goedgekeurd.
- [ ] Datum (22/10/2026) en uren (18:00–24:00) zijn vastgelegd.
- [ ] Capaciteit is ingeschat voor deelnemers, tafels en netwerkpoorten (capaciteit: via IEEE).
- [ ] Budgetposten (Stuvo + leaderboard) zijn afgebakend; totaalbudget via IEEE.
- [ ] Stakeholderregister en RACI-matrix zijn opgesteld.
- [ ] De docent / product owner (Leroy Mathieu) heeft het concept goedgekeurd.

| Veld | Waarde |
|---|---|
| Status conceptnota | Uitvoeringsvoorbereiding |
| Opsteller | Kyell, Jules |
| Datum | 2026-10-16 |
| Go/no-go (Gate 1) | Open — bespreking 16/10 met Leroy |
