# LAN-party 2026

Project 3 voor Network Experience: het ontwerpen, voorbereiden en organiseren van een veilige, inclusieve en technisch sterke LAN-party voor studenten.

## Over dit project

Dit project behandelt het volledige traject van een LAN-party, van behoefteanalyse en budgettering tot netwerkbeheer, technische ondersteuning, uitvoering en evaluatie.

De LAN-party gaat alleen door na een formele go/no-go en de nodige goedkeuringen van de betrokken diensten. Als een evenement niet wordt goedgekeurd, wordt dezelfde technische en organisatorische aanpak uitgewerkt in een tabletopoefening en een goedgekeurde dry-run.

## Doelstellingen

- Een haalbaar en professioneel evenement uitwerken.
- Een veilig, stabiel en beheersbaar netwerk ontwerpen.
- Deelnemers en crew duidelijk informeren en ondersteunen.
- Alle technische scenario's vooraf testen in een toegelaten proefopstelling.
- Beslissingen, risico's, incidenten en resultaten aantoonbaar documenteren.

## Projectonderdelen

Het project omvat onder andere:

- projectplanning, begroting en stakeholderbeheer;
- aanvragen en goedkeuringen bij Stuvo, lokaalbeheer en IT;
- capaciteits-, stroom-, lokaal- en kabelplan;
- netwerkontwerp met beheerde switches, monitoring en configuratieback-ups;
- caching en lokale gameservices waar dit technisch en juridisch is toegelaten;
- inschrijving, privacy, gedragscode en communicatie;
- servicedesk, incidentbeheer en escalatie;
- draaiboek voor opbouw, evenement en afbraak;
- evaluatie op basis van metingen, incidenten en deelnemersfeedback.

## Go/no-go

Het evenement kan pas doorgaan wanneer de volgende gates zijn goedgekeurd:

| Gate | Vereiste goedkeuring |
| --- | --- |
| Concept | Doel, doelgroep, datumopties, capaciteit en budgeteigenaar |
| Locatie | Lokaal, openingsuren, evacuatie, toegankelijkheid, sanitair en toezicht |
| Techniek | Uplink, switches, DHCP/routing, stroomplan en toegelaten caching |
| Communicatie | Inschrijving, privacytekst, gedragscode en goedgekeurde communicatie |
| Uitvoering | Crew, support, noodnummers, rollback en cleanup |

Zonder formele goedkeuring wordt er geen verbinding gemaakt met het campusnetwerk en wordt er niet gecommuniceerd alsof het om een officieel evenement gaat.

## Technische uitgangspunten

- De door IT goedgekeurde uplink en diensten vormen de basis van het netwerkontwerp.
- Een eigen DHCP-server, router, NAT-oplossing of access point wordt niet gebruikt zonder expliciete toestemming.
- Caching, bijvoorbeeld met LANCache, wordt alleen ingezet voor toegelaten platformen en na testen van opslag, hitratio, DNS-impact en fallback.
- Deelnemersverkeer wordt niet inhoudelijk geïnspecteerd.
- Er worden geen illegale gamebestanden gedownload of gedistribueerd.
- Configuratiebestanden bevatten geen wachtwoorden, tokens of andere geheimen.

## Verplichte technische scenario's

De volgende scenario's worden getest in een toegelaten proefopstelling:

1. Een nieuwe deelnemer aansluiten en correcte connectiviteit verkrijgen.
2. Een foutief aangesloten DHCP- of routercomponent detecteren zonder het campusnetwerk te beïnvloeden.
3. Een cache hit en cache miss testen met een werkende fallback.
4. Een gameserver bereiken en de basisbelasting meten.
5. Een kabel-, switchpoort- of gameserverstoring diagnosticeren.
6. De cache uitschakelen zonder algemene internettoegang te verbreken.
7. Een monitoringalarm ontvangen en volgens het runbook behandelen.
8. De configuratie van een switch of service herstellen.

## Team en verantwoordelijkheden

Vul de namen aan en wijs voor elke taak een verantwoordelijke en eventueel een back-up aan. De verantwoordelijke bewaakt de voortgang en rapporteert over de taak in het logboek.

