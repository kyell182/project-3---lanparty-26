# Projectplan — LAN-party 26

> Datum, locatie en team zijn vastgelegd; capaciteitswaarden en IT-toestemmingen worden nog ingevuld na overleg met betrokken diensten.

## 1. Projectidentiteit

| Veld               | Waarde                            |
| ------------------ | --------------------------------- |
| Project/groep      | Project 3: LAN-party 26           |
| Opdrachtgever      | Leroy Mathieu                     |
| Product owner      | Leroy Mathieu                     |
| Technische coach   | Leroy Mathieu                     |
| Projectcoördinatie | Kyell                             |
| Start/eind         | Semester 1 Academiejaar 2026–2027 |
| Status | Uitvoeringsvoorbereiding — alle vijf gates open, te sluiten vóór 20/10 |

## 2. Samenvatting

Het project ontwerpt en bereidt een veilige, inclusieve en technisch sterke LAN-party voor studenten voor. De groep behandelt het volledige traject: behoefteanalyse, budget, goedkeuringen, locatie en stroom, netwerk en caching, gameservices, inschrijving, communicatie, support, uitvoering en evaluatie.

De LAN-party gaat alleen door na formele goedkeuring van de relevante gates. Als het evenement niet wordt goedgekeurd, wordt dezelfde technische en organisatorische diepgang aangetoond met een tabletopoefening en een goedgekeurde kleinschalige dry-run.

## 3. Probleem en gebruikers

Studenten willen een georganiseerd evenement waarin ze samen kunnen gamen in een stabiele, veilige en inclusieve omgeving. Zonder voorafgaande voorbereiding bestaan risico’s rond netwerkbelasting, stroom, veiligheid, privacy, ondersteuning en communicatie.

### Gebruikers en stakeholders

- deelnemers aan de LAN-party;
- vrijwillige crew en supportmedewerkers;
- Stuvo/studentenvoorzieningen;
- opleidingshoofd en docenten;
- lokaalplanning, gebouwbeheer en preventie;
- IT- en netwerkbeheer;
- eventuele materiaal- of cateringpartners binnen het campusbeleid.

De definitieve doelgroep, capaciteit en gebruikersbehoeften worden vastgelegd in de conceptnota.

## 4. Doelstellingen

1. Een haalbaar en professioneel LAN-partyconcept uitwerken.
2. De nodige goedkeuringen tijdig en schriftelijk verkrijgen.
3. Een beheersbaar netwerkontwerp maken op basis van de door IT goedgekeurde uplink en diensten.
4. Caching, lokale gameservices, monitoring en support testen in een toegelaten proefopstelling.
5. Deelnemers informeren met minimale gegevensverwerking, duidelijke voorwaarden en een gedragscode.
6. Een dry-run, formele go/no-go en — indien toegestaan — het evenement uitvoeren.
7. Resultaten, incidenten, metingen en verbeterpunten overdraagbaar documenteren.

## 5. Succescriteria

| Indicator             | Nulmeting                        | Doelwaarde                                                           | Meetmethode                  |
| --------------------- | -------------------------------- | -------------------------------------------------------------------- | ---------------------------- |
| Goedkeuringen         | Geen formele gates geregistreerd | Alle vereiste gates geregistreerd vóór uitvoering                    | Akkoordregistratie/beslislog |
| Technische scenario’s | Nog niet getest                  | Alle 8 scenario’s geslaagd of voorzien van gedocumenteerde beperking | Testverslagen                |
| Netwerkstabiliteit    | Nog te bepalen                   | Median latency en packet loss binnen vooraf afgesproken grens        | Monitoring en testclients    |
| Cachewerking          | Nog te bepalen                   | Hit, miss, fallback en DNS-impact aantoonbaar                        | Cachebenchmark               |
| Support               | Nog te bepalen                   | Triage, escalatie en gemiddelde oplostijd geregistreerd              | Servicedesk- en incidentlog  |
| Veiligheid            | Nog te bepalen                   | Geen vermijdbaar veiligheids- of netwerkincident                     | Draaiboek en incidentlog     |
| Uitvoering            | Nog te bepalen                   | Opbouw en afbraak binnen afgesproken venster                         | Tijdregistratie              |
| Overdracht            | Geen overdrachtsdossier          | Dossier, runbooks, tests en evaluatie compleet                       | Review vóór oplevering       |

