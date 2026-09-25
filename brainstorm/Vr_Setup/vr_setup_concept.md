## Concept — Pico 4 VR-LAN + lokale casting

### Doel

We willen onderzoeken of we tijdens de LAN-party meerdere **Pico 4-headsets** rechtstreeks met elkaar kunnen laten spelen via een lokaal netwerk, zonder dat voor de VR-game een gaming-pc nodig is.

De game **Quake3Quest** draait rechtstreeks op de Pico 4. De Pico's worden daarom zelf als gameclients gebruikt.

Daarnaast willen we onderzoeken of het beeld van de Pico 4 tijdens het spelen lokaal kan worden gecast naar een centrale mini-pc. Deze mini-pc kan de beelden eventueel met OBS combineren en weergeven op een TV of beamer.

> **Belangrijk:** dit is voorlopig een technisch concept en moet in een proefopstelling worden gevalideerd. Vooral de gelijktijdige casting van meerdere Pico 4-headsets moet worden getest op netwerkbelasting, stabiliteit en prestaties.

### Voorgestelde opstelling

```text
                         GEEN INTERNET
                              X
                              │
                       ┌──────┴──────┐
                       │    ROUTER    │
                       │     DHCP     │
                       └──────┬───────┘
                              │
             ┌────────────────┼────────────────┐
             │                │                │
          Pico 4 #1        Pico 4 #2       Pico 4 #3 ...
             │                │                │
             └────────────────┼────────────────┘
                              │
                         Lokaal LAN
                              │
                       ┌──────┴───────┐
                       │   Mini-PC    │
                       │ OBS / beeld  │
                       └──────┬───────┘
                              │
                              ▼
                         TV / Beamer
```

Bij een grotere testopstelling kan een aparte beheerde switch worden gebruikt:

```text
Pico 4 #1 ─┐
Pico 4 #2 ─┤
Pico 4 #3 ─┤
Pico 4 #4 ─┤
Pico 4 #5 ─┤
Pico 4 #6 ─┼── Wi-Fi / LAN ── Router/Switch ── Mini-PC ── TV/Beamer
Pico 4 #7 ─┤
Pico 4 #8 ─┘
```

### Werking

1. De router vormt een volledig geïsoleerd testnetwerk.
2. De router deelt lokale IP-adressen uit via DHCP.
3. De Pico 4-headsets verbinden met hetzelfde lokale netwerk.
4. Quake3Quest draait rechtstreeks op iedere Pico 4.
5. De multiplayercommunicatie verloopt waar mogelijk rechtstreeks via het lokale netwerk.
6. Internet is tijdens de technische proef niet noodzakelijk wanneer de game en benodigde bestanden al lokaal beschikbaar zijn.
7. Het beeld van een Pico 4 kan eventueel via de beschikbare castingfunctie naar een lokaal systeem worden gestuurd.
8. De centrale mini-pc ontvangt de castbeelden en kan ze met OBS combineren.
9. Het gecombineerde beeld kan op een TV of beamer worden weergegeven.

### Belangrijk technisch aandachtspunt: casting

Het grootste aandachtspunt is niet het draaien van Quake3Quest zelf, maar het **gelijktijdig streamen/casten van meerdere Pico 4-headsets**.

Daarom wordt dit stapsgewijs getest:

| Test   | Aantal Pico 4 | Doel                                  |
| ------ | ------------: | ------------------------------------- |
| Test 1 |             1 | Game + casting controleren            |
| Test 2 |             2 | Multiplayer + casting controleren     |
| Test 3 |             4 | Netwerkbelasting en stabiliteit meten |
| Test 4 |             8 | Volledige beoogde opstelling testen   |

Tijdens elke test worden minimaal gemeten:

* netwerkverkeer;
* latency;
* packet loss;
* stabiliteit van de multiplayer;
* FPS/ervaring op de Pico 4;
* stabiliteit van de casting;
* CPU/RAM/netwerkbelasting van de mini-pc;
* eventuele vertraging tussen de Pico 4 en het publieke scherm.

### Waarom een geïsoleerd netwerk?

De eerste testen worden uitgevoerd op een **eigen, niet met internet verbonden router/switch**.

```text
Campusnetwerk
      │
      X  ← NIET VERBONDEN
      │
Eigen testnetwerk
      │
 ┌────┴─────┐
 │ Router   │
 │ DHCP     │
 └────┬─────┘
      │
 Pico's + mini-PC
```

Hierdoor kunnen DHCP, lokale multiplayer en netwerkstoringen veilig worden getest zonder invloed op het campusnetwerk.

Dit sluit aan bij de projectvereiste dat een eigen DHCP-server, router of NAT **niet zonder expliciete toestemming op het campusnetwerk mag worden aangesloten**.

### Mogelijke uitbreiding

Indien de casting van alle acht Pico 4-headsets te veel netwerkverkeer veroorzaakt, kan een alternatief worden onderzocht waarbij slechts één of enkele Pico's tegelijk naar het publieke scherm worden gecast.

Een andere mogelijkheid is om alleen tijdens bepaalde momenten een spelerbeeld te tonen, terwijl alle Pico's wel lokaal blijven deelnemen aan de multiplayer.

### Voorlopige hypothese

Omdat Quake3Quest rechtstreeks op de Pico 4 draait, zijn er geen acht gaming-pc's nodig. De belangrijkste technische uitdaging wordt daarom verwacht bij het **lokale netwerk en de gelijktijdige casting**, niet bij het uitvoeren van de game op externe gaming-pc's.

De definitieve keuze voor de castingoplossing wordt pas gemaakt nadat de proefopstelling met meerdere Pico 4-headsets succesvol is getest.
