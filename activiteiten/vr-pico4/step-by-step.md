# Step-by-step — VR-setup Quake3Quest voor de LAN-party

> Vervolging op [vr-setup-concept.md](./vr-setup-concept.md).
> **Wijziging t.o.v. concept:** géén aparte mini-PC. In plaats daarvan draait een **VM in de Proxmox-cluster "Smith"** als dedicated Quake3-server (ioquake3). Casting wordt rechtstreeks van de Pico 4 naar TV/Chromecast gedaan (zie stap 7).

## Netwerktopologie

```text
LAN-party netwerk (geen internet nodig)
  Router/switch + DHCP
     │
     ├── Pico 4 #1 … Pico 4 #8   (Wi-Fi)
     │        └── Quake3Quest (standalone, draait op de headset)
     │
     └── VM nx-g03-lanparty-vr-01 (Proxmox Smith, gekabeld)
              └── ioquake3 dedicated server, UDP 27960
              └── (optioneel) casting-ontvanger/OBS — alleen mits GPU-toegewezen, zie stap 7
```

**Belangrijkst netwerkpunt:** de VM zit in het campus/Proxmox-netwerk en de Pico's op het LAN-party-netwerk. Er moet een goedgekeurd netwerkpad tussen beide zijn (zie stap 1). Is dat niet mogelijk, dan is de VM bereikbaar via een extra interface/segment op het LAN-party-netwerk — dit is een **change request**, niet zelfstandig uit te voeren.

---

## Stap 1 — Toestemmingen en change request (week vóór opbouw)

1. Check de go/no-go-gates (techniek) in de projectfiche 03-lan-party.
2. Check je Proxmox-scope: pool, toegewezen VMID-range, beschikbare bridge/VLAN (zie `docs/02-toegang-en-accounts.md` en `docs/04-smith-proxmox.md`).
3. Dien een **change request** in voor:
   - het netwerkpad tussen het LAN-party-netwerk en de bridge/VLAN van de VM;
   - eventueel een tweede NIC voor de VM op het LAN-party-segment;
   - firewallregels: UDP 27960 van LAN-party-subnet → VM (en eventueel UDP 27961 voor VoIP/geluid).
4. Reserveer een statisch IP of DNS-naam voor de VM, bijv. `10.x.x.20` / `q3vr.lanparty.local`.
5. Documenteer in het netwerkplan (`docs/05-netwerkplan.md`): bron, bestemming, protocol, poort, eigenaar.

**Stop-criterium:** geen akkoord van IT → geen VM met verbinding op het LAN-party-netwerk. Fallback: één Pico draait listen-server (zie stap 6, alternatief B).

## Stap 2 — VM aanmaken in Proxmox (Smith)

