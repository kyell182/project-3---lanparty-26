# Conceptnota — LAN-party 26

> Conceptnota voor het evenement "LAN-party 26". Deze nota vormt de basis voor **Gate 1: Concept akkoord**. Definitieve waarden (datum, locatie, capaciteit, budget) worden ingevuld na overleg met de betrokken diensten en de studentenbevraging.

## 1. Doel

Een veilige, inclusieve en technisch sterke LAN-party organiseren voor studenten, waarin zij samen kunnen gamen in een stabiele en beheersbare omgeving. Het project toont het volledige traject van concept tot uitvoering, inclusief goedkeuringen, netwerkontwerp, caching, support, veiligheid en evaluatie.

## 2. Probleem en behoefte

Studenten willen een georganiseerd evenement waarin ze samen kunnen gamen. Zonder voorafgaande voorbereiding bestaan risico's rond netwerkbelasting, stroom, veiligheid, privacy, ondersteuning en communicatie. Een gestructureerde aanpak zorgt voor een stabiel netwerk, een veilige omgeving en een goede deelnemersexperience.

## 3. Doelgroep

- Studenten van de campus als hoofddoelgroep.
- Deelnemers variëren van casual gamers tot competitieve spelers.
- Deelnemers die niet meespelen, krijgen inclusieve nevenactiviteiten (boardgames, RetroPie, Arduino-entertainment).

De definitieve doelgroepomvang wordt bepaald op basis van de studentenbevraging en de capaciteit van de locatie.

## 4. Concept en kenmerken

| Onderdeel | Concept | Status |
|---|---|---|
| Speelopstelling | Bekabelde LAN-opstelling met beheerde switches; eigen DHCP/AP alleen na IT-goedkeuring | Concept |
| Caching | LANCache voor toegelaten platformen (o.a. Steam); getest op opslag, hitratio, DNS-impact en fallback | Concept |
| Lokale gameservers | Pico 4 LAN-concept met Quake3Quest en mogelijke casting; overige lokale servers waar licenties dit toelaten | Concept |
| RetroPie | RetroPie op minipc voor klassieke games; handleiding en setup door Kyell | Concept |
| Arduino-controller | Ontdekking van mogelijkheden voor een Arduino-gebaseerde controller of entertainmentelement | Concept |
| Boardgames / Spellenlab | Inclusieve nevenactiviteit via Spellenlab voor niet-meespelende deelnemers | Concept |
| Leaderboard / stream | Live scoreboard of stream met expliciete privacytoestemming (Could) | Concept |
| Inschrijving | Minimale gegevensverwerking met privacytekst, bewaartermijn en gedragscode | Concept |
| Support | Servicedesk met triage, gekende problemen, reservekabels en escalatiepad | Concept |

## 5. Datumopties en timing

| Optie | Datum | Opmerking |
|---|---|---|
| 1 | Eind november 2026 | Eerste voorkeur; te verifiëren met gebouwbeheer en Stuvo |

De definitieve datum wordt vastgelegd na akkoord van Stuvo, gebouwbeheer en IT. Het evenement is gepland als eenmalig dag- of weekendevent.

## 6. Locatie en capaciteit (concept)

| Aspect | Concept | Status |
|---|---|---|
| Locatie | Interne campusruimte, te bevestigen | Open |
| Capaciteit deelnemers | Te bepalen via bevraging en lokaal | Open |
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

## 8. Budgetraming (concept)

| Categorie | Raambedrag | Eigenaar | Opmerking |
|---|---|---|---|
| Materialen (kabels, labels, verbruiksmateriaal) | Te bepalen | Kyell / Jules | |
| Eventuele catering (binnen campusbeleid) | Te bepalen | Nog te bepalen | |
| Technische middelen (switches, cachinghardware) | Te bepalen | Kyell | |
| Communicatie (aankondiging, drukwerk indien nodig) | Te bepalen | Jules | |
| Reserve / onvoorziene kosten | Te bepalen | Nog te bepalen | |
| **Totaal (concept)** | **Te bepalen** | **Nog te bepalen** | |

Het budget wordt uitgewerkt na het concept-akkoord en bevestigd bij de budgeteigenaar.

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

Deze conceptnota is de basis voor de formele **Gate 1: Concept akkoord**. De volgende punten moeten bevestigd zijn:

- [ ] Doel en doelgroep zijn geformuleerd en goedgekeurd.
- [ ] Datumopties zijn beoordeeld en een voorkeursoptie vastgelegd.
- [ ] Capaciteit is ingeschat voor deelnemers, tafels en netwerkpoorten.
- [ ] Begroting en budgeteigenaar zijn benoemd.
- [ ] Stakeholderregister en RACI-matrix zijn opgesteld.
- [ ] De docent / product owner (Leroy Mathieu) heeft het concept goedgekeurd.

| Veld | Waarde |
|---|---|
| Status conceptnota | Concept |
| Opsteller | Kyell, Jules |
| Datum | 2026-10-02 |
| Go/no-go (Gate 1) | Nog te beoordelen |
