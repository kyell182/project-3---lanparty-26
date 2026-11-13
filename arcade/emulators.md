# Emulators op de arcadekast

Overzicht van alle systemen die op de arcade-pc in `~/RetroPie/roms/` staan, met de bestandsformaten, de zip-regel, of er een BIOS nodig is en de teststatus. De algemene uitleg over kopiëren en zip staat in [bestanden-kopieren.md](bestanden-kopieren.md).

> De kolommen "Formaten", "Zip" en "BIOS" komen uit de algemene RetroPie-kennis en zijn niet per systeem op de kast gecontroleerd. Waar iets onzeker is, staat "controleren". De kolommen "Core" en "Games" komen uit de inventaris van 2026-11-13 op de arcade-pc. Welke BIOS-bestanden je gebruikt en waar je ze vandaan haalt, is de verantwoordelijkheid van de gebruiker.

Inventaris opnieuw maken op de arcade-pc:

```bash
for d in ~/RetroPie/roms/*/; do echo "$(basename $d): $(find $d -type f | wc -l)"; done
ls /opt/retropie/libretrocores/
ls ~/RetroPie/BIOS/
```

## Legenda

- **Zip:** `ja` = mag in zip blijven (1 spel per zip), `nee` = uitpakken, `nooit uitpakken` = zip moet intact blijven.
- **Games:** aantal spelbestanden volgens extensie (gemeten op 2026-11-13). De mappen bevatten daarnaast veel afbeeldingen (`.png`), video's (`.mp4`) en savegames (`.srm`), die niet meetellen. `leeg` = geen bestanden, dus niets te testen.
- **Status:** `werkt`, `werkt niet`, `nog te testen`. Noteer bij `werkt niet` wat er mis is.

## Bevindingen (2026-11-13)

Gemeten via SSH op de arcade-pc.

- **PSX-BIOS ontbreekt:** er staat nergens een BIOS-bestand (`scph*`) op de pc. `lr-beetle-psx` start daardoor waarschijnlijk geen enkel PlayStation-spel. Het gaat om 54 spellen (50 `.chd`, 4 `.pbp`). Dit is het belangrijkste open punt.
- **Neo Geo is in orde:** `neogeo.zip` staat in `roms/neogeo/`, waar `lr-fbneo` hem verwacht.
- **`genesis` is een symlink naar `megadrive`:** er zijn dus geen dubbele spellen. Houd dit zo.
- **N64 werkt:** het laatst gestarte spel (Carmageddon 64, `lr-mupen64plus`) startte zonder fout.
- **Standaard cores:** nes `lr-fceumm`, snes `lr-snes9x`, gb en gbc `lr-gambatte`, gba `lr-mgba`, megadrive en gamegear `lr-genesis-plus-gx`, n64 `lr-mupen64plus`, psx `lr-beetle-psx`, pcengine `lr-beetle-pce-fast`, neogeo en fba `lr-fbneo`, mame-libretro `lr-mame2003`.
- **MAME:** alleen `lr-mame2003` is geïnstalleerd. De verzameling in `mame-libretro` moet bij die versie passen.
- **GBA-BIOS en PC Engine-cd-BIOS ontbreken:** geen probleem voor de huidige spellen (GBA-BIOS is optioneel, de PC Engine-map bevat alleen `.pce`-kaartjes).
- **Geen core voor MSX, ColecoVision en Channel F.** Die mappen zijn leeg.

Nog te testen: een spel starten per systeem. Alleen N64 is bevestigd.
## Consoles en handhelds met cartridges

| Systeem | Map | Core | Formaten | Zip | BIOS | Games | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NES | `nes` | `lr-fceumm`, `lr-nestopia` | `.nes` | ja | nee | 1804 `.nes` + 994 zip | nog te testen |
| Famicom Disk System | `fds` | `lr-fceumm` | `.fds` | ja | ja (`disksys.rom`) | leeg | – |
| SNES | `snes` | `lr-snes9x` | `.sfc`, `.smc` | ja | nee | 1246 zip + 282 `.smc` + 170 `.sfc` | nog te testen |
| Nintendo 64 | `n64` | `lr-mupen64plus`, `lr-parallel-n64` | `.z64`, `.n64`, `.v64` | controleren | nee | 77 `.n64` | werkt (Carmageddon 64 gestart zonder fout in het log) |
| Game Boy | `gb` | `lr-gambatte` | `.gb` | ja | nee | 3244 zip + 425 `.gb` | nog te testen |
| Game Boy Color | `gbc` | `lr-gambatte` | `.gbc` | ja | nee | 2017 zip + 56 `.gbc` | nog te testen |
| Game Boy Advance | `gba` | `lr-mgba`, `lr-vba-next` | `.gba` | ja | optioneel (`gba_bios.bin`), ontbreekt | 1070 zip | nog te testen |
| Master System | `mastersystem` | `lr-genesis-plus-gx` | `.sms` | ja | nee | leeg | – |
| SG-1000 | `sg-1000` | `lr-genesis-plus-gx` | `.sg` | ja | nee | leeg | – |
| Game Gear | `gamegear` | `lr-genesis-plus-gx` | `.gg` | ja | nee | 262 zip | nog te testen |
| Mega Drive (Europa, Japan) | `megadrive` | `lr-genesis-plus-gx`, `lr-picodrive` | `.md`, `.bin`, `.gen` | ja | nee | 907 zip + 306 `.bin` | nog te testen |
| Genesis (Noord-Amerika) | `genesis` | `lr-genesis-plus-gx`, `lr-picodrive` | `.md`, `.bin`, `.gen` | ja | nee | symlink naar `megadrive` | nog te testen |
| Sega 32X | `sega32x` | `lr-picodrive` | `.32x` | ja | nee | leeg | – |
| PC Engine | `pcengine` | `lr-beetle-pce-fast`, `lr-beetle-supergrafx` | `.pce` | ja | nee voor kaartjes, ja voor cd (`syscard3.pce`), ontbreekt | 69 `.pce` | nog te testen |
| Neo Geo Pocket | `ngp` | `lr-beetle-ngp` | `.ngp` | ja | nee | leeg | – |
| Neo Geo Pocket Color | `ngpc` | `lr-beetle-ngp` | `.ngc` | ja | nee | leeg | – |

