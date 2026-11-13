# Arcadekast

Zijproject van de LAN-party: een minipc (Dell Optiplex 7010) ombouwen tot een arcadekast met RetroPie, als nevenactiviteit voor deelnemers die niet meespelen. Eigenaar: Kyell.

Het project hangt niet af van het netwerkontwerp of de monitoringstack en kan los van de rest van de repository worden uitgewerkt. Beslissingen en acties over de arcadekast staan, net als de rest van het project, in het gedeelde [logboek](../organisatie/logboek.md).

## Inhoud

| Bestand | Inhoud |
| --- | --- |
| [installatie-retropie.md](installatie-retropie.md) | Stap 1: Ubuntu + RetroPie op een pc |
| [bestanden-kopieren.md](bestanden-kopieren.md) | Stap 2: bestanden via `scp` op de arcade-pc zetten en reservekopieën maken, plus checklist voor emulators die niet werken |
| [scherm-en-autostart.md](scherm-en-autostart.md) | Autostart van EmulationStation en het schermscript (Dell verticaal, HP horizontaal) |
| [scripts/](scripts/) | Kopie van de scripts en autostart-bestanden van de arcade-pc |
| [emulators.md](emulators.md) | Overzicht van alle systemen op de kast: formaten, zip-regel, BIOS en teststatus |
| [controllers.md](controllers.md) | Stap 3: controllers mappen en het configuratiemenu afschermen |
| `credentials.md` | Inloggegevens van de arcade-pc. Staat in `.gitignore` en mag nooit gecommit worden |
| [assets/](assets/) | Afbeeldingen voor de handleiding |

## Opstelling

- **Pc:** Dell Optiplex 7010 met Ubuntu en RetroPie (Basic Install).
- **Kast:** fysieke arcadekast met een hub vooraan geïnstalleerd.
- **Controllers:** 8BitDo-controllers. Elke andere controller kan ook, mits correct gemapt.
- **Games:** ROM's en BIOS-bestanden zijn de verantwoordelijkheid van de gebruiker. Het project levert of documenteert ze niet.

## Status

Aanwezig op de LAN-party van 2026-10-26 en een succes.

### Werkt

- [x] RetroPie geïnstalleerd
- [x] Autostart van RetroPie
- [x] Script voor het scherm
- [x] Controllers
- [x] Het grootste deel van de games

### Nog te doen

- [ ] Alle systemen in [emulators.md](emulators.md) testen, de kolom Status invullen en wat niet werkt herstellen
- [ ] Oriëntatie van de gebruikersinterface bekijken
- [ ] Vaste knoppen van de kast installeren
- [ ] Arduino mini programmeren voor de besturing van de kast (handleiding volgt)
- [ ] Verhinderen dat deelnemers in het configuratiemenu belanden en zo de mapping van de besturing kwijtraken (menu vergrendelen of een vaste mapping afdwingen)
- [x] Handleiding van het schermscript en de autostart: [scherm-en-autostart.md](scherm-en-autostart.md)
- [ ] PSX-BIOS ontbreekt op de arcade-pc: PlayStation-spellen starten waarschijnlijk niet (zie [emulators.md](emulators.md))
- [ ] Installatiehandleiding controleren
- [ ] Nieuwe handleidingen ([bestanden-kopieren.md](bestanden-kopieren.md), [controllers.md](controllers.md)) testen op de echte kast en aanvullen waar nodig

### Open vragen

- Welke emulators werken niet, en waarom?
- Hoe blokkeren we het configuratiemenu voor deelnemers zonder dat wij er zelf niet meer in kunnen?
- Welke games mogen op een schoolevenement worden aangeboden? Wordt besproken met meneer Calleeuw; leg de beslissing daarna vast in het logboek.