De concrete drempelwaarden worden tijdens de laboproef (week 17, Kyell) vastgelegd en vóór de dry-run bevestigd.

> **Eigenschappen van deze editie.** De LAN-party vindt plaats op **donderdag 22 oktober 2026, 18:00–24:00**, in **Stuvo**. De overkoepelende organisatie is in handen van **IEEE student branch Brugge** (aanspreekpunt: Jonas Rollier); ons project is zelf verantwoordelijk voor de **inrichting en uitvoering in Stuvo** en voor de **leaderboard**. Deze twee vormen de kern van onze scope.

## 6. Scope

### Must

- projectplan, begroting, stakeholderregister, risicoanalyse en beslislog;
- de inrichting en uitvoering van de LAN-party in Stuvo (lokaal, tafels, stroom, opbouw);
- de leaderboard: live scoreboard met resultaten en expliciete privacytoestemming (zie [leaderboard.md](leaderboard.md));
- schriftelijke aanvragen aan Stuvo en betrokken interne diensten;
- capaciteitsplan voor deelnemers, poorten, uplink, IP-adressen, bandbreedte en stroom;
- fysiek lokaal-, tafel-, kabel- en veiligheidsplan;
- netwerkontwerp op basis van de IT-goedgekeurde infrastructuur;
- beheerde switches, gescheiden beheer, configuratieback-up en monitoring;
- caching/downloadstrategie met opslag-, hitratio-, DNS- en fallbacktest;
- toegelaten lokale game- of ondersteunende servers;
- inschrijving, privacytekst, bewaartermijn, deelnemersvoorwaarden en gedragscode;
- communicatieplan voor aankondiging, praktische informatie, wijzigingen en incidenten;
- servicedesk met triage, gekende problemen, reservekabels en escalatiepad;
- draaiboek van opbouw tot afbraak met ploegenschema;
- dry-run met meerdere clients en formele go/no-go;
- evaluatie met metingen, incidenten, feedback en aanbevelingen.

### Should

- interne statuspagina en dashboards;
- compatibiliteitschecklist;
- toernooischema en inclusieve nevenactiviteiten;
- offline pakket met toegelaten drivers, clients of documentatie.

### Could

- captive portal of deelnemersdashboard na IT-goedkeuring;
- live stream van toernooirondes met expliciete privacytoestemming (de leaderboard zelf is een Must);
- duurzaamheidsmeting;
- n8n-integratie via een testsink of goedgekeurd kanaal;
- RetroPie, Arduino-controller of andere entertainmentuitbreidingen.

### Won’t this iteration

- aansluiting op of configuratie van campusinfrastructuur vóór goedkeuring;
- eigen DHCP, router, NAT of draadloze access points zonder toestemming;
- illegale gamebestanden of inhoudelijke inspectie van deelnemersverkeer;
- onbeheerde port forwards of publieke gameservers;
- opslag van betalings- of gezondheidsgegevens in de repository;
- uitbreidingen die Must-resultaten of veiligheid in gevaar brengen.

## 7. Werkwijze en verantwoordelijkheden

De groepsleden (Kyell en Jules) en de taakverdeling zijn definitief. Voor elke kritieke taak wordt een primaire én secundaire eigenaar aangeduid.

