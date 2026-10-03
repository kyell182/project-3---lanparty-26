# Risicoanalyse — LAN-party 26

> Werkdocument voor risico-identificatie, opvolging en go/no-go-beslissingen. Eigenaars worden ingevuld nadat de groepsverdeling is besproken.

## 1. Doel en methode

Deze risicoanalyse ondersteunt veilige beslissingen tijdens ontwerp, laboproef, dry-run en uitvoering. Risico’s worden opnieuw bekeken bij elke mijlpaal, wijziging, incident en go/no-go-gate.

### Schaal

- **Kans:** 1 = zeldzaam, 2 = onwaarschijnlijk, 3 = mogelijk, 4 = waarschijnlijk, 5 = bijna zeker.
- **Impact:** 1 = verwaarloosbaar, 2 = beperkt, 3 = merkbaar, 4 = ernstig, 5 = kritiek voor veiligheid, privacy, netwerk of doorgang.
- **Score:** kans × impact.
  - 1–4: laag — opvolgen.
  - 5–9: middel — maatregel en eigenaar vereist.
  - 10–16: hoog — actief behandelen en vóór de volgende gate opvolgen.
  - 17–25: kritiek — uitvoering blokkeren tot het risico aanvaardbaar is.

Een risico is niet “opgelost” omdat een maatregel gepland is. Het restrisico wordt pas verlaagd na test, akkoord of aantoonbaar bewijs.

## 2. Risicoregister

| ID | Risico en oorzaak | Gevolg | K | I | Score | Preventie/mitigatie | Trigger en reactie | Eigenaar | Status/restrisico |
|---|---|---|---:|---:|---:|---|---|---|---|
| R01 | Goedkeuringen van Stuvo, gebouwbeheer of IT komen te laat of ontbreken. | Evenement kan niet officieel doorgaan; planning schuift op. | 3 | 5 | 15 | Aanvragen in week 3 indienen, doorlooptijd opvolgen en alternatieve tabletop/dry-run voorbereiden. | Geen akkoord vóór gate: geen campusaansluiting of officiële communicatie; escaleren naar docent. | Nog te bepalen | Open / hoog tot akkoord |
| R02 | Een eigen DHCP-, router-, NAT- of AP-functie raakt het campusnetwerk. | Verkeerde adressen, netwerkuitval of impact op andere gebruikers. | 2 | 5 | 10 | Alleen IT-goedgekeurde diensten gebruiken; rogue-DHCP-scenario in geïsoleerde laboproef testen; change request verplicht. | Onverwachte DHCP-offers of routing: component onmiddellijk isoleren, IT verwittigen en incident registreren. | Netwerkverantwoordelijke | Open / hoog |
| R03 | Uplink, IP-adressen, poorten of bandbreedte zijn onvoldoende voor de deelnemerscapaciteit. | Hoge latency, packet loss, onbruikbare gameservers of downloads. | 3 | 4 | 12 | Capaciteitsplan, test met meerdere clients, vooraf bepaalde SLO’s en limiet op inschrijvingen. | Drempel overschreden: deelnemerscapaciteit beperken, bulkverkeer verminderen en escaleren naar IT. | Netwerkverantwoordelijke | Open / middel |
| R04 | Stroomgroepen worden overbelast of kabels vormen een veiligheidsrisico. | Stroomuitval, schade, brandgevaar of evacuatieprobleem. | 3 | 5 | 15 | Stroomplan laten controleren door gebouwbeheer/preventie; belasting meten; kabelroutes en nooduitgangen vrijhouden. | Warmte, uitval, losse kabel of geblokkeerde uitgang: activiteit stoppen en gebouwprocedure volgen. | Locatie/stroom-eigenaar | Open / hoog |
| R05 | Onbedoelde switchloop of verkeerd aangesloten apparatuur veroorzaakt een broadcast storm. | Netwerkuitval en impact op deelnemers of campus. | 3 | 4 | 12 | Managed switches, RSTP/BPDU-bescherming waar IT dit toestaat, duidelijke labels en deelnemersinstructies. | Poortflapping of stormalarm: poort isoleren, topologie controleren en incidentlog bijwerken. | Netwerkverantwoordelijke | Open / middel |
| R06 | LANCache werkt niet, veroorzaakt DNS-problemen of heeft geen bruikbare fallback. | Downloads falen of algemene internettoegang wordt verstoord. | 3 | 4 | 12 | Alleen toegelaten platformen; hit/miss, DNS-impact, opslag, uitschakeling en fallback vooraf testen. | Cachefout of DNS-impact: cache uitschakelen volgens runbook en directe fallback valideren. | Kyell | Open / middel |
| R07 | Lokale gameserver valt uit of kan de basisbelasting niet dragen. | Toernooi of geplande gameflow kan niet doorgaan. | 3 | 3 | 9 | Compatibiliteits- en belastingtest, reserveconfiguratie, rollback en alternatieve game/activiteit. | Server onbereikbaar of overbelast: service herstellen of gecontroleerd overschakelen naar fallback. | Gameserver-eigenaar | Open / middel |
| R08 | Monitoring detecteert problemen niet of alerts worden niet opgevolgd. | Storingen duren langer; succesmetingen ontbreken. | 3 | 4 | 12 | Alertmatrix met drempel, eigenaar en actie; alerts vóór dry-run testen; dashboard intern beschikbaar. | Alert zonder reactie: eigenaar/escalatie bellen en handmatige meting uitvoeren. | Monitoring-eigenaar | Open / middel |
| R09 | Configuratie- of unieke eventdata kan niet worden hersteld. | Lang herstel, dataverlies of niet-overdraagbare dienst. | 2 | 5 | 10 | Configuratie zonder secrets in Git; back-upretentie, RPO/RTO en restore op aparte omgeving testen. | Back-up faalt of restore faalt: gebruik laatste gevalideerde back-up, stop wijzigingen en verbeter procedure. | Operations-eigenaar | Open / middel |
| R10 | Secrets, persoonsgegevens of ongeschoonde configuraties belanden in Git/logs. | Privacyincident, accountmisbruik of onveilige overdracht. | 3 | 5 | 15 | Dataminimalisatie, secretprocedure buiten Git, secretscan, review en beperkte logretentie. | Secret gelekt: intrekken/roteren, toegang controleren, incident melden en gegevens verwijderen volgens procedure. | Security/privacy-eigenaar | Open / hoog |
| R11 | Inschrijving of communicatie start vóór formele goedkeuring. | Onbevoegd evenement, reputatieschade of privacyproblemen. | 2 | 4 | 8 | Communicatie-gate expliciet registreren; berichten vooraf laten reviewen; testdata gebruiken. | Niet-goedgekeurd bericht: onmiddellijk intrekken, docent informeren en communicatie corrigeren. | Communicatie-eigenaar | Open / middel |
| R12 | Privacytekst, bewaartermijn of gedragscode is onvolledig. | Onduidelijke deelnemersvoorwaarden of onnodige gegevensverwerking. | 3 | 4 | 12 | Alleen noodzakelijke gegevens verzamelen; privacytekst, toestemming en verwijderprocedure vóór inschrijving reviewen. | Onjuiste gegevens of bezwaar: registratie stoppen, gegevens corrigeren/verwijderen en verantwoordelijke informeren. | Jules (registratie); privacy-eigenaar nog te bepalen | Open / middel |
| R13 | Te weinig crew, onduidelijke eigenaars of ontbrekende back-ups. | Support, veiligheid of uitvoering valt stil bij afwezigheid. | 3 | 4 | 12 | Primaire en secundaire eigenaar per kritieke taak; ploegenschema, briefing en escalatiepad. | Afwezigheid of onbemande rol: back-up activeren of onderdeel gecontroleerd schrappen. | Kyell | Open / middel |
| R14 | Draaiboek, noodprocedure of cleanup is niet uitvoerbaar. | Chaotische opbouw/afbraak, veiligheidsproblemen of laattijdige oplevering. | 3 | 4 | 12 | Draaiboek volgens template, tabletop, dry-run en expliciete go/no-go-check. | Stappen niet uitvoerbaar tijdens dry-run: gate blokkeren tot aangepaste test geslaagd is. | Eventverantwoordelijke | Open / middel |
| R15 | Hardware, kabels, opslag of andere materialen zijn niet beschikbaar of defect. | Test of evenement kan niet volledig doorgaan. | 3 | 3 | 9 | Materiaallijst, reservemateriaal, voorafgaande controle en compatibiliteitstest. | Tekort/defect: capaciteit verlagen, reserve inzetten of scope beperken. | Materiaal-eigenaar | Open / laag-middel |
| R16 | Scope groeit door optionele ideeën zoals stream, leaderboard, RetroPie of Arduino. | Must-eisen, tests en documentatie raken achterop. | 4 | 3 | 12 | Must/Should/Could-prioritering; uitbreidingen pas na technische en organisatorische gates. | Must-mijlpaal loopt uit: Could-onderdeel uitstellen of schrappen. | Kyell | Open / middel |
| R17 | Een belastende load-, security- of failovertest wordt zonder akkoord uitgevoerd. | Impact op Smith, campusdiensten of andere groepen. | 2 | 5 | 10 | Change request, testvenster, stopconditie en beperkte scope vooraf vastleggen. | Onverwachte belasting of incident: test stoppen, docent/IT informeren en impact documenteren. | Technische test-eigenaar | Open / middel |
| R18 | Het evenement wordt uitgevoerd zonder geslaagde dry-run of formele go/no-go. | Onveilige of instabiele uitvoering; onvoldoende bewijs. | 2 | 5 | 10 | Go/no-go-checklist, dry-run met meerdere clients en fallback naar tabletop/dry-run. | Gate ontbreekt of test faalt: evenement niet uitvoeren. | Docent/eventverantwoordelijke | Open / hoog |

