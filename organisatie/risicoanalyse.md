# Risicoanalyse — LAN-party 26

> Werkdocument voor risico-identificatie, opvolging en go/no-go-beslissingen. Eigenaars zijn ingevuld (team: Kyell en Jules). Scores zijn op 2026-10-16 herbekeken gezien de ingekorte planning (alle gates vóór 20/10).

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
| R01 | Goedkeuringen van Stuvo, gebouwbeheer of IT komen te laat of ontbreken. | Evenement kan niet officieel doorgaan; planning schuift op. | 4 | 5 | 20 | Alle aanvragen vóór 20/10 indienen; doorlooptijd dagelijks opvolgen; alternatieve tabletop/dry-run voorbereiden. | Geen akkoord vóór de gate: geen campusaansluiting of officiële communicatie; escaleren naar docent. | Kyell + Jules (Jules: Stuvo, Kyell: IT/IEEE) | Open / kritiek tot akkoord |
| R02 | Een eigen DHCP-, router-, NAT- of AP-functie raakt het campusnetwerk. | Verkeerde adressen, netwerkuitval of impact op andere gebruikers. | 2 | 5 | 10 | Alleen IT-goedgekeurde diensten gebruiken; rogue-DHCP-scenario in geïsoleerde laboproef testen; change request verplicht. | Onverwachte DHCP-offers of routing: component onmiddellijk isoleren, IT verwittigen en incident registreren. | Kyell | Open / hoog |
| R03 | Uplink, IP-adressen, poorten of bandbreedte zijn onvoldoende voor de deelnemerscapaciteit. | Hoge latency, packet loss, onbruikbare gameservers of downloads. | 3 | 4 | 12 | Capaciteitsplan op basis van IEEE-inschrijving; test met meerdere clients; SLO’s tijdens laboproef (week 17); limiet op inschrijvingen. | Drempel overschreden: deelnemerscapaciteit beperken, bulkverkeer verminderen en escaleren naar IT. | Kyell | Open / middel |
| R04 | Stroomgroepen worden overbelast of kabels vormen een veiligheidsrisico. | Stroomuitval, schade, brandgevaar of evacuatieprobleem. | 3 | 5 | 15 | Stroomplan (vóór 18/10) laten controleren door gebouwbeheer/preventie; belasting meten; kabelroutes en nooduitgangen vrijhouden. | Warmte, uitval, losse kabel of geblokkeerde uitgang: activiteit stoppen en gebouwprocedure volgen. | Jules | Open / hoog |
| R05 | Onbedoelde switchloop of verkeerd aangesloten apparatuur veroorzaakt een broadcast storm. | Netwerkuitval en impact op deelnemers of campus. | 3 | 4 | 12 | Managed switches, RSTP/BPDU-bescherming waar IT dit toestaat, duidelijke labels en deelnemersinstructies. | Poortflapping of stormalarm: poort isoleren, topologie controleren en incidentlog bijwerken. | Kyell | Open / middel |
| R06 | LANCache werkt niet, veroorzaakt DNS-problemen of heeft geen bruikbare fallback. | Downloads falen of algemene internettoegang wordt verstoord. | 3 | 4 | 12 | Alleen toegelaten platformen; hit/miss, DNS-impact, opslag, uitschakeling en fallback vooraf testen (vóór 20/10). | Cachefout of DNS-impact: cache uitschakelen volgens runbook en directe fallback valideren. | Kyell | Open / middel |
| R07 | Lokale gameserver (RetroPie) of VR-val (Pico 4) raakt onbruikbaar. | Toernooi of geplande gameflow kan niet doorgaan. | 3 | 3 | 9 | Compatibiliteits- en belastingtest vóór 20/10; reserveconfiguratie; casting-uitval (VR); alternatieve game/activiteit. | Server onbereikbaar of overbelast: service herstellen of gecontroleerd overschakelen naar fallback. | Jules (VR), Kyell (RetroPie) | Open / middel |
| R08 | Monitoring detecteert problemen niet of alerts worden niet opgevolgd. | Storingen duren langer; succesmetingen ontbreken. | 3 | 4 | 12 | Alertmatrix met drempel, eigenaar en actie; alerts vóór dry-run testen; dashboard intern beschikbaar. | Alert zonder reactie: eigenaar/escalatie bellen en handmatige meting uitvoeren. | Kyell | Open / middel |
| R09 | Configuratie- of unieke eventdata kan niet worden hersteld. | Lang herstel, dataverlies of niet-overdraagbare dienst. | 2 | 5 | 10 | Configuratie zonder secrets in Git; back-upretentie, RPO/RTO en restore op aparte omgeving testen tijdens laboproef. | Back-up faalt of restore faalt: gebruik laatste gevalideerde back-up, stop wijzigingen en verbeter procedure. | Kyell | Open / middel |
| R10 | Secrets, persoonsgegevens of ongeschoonde configuraties belanden in Git/logs. | Privacyincident, accountmisbruik of onveilige overdracht. | 3 | 5 | 15 | Dataminimalisatie; secretprocedure buiten Git; secretscan, review en beperkte logretentie; leaderboard-data lokaal en pseudoniem. | Secret gelekt: intrekken/roteren, toegang controleren, incident melden en gegevens verwijderen volgens procedure. | Jules (privacy) / Kyell (security) | Open / hoog |
| R11 | Inschrijving of communicatie start vóór formele goedkeuring. | Onbevoegd evenement, reputatieschade of privacyproblemen. | 2 | 4 | 8 | Communicatie-gate expliciet registreren (vóór 20/10); berichten via IEEE vooraf laten reviewen; testdata gebruiken. | Niet-goedgekeurd bericht: onmiddellijk intrekken, docent informeren en communicatie corrigeren. | Jules | Open / middel |
| R12 | Privacytekst, bewaartermijn of gedragscode is onvolledig. | Onduidelijke deelnemersvoorwaarden of onnodige gegevensverwerking. | 3 | 4 | 12 | Alleen noodzakelijke gegevens verzamelen; privacytekst, toestemming (via IEEE-inschrijving) en verwijderprocedure vóór inschrijving reviewen. | Onjuiste gegevens of bezwaar: registratie stoppen, gegevens corrigeren/verwijderen en verantwoordelijke informeren. | Jules | Open / middel |
| R13 | Te weinig crew, onduidelijke eigenaars of ontbrekende back-ups. | Support, veiligheid of uitvoering valt stil bij afwezigheid. | 3 | 4 | 12 | Primaire en secundaire eigenaar per kritieke taak (RACI); ploegenschema; crew vóór 20/10 afstemmen met IEEE; briefing en escalatiepad. | Afwezigheid of onbemande rol: back-up activeren of onderdeel gecontroleerd schrappen. | Kyell | Open / middel |
| R14 | Draaiboek, noodprocedure of cleanup is niet uitvoerbaar. | Chaotische opbouw/afbraak, veiligheidsproblemen of laattijdige oplevering. | 3 | 4 | 12 | Draaiboek vóór 21/10 klaar; tabletop, dry-run en expliciete go/no-go-check (formele go/no-go: 21/10). | Stappen niet uitvoerbaar tijdens dry-run: gate blokkeren tot aangepaste test geslaagd is. | Jules | Open / middel |
| R15 | Hardware, kabels, opslag of andere materialen zijn niet beschikbaar of defect. | Test of evenement kan niet volledig doorgaan. | 3 | 3 | 9 | Materiaallijst, reservemateriaal (o.a. reservekabels), controle vóór opbouw (21/10) en compatibiliteitstest. | Tekort/defect: capaciteit verlagen, reserve inzetten of scope beperken. | Kyell | Open / laag-middel |
| R16 | Scope groeit door optionele ideeën zoals stream, extra gameservers of Arduino-uitbreidingen. | Must-eisen, tests en documentatie raken achterop. | 3 | 3 | 9 | Leaderboard en RetroPie zijn nu gepland (scope stabiel); verdere uitbreidingen pas na alle gates. | Must-mijlpaal loopt uit: Could-onderdeel uitstellen of schrappen. | Kyell | Open / laag-middel |
| R17 | Een belastende load-, security- of failovertest wordt zonder akkoord uitgevoerd. | Impact op Smith, campusdiensten of andere groepen. | 2 | 5 | 10 | Change request, testvenster, stopconditie en beperkte scope vooraf vastleggen; tests alleen in labomgeving en goedgekeurde eventomgeving. | Onverwachte belasting of incident: test stoppen, docent/IT informeren en impact documenteren. | Kyell | Open / hoog |
| R18 | Het evenement wordt uitgevoerd zonder geslaagde dry-run of formele go/no-go. | Onveilige of instabiele uitvoering; onvoldoende bewijs. | 2 | 5 | 10 | Go/no-go-checklist; dry-run met meerdere clients op 21/10; formele go/no-go vóór opbouw; fallback naar tabletop/dry-run. | Gate ontbreekt of test faalt: evenement niet uitvoeren. | Docent / Jules (event) / Kyell (techniek) | Open / hoog |

## 3. Kritieke afhankelijkheden

- Uplink, netwerkdiensten, switches, caching en eventuele changes vereisen IT-overleg.
- Deelnemerscapaciteit wordt bepaald door IEEE student branch Brugge (inschrijving).
- De crew moet vóór de eventdag in overleg met IEEE worden afgestemd.
- Gates en bewijsstukken moeten afgestemd zijn met IEEE (contact: Jonas Rollier).
- Stroom- en veiligheidsbeoordeling vereisen akkoord van gebouwbeheer en preventie (Stuvo).
- Smith-resourcequota, VMID-range en toegestane netwerken moeten vóór de opbouw bekend zijn.

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