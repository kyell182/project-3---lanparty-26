# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Wat dit is

Een **documentatierepository** (Markdown, Mermaid, één PDF) voor "Project 3 – LAN-party 2026" (VIVES, Network Experience), met één uitzondering: de map `monitoring/` bevat een Docker Compose-stack. Er is verder geen code, build, lint of test. Alle inhoud is in het **Nederlands**; schrijf nieuwe documenten ook in het Nederlands en volg de stijl van de bestaande bestanden. Mermaid-diagrammen worden gerenderd door de Markdown-viewer; er is geen aparte tool.

## Architectuur

De mappen zijn georganiseerd per onderwerp. `README.md` bevat de leesroute en de tabel "Waar vind ik wat" voor mensen. Dit is de kaart voor jou:

- `03-lan-party.md` – volledige opdrachtomschrijving; bron van waarheid voor vereisten.
- `README.md` – projectoverzicht: leesroute, go/no-go-gates, verplichte testscenario's, team, planning, scope, repositorystructuur. Startpunt voor wie nieuw is.
- `organisatie en projectsturing/` – projectplan, conceptnota, stakeholderregister, RACI-matrix, risicoanalyse, studentenbevraging en `todo.md` (afvinkbare checklist per fase, gekoppeld aan gates en weken). Door het team zelf onderhouden.
- `logging/logboek.md` – logboektabel (Datum, Type, Onderwerp, Beschrijving, Eigenaar). Types: Beslissing, Actie, Test, Probleem, Incident, Evaluatie.
- `brainstorm/` – alleen eerste ideeën: `concepten.md`, `Vr_Setup/` (Pico 4 / Quake3Quest) en de lay-out als pdf.
- `netwerkontwerp/` – het technische ontwerp. Modules die naar elkaar verwijzen:
  - `NETWERK_ARCHITECTUUR.md` (1): pfSense → core switch; VLAN 10 Management `10.10.10.0/24`, VLAN 20 Core Services `10.10.20.0/24`, VLAN 30 Gamers `10.10.30.0/22`; stroomberekening (max. 5–6 pc's per 16A-groep).
  - `MONITORING_STACK.md` (2): Telegraf (SNMP) → InfluxDB → Grafana. De uitvoering staat in `monitoring/`.
  - `SERVER_SERVICES.md` (3): LanCache in Docker, DNS via pfSense/Unbound.
  - `NETWERK_OVERZICHT.md` – samenvatting van module 1–3 met verduidelijkte schema's en openstaande punten; houd synchroon met de modules.
  - `SCHAALBAAR_ONTWERP.md` – voorstel met identieke "blokken" (VLAN + `/24` per 192 pc's) zodat het ontwerp van 100 tot 10 000 deelnemers schaalt; vervangt voorgesteld het enkele VLAN 30 uit module 1. Nog niet goedgekeurd.
- `gedeeld/BEGRIPPEN.md` – begrippenlijst (alfabetisch, met ankers), gebruikt door bijna alle documenten. Link ernaar met `BEGRIPPEN.md#begrip` en voeg nieuwe vaktermen hier toe in plaats van ze telkens opnieuw uit te leggen.
- `lan-70/LAN_70_OPSTELLING.md` – netwerkopstelling voor een LAN van 70 (tier S, 1 blok), geschreven voor de **studentenvereniging**; gebruikt het schaalbare ontwerp.
- `draaiboek/` – herbruikbaar draaiboek voor **VIVES zelf** voor latere LAN's, per fase genummerd (`00_OVERZICHT` met rollen, gates en tijdlijn, tot `05_BIJLAGEN` met sjablonen). Pas het aan na elke evaluatie. `00_OVERZICHT.md` is het startpunt.
- `monitoring/` – de enige map met code: Docker Compose voor de TIG-stack (Telegraf, InfluxDB, Grafana) met Telegraf-config en een voorgeprovisioneerd Grafana-dashboard. Start met `cd monitoring && cp .env.example .env && docker compose up -d`; `monitoring/lan-70/` bevat een variant met ingevulde `.env` voor de LAN van 70 (`include` van de gedeelde Compose-file). Apparaten staan in `SNMP_APPARATEN` in `.env`; Grafana-alarmen in `grafana/provisioning/alerting/alarmen.yml`. Geheimen staan alleen in `.env` (gitignored). Controleer wijzigingen met `docker compose --env-file <env> config --quiet`. `HANDLEIDING.md` is voor beginners, `README.md` is de naslag.
- `retro/` – RetroPie-installatiehandleiding (arcadekast op minipc). `retro/credentials.md` is gitignored en mag nooit gecommit worden.
- `locatie/`, `schema's/` – nog lege mappen (daarom niet in git).

Wijzig je het IP-plan, de VLANs of de services in één module van `netwerkontwerp/`, controleer dan de andere en `lan-70/`. Voeg je een map toe, verplaats of hernoem je een bestand, werk dan deze sectie en de "Repositorystructuur" in `README.md` bij, en controleer de relatieve links (ook de ankers naar `BEGRIPPEN.md`).

## Projectregels voor documenten

- **Go/no-go-gates** (Concept, Locatie, Techniek, Communicatie, Uitvoering): zonder formeel akkoord geen verbinding met het campusnetwerk en geen communicatie als officieel evenement.
- Geen eigen DHCP/router/NAT/access point zonder expliciete toestemming van IT; uplink en diensten komen van IT.
- Caching (LANCache) alleen voor toegelaten platformen; geen illegale gamebestanden; deelnemersverkeer niet inhoudelijk inspecteren.
- Geen geheimen, betalings- of gezondheidsgegevens in de repo.
- Nieuwe beslissingen, tests en incidenten komen in `logging/logboek.md`; vink afgewerkte punten af in `organisatie en projectsturing/todo.md` en de README-checklists.

## Conventies

- Commitberichten volgen conventional commits (`refactor:`, `docs:`, …) in het Engels, zoals de bestaande historie.
- Nieuwe schema's zijn Mermaid in Markdown, geen losse afbeeldingen.
- Links tussen documenten zijn relatief. Verplaats je bestanden, herbereken dan alle links die ernaar verwijzen.
