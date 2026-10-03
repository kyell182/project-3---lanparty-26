# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Wat dit is

Een **documentatie-only repository** (Markdown, Mermaid, één PDF) voor "Project 3 – LAN-party 2026" (VIVES, Network Experience). Er is geen code, build, lint of test: er valt niets te starten of te draaien. Alle inhoud is in het **Nederlands**; schrijf nieuwe documenten ook in het Nederlands en volg de stijl van de bestaande bestanden. Mermaid-diagrammen worden gerenderd door de Markdown-viewer; er is geen aparte tool.

## Architectuur

- `03-lan-party.md` – volledige opdrachtomschrijving; bron van waarheid voor vereisten.
- `README.md` – projectoverzicht: go/no-go-gates, verplichte testscenario's, team/RACI-tabel, checklists, planning, scope. Startpunt voor wie nieuw is.
- `todo.md` – afvinkbare checklist per fase (0–9), gekoppeld aan gates en weken.
- `logging/logboek.md` – logboektabel (Datum, Type, Onderwerp, Beschrijving, Eigenaar). Types: Beslissing, Actie, Test, Probleem, Incident, Evaluatie.
- `brainstorm/` – technisch ontwerp in genummerde modules die naar elkaar verwijzen:
  - `NETWERK_ARCHITECTUUR.md` (1): pfSense → core switch; VLAN 10 Management `10.10.10.0/24`, VLAN 20 Core Services `10.10.20.0/24`, VLAN 30 Gamers `10.10.30.0/22`; stroomberekening (max. 5–6 pc's per 16A-groep).
  - `MONITORING_STACK.md` (2): Telegraf (SNMP) → InfluxDB → Grafana.
  - `SERVER_SERVICES.md` (3): LanCache in Docker, DNS via pfSense/Unbound.
  - `concepten.md`, `Vr_Setup/` – eerste ideeën (o.a. Pico 4 / Quake3Quest).
- `retro/` – RetroPie-installatiehandleiding (arcadekast op minipc). `retro/credentials.md` is gitignored en mag nooit gecommit worden.
- `locatie/`, `schema's/` – nog lege mappen (daarom niet in git).

Wijzig je het IP-plan, de VLANs of de services in één brainstorm-module, controleer dan de andere twee. Voeg je een map toe of hernoem je er een, werk dan deze sectie en de "Repositorystructuur" in `README.md` bij.

## Projectregels voor documenten

- **Go/no-go-gates** (Concept, Locatie, Techniek, Communicatie, Uitvoering): zonder formeel akkoord geen verbinding met het campusnetwerk en geen communicatie als officieel evenement.
- Geen eigen DHCP/router/NAT/access point zonder expliciete toestemming van IT; uplink en diensten komen van IT.
- Caching (LANCache) alleen voor toegelaten platformen; geen illegale gamebestanden; deelnemersverkeer niet inhoudelijk inspecteren.
- Geen geheimen, betalings- of gezondheidsgegevens in de repo.
- Nieuwe beslissingen, tests en incidenten komen in `logging/logboek.md`; vink afgewerkte punten af in `todo.md` en de README-checklists.

## Conventies

- Commitberichten volgen conventional commits (`refactor:`, `docs:`, …) in het Engels, zoals de bestaande historie.
- Nieuwe schema's zijn Mermaid in Markdown, geen losse afbeeldingen.
