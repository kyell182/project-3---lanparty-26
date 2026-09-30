# Projectplan — LAN-party 26

> Namen, definitieve datum, locatie en capaciteitswaarden worden ingevuld na overleg met betrokken diensten.

## 1. Projectidentiteit

| Veld | Waarde |
|---|---|
| Project/groep | Project 3: LAN-party 26 |
| Opdrachtgever | Leroy Mathieu |
| Product owner | Leroy Mathieu |
| Technische coach | Leroy Mathieu |
| Projectcoördinatie | Kyell |
| Start/eind | Academiejaar 2026–2027; definitieve data te bevestigen |
| Status | Initiatie en conceptvorming |

## 2. Samenvatting

Het project ontwerpt en bereidt een veilige, inclusieve en technisch sterke LAN-party voor studenten voor. De groep behandelt het volledige traject: behoefteanalyse, budget, goedkeuringen, locatie en stroom, netwerk en caching, gameservices, inschrijving, communicatie, support, uitvoering en evaluatie.

De LAN-party gaat alleen door na formele goedkeuring van de relevante gates. Als het evenement niet wordt goedgekeurd, wordt dezelfde technische en organisatorische diepgang aangetoond met een tabletopoefening en een goedgekeurde kleinschalige dry-run.

## 3. Probleem en gebruikers

Studenten hebben nood aan een georganiseerd evenement waarin ze samen kunnen gamen in een stabiele, veilige en inclusieve omgeving. Zonder voorafgaande voorbereiding bestaan risico’s rond netwerkbelasting, stroom, veiligheid, privacy, ondersteuning en communicatie.

### Gebruikers en betrokkenen

- deelnemers aan de LAN-party;
- vrijwillige crew en supportmedewerkers;
- Stuvo/studentenvoorzieningen;
- opleidingshoofd en docent;
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

| Indicator | Nulmeting | Doelwaarde | Meetmethode |
|---|---|---|---|
| Goedkeuringen | Geen formele gates geregistreerd | Alle vereiste gates geregistreerd vóór uitvoering | Akkoordregistratie/beslislog |
| Technische scenario’s | Nog niet getest | Alle 8 scenario’s geslaagd of voorzien van gedocumenteerde beperking | Testverslagen |
| Netwerkstabiliteit | Nog te bepalen | Median latency en packet loss binnen vooraf afgesproken grens | Monitoring en testclients |
| Cachewerking | Nog te bepalen | Hit, miss, fallback en DNS-impact aantoonbaar | Cachebenchmark |
| Support | Nog te bepalen | Triage, escalatie en gemiddelde oplostijd geregistreerd | Servicedesk- en incidentlog |
| Veiligheid | Nog te bepalen | Geen vermijdbaar veiligheids- of netwerkincident | Draaiboek en incidentlog |
| Uitvoering | Nog te bepalen | Opbouw en afbraak binnen afgesproken venster | Tijdregistratie |
| Overdracht | Geen overdrachtsdossier | Dossier, runbooks, tests en evaluatie compleet | Review vóór oplevering |

De concrete drempelwaarden worden vastgelegd vóór de laboproef en dry-run.

## 6. Scope

### Must

- projectplan, begroting, stakeholderregister, risicoanalyse en beslislog;
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
- live scoreboard of stream met expliciete privacytoestemming;
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

De groepsleden en de definitieve verdeling worden later gezamenlijk besproken. Tot dan blijven eigenaarsvelden open. Voor elke kritieke taak wordt daarna een primaire én secundaire eigenaar aangeduid.

| Onderdeel | Primaire eigenaar | Back-up | Status |
|---|---|---|---|
| Projectcoördinatie | Kyell | Nog te bepalen | Open |
| Budget en aanvragen | Nog te bepalen | Nog te bepalen | Open |
| Locatie, tafels en stroom | Jules | Nog te bepalen | Open |
| Netwerk en bekabeling | Nog te bepalen | Nog te bepalen | Open |
| Cachingserver | Kyell | Nog te bepalen | Open |
| Lokale gameservers | Nog te bepalen | Nog te bepalen | Open |
| Monitoring, back-up en herstel | Nog te bepalen | Nog te bepalen | Open |
| Deelnemersregistratie | Jules | Nog te bepalen | Open |
| Privacy | Nog te bepalen | Nog te bepalen | Open |
| Communicatie en gedragscode | Nog te bepalen | Nog te bepalen | Open |
| Support en incidenten | Nog te bepalen | Nog te bepalen | Open |
| Draaiboek en uitvoering | Nog te bepalen | Nog te bepalen | Open |
| Evaluatie en overdracht | Nog te bepalen | Nog te bepalen | Open |

De groep werkt met issues, acceptatiecriteria, testbewijs en documentatie. Betekenisvolle wijzigingen verlopen via review/pull request. Een issue wordt pas gesloten wanneer uitvoering, validatie, documentatie en risico/rollback zijn geregistreerd.

## 8. Stakeholders en communicatie

