# Logboek

Dit logboek bevat belangrijke beslissingen, acties, testen, problemen en incidenten van het LAN-partyproject. Het geldt voor de hele repository, ook voor zijprojecten zoals [arcade/](../arcade/README.md).

Gebruik voor `Type` bijvoorbeeld `Beslissing`, `Actie`, `Test`, `Probleem`, `Incident` of `Evaluatie`. Noteer bij een incident geen gevoelige persoonsgegevens.

Voeg waar mogelijk een link naar bewijs toe, zoals een document, screenshot, configuratie zonder geheimen of testresultaat. Vul altijd de datum in, ook als die gelijk is aan de rij erboven.

| Datum | Type | Onderwerp | Beschrijving | Eigenaar |
| --- | :---: | --- | --- | :---: |
| 2026-09-22 | Actie | Projectdocumentatie | Logboek en checklists toegevoegd. | Kyell |
| 2026-09-22 | Actie | Brainstorm | Eerste brainstormsessie gehouden en repository klaargezet. | Kyell |
| 2026-09-22 | Actie | Arcadekast | Hardware bekeken voor RetroPie op een minipc. | Kyell |
| 2026-09-22 | Actie | Arcadekast | Handleiding voor de installatie van RetroPie op de minipc geschreven (zie [arcade/](../arcade/installatie-retropie.md)). | Kyell |
| 2026-09-25 | Actie | Organisatie | Contact gelegd met meneer Calleeuw: aanvraag voor een gesprek over de organisatie van de LAN-party. | Kyell |
| 2026-09-25 | Actie | LAN-party concept | Concept uitgewerkt voor een lokale LAN-opstelling, plus research. | Kyell |
| 2026-09-25 | Actie | Pico 4 LAN-concept | Concept en documentatie uitgewerkt voor een lokale Pico 4 LAN-opstelling met Quake3Quest en mogelijke casting. | Jason |
| 2026-09-30 | Actie | Projectdocumentatie | `todo.md` uitgebreid met week-per-week checklists. | Jules |
| 2026-09-30 | Beslissing | Projectdocumentatie | Projectplan en risicoanalyse opgesplitst in eigen documenten. | Jules |
| 2026-10-01 | Actie | Projectdocumentatie | Projectplan en risicoanalyse vervolledigd. | Jules |
| 2026-10-01 | Actie | Organisatie | Voorstel voor een Microsoft Form aangemaakt. | Jules |
| 2026-10-02 | Actie | Projectdocumentatie | Stakeholderregister, RACI-matrix en conceptnota opgesteld. | Jules |
| 2026-10-03 | Actie | Projectdocumentatie | `CLAUDE.md` toegevoegd en de repositorystructuur in de README gecorrigeerd. | Kyell |
| 2026-10-04 | Actie | Netwerkontwerp | Netwerkontwerp verplaatst naar `netwerkontwerp/`; overzicht en schaalbaar ontwerp (blokken per 192 pc's) geschreven. Schaalbaar ontwerp is nog niet goedgekeurd. | Kyell |
| 2026-10-04 | Actie | Monitoring | Docker Compose-stack (Telegraf, InfluxDB, Grafana) met dashboard en alarmen opgezet in `monitoring/`. Nog niet getest op echte apparaten. | Kyell |
| 2026-10-04 | Actie | Draaiboek en LAN 70 | Herbruikbaar draaiboek voor VIVES (fase 00 tot 05), begrippenlijst en netwerkopstelling voor een LAN van 70 toegevoegd. | Kyell |
| 2026-10-15 | Beslissing | Datum, locatie en hoofdtaak | De evenementdatum is vastgelegd op vrijdag 22 oktober 2026 in Stuvo. De overkoepelende organisatie ligt bij IEEE student branch Brugge (aanspreekpunt: Jonas Rollier); ons project is verantwoordelijk voor de inrichting/uitvoering in Stuvo en voor de leaderboard (nieuw, eigenaar: Jules). Team: Kyell, Jules, Jason. Planningshorizon sterk gecomprimeerd; gates worden waar mogelijk samengevoegd met de IEEE-gates. | Kyell, Jules, Jason |
| 2026-10-15 | Actie | Repositorystructuur | Repository professioneel gerestructureerd naar thematische mappen (`docs/`, `organisatie/`, `draaiboek/`, `netwerk/`, `monitoring/`, `activiteiten/`) met kebab-case bestandsnamen; alle relatieve links, CLAUDE.md en README bijgewerkt en geverifieerd. | Jules |
| 2026-10-16 | Beslissing | Team en taken | Jason verlaat het team; Jules neemt VR (Pico 4 / Quake 3 Quest) over. Team definitief: Kyell en Jules. Alle documenten (RACI, stakeholderregister, projectplan, risicoanalyse) bijgewerkt. | Jules |
| 2026-10-16 | Beslissing | Planning en gates | Alle 5 gates sluiten vóór 20/10; Gate 1 (Initiatief) wordt besproken op vrijdag 16/10 met Leroy Mathieu. Eventuren vastgelegd: donderdag 22/10, 18:00–24:00 in Stuvo. De bevraging wordt afgevoerd — IEEE student branch Brugge doet de inschrijving zelf. | Kyell, Jules |
| 2026-10-16 | Beslissing | Leaderboard | Ontwikkeling gestart (week 16), eigenaar Jules (back-up Kyell). Games dynamisch toevoegbaar, privacytoestemming via IEEE-inschrijfformulier, pseudoniemen, data binnen 1 week na het event verwijderd. | Jules |
| 2026-10-16 | Actie | Leaderboard | Leaderboard volledig uitgewerkt: Python-stdlib server + JSON-opslag, LAN Admin-pagina (dropdowns voor game/speler, score 0–100, spelers en games naast elkaar, history laatste 20 met undo, danger zone), groot-schermweergave met top-3 (gold/silver/bronze) en kolom "Best Game", speler-registratiepagina. Scoring: totaal = som van alle 0–100 scores; beste game = hoogste enkelvoudige score (tiebreak: meest ingevuld). UI van de leaderboard-pagina's Engelstalig. Documentatie (leaderboard/README.md) en dit logboek bijgewerkt. | Jules |
| 2026-10-16 | Beslissing | Leaderboard → LAN-portaal | De Python-stdlib leaderboard is **DEPRECATED** en wordt **niet meer gebruikt**. **Kyell** heeft het uitgrown tot een volwaardig **LAN-portaal** ([github.com/kyell182/lan-portaal](https://github.com/kyell182/lan-portaal)): Docker, volledig offline; scoreboard + toernooien met live brackets (knock-out, Swiss, poules, …), edities/events, zitplan, prijzen, Discord-meldingen, PWA; admin login, publiek ziet live bijwerkingen (SSE). De Python-code (`leaderboard/`) blijft in de repo ter referentie en wordt niet meer onderhouden. Alle documentatie (leaderboard/README.md, organisatie/leaderboard.md, CLAUDE.md, README.md, todo.md) aangepast met de deprecation en de verwijzing naar het portaal; privacykaders (pseudoniem, lokaal bewaren, verwijderen binnen 1 week) blijven gelden op het portaal. | Jules, Kyell |
| 2026-10-26 | Actie | LAN-party | LAN-party is doorgegaan. | Kyell, Jules |
| 2026-10-26 | Test | Netwerk en portaal | Netwerk en portaal hebben het hele event goed volgehouden. | Kyell, Jules |
| 2026-10-26 | Evaluatie | Netwerkincidenten | Geen incidenten aan de netwerkkant tijdens het event. | Kyell, Jules |
| 2026-10-26 | Actie | Afbraak | Al het materiaal is teruggelegd in lokaal 303. | Kyell, Jules |
| 2026-10-26 | Evaluatie | Arcadekast | Arcadekast was aanwezig op de LAN-party en was een succes. Probleem: deelnemers kwamen soms in het configuratiemenu terecht, waardoor de besturing soms niet meer gemapt was. | Kyell |
| 2026-11-13 | Evaluatie | Arcadekast | Stand van zaken: RetroPie geïnstalleerd, autostart en schermscript werken, controllers werken, het grootste deel van de emulators werkt. Open punten staan in [arcade/README.md](../arcade/README.md). | Kyell |
| 2026-11-13 | Test | Arcadekast | Inventaris van de arcade-pc via SSH: N64 start zonder fout; PSX-BIOS ontbreekt waardoor PlayStation-spellen waarschijnlijk niet starten; `genesis` is een symlink naar `megadrive`. Zie [emulators.md](../arcade/emulators.md). | Kyell |
| 2026-11-13 | Actie | Arcadekast | Autostart en schermscript gedocumenteerd ([scherm-en-autostart.md](../arcade/scherm-en-autostart.md)); kopieën van de scripts in `arcade/scripts/`. | Kyell |
| 2026-11-13 | Actie | Arcadekast | Arcadekast ondergebracht in een eigen map `arcade/` als zijproject; `activiteiten/retropie/` verplaatst naar `arcade/`. | Kyell |
