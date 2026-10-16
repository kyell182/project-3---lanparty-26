# Todo — LAN-party 26

> Taakaanduidingen en checklists per fase. Rollen en eindverantwoordelijkheden staan in de [raci-matrix](raci-matrix.md); planning en governance in het [projectplan](projectplan.md). Event: **donderdag 22 oktober 2026, 18:00–24:00, Stuvo**.

## Fase 1 — Voorbereiding (15/10 → 20/10)

Doel: alle vijf de gates gesloten vóór 20/10, laboproef uitgevoerd, LAN-portaal gestart.

| # | Taak | Eigenaar | Deadline | Gate | Status |
|---|---|---|---|---|---|
| 1.1 | Gate 1 bespreken met Leroy (concept akkoord) | Kyell + Jules | 16/10 | Gate 1 | ☐ |
| 1.2 | Contact met Jonas (IEEE): gates afstemmen, bewijsstukken-splitsing bevestigen (wij: Stuvo + leaderboard; IEEE: overkoepelende organisatie en inschrijving) | Kyell | 17/10 | Gate 1–5 | ☐ |
| 1.3 | Deelnemerscapaciteit laten bepalen door IEEE en opschrijven in [conceptnota](conceptnota.md) | Kyell | 17/10 | Gate 1 | ☐ |
| 1.4 | Stroom- en tafelplan voor Stuvo uitwerken en laten controleren (gebouwbeheer/preventie) | Jules | 18/10 | Gate 2 | ☐ |
| 1.5 | Lokaalplan (evacuatie, toegankelijkheid, toezicht) afronden met preventie | Jules | 18/10 | Gate 2 | ☐ |
| 1.6 | Laboproef met de 8 verplichte scenario's uitvoeren op Proxmox/Smith (lab) | Kyell | 20/10 | Gate 3 | ☐ |
| 1.7 | SLO-drempelwaarden voor latency/packet loss vastleggen tijdens de laboproef | Kyell | 20/10 | Gate 3 | ☐ |
| 1.8 | Caching: hit/miss, DNS-impact, opslag en fallback testen | Kyell | 20/10 | Gate 3 | ☐ |
| 1.9 | Communicatiepakket (via IEEE-inschrijving): privacytekst, gedragscode, toestemmingen checken | Jules | 19/10 | Gate 4 | ☐ |
| 1.10 | LAN-portaal: opzetten in Stuvo-minimale infra (Docker, offline) — vervangt de oorspr. Python-leaderboard ([kyell182/lan-portaal](https://github.com/kyell182/lan-portaal)) | Kyell | 20/10 | Gate 3 + 4 | ☐ |
| 1.11 | Privacy-notitie LAN-portaal afronden (pseudoniem, lokaal bewaren, verwijderen na event) | Jules | 19/10 | Gate 4 | ☐ |
| 1.12 | VR-opstelling (Pico 4 / Quake3Quest) afwerken: installatie, test, casting-uitvallen | Jules | 20/10 | Gate 5 | ☐ |
| 1.13 | RetroPie en Arduino-controller testen op de eventhardware | Kyell | 20/10 | Gate 5 | ☐ |
| 1.14 | Alle vijf gates registeren in het [logboek](logboek.md) met bewijs | Kyell | 20/10 | Gate 1–5 | ☐ |
| 1.15 | Dry-run plannen (datum na Gate 4) en crew afstemmen met IEEE | Kyell | 20/10 | Gate 5 | ☐ |

## Fase 2 — Eventdag (donderdag 22/10, 18:00–24:00)

Voorafgaande dag (21/10): opbouw in Stuvo; dry-run met meerdere clients; formele go/no-go (Gate 5). Het draaiboek (nog uit te werken in `../draaiboek/`) fungeert als leidraad voor de dag.

| # | Taak | Eigenaar | Tijdstip | Status |
|---|---|---|---|---|
| 2.1 | Opbouw: netwerk, kabels, stroom, schermen, LAN-portaal | Kyell + Jules + crew | 21/10, vanaf 15:00 | ☐ |
| 2.2 | Dry-run: 8 scenario's op de eventhardware, monitoring live | Kyell | 21/10, 17:00–19:00 | ☐ |
| 2.3 | Formele go/no-go registreren in [logboek](logboek.md) | Kyell + Jules | 21/10, 19:00 | ☐ |
| 2.4 | Deelnemers onthaal en aansluiting (via IEEE-registratielijst) | Jules + crew | 22/10, 18:00 | ☐ |
| 2.5 | LAN-portaal live: toernooien/resultaten invoeren, live brackets en scoreboard op scherm | Kyell | 22/10, gedurende event | ☐ |
| 2.6 | VR-sessies (Pico 4 / Quake3Quest) | Jules + crew | 22/10, gedurende event | ☐ |
| 2.7 | Servicedesk: triage, gekende problemen, escalatiepad | Kyell + Jules + crew | 22/10, gedurende event | ☐ |
| 2.8 | Monitoring actief houden; incidentlog bijhouden | Kyell | 22/10, gedurende event | ☐ |
| 2.9 | Afruiming: nettafels, metingen (latency/packet loss/cachewinst) opsommen | Kyell + Jules | 22/10, 23:00–23:30 | ☐ |
| 2.10 | Afbraak en cleanup Stuvo | Kyell + Jules + crew | 22/10, 23:30–24:00 | ☐ |

## Fase 3 — Nadien (23/10 → oplevering)

| # | Taak | Eigenaar | Deadline | Status |
|---|---|---|---|---|
| 3.1 | Evaluatie: metingen vs SLO, incidenten, feedback, aanbevelingen | Jules + Kyell | eind oktober | ☐ |
| 3.2 | Scoreboard-data en persoonsgegevens verwijderen volgens bewaartermijn | Jules | 1 week na event | ☐ |
| 3.3 | Overdrachtsdossier afwerken (bewijsstukken, runbooks, tests) conform [opdracht](../docs/opdracht.md) | Kyell | eind oktober | ☐ |
| 3.4 | Eindlogboekcontrole: alle gates, incidenten en beslissingen geregistreerd | Kyell | eind oktober | ☐ |
