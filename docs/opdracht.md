# Project 3 — LAN-party van A tot Z

## Opdracht

Ontwerp en organiseer een veilige, inclusieve en technisch sterke LAN-party voor studenten. De groep is verantwoordelijk voor het volledige traject: behoefte en budget, toestemming bij Stuvo en interne diensten, lokaal en elektriciteit, inschrijving en communicatie, netwerk en caching, gameservices, support, veiligheid, uitvoering en evaluatie.

Een evenement mag alleen doorgaan na de formele go/no-go. Zonder toestemming levert de groep dezelfde technische en organisatorische diepgang via een tabletopoefening en een kleinschalige goedgekeurde dry-run.

## Stakeholders

- Stuvo en/of studentenvoorzieningen;
- opleidingshoofd en docent;
- lokaalplanning, gebouwbeheer en preventie;
- IT- en netwerkbeheer;
- deelnemers en vrijwillige crew;
- eventuele catering- of materiaalpartners.

Maak een RACI-matrix: wie beslist, wie voert uit, wie wordt geraadpleegd en wie wordt geïnformeerd?

## Go/no-go-gates

| Gate | Minimaal akkoord |
|---|---|
| Concept | doel, doelgroep, datumopties, capaciteit en budgeteigenaar |
| Locatie | lokaal, openingsuren, evacuatie, toegankelijkheid, sanitair en toezicht |
| Techniek | uplink, eigen switches/AP's, DHCP/routing, stroomplan en toegelaten caching |
| Communicatie | inschrijfformulier, privacytekst, gedragscode en goedgekeurd bericht |
| Uitvoering | crew, support, noodnummers, rollback en cleanup |

Geen akkoord betekent geen aansluiting op campusnetwerk en geen communicatie als officieel evenement.

## Must

- Projectplan, begroting, stakeholderregister, risicoanalyse en beslislog.
- Schriftelijke aanvraag aan Stuvo en betrokken interne diensten met voldoende doorlooptijd.
- Capaciteitsplan voor deelnemers, bekabelde poorten, uplink, IP-adressen, bandbreedte en stroom.
- Fysiek plan met tafels, kabelroutes, labelconventie, nooduitgangen en helpdesk.
- Netwerkontwerp dat uitgaat van de door IT goedgekeurde uplink en diensten; nooit een eigen DHCP-server of router zonder expliciet akkoord.
- Beheerde switches, gescheiden beheer, veilige configuratieback-up en monitoring.
- Caching/downloadstrategie, bijvoorbeeld LANCache, alleen voor toegelaten platformen en na test van opslag, hit ratio, DNS-impact en fallback.
- Lokale game- of ondersteunende servers waar licentie en game dit toelaten.
- Inschrijving met minimale gegevens, bewaartermijn, deelnemersvoorwaarden en gedragscode.
- Communicatieplan voor aankondiging, praktische info, wijzigingen en incidenten.
- Servicedesk met triage, gekende problemen, reservekabels en escalatiepad.
- Gedetailleerd draaiboek van opbouw tot afbraak, met ploegenschema.
- Dry-run met meerdere clients en een formele go/no-gocheck.
- Evaluatie achteraf met metingen, incidenten, feedback en aanbevelingen.

## Should

- Interne statuspagina en dashboards voor uplink, switchpoorten, DHCP-capaciteit, latency, packet loss, cache en gameservers.
- Voorafgaande compatibiliteitschecklist voor deelnemers.
- Toernooischema met duidelijke regels en verantwoordelijke.
- Inclusieve nevenactiviteiten voor deelnemers die niet dezelfde games spelen.
- Offline pakket met drivers, clients of documentatie voor zover licenties dit toelaten.

## Could

- Captive portal of deelnemersdashboard, alleen met akkoord van IT.
- Live scoreboard of stream met expliciete privacytoestemming.
- Duurzaamheidsmeting van energie, herbruikbare materialen en transport.
- Integratie met n8n voor bevestigingen en crewalerts via testsink of goedgekeurd kanaal.

## Niet in scope

- aansluiten of configureren vóór goedkeuring;
- eigen draadloze access points, DHCP of NAT op het campusnetwerk zonder toestemming;
- downloaden of distribueren van illegale gamebestanden;
- inspecteren van inhoudelijk deelnemersverkeer;
- onbeheerde port forwards of publieke gameservers;
- opslag van betalings- of gezondheidsgegevens in de projectrepo;
- alcohol- of cateringafspraken buiten het beleid van campus en Stuvo.

## Verplichte technische scenario's

Test in een toegelaten proefopstelling:

1. nieuwe deelnemer aansluiten en correct adres/connectiviteit verkrijgen;
2. onbekende of verkeerd aangesloten DHCP-/routerfunctie detecteren zonder het campusnetwerk te raken;
3. cache hit en cache miss met werkende fallback meten;
4. gameserver bereiken en basisbelasting meten;
5. kabel-, switchpoort- of gameserverstoring diagnosticeren;
6. cache uitschakelen zonder algemene internettoegang te breken;
7. monitoringalarm ontvangen en volgens runbook behandelen;
8. configuratie van een switch of service herstellen.

## Succesmetingen

- opbouw en afbraak binnen afgesproken venster;
- geen veiligheids- of netwerkincident met vermijdbare impact;
- afgesproken deelnemerscapaciteit en opkomst;
- mediane latency en packet loss binnen vooraf bepaalde grens;
- cache-effect aantoonbaar zonder afhankelijkheid te creëren;
- gemiddelde oplostijd van supportvragen;
- deelnemersfeedback en correcte verwijdering van gegevens na retentie.

## Mijlpalen

- Week 2: conceptnota, datumopties, stakeholders en budgetraming.
- Week 3: aanvragen aan Stuvo, lokaalbeheer en IT.
- Week 5: voorlopig netwerk-, stroom-, veiligheids- en communicatieplan.
- Week 7: technische laboproef met caching en monitoring.
- Week 9: inschrijving/communicatie alleen na akkoord; definitief draaiboek.
- Week 10 of 11: generale repetitie en go/no-go.
- Evenement: uitvoering, incidentlog en cleanup.
- Week 12: evaluatie en overdraagbaar draaiboek.

## Verplichte bewijsstukken

Goedgekeurde aanvragen of geanonimiseerde akkoordregistratie, RACI, begroting, lokaal- en kabelplan, netwerkdiagram, IP- en bandbreedteplan, cachebenchmark, switchconfiguratie zonder secrets, privacy- en communicatieplan, gedragscode, draaiboek, servicedeskprocedure, incidentlog en evaluatierapport.
