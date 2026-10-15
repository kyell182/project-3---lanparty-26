# Module 1: Netwerk Architectuur & Topologie

Dit document beschrijft de fysieke en logische inrichting van de netwerkinfrastructuur om een stabiele gaming-omgeving te garanderen.

## 1. Visuele Topologie (Mermaid)

```mermaid
graph TD
    %% Internet & Core Router
    WAN[🌐 VIVES Schoolnetwerk / Internet] -->|WAN Poort| Router[🔥 pfSense Firewall / Router]
    
    %% Trunk to Core Switch
    Router -->|Trunk Poort: Alle VLANs| CoreSwitch[🎛️ Core Managed Switch]
    
    %% VLAN Splitsingen
    CoreSwitch -->|Trunk / VLAN 20| ServerRack[🖥️ Server Rack / Docker Host]
    CoreSwitch -->|Access / VLAN 10| AdminPC[💻 Beheer / Crew PC]
    CoreSwitch -->|Trunk / VLAN 30| ClientSwitches[🔌 Deelnemers Switches]
    
    %% Servers detail
    subgraph VLAN 20: Core Services
        ServerRack --> LC[📦 LanCache Server]
        ServerRack --> GS[🎮 Dedicated Game Servers]
        ServerRack --> MS[📊 Grafana / InfluxDB Monitoring]
    end
    
    %% Clients detail
    subgraph VLAN 30: Deelnemers / Gamers
        ClientSwitches --> SwA[Switch A]
        ClientSwitches --> SwB[Switch B]
        SwA --> PC1[PC 1]
        SwA --> PC2[PC 2]
        SwB --> PC3[PC 3]
        SwB --> PC4[PC 4]
    end

    %% Styling
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px;
    classDef router fill:#ffcccc,stroke:#ff0000,stroke-width:2px;
    classDef server fill:#ccffcc,stroke:#00aa00,stroke-width:2px;
    class Router router;
    class LC,GS,MS server;
```

## 2. Logisch Ontwerp: VLAN & Subnetting

Om broadcast-domeinen te verkleinen en netwerkverkeer strikt te scheiden, hanteren we de volgende indeling:

| VLAN ID     | Netwerknaam      | IP-Range / Subnet | Doel                                                   |
| :---------- | :--------------- | :---------------- | :----------------------------------------------------- |
| **VLAN 10** | Management       | `10.10.10.0/24`   | Beheer van switches, routers en access points.         |
| **VLAN 20** | Core Services    | `10.10.20.0/24`   | Dedicated game servers, LanCache en monitoring host.   |
| **VLAN 30** | Gamers / Clients | `10.10.30.0/22`   | Subnet voor deelnemers (biedt ruimte aan ~1000 hosts). |

## 3. Capaciteitsberekening (Stroom & Netwerk)

### Netwerk Bandbreedte

* **Edge-poorten (Naar de gamer):** Elke pc krijgt een **1 Gbps Full-Duplex** verbinding.
* **Uplinks (Inter-switch trunks):** Minimale vereiste is **Link Aggregation (LACP)** met 2x 1 Gbps-lijnen, of bij voorkeur een dedicated **10 Gbps SFP+** uplink naar de Core Switch om bottlenecks te voorkomen bij gelijktijdige downloads.

### Stroomvoorziening (Lab-veiligheid)

Een gemiddelde gaming-pc verbruikt onder piekbelasting circa **500 Watt**.

* **Formule:** `Vermogen (W) = Spanning (V) × Stroom (A)`
* **Lab-groep:** Een standaard Belgische zekeringgroep levert `230V × 16A = 3.680 Watt`.
* **Veiligheidsmarge (80%):** Belast een groep tot maximaal `approx 2.944 Watt`.
* **Conclusie:** Plaats **maximaal 5 tot 6 gaming-pc's per fysieke stroomkring**. Verdeel de tafels bewust over verschillende wandcontactdozen (groepen) in het VIVES-lab.

```mermaid
graph LR
    subgraph Stroomverdeling Lab
        G1[🔌 Groep 1: 16A / 230V] -->|Max 5-6 PCs| T1[Tafel A]
        G2[🔌 Groep 2: 16A / 230V] -->|Max 5-6 PCs| T2[Tafel B]
        G3[🔌 Groep 3: 16A / 230V] -->|Gereserveerd| SR[Server Rack / Crew]
    end
```
