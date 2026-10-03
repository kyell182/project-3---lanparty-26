# Begrippenlijst

Uitleg van de vaktermen in de netwerkdocumenten, alfabetisch. Elk begrip heeft een korte uitleg en wat het in dit project betekent. Gebruikt in o.a. [SCHAALBAAR_ONTWERP.md](../netwerkontwerp/SCHAALBAAR_ONTWERP.md).

## .env-bestand

Een tekstbestand met de instellingen en wachtwoorden die [Docker Compose](#docker-compose) bij het starten leest. Elke regel heeft de vorm `NAAM=waarde`, zonder spaties en zonder aanhalingstekens. Het bestand bevat geheimen en staat daarom nooit in git.

## Access-switch

Een switch waar eindapparaten (pc's) rechtstreeks op aangesloten worden. Hij vormt de onderste laag van het netwerk en heeft een [uplink](#uplink) naar de [core-switch](#core-switch).

**In dit project:** een [blok](#blok) bestaat uit 4 access-switches van 48 poorten.

## ARP

Het protocol waarmee een apparaat het MAC-adres bij een IP-adres opvraagt. Dit gebeurt met een broadcast: de vraag gaat naar iedereen in het [broadcastdomein](#broadcastdomein).

## Bandbreedte

De hoeveelheid data die per seconde door een verbinding kan, in bits per seconde. 1 Gbps (gigabit per seconde) is theoretisch ongeveer 125 MB/s.

## Blok

Een eigen term van dit project: de vaste bouwsteen van het gamernetwerk. Eén blok is 192 pc's, met een eigen [VLAN](#vlan), een eigen `/24`-[subnet](#subnet) en eigen [access-switches](#access-switch). Alle blokken zijn identiek.

## Bottleneck

Het onderdeel dat de totale snelheid beperkt, zoals een [uplink](#uplink) die kleiner is dan het verkeer dat erover moet. Het hele systeem is zo snel als zijn zwakste schakel.

## BPDU Guard

Een beveiliging op switchpoorten naar eindgebruikers. Komt er op zo'n poort een [STP](#rstp)-bericht (BPDU) binnen, dan is er een switch aangesloten die daar niet hoort. De poort wordt dan automatisch uitgeschakeld. Zo voorkom je dat een deelnemer met een eigen switch een [loop](#switching-loop) veroorzaakt.

## Broadcastdomein

Alle apparaten die elkaars broadcast-berichten ontvangen (bijvoorbeeld [ARP](#arp) en [DHCP](#dhcp)-discover). Een broadcastdomein stopt bij een router. Hoe groter het domein, hoe meer ruis, en hoe meer apparaten een storing treft.

**In dit project:** elk [VLAN](#vlan) is één broadcastdomein. Daarom krijgt elk [blok](#blok) een eigen VLAN.

## Cache hit en cache miss

Bij een **hit** staat het gevraagde bestand al in de [cache](#lancache) en wordt het lokaal geleverd. Bij een **miss** staat het er nog niet in: de cache haalt het eerst van het internet en bewaart het.

## CIDR

De notatie `/24` achter een IP-adres. Het getal zegt hoeveel bits bij het netwerkdeel horen. De rest zijn hostbits. Aantal bruikbare hosts = `2^(hostbits) - 2`.

| Notatie | Hostbits | Bruikbare hosts |
| :-- | :-- | :-- |
| `/24` | 8 | 254 |
| `/23` | 9 | 510 |
| `/22` | 10 | 1 022 |
| `/16` | 16 | 65 534 |

## Collector

Een programma dat metingen verzamelt en doorstuurt. In dit project is dat **Telegraf**: het haalt via [SNMP](#snmp) gegevens op van de switches en schrijft ze naar [InfluxDB](#influxdb).

## Core-switch

De centrale switch waar alle [blokken](#blok) en servers op aansluiten. In dit ontwerp is dat een [L3-switch](#l3-switch), zodat hij ook de [routering](#routering) tussen de VLANs doet.

## DHCP

Het protocol waarmee apparaten automatisch een IP-adres, [gateway](#gateway) en DNS-server krijgen. Een client stuurt daarvoor een broadcast (DHCP-discover).

## DHCP-relay

Een functie op de [gateway](#gateway) die DHCP-broadcasts doorstuurt als gewoon verkeer naar een DHCP-server in een ander [subnet](#subnet). Op Cisco heet dit `ip helper-address`. Zo hoeft er niet in elk blok een eigen DHCP-server te staan.

## DHCP-scope

Het adresbereik dat een DHCP-server voor één subnet mag uitdelen, bijvoorbeeld `10.30.1.10` tot `10.30.1.250` voor blok 1.

## DHCP snooping

Een beveiliging op een managed switch. De switch kijkt naar al het DHCP-verkeer. Alleen poorten die als **trusted** zijn ingesteld, mogen DHCP-aanbiedingen versturen. Op alle andere poorten (**untrusted**) worden ze weggegooid. Zie ook [rogue DHCP-server](#rogue-dhcp-server).

## DNS-override

Een DNS-instelling die een bepaalde naam naar een zelfgekozen IP-adres laat wijzen. In dit project laat pfSense game-domeinen (zoals `steampowered.com`) naar de [LanCache](#lancache) wijzen in plaats van naar het internet. Haal je de override weg, dan gaan clients weer rechtstreeks naar het internet. Dat is de fallback. In module 3 heet dit **DNS Redirection**.

## Docker Compose

Een hulpmiddel dat meerdere programma's (containers) tegelijk start vanuit één bestand, met één commando: `docker compose up -d`. Het leest daarbij de instellingen uit het [.env-bestand](#env-bestand).

## Docker-host

Een server waarop Docker-containers draaien. Een container is een afgeschermd pakketje software met alles wat het nodig heeft, zodat je het overal op dezelfde manier kunt starten. In dit project draaien LanCache, game servers en monitoring als containers op zo'n host.

## Downsampling

Oude metingen samenvatten, bijvoorbeeld van elke 10 seconden naar één gemiddelde per minuut. Zo blijft de database klein en kun je toch lang terugkijken.

## Gateway

Het IP-adres waar een apparaat verkeer naartoe stuurt dat buiten zijn eigen [subnet](#subnet) moet. Meestal het eerste adres, bijvoorbeeld `10.30.1.1` voor blok 1. Dat adres staat op de [core-switch](#core-switch).

## Grafana

Software om metingen in grafieken en dashboards te tonen. Het leest uit [InfluxDB](#influxdb).

## InfluxDB

Een database voor tijdreeksen: metingen met een tijdstip, zoals "bytes door poort 3 om 14:02:10".

## IP-adres

Het nummer waarmee een apparaat in een netwerk gevonden wordt, bijvoorbeeld `10.10.10.2`. Het is te vergelijken met een huisnummer. Het hoort bij een [subnet](#subnet).

## L3-switch

Een switch die ook kan [routeren](#routering) tussen VLANs, in hardware. Daardoor is hij veel sneller dan een firewall of router die dit in software doet. Zie [laag 2 en laag 3](#laag-2-en-laag-3).

## Laag 2 en laag 3

Lagen uit het OSI-model. **Laag 2** schakelt op MAC-adres (gewone switch). **Laag 3** werkt op IP-adres en routeert tussen netwerken (router, [L3-switch](#l3-switch)).

## LACP

Link Aggregation Control Protocol (802.3ad). Bundelt meerdere fysieke kabels tot één logische verbinding, voor meer [bandbreedte](#bandbreedte) en als reserve als één kabel uitvalt. Eén enkele download blijft wel beperkt tot de snelheid van één kabel, want de verdeling gebeurt per verbinding.

## LanCache

Een server die game-downloads (Steam, Epic, enz.) lokaal bewaart. De eerste client haalt het bestand van het internet ([cache miss](#cache-hit-en-cache-miss)), de volgende krijgen het lokaal ([cache hit](#cache-hit-en-cache-miss)). Dat spaart internetverkeer. Clients worden ernaartoe gestuurd via een [DNS-override](#dns-override).

## NAT

Network Address Translation. Een router vervangt het interne IP-adres van een pakket door zijn eigen publieke adres, zodat veel interne apparaten één uitgaand adres delen.

## NVMe-ssd

Een snelle schijf die via PCIe communiceert, in plaats van via SATA. Een NVMe-ssd verwerkt veel meer opdrachten tegelijk en haalt GB/s. Daardoor kan de [LanCache](#lancache) meerdere gelijktijdige 1 Gbps-downloads voeden zonder dat de schijf de [bottleneck](#bottleneck) wordt.

## pfSense

Een firewall- en routerbesturingssysteem. In dit project zit het aan de rand van het netwerk: het doet [NAT](#nat), [QoS](#qos) en de [DNS-override](#dns-override).

## Polling

Op vaste tijden een apparaat bevragen. De [collector](#collector) vraagt bijvoorbeeld elke 10 seconden via [SNMP](#snmp) de tellers van een switch op.

## QoS

Quality of Service. Verkeer in prioriteitsklassen verdelen, zodat gevoelig verkeer (ping, gaming) voorrang krijgt op grote downloads.

## Queues

De wachtrijen waarin [traffic shaping](#traffic-shaping) het verkeer verdeelt. In module 3 zijn dat er drie:

- **Realtime queue:** hoogste prioriteit, voor ping (ICMP) en UDP-gameverkeer.
- **Default queue:** normale prioriteit, voor gewoon webverkeer (HTTP en HTTPS).
- **Bulk queue:** laagste prioriteit, voor grote downloads en verkeer dat niet gecachet kan worden. Krijgt een harde bandbreedtelimiet per IP of subnet.

## Redundantie

Reserveonderdelen voor het geval iets uitvalt, bijvoorbeeld twee [core-switches](#core-switch) in plaats van één.

## Rogue DHCP-server

Een DHCP-server die er niet hoort, bijvoorbeeld de thuisrouter van een deelnemer. Clients die van hem een adres krijgen, raken hun verbinding kwijt. [DHCP snooping](#dhcp-snooping) blokkeert dit.

## Routering

Verkeer doorsturen van het ene [subnet](#subnet) naar het andere, op basis van IP-adressen. Zonder routering kunnen twee VLANs niet met elkaar praten.

## RSTP

Rapid Spanning Tree Protocol (802.1w). Het schakelt redundante verbindingen tussen switches zo uit dat er geen [loop](#switching-loop) ontstaat, en herstelt na een wijziging binnen ongeveer een seconde. Op poorten naar gamers wordt **Edge Port** (PortFast) ingesteld zodat de poort meteen werkt.

## SNMP

Simple Network Management Protocol. Een standaardprotocol waarmee je tellers van switches opvraagt, zoals verkeer per poort, foutenaantallen en CPU-belasting.

## SNMP-community

Een soort wachtwoord voor [SNMP](#snmp). Een apparaat geeft alleen zijn metingen als de vraag dezelfde community meestuurt. De standaardwaarde `public` kent iedereen, dus kies een eigen, willekeurige waarde. Stel hem in als alleen-lezen.

## Stroomgroep

Een elektrische groep (zekering) in een gebouw. Een Belgische groep van 16 A bij 230 V levert 3 680 W. Bij 80% belasting (2 944 W) en 500 W per pc zijn dat maximaal 5 pc's per groep.

## Subnet

Een deel van het IP-adresbereik dat één netwerk vormt, genoteerd met [CIDR](#cidr). Een [VLAN](#vlan) hoort meestal bij precies één subnet.

## Switching loop

Een kabel die een kring vormt tussen switchpoorten. Broadcastberichten blijven eindeloos rondgaan (broadcast storm) en leggen de switches plat. [RSTP](#rstp) en [BPDU Guard](#bpdu-guard) voorkomen dit.

## Tier

Een eigen term van dit project: een grootteklasse van het evenement. **S** is tot 100 deelnemers, **M** tot 1 000 en **L** tot 10 000.

## Token

Een lange, geheime tekenreeks waarmee een programma bij een ander programma mag, vergelijkbaar met een wachtwoord voor programma's. In deze stack gebruiken Telegraf en Grafana het token om bij [InfluxDB](#influxdb) te komen.

## Traffic shaping

Het verkeer op de firewall verdelen over [queues](#queues) met verschillende prioriteit. Zo houden spelers een lage ping, ook als anderen zwaar downloaden. Dit is de uitvoering van [QoS](#qos) in pfSense.

## Trusted en untrusted

Instelling van een switchpoort voor [DHCP snooping](#dhcp-snooping). Een **trusted** poort mag DHCP-aanbiedingen versturen (de uplink naar de officiële DHCP-server). Op een **untrusted** poort, zoals elke gamerpoort, worden ze door de switch weggegooid.

## Uplink

De verbinding van een switch naar een hogere laag in het netwerk, of naar het internet. Een te kleine uplink is vaak de [bottleneck](#bottleneck).

## VLAN

Virtual LAN. Op één fysieke switch maak je meerdere logische netwerken, elk met een eigen [broadcastdomein](#broadcastdomein). Een VLAN heeft een nummer (1–4094). Apparaten in verschillende VLANs kunnen alleen via [routering](#routering) met elkaar praten.

**In dit project:** VLAN 10 is Management, VLAN 20 is Core Services, en elk [blok](#blok) krijgt VLAN `100 + n`.
