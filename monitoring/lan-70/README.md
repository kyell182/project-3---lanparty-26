# Monitoring voor de LAN van 70

Dit is de kant-en-klare monitoring voor de opstelling in [LAN_70_OPSTELLING.md](../../lan-70/LAN_70_OPSTELLING.md). De map gebruikt dezelfde stack als [monitoring/](../README.md), maar met de instellingen voor 70 deelnemers al ingevuld in `.env`.

Geen voorkennis? Volg dan de [HANDLEIDING](../HANDLEIDING.md). Die legt per onderdeel uit wat je invult en hoe je controleert dat het werkt.

## Starten

```bash
cd monitoring/lan-70
docker compose up -d
```

Daarna open je `http://<server>:3000` en log je in met de gegevens uit `.env`. Het dashboard **LAN-party overzicht** staat klaar. Uitleg van het dashboard en de alarmen staat in de [hoofd-README](../README.md#het-dashboard-uitgelegd).

Stoppen: `docker compose down`. Stoppen en alle data wissen: `docker compose down -v`.

## Wat er in `.env` staat

| Instelling | Waarde | Waarom |
| :-- | :-- | :-- |
| Wachtwoorden en token | Willekeurig gegenereerd | Sterke geheimen, uniek voor deze opstelling |
| `SNMP_COMMUNITY` | Willekeurig gegenereerd | Zet **dezelfde** community op pfSense en beide switches |
| `SNMP_APPARATEN` | `10.10.10.1,10.10.10.2,10.10.10.3` | pfSense en de twee switches uit het ontwerp, in het beheernetwerk (VLAN 10) |
| `PING_DOELEN` | `10.10.20.10,1.1.1.1` | De server in VLAN 20, en het internet om de uplink te testen |
| Retentie | 30 dagen | Ruim genoeg voor het evenement en de evaluatie |

De IP-adressen komen uit het IP-plan, maar de echte adressen zijn nog niet bevestigd. Controleer ze voor je start. Het pingdoel voor het internet (`1.1.1.1`) kan op het campusnetwerk geblokkeerd zijn. Vervang het dan door de gateway die IT opgeeft. Een extra switch voeg je toe door het IP achter `SNMP_APPARATEN` te zetten (zie [Apparaten toevoegen](../README.md#apparaten-toevoegen)).

## Voordat je het gebruikt

1. Zet SNMP aan op pfSense en de twee switches, met de community uit `.env`, alleen lezen en beperkt tot het IP van deze server.
2. Open de firewall: de server mag UDP 161 naar VLAN 10, en de crew-pc (VLAN 10) mag TCP 3000 naar de server.
3. Test alles in de labproef, bij scenario 7 uit het [draaiboek](../../draaiboek/00_OVERZICHT.md).

Zolang de apparaten niet bestaan of SNMP niet aanstaat, start de stack wel, maar zijn de poortpanelen leeg. Het alarm *Geen SNMP-data van een apparaat* gaat dan af. Dat is bedoeld.

## Een `.env` op een andere computer

`.env` staat in `.gitignore` en komt dus niet mee via git. Maak op een andere computer een nieuwe: kopieer `.env.example` naar `.env` en vul de lege waarden in.