| Onderdeel | Verantwoordelijke | Back-up | Status | Opmerking |
| --- | --- | --- | --- | --- |
| Projectcoordinatie | Kyell |  | Nog te starten |  |
| GitHub en documentatie | Kyell |  | Bezig | Repository onderhouden |
| Budget en inkomsten |  |  | Nog te starten |  |
| Communicatie en informatie |  |  | Nog te starten |  |
| Deelnemersregistratie | Jules |  | Nog te starten |  |
| Locatie, tafels en stroom | Jules |  | Nog te starten |  |
| Netwerk en bekabeling |  |  | Nog te starten |  |
| Cachingserver | Kyell |  | Nog te starten | Steam-caching onderzoeken |
| Lokale gameservers |  |  | Nog te starten |  |
| RetroPie en minicomputer | Kyell |  | Nog te starten |  |
| Arduino-controller | Kyell |  | Nog te starten | Mogelijkheden onderzoeken |
| Games en toernooien | Jules |  | Nog te starten |  |
| Boardgames en nevenactiviteiten | Jules |  | Nog te starten | Spellenlab bekijken |
| Gedragscode en disclaimer |  |  | Nog te starten |  |
| Support en incidenten |  |  | Nog te starten |  |
| Leaderboard en stream |  |  | Nog te starten | Privacytoestemming voorzien |
| Evaluatie |  |  | Nog te starten |  |

Gebruik voor `Status` bijvoorbeeld `Nog te starten`, `Bezig`, `Geblokkeerd` of `Afgerond`.

## Logboek

Het afzonderlijke [logboek](logging/logboek.md) bevat belangrijke beslissingen, acties, testen, problemen en incidenten. Voeg waar mogelijk een link naar bewijs toe, zoals een document, screenshot, configuratie zonder geheimen of testresultaat.

## Planning

| Moment | Mijlpaal |
| --- | --- |
| Week 2 | Conceptnota, datumopties, stakeholders en budgetraming |
| Week 3 | Aanvragen aan Stuvo, lokaalbeheer en IT |
| Week 5 | Voorlopig netwerk-, stroom-, veiligheids- en communicatieplan |
| Week 7 | Technische laboproef met caching en monitoring |
| Week 9 | Inschrijving, communicatie na akkoord en definitief draaiboek |
| Week 10 of 11 | Generale repetitie en formele go/no-go |
| Evenement | Uitvoering, incidentregistratie en cleanup |
| Week 12 | Evaluatie en overdraagbaar draaiboek |

## Succesmetingen

Het project wordt geëvalueerd aan de hand van:

- een opbouw en afbraak binnen het afgesproken tijdsvenster;
- het uitblijven van vermijdbare veiligheids- en netwerkincidenten;
- de afgesproken deelnemerscapaciteit en opkomst;
- vooraf bepaalde grenzen voor mediane latency en packet loss;
- aantoonbare cachewinst zonder afhankelijkheid van de cache;
- de gemiddelde oplostijd van supportvragen;
- deelnemersfeedback en correcte verwijdering van gegevens na de bewaartermijn.

## Repositorystructuur

```text
.
├── 03-lan-party.md    				# Volledige opdrachtomschrijving en vereisten
├── README.md         				# Projectoverzicht en werkwijze
├── organisatie en projectsturing
|	├── todo.md						# Checklists week-per-week
|	├── risicoanalyse.md  			# Risicobepaling en opvolging van go/no-go-beslissingen
|	├── projectplan.md    			# Namen, datums, locaties, ...
|	├── stakeholderregister.md		# Alle betrokkenen met belang, invloed en communicatie
|	├── raci-matrix.md    			# Beslissen, uitvoeren, raadplegen en informeren per taak
|	└── conceptnota.md    			# Conceptnota als basis voor Gate 1: Concept akkoord
├── logging
|	└── logboek.md		  			# Beslissingen, acties, testen en incidenten
└── brainstorm/
	└── concepten.md      			# Eerste ideeën en conceptuitwerking
```

Projectdocumenten en bewijsstukken worden toegevoegd zodra ze zijn uitgewerkt en goedgekeurd. Denk hierbij aan de RACI-matrix, begroting, risicoanalyse, netwerkdiagram, IP- en bandbreedteplan, cachebenchmark, privacy- en communicatieplan, gedragscode, draaiboek, servicedeskprocedure, incidentlog en evaluatierapport.

## Scope

### Binnen scope

- Organisatie en technische voorbereiding van de LAN-party.
- Netwerk-, stroom-, lokaal- en veiligheidsplanning.
- Testen, monitoring, support en incidentbeheer.
- Communicatie, inschrijving en evaluatie.

### Buiten scope

- Aansluiten of configureren vóór goedkeuring.
- Niet-goedgekeurde draadloze access points, DHCP, NAT of publieke gameservers.
- Opslag van betalings- of gezondheidsgegevens in deze repository.
- Alcohol- of cateringafspraken buiten het beleid van de campus en Stuvo.

## Referentie

De volledige opdrachtomschrijving staat in [03-lan-party.md](03-lan-party.md).