| Stakeholder | Belang/beslissing | Communicatie | Eigenaar |
|---|---|---|---|
| Docent/opleidingshoofd | Opdracht, scope en formele gates | Wekelijks en bij escalatie | Leroy Mathieu |
| Stuvo | Evenement en studentenvoorzieningen | Concept en aanvraag; opvolging volgens afspraak | Nog te bepalen |
| Lokaalplanning/gebouwbeheer | Lokaal, openingsuren, opbouw en cleanup | Voor aanvraag en vóór uitvoering | Nog te bepalen |
| Preventie | Evacuatie, veiligheid en toegankelijkheid | Tijdens locatieontwerp en go/no-go | Nog te bepalen |
| IT/netwerkbeheer | Uplink, netwerkdiensten, changes en caching | Ontwerp, change request en technische gate | Nog te bepalen |
| Deelnemers | Inschrijving, voorwaarden en praktische info | Alleen na communicatiegoedkeuring | Jules (registratie) |
| Crew | Uitvoering en support | Briefing, draaiboek en eventdag | Nog te bepalen |

Externe communicatie en communicatie naar studenten wordt vooraf goedgekeurd. Gebruik voor tests geen echte mailinglijsten of onnodige persoonsgegevens.

## 9. Go/no-go-gates

| Gate | Vereiste voor akkoord | Bewijs |
|---|---|---|
| Concept | Doel, doelgroep, datumopties, capaciteit en budgeteigenaar | Conceptnota en akkoordregistratie |
| Locatie | Lokaal, openingsuren, evacuatie, toegankelijkheid, sanitair en toezicht | Lokaal-, stroom- en veiligheidsplan |
| Techniek | Uplink, switches, DHCP/routing, stroom en caching zijn toegelaten | Netwerkplan, change/akkoord en technische tests |
| Communicatie | Inschrijving, privacy, gedragscode en bericht zijn goedgekeurd | Communicatiepakket en akkoord |
| Uitvoering | Crew, support, noodnummers, rollback en cleanup zijn klaar | Dry-run, draaiboek en formele go/no-go |

Geen akkoord betekent geen aansluiting op het campusnetwerk en geen communicatie alsof het evenement officieel doorgaat.

## 10. Planning en mijlpalen

| Week | Resultaat |
|---:|---|
| 1 | Intake, repository, logboek, brainstorm en eerste stakeholdercontact |
| 2 | Conceptnota, datumopties, stakeholders, RACI en budgetraming |
| 3 | Aanvragen voor Stuvo, lokaalbeheer, preventie en IT |
| 4 | Architectuur, dataflow, dreigingen, resourcebudget en proof-of-concept |
| 5 | Voorlopig netwerk-, stroom-, veiligheids- en communicatieplan; technische gate |
| 6 | Kernflows, gameserver, servicedesk en eerste runbooks |
| 7 | Technische laboproef, caching, monitoring, security en herstel |
| 8 | Operations, logging, back-up, restore en incidentrunbooks |
| 9 | Communicatie na akkoord, inschrijving, automatisering en definitief draaiboek |
| 10 | Dry-run/generale repetitie en gebruikerstest |
| 11 | Stabilisatie, capaciteit, rollback en formele uitvoerings-go/no-go |
| Event | Uitvoering, monitoring, support, incidentlog en cleanup |
| 12 | Evaluatie, gegevenscleanup en overdracht |

Elke week bevat minstens bijgewerkte issues, één beslissing of resultaat, test-/validatiebewijs, risico’s/blokkades en een korte reflectie op resources en volgende stappen.

## 11. Techniek, security en operations

- Werk uitsluitend binnen de toegewezen Smith-pool, VMID-range, netwerken en quota.
- Maak geen permanente VM vóór gebruikers, Must-resultaten, resources, netwerkflows en herstelprocedure duidelijk zijn.
- Vraag vooraf een change request voor VLAN, bridge, routing, firewall, gedeelde netwerkdiensten, caching, eventinfrastructuur, persoonsgegevens of belastende tests.
- Gebruik geen secrets, tokens, private keys of ongeschoonde exports in Git.
- Gebruik persoonlijke beheeraccounts, least privilege, hostfirewall, updates, tijdsynchronisatie en logrotatie.
- Documenteer per service doel, eigenaar, resources, netwerkflows, configuratie, monitoring, back-up, restore, rollback en stopprocedure.
- Test restore op een aparte omgeving; een Proxmox-snapshot alleen is geen volledige herstelstrategie.
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

- definitieve groepsleden en taakverdeling;
- opdrachtgever, product owner en technische coach;
- doelgroep, datum, locatie en deelnemerscapaciteit;
- budget en resourcequota;
- IT-goedgekeurde uplink en toegelaten netwerkdiensten;
- toegelaten cachingplatformen en gameservers;
- keuze welke Should/Could-onderdelen haalbaar zijn.

## 14. Goedkeuring

| Rol | Beslissing | Datum | Opmerking |
|---|---|---|---|
| Opdrachtgever/docent | Nog te beoordelen | Nog te bepalen | Projectplan bespreken vóór technische uitvoering |
| IT/netwerkbeheer | Nog te beoordelen | Nog te bepalen | Nodig voor netwerk- en cachingchanges |
| Stuvo/gebouwbeheer/preventie | Nog te beoordelen | Nog te bepalen | Nodig voor evenement en locatie |
