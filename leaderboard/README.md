# Leaderboard — LAN-Party 26

> ## ⚠️ DEPRECATED — vervangen door het LAN-portaal
> Dit Python-stdlib leaderboard wordt **niet meer gebruikt** voor de LAN-Party 26.
> **Kyell** heeft het uitgrown tot een volwaardig **LAN-portaal**:
> [**github.com/kyell182/lan-portaal**](https://github.com/kyell182/lan-portaal).
>
> Het portaal is volledig offline draaiend (Docker) en omvat naast het
> scoreboard ook toernooien met live brackets (knock-out, Swiss, poules, …),
> edities/events, zitplan, prijzen, Discord-meldingen en een PWA. Alleen admins
> melden aan; het publiek ziet alles live bijwerken — handig op een beamer.
>
> Deze code wordt hierbij **behouden ter referentie** (en voor de documentatie
> van de oorspronkelijke eisen); hij wordt niet meer onderhouden of uitgerold.

<details>
<summary>Originele documentatie (Python-leaderboard, ter referentie)</summary>

Live scoreboard voor de LAN-Party 26 (Stuvo). De **LAN Admin** voert scores in
via een webpagina; het groot scherm toont per-game top-10 én een globale
totaalstand (met de beste game per speler), en ververst zich zelf om de paar
seconden. De user interface van de leaderboard-pagina's is Engelstalig.

Bouwkost: **Jules** (back-up: Kyell) · [opdracht](../docs/opdracht.md) · [spec](../organisatie/leaderboard.md)

## Technische keus

- **Python 3.10+, uitsluitend stdlib** — geen pip-pakketten, geen database.
  Eén proces, één JSON-bestand: eenvoudig op te starten, af te sluiten en
  te wissen. (Keus tussen de drie opties uit [organisatie/leaderboard.md §4](../organisatie/leaderboard.md#4-mogelijke-technologie).)
- Data: `data/leaderboard.json` (lokaal, niet in git).
- Netwerk: server staat op **VLAN 20 (core services)** — bereikbaar voor de
  LAN Admin, niet voor het deelnemersnetwerk. Scherm en LAN Admin-pagina
  lopen dus over de interne lijn.

## Starten

```
cd leaderboard
py server.py                 # poort 8321
py server.py --port 9000     # andere poort
py server.py --wachtwoord "MijnWachtwoord"   # LAN Admin-wachtwoord (1×)
```

Bij de eerste start wordt een LAN Admin-wachtwoord gegenereerd (of met
`--wachtwoord` ingesteld) en opgeslagen in `config.json` — dat bestand is
git-geïnformeerd en **nooit in de repo**. Het wachtwoord verschijnt één keer
in de console.

| Rol | URL |
| --- | --- |
| Groot scherm | `http://<ip-leaderboard>:8321/` |
| Spelers: zelf Player-naam kiezen | `http://<ip-leaderboard>:8321/registreer` |
| LAN Admin: scores invoeren, beheren | `http://<ip-leaderboard>:8321/crew` |

Het scherm ververst zelf elke 3 seconden; de LAN Admin-pagina elke 5 seconden.

## Scoring (0–100 per invoer)

Per ingevoerde score kiest de LAN Admin een game én een speler (beide
dropdowns) en typt een score tussen **0 en 100**. Het is de **eigen
inschatting** van de crew — er wordt geen "ware" game-score genormaliseerd.

- **Totaalstand**: het totaal van een speler is de **som van alle ingevoerde
  0–100 scores** over alle games. Speelt een speler hetzelfde spel twee keer,
  dan telt dat beide mee.
- **Beste game**: op het scherm staat naast het totaal de **beste game** van
  de speler = de hoogste enkelvoudige 0–100 score over alle gespeelde games.
  Bij een gelijke score wint de game waarin de speler **meest scores ingav**.
- **Per game**: de top-10 per game is de som van de 0–100 scores in die game.

## Spelers en moderatie

- Een speler verschijnt automatisch bij de eerste score (LAN Admin kiest de
  speler uit een dropdown of voegt die toe) of registreert zich zelf via
  `/registreer`.
- Player-namen: 2–40 tekens, letters/cijfers en beperkte leestekens; de
  server weigert ongeldige namen.
- De LAN Admin kan op `/crew` **elke speler of game verwijderen** (met al
  haar/zijn scores) — de afhaak voor vals spelende of ongeschikte namen.
- **History (laatste 20)**: elke ingevoerde score staat in een log met de
  mogelijkheid om haar **te ongedoen** maken (score wordt afgetrokken, de
  historie-regel wordt verwijderd).
- Data bevat **alleen Player-namen**: geen echte namen, geen e-mail.

## Data wissen (privacy)

Bewaartermijn: **≤ 1 week na het event** (zie [todo.md §fase 3](../organisatie/todo.md)).
Twee manieren:

1. **Via de LAN Admin-pagina**: knop *Danger Zone → Wipe All Data*
   (dubbele bevestiging).
2. **Handmatig**: `data\leaderboard.json` (en `config.json`) van de
   machine verwijderen.

Daarna staat het systeem weer leeg, klaar voor het volgende event.

## Structuur

| Bestand | Functie |
| --- | --- |
| `opslag.py` | Datalaag: JSON-bestand, validatie, normalisatie, ranglijsten (threadveilig). |
| `server.py` | HTTP-laag: pagina's + JSON-API (stdlib `http.server`). |
| `static/scherm.html` | Groot-schermweergave (totaalstand met beste game + per-game top-10). |
| `static/crew.html` + `crew.js` | LAN Admin-ingang: scores, spelers, games, history/undo, reset. |
| `static/crew-login.html` | LAN Admin-wachtwoordformulier. |
| `static/registreer.html` | Spelers kiezen zelf een Player-naam. |
| `data/` | Lokaal JSON-bestand (git-geïnformeerd; te verwijderen). |
| `config.json` | LAN Admin-wachtwoord (git-geïnformeerd; te verwijderen). |

</details>