## Schijf-systemen

| Systeem | Map | Core | Formaten | Zip | BIOS | Games | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PlayStation | `psx` | `lr-beetle-psx` | `.cue` met `.bin`, `.chd`, `.pbp`, `.m3u` | nee | ja, ontbreekt | 50 `.chd` + 4 `.pbp` | werkt waarschijnlijk niet: BIOS ontbreekt |
| Sega CD | `segacd` | `lr-genesis-plus-gx` | `.cue` met `.bin`, `.chd`, `.iso` | nee | ja (per regio) | leeg | – |

Alle bestanden van één schijf, zoals de `.cue` en de bijhorende `.bin`-bestanden, moeten samen in dezelfde map staan.

## Oudere consoles en computers

Alle systemen in deze tabel zijn leeg. De cores voor Atari, Lynx, Vectrex, Amstrad en ZX Spectrum zijn wel geïnstalleerd. MSX, ColecoVision en Channel F hebben nog geen core.

| Systeem | Map | Core | Formaten | Zip | BIOS | Games |
| --- | --- | --- | --- | --- | --- | --- |
| Atari 2600 | `atari2600` | `lr-stella2014` | `.a26`, `.bin` | ja | nee | leeg |
| Atari 5200 | `atari5200` | `lr-atari800` | `.a52`, `.bin` | ja | ja | leeg |
| Atari 7800 | `atari7800` | `lr-prosystem` | `.a78` | ja | optioneel | leeg |
| Atari 800 | `atari800` | `lr-atari800` | `.atr`, `.xex`, `.cas` | controleren | ja | leeg |
| Atari Lynx | `atarilynx` | `lr-handy` | `.lnx` | ja | ja (`lynxboot.img`) | leeg |
| ColecoVision | `coleco` | niet geïnstalleerd | `.col` | ja | ja (`colecovision.rom`) | leeg |
| Fairchild Channel F | `channelf` | niet geïnstalleerd | `.bin`, `.chf` | ja | ja | leeg |
| Vectrex | `vectrex` | `lr-vecx` | `.vec`, `.bin` | ja | nee | leeg |
| MSX | `msx` | niet geïnstalleerd | `.rom`, `.mx1`, `.mx2`, `.dsk` | ja | ja | leeg |
| Amstrad CPC | `amstradcpc` | `lr-caprice32` | `.dsk`, `.cdt`, `.sna` | ja | controleren | leeg |
| ZX Spectrum | `zxspectrum` | `lr-fuse` | `.tzx`, `.tap`, `.z80`, `.sna` | ja | nee | leeg |

## Arcade

| Systeem | Map | Core | Formaten | Zip | BIOS | Games | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Arcade | `arcade` | `lr-fbneo`, `lr-mame2003` | `.zip` | nooit uitpakken | soms | leeg | – |
| FinalBurn Alpha | `fba` | `lr-fbneo` | `.zip` | nooit uitpakken | soms | 64 zip | nog te testen |
| MAME (libretro) | `mame-libretro` | `lr-mame2003` | `.zip` | nooit uitpakken | soms | 1509 zip | nog te testen |
| Neo Geo | `neogeo` | `lr-fbneo` | `.zip` | nooit uitpakken | ja (`neogeo.zip`), staat in `roms/neogeo/` | 148 zip | nog te testen |

Bij arcade-spellen moet de versie van de spelverzameling overeenkomen met de emulator. Meng daarom spellen van verschillende emulators niet in één map. De drie mappen `arcade`, `fba` en `mame-libretro` bevatten verschillende spelverzamelingen voor verschillende emulators.

## Een systeem werkt niet?

Doorloop de beslisboom in [bestanden-kopieren.md](bestanden-kopieren.md#een-emulator-werkt-niet) (juiste map, BIOS, emulator geïnstalleerd, logbestand) en noteer het resultaat in de kolom Status.