## 3. Kritieke afhankelijkheden

- Definitieve groepsleden en taakverdeling zijn nog niet vastgelegd.
- Locatie, datum, capaciteit en budget moeten nog worden bevestigd.
- Uplink, netwerkdiensten, switches, caching en eventuele changes vereisen IT-overleg.
- Stroom- en veiligheidsbeoordeling vereisen gebouwbeheer en preventie.
- Inschrijving en communicatie vereisen goedkeuring en een privacybeslissing.
- Smith-resourcequota, VMID-range en toegestane netwerken moeten vóór permanente technische opbouw bekend zijn.

## 4. Opvolging en escalatie

### Wekelijks

- Risicoscores en nieuwe risico’s bespreken tijdens het statusmoment.
- Maatregelen, eigenaars en deadlines actualiseren.
- Nieuwe risico’s, blokkades, incidenten en wijzigingen in het logboek zetten.
- Eén risico- of testresultaat toevoegen aan het wekelijkse bewijs.

### Bij een incident

1. Veiligheid en impact eerst beperken.
2. Component of activiteit isoleren wanneer nodig.
3. Geen verdere wijzigingen uitvoeren zonder eigenaar en beslissing.
4. Docent/IT of gebouwbeheer escaleren volgens de situatie.
5. Tijdstip, impact, acties, metingen en herstel registreren.
6. Risico, runbook en projectplan bijwerken.

### Gatevoorwaarden

Een go/no-go wordt niet gegeven wanneer een kritiek risico onbehandeld is, een verplichte goedkeuring ontbreekt, de dry-run faalt of rollback/herstel niet aantoonbaar werkt.