Conventie: `nx-g03-lanparty-vr-01`, VMID uit de **toegewezen range** (vraag het exacte nummer aan de docent; geen VMID's buiten de range).

Via de **web-GUI** (https://<proxmox-node>/:8006, inloggen met eigen account):

1. Links: **Datacenter** → **Create** (of jouw pool → Create).
2. Tab **General**:
   - **VM ID**: uit de toegewezen range
   - **Name**: `nx-g03-lanparty-vr-01`
3. Tab **OS**:
   - **Type**: Linux
   - **Version**: Debian (12)
   - **Storage**: door docent toegestane storage
   - **CD/DVD**: "None" of de Debian 12 ISO als die al op de storage staat; anders "Preconfigure: Use cloud-init" en een eigen ISO later
4. Tab **System**:
   - vink **Cloud-Init** aan (beheer via cloud-init, geen snowflake)
   - **Machine**: q35
   - **BIOS**: SeaBIOS
5. Tab **CPU**: 2 vCPU's, Type: host. Geen overcommit aannemen zonder bevestiging.
6. Tab **Memory**: 2048 MB. **Geen ballooning** als het niet door de docent is bevestigd.
7. Tab **Disk**: 16 GB, bus virtio, storage = toegestane storage.
8. Tab **Network**:
   - **Bridge**: door docent toegewezen bridge
   - **Firewall**: aan (hostfirewall is de standaard; de toegestane regels uit stap 1)
9. Klik **Create**.

Of via **CLI** (Datacenter → Console), ter verwerking/documentatie:

```bash
qm create 2501 --name nx-g03-lanparty-vr-01 \
  --memory 2048 --cores 2 --cpu type=host \
  --net0 virtio,bridge=vmbr1,firewall=1 \
  --scsi0 <storage>:16,ssd=1 \
  --agent enabled=1 \
  --ostype l26
qm set 2501 --ide2 <storage>:cloudinit
```

10. Sluit de VM aan bij de groeps**pool** (Datacenter → Pools → Pool → Add → Virtual Machine).
11. Vul het resourcebudget-anpasveld in (`docs/04-smith-proxmox.md`): eigenaar, functie, resourceprofiel, netwerkpad, backupklasse, verwijderbesluit.

## Stap 3 — Gast-OS opzetten

1. Start de VM vanuit de GUI (of `qm start 2501`).
2. Via de **console** (GUI → Console) of SSH: Debian 12 installeren (of cloud-init user/data vóór eerste start instellen).
3. Maak een persoonlijk sudo-gebruiker aan, schakel root-login af, zet SSH-key-based login.
4. Werk de VM door: `apt update && apt upgrade -y && apt install -y ufw unattended-upgrades`
5. Hostfirewall (ufw):

```bash
ufw default deny incoming
ufw default allow outgoing
ufw allow from <LAN-party-subnet> proto udp to any port 27960
ufw allow from <beheer-subnet> proto tcp to any port 22
ufw enable
```

6. Zet een statisch IP of DHCP-reservering (afspraken uit stap 1) in `/etc/network/interfaces` of netplan; controleer met `ip addr`.
7. **Acceptatietest:** vanaf een testapparaat in het LAN-party-netwerk: `nc -zvu <vm-ip> 27960` (mis nu, moet verbinding proeven na stap 4) en vanaf het beheernetwerk: toegestaan/niet-toegestaan pad testen volgens `docs/03-netwerk-en-firewall.md`.

## Stap 4 — ioquake3 dedicated server installeren

1. Op de VM (als normaal gebruiker):

```bash
sudo apt install -y ioquake3
```

2. **Gamebestanden (legaal!):** de `.pk3`-bestanden van Quake III Arena komen uit jouw **legaal aangekochte** copy (Steam/Epic). Kopieer de `id1/`-pakketten (bijv. `pak0.pk3`…`pak4.pk3`, `missionpack`) naar `/usr/share/ioquake3/baseq3/`. De gratis ioquake3-engine levert géén content.
3. Maak `~/.quake3/ioquake3/baseq3/server.cfg` (of `/usr/share/ioquake3/baseq3/` als system-wijd):

```text
set sv_hostname "LAN Party Q3 VR Server"
set maxclients "16"
set server_motd0 "LAN-party server — goede spelletjes!"
set g_password ""
set sv_wwwDownload "0"
map q3dm1
```

4. Maak een **systemd-service** zodat de server na reboot draait:

```ini
# /etc/systemd/system/quake3server.service
[Unit]
Description=ioquake3 dedicated server
After=network-online.target

[Service]
User=q3vr
WorkingDirectory=/usr/share/ioquake3
ExecStart=/usr/games/ioquake3 +set dedicated 1 +exec server.cfg
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now quake3server
```

5. **Verificatie:** `journalctl -u quake3server -f` toont "listening on ... 27960". Vanuit een apparaat in het LAN-party-netwerk: `nc -zvu <vm-ip> 27960` → open.

## Stap 5 — Quake3Quest installeren op de Pico 4

Quake3Quest staat **niet** in de reguliere Pico Store → sideloading is nodig.

Per Pico 4:

1. **SideQuest (PC-app)** downloaden en installeren op een beheer-PC met internet (bijv. een laptop van de crew, buiten het LAN-party-netwerk): <https://sidequestvr.com> — app "Quake3Quest" / "Quake3Pico" (Pico-build). Alternatief: APK rechtstreeks van de project-releases.
2. Op de Pico 4: **Instellingen → Systeem → Gebruiker** → **Ontwikkelaarsmodus** aan.
3. Pico 4 via USB (of SideQuest over Wi-Fi) verbinden met de PC; in SideQuest het pakket **installeren op apparaat**.
4. App één keer openen (maakt mappen aan), afsluiten, opnieuw openen.
5. Kopieer de legaal aangekochte `.pk3`-bestanden (dezelfde als in stap 4.2) naar `/ioquake3quest/baseq3/` op de Pico 4 (via SideQuest file browser of USB). Zónder deze pakjes werkt de game onvolledig.
6. Test op één Pico: single-player map openen, controleren dat de game draait.
7. Herhaal per headset (×8). Voorziet de Pico's van een gelabeld Wi-Fi-netwerknaam zodat ze automatisch verbinden.

**Voorraad:** houd een USB-Stick/SD met de APK + pk3-bestanden als offline-installatieset bij de crew (moet wel licentie- conform blijven: alleen eigen legale copies).

## Stap 6 — Netwerk en multiplayer testen (oplopend)

Op het LAN-party-netwerk, Pico's via Wi-Fi aangesloten:

| Test | Opstelling | Doel |
|------|------------|------|
| T1 | 1 Pico + VM-server | Pico kan de VM-server bereiken via IP (Join → server toevoegen → `<vm-ip>`) |
| T2 | 2 Pico's + VM-server | Multiplayer via dedicated server |
| T3 | 4 Pico's + VM-server | Netwerkbelasting, latency, packet loss meten |
| T4 | 8 Pico's + VM-server | Volledige opstelling, stabiel over ≥30 min |

Per test meten: latency/packet loss (bijv. `mtr` of switch-counters), FPS-ervaring op de Pico, belasting VM (CPU/RAM via Proxmox GUI), stabiliteit van de matching.

**Alternatief B (fallback als VM niet bereikbaar is):** één Pico draait **listen-server** — Quake3Quest → Multiplayer → **Create** → "Pure server" op **NO** → Fight. Andere Pico's: Multiplayer → **Join** → "Server: Local". De VM is dan alleen voor monitoring/OBS.

## Stap 7 — Casting naar het publieke scherm

De oorspronkelijke mini-PC (OBS-combinatie) vervalt. Realistische opties voor de VM, in volgorde van voorkeur:

1. **Direct casten (aanbevolen):** Pico 4 heeft ingebouwd screen-mirroring → rechtstreeks naar smart-TV/Chromecast op het LAN-party-netwerk. Geen VM nodig; VM blijft dedicated-server-only. Voorbeeld-gebruiker: draaiende speler tonen via één headset die wordt gecast.
2. **VM met GPU (alleen met toestemming):** indien de Smith-cluster dit toestaat (change request + GPU-passthrough), kan OBS met een X/wayland-session in de VM draaien en het beeld op een TV weergeven. Realiteit: extra complexiteit, pas als optie 1 tekortschiet.
3. **Géén centraal scherm:** draai de activiteit puur op de headsets; VM draait alleen de server + monitoring.

Voor elke optie: eerst proeven in een testopstelling (zie concept: testmatrix 1→2→4→8), dan definitief vastleggen in het draaiboek.

## Stap 8 — Monitoring en backup

1. Koppel de VM aan de projectmonitoring (Grafana/Telegraf, zie `monitoring/` in de projectrepo): CPU, RAM, netwerkbinnenkomst, UDP-packets op 27960.
2. Melding voor diskgroei en langdurige hoge belasting (`docs/04-smith-proxmox.md`).
3. Backupklasse vastleggen en één **backup-test** uitvoeren (template: `docs/templates/backup-test-template.md`). Voor een LAN-party is een restore ≤ de doorlooptijd naar het evenement het streefniveau.

## Stap 9 — Draaiboek, opbouw en cleanup

1. Vul de VR-setup in het draaiboek (`draaiboek/02-opbouw.md`): wie schakelt de VM in (`systemctl status quake3server`), wie verdeelt de Pico's, wie doet de first-join test (T1) voor de eerste spelers.
2. Opbouwdag: VM vóór opening starten, T1 doen met één Pico, daarna spelers toe laten.
3. Afbrakedag (zie `docs/04-smith-proxmox.md`, verwijderbesluit):
   - VM stoppen, back-up waar nodig
   - VM **gecontroleerd verwijderen** na acceptatie van het project (GUI → VM → Remove, of `qm destroy 2501`)
   - Change request afsluiten, firewallregels laten verwijderen
   - Pico's resetten naar fabrieksinstellingen als ze niet van de groep blijven
4. Log alles in het incidentlog en de evaluatie; bewaar de testresultaten als bewijsstuk (cachebenchmark-analoog: de VR-benchmark met T1–T4-metingen).

## Open vragen / risico's

- **Netwerkpad VM ↔ LAN-party-netwerk** hangt af van het IT-akkoord; zonder dat valt terug op Alternatief B (listen-server op een Pico).
- **Legale content:** `.pk3`-bestanden alleen van legaal aangekochte Quake III Arena-copies; geen gedeelde/illegale bestanden verspreiden (projectscope "niet in scope").
- **Casting van 8 Pico's tegelijk** blijft een te-valideren hypothese; de VM draagt die last alleen als optie 2 kiest.
- VMID-range en exacte bridge/VLAN zijn per groep door de docent toe te kennen — invullen in deze doc vóór uitvoering.