| Onderdeel                      | Primaire eigenaar | Back-up        | Status |
| ------------------------------ | ----------------- | -------------- | ------ |
| Projectcoördinatie             | Kyell             | Jules          | Actief |
| Budget (Stuvo/leaderboard, via IEEE) | Kyell       | Jules          | Actief |
| Locatie, tafels en stroom      | Jules             | Kyell          | Actief |
| Netwerk en bekabeling          | Kyell             | Kyell          | Actief |
| Cachingserver                  | Kyell             | Jules          | Actief |
| Leaderboard (core)             | Jules             | Kyell          | Actief |
| Lokale gameservers (RetroPie)  | Kyell             | Kyell          | Actief |
| VR / Pico 4                    | Jules             | Jules          | Actief |
| Monitoring, back-up en herstel | Kyell             | Kyell          | Actief |
| Deelnemersregistratie          | Jules             | Kyell          | Actief |
| Privacy                        | Jules             | Jules          | Actief |
| Communicatie en gedragscode    | Jules             | Jules          | Actief |
| Support en incidenten          | Kyell + Jules + crew | Kyell     | Actief |
| Draaiboek en uitvoering        | Jules             | Kyell          | Actief |
| Evaluatie en overdracht        | Jules + Kyell     | Jules + Kyell  | Actief |

De groep werkt met issues, acceptatiecriteria, testbewijs en documentatie. Betekenisvolle wijzigingen verlopen via review/pull request. Een issue wordt pas gesloten wanneer uitvoering, validatie, documentatie en risico/rollback zijn geregistreerd.

## 8. Stakeholders en communicatie

Het volledige overzicht met contactgegevens en frequentie staat in het [stakeholderregister](stakeholderregister.md). Belangrijkste aansluitpunten voor dit plan:

| Stakeholder                 | Belang/beslissing                            | Aansluiting |
| --------------------------- | -------------------------------------------- | ----------- |
| Leroy (projectgever)         | Opdracht, scope en formele gates             | Gate 1: 16/10 |
| IEEE student branch Brugge  | Hoofdorganisator, inschrijving, bewijsstukken | Via Kyell |
| Stuvo / gebouwbeheer / preventie | Lokaal, stroom, veiligheid, opbouw/cleanup | Via Jules |
| IT / netwerkbeheer          | Uplink, netwerkdiensten, change request      | Via Kyell |
| Deelnemers                  | Inschrijving, voorwaarden, praktische info    | Via Jules |
| Crew                        | Uitvoering en support                        | Via Kyell + Jules |

Externe communicatie en communicatie naar studenten wordt vooraf goedgekeurd. Gebruik voor tests geen echte mailinglijsten of onnodige persoonsgegevens.

## 9. Go/no-go-gates

**Alle vijf de gates moeten vóór 20/10 gesloten zijn.** Gate 1 (concept) wordt besproken in een meeting met Leroy op **vrijdag 16/10**. Elke gesloten gate wordt in het [logboek](logboek.md) geregistreerd met bewijs.

| Gate         | Vereiste voor akkoord                                                   | Bewijs                                          | Deadline |
| ------------ | ----------------------------------------------------------------------- | ----------------------------------------------- | -------- |
| 1 — Concept  | Doel, doelgroep, datum, capaciteit en budgeteigenaar akkoord            | Conceptnota en akkoordregistratie               | 16/10 (meeting met Leroy) |
| 2 — Locatie  | Lokaal, openingsuren, evacuatie, toegankelijkheid, sanitair en toezicht | Lokaal-, stroom- en veiligheidsplan             | 20/10 |
| 3 — Techniek | Uplink, switches, DHCP/routing, stroom en caching zijn toegelaten       | Netwerkplan, change/akkoord en technische tests (laboproef) | 20/10 |
| 4 — Communicatie | Inschrijving, privacy, gedragscode en bericht zijn goedgekeurd       | Communicatiepakket en akkoord                   | 20/10 |
| 5 — Uitvoering | Crew, support, noodnummers, rollback en cleanup zijn klaar           | Dry-run, draaiboek en formele go/no-go          | na Gate 4, vóór opbouw |

Geen akkoord betekent geen aansluiting op het campusnetwerk en geen communicatie alsof het evenement officieel doorgaat.

## 10. Fasesplan

