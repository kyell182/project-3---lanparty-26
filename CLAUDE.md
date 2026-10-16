# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Wat dit is

Een **documentatierepository** (Markdown, Mermaid, één PDF) voor "Project 3 – LAN-party 26" (VIVES, Network Experience), met één uitzondering: de map `monitoring/` bevat een Docker Compose-stack. Er is verder geen code, build, lint of test. Alle inhoud is in het **Nederlands**; schrijf nieuwe documenten ook in het Nederlands en volg de stijl van de bestaande bestanden. Mermaid-diagrammen worden gerenderd door de Markdown-viewer; er is geen aparte tool.

## Architectuur

De mappen zijn georganiseerd per onderwerp. `README.md` bevat de leesroute en de tabel "Waar vind ik wat" voor mensen. Dit is de kaart voor jou:

- `README.md` – projectoverzicht: leesroute, go/no-go-gates, verplichte testscenario's, team, planning, scope, repositorystructuur. Startpunt voor wie nieuw is.
- `docs/` – `opdracht.md` (volledige opdrachtomschrijving; bron van waarheid voor vereisten) en `begrippen.md` (begrippenlijst, alfabetisch, met ankers, gebruikt door bijna alle documenten; link ernaar met `begrippen.md#begrip` en voeg nieuwe vaktermen hier toe in plaats van ze telkens opnieuw uit te leggen).
- `organisatie/` – projectsturing: projectplan, conceptnota, **leaderboard** (oorspronkelijke hoofdtaak: live scoreboard, privacytoestemming — **de Python-leaderboard is DEPRECATED en vervangen door het [LAN-portaal](https://github.com/kyell182/lan-portaal)** van Kyell), stakeholderregister, RACI-matrix, risicoanalyse, `bevraging-microsoft-forms.md`, `logboek.md` (tabel Datum, Type, Onderwerp, Beschrijving, Eigenaar; types: Beslissing, Actie, Test, Probleem, Incident, Evaluatie) en `todo.md` (afvinkbare checklist per fase, gekoppeld aan gates en weken). Door het team zelf onderhouden.
- `activiteiten/` – bijdragen aan de LAN-party: `concepten.md` (eerste ideeën en taakverdeling), `layout-lan-party.pdf` (zaalindeling Stuvo), `vr-pico4/vr-setup-concept.md` (Pico 4 / Quake3Quest) en `retropie/` (installatiehandleiding arcadekast; `retropie/assets/` met afbeeldingen). `activiteiten/retropie/credentials.md` is gitignored en mag nooit gecommit worden.
- `netwerk/` – het technische ontwerp. Modules die naar elkaar verwijzen:
  - `architectuur.md` (1): pfSense → core switch; VLAN 10 Management `10.10.10.0/24`, VLAN 20 Core Services `10.10.20.0/24`, VLAN 30 Gamers `10.10.30.0/22`; stroomberekening (max. 5–6 pc's per 16A-groep).
  - `monitoring-stack.md` (2): Telegraf (SNMP) → InfluxDB → Grafana. De uitvoering staat in `monitoring/`.
  - `server-services.md` (3): LanCache in Docker, DNS via pfSense/Unbound.
  - `overzicht.md` – samenvatting van module 1–3 met verduidelijkte schema's en openstaande punten; houd synchroon met de modules.
  - `schaalbaar-ontwerp.md` – voorstel met identieke "blokken" (VLAN + `/24` per 192 pc's) zodat het ontwerp van 100 tot 10 000 deelnemers schaalt; vervangt voorgesteld het enkele VLAN 30 uit module 1. Nog niet goedgekeurd.
  - `lan-70-opstelling.md` – netwerkopstelling voor een LAN van 70 (tier S, 1 blok), geschreven voor de **studentenvereniging**; gebruikt het schaalbare ontwerp.
- `draaiboek/` – herbruikbaar draaiboek voor **VIVES zelf** voor latere LAN's, per fase genummerd (`00-overzicht` met rollen, gates en tijdlijn, tot `05-bijlagen` met sjablonen). Pas het aan na elke evaluatie. `00-overzicht.md` is het startpunt.
- `monitoring/` – de enige map met code: Docker Compose voor de TIG-stack (Telegraf, InfluxDB, Grafana) met Telegraf-config en een voorgeprovisioneerd Grafana-dashboard. Start met `cd monitoring && cp .env.example .env && docker compose up -d`; `monitoring/lan-70/` bevat een variant met ingevulde `.env` voor de LAN van 70 (`include` van de gedeelde Compose-file). Apparaten staan in `SNMP_APPARATEN` in `.env`; Grafana-alarmen in `grafana/provisioning/alerting/alarmen.yml`. Geheimen staan alleen in `.env` (gitignored). Controleer wijzigingen met `docker compose --env-file <env> config --quiet`. `HANDLEIDING.md` is voor beginners, `README.md` is de naslag.
Wijzig je het IP-plan, de VLANs of de services in één module van `netwerk/`, controleer dan de andere modules en `netwerk/lan-70-opstelling.md`. Voeg je een map toe, verplaats of hernoem je een bestand, werk dan deze sectie en de "Repositorystructuur" in `README.md` bij, en controleer de relatieve links (ook de ankers naar `docs/begrippen.md`).

## Projectregels voor documenten

- **Go/no-go-gates** (Concept, Locatie, Techniek, Communicatie, Uitvoering): zonder formeel akkoord geen verbinding met het campusnetwerk en geen communicatie als officieel evenement.
- Geen eigen DHCP/router/NAT/access point zonder expliciete toestemming van IT; uplink en diensten komen van IT.
- Caching (LANCache) alleen voor toegelaten platformen; geen illegale gamebestanden; deelnemersverkeer niet inhoudelijk inspecteren.
- Geen geheimen, betalings- of gezondheidsgegevens in de repo.
- Nieuwe beslissingen, tests en incidenten komen in `organisatie/logboek.md`; vink afgewerkte punten af in `organisatie/todo.md` en de README-checklists.

## Conventies

- Commitberichten volgen conventional commits (`refactor:`, `docs:`, …) in het Engels, zoals de bestaande historie.
- Nieuwe schema's zijn Mermaid in Markdown, geen losse afbeeldingen.
- Links tussen documenten zijn relatief. Verplaats je bestanden, herbereken dan alle links die ernaar verwijzen.
