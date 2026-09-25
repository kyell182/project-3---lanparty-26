# 🛠️ Module 3: Core Server Services & Optimalisatie

Dit document behandelt de softwarematige inrichting en netwerkaanpassingen om de LAN-party stabiel en performant te houden.

## 1. LanCache.net Werking

LanCache functioneert als een transparante HTTP proxy cache die specifiek is ontworpen voor game-distributieplatformen (Steam, Epic Games, Riot Games, Blizzard, Windows Update).

```mermaid
graph TD
    subgraph Internet
        Steam[☁️ Steam Content Servers]
    end

    subgraph LAN Infrastructuur (VIVES Lab)
        DNS[🔥 pfSense DNS / Unbound]
        LC[📦 LanCache Server / Docker]
        PC1[💻 Gamer PC 1]
        PC2[💻 Gamer PC 2]
    end

    %% Eerste Download Stroom
    PC1 -->|1. Vraagt game-update| DNS
    DNS -->|2. Intercepteert & Verwijst naar LanCache IP| PC1
    PC1 -->|3. Download verzoek| LC
    LC -->|4. Cache MISS: Haal op van internet| Steam
    Steam -->|5. Levert bestanden| LC
    LC -->|6. Slaat lokaal op + Pusht naar PC 1| PC1

    %% Tweede Download Stroom
    PC2 -->|7. Vraagt ZELFDE game-update| LC
    LC -->|8. Cache HIT: Lever direct uit NVMe/RAM op 1Gbps+| PC2
```

### Belangrijke LanCache Netwerkvereisten:
*   **DNS Redirection:** pfSense (Unbound DNS) moet zo geconfigureerd worden dat DNS-aanvragen voor bekende game-CDNs (zoals `*.steampowered.com`) niet naar het internet worden gestuurd, maar resolven naar het lokale IP-adres van de LanCache server.
*   **Hardware-advies:** De LanCache server vereist snelle opslag (**NVMe SSD's**) en voldoende RAM om de hoge doorvoersnelheid van meerdere gelijktijdige 1 Gbps client-downloads bij te kunnen houden.

## 2. Netwerkbeveiliging & Stabiliteit op de Switches

Om te voorkomen dat studenten (bewust of onbewust) de infrastructuur platleggen, moeten de managed switches geconfigureerd worden met de volgende protocollen:

### Spanning Tree Protocol (STP / RSTP)
*   **Risico:** Een gamer verbindt per ongeluk twee poorten van een switch met dezelfde ethernetkabel (switching loop). Dit veroorzaakt een broadcast storm die de switch CPU 100% belast en het netwerk crasht.
*   **Mitigatie:** Activeer **Rapid Spanning Tree Protocol (RSTP)** op alle switches. Schakel `Edge Port` (of `PortFast`) in op poorten naar eindgebruikers, gecombineerd met `BPDU Guard` om de poort direct uit te schakelen zodra er een ongewenste switch wordt gedetectecteerd.

### DHCP Snooping & Rogue DHCP Protection
*   **Risico:** Een deelnemer sluit een eigen thuisrouter aan op het netwerk. Deze router begint IP-adressen uit te delen in een foutieve range, waardoor gamers hun internet- en LAN-verbinding verliezen.
*   **Mitigatie:** Schakel **DHCP Snooping** in op alle switches. Markeer alléén de uplink-poort die naar de officiële pfSense-router leidt als **Trusted**. Alle overige poorten naar gamers worden gemarkeerd als **Untrusted**. DHCP-aanbiedingen (DHCPOFFER) van untrusted poorten worden direct door de switch gedropt.

## 3. Quality of Service (QoS) & Traffic Shaping op pfSense

Om te voorkomen dat een grote internetdownload (bijvoorbeeld een game die nog niet in de cache staat) de latency (ping) van actieve spelers verpest, richten we **Traffic Shaping** in op de pfSense-firewall via de *Wizard -> Multiple Lan/Wan*:

1.  **Realtime Queue (Hoogste Prioriteit):** ICMP (Ping) en bekende game-verkeer UDP-poorten.
2.  **Default Queue (Normale Prioriteit):** Standaard webverkeer (HTTP/HTTPS).
3.  **Bulk Queue (Laagste Prioriteit):** Grote downloads en netwerkverkeer dat niet gecached kan worden. Er wordt een harde bandbreedtelimiet ingesteld per IP of per subnet voor bulkverkeer.