> **Bijgewerkt (16 okt).** De evenementdatum is **donderdag 22 oktober 2026, 18:00–24:00**, in Stuvo. Het oorspronkelijke 12-wekenmodel uit augustus is niet meer toepasbaar: het event valt in week 19, waardoor de voorbereiding en alle gates in de lopende weken intensiever moeten worden opgepakt. Het project wordt daarom ingedeeld in drie fasen met **20/10 als hard keerpunt** (alle gates gesloten).

| Fase | Tijd | Doel | Levert |
|------|------|------|--------|
| 1 — Voorbereiding | 15/10 → 20/10 | Alle gates sluiten, laboproef uitvoeren, leaderboard opzetten | Gates 1–5 gesloten; SLO-drempelwaarden vast; leaderboard-opzet |
| 2 — Eventweek | 21/10 → 22/10 | Opbouw in Stuvo, dry-run, formele go/no-go, event 18:00–24:00 | Geslaagde dry-run; uitgevoerde LAN-party; incidentlog |
| 3 — Nadien | 23/10 → oplevering | Evaluatie, gegevenscleanup, overdracht | Evaluatierapport; overdrachtsdossier; eindlogboek |

De taakdetail per taak met eigenaar en deadline staat in de [todo](todo.md); de RACI per taak in de [raci-matrix](raci-matrix.md).

## 11. Techniek, security en operations

- Werk uitsluitend binnen de toegewezen Smith-pool, VMID-range, netwerken en quota.
- Maak geen permanente VM vóór gebruikers, Must-resultaten, resources, netwerkflows en herstelprocedure duidelijk zijn.
- Vraag vooraf een change request voor VLAN, bridge, routing, firewall, gedeelde netwerkdiensten, caching, eventinfrastructuur, persoonsgegevens of belastende tests.
- Gebruik geen secrets, tokens, private keys of ongeschoonde exports in Git.
- Gebruik persoonlijke beheeraccounts, least privilege, hostfirewall, updates, tijdsynchronisatie en logrotatie.
- Documenteer per service doel, eigenaar, resources, netwerkflows, configuratie, monitoring, back-up, restore, rollback en stopprocedure.
- De laboproef (week 17) toetst de 8 verplichte scenario's op de labomgeving (Proxmox/Smith), inclusief test restore op een aparte omgeving. De dry-run herhaalt dezelfde scenario's op de eventhardware in Stuvo.
- Beperk monitoring en logging tot wat nodig is voor werking en diagnose; inspecteer geen inhoudelijk deelnemersverkeer.

## 12. Oplevering en bewijs

Het overdrachtsdossier bevat minimaal:

- goedgekeurde aanvragen of geanonimiseerde akkoordregistratie;
- RACI, begroting, risicoanalyse en beslislog;
- lokaal-, stroom- en kabelplan;
- netwerkdiagram, IP- en bandbreedteplan;
- cachebenchmark en technische testresultaten;
- switchconfiguratie zonder secrets;
- privacy- en communicatieplan en gedragscode;
- draaiboek, servicedeskprocedure en runbooks;
- incidentlog, evaluatierapport en overdraagbare documentatie.

## 13. Open beslissingen

- deelnemerscapaciteit: wordt door IEEE bepaald en hierin opgeschreven;
- IT-goedgekeurde uplink en toegelaten netwerkdiensten;
- toegelaten cachingplatformen;
- crew en dry-run: de eventcrew wordt afgestemd met IEEE en de dry-run ingepland na Gate 4 (eigenaar: Kyell);
- samenwerking IEEE: de afstemming van gates en de splitsing van bewijsstukken wordt bevestigd (contact: Jonas Rollier).

## 14. Goedkeuring

| Rol                          | Beslissing        | Datum          | Opmerking                                        |
| ---------------------------- | ----------------- | -------------- | ------------------------------------------------ |
| Opdrachtgever/docent (Leroy) | Open              | Nog te bepalen | Gate 1-bespreking: 16/10; alle gates vóór 20/10  |
| IT/netwerkbeheer             | Open              | Nog te bepalen | Nodig voor netwerk- en cachingchanges            |
| Stuvo/gebouwbeheer/preventie | Open              | Nog te bepalen | Nodig voor evenement en locatie (contact via Jules) |
