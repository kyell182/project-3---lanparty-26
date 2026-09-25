# LAN-party 26 — Todo-lijst

> Afvinkbaar checklist per fase. Houd het beslislog bij voor elke beslissing en gate.

## 0. Kader en projectsturing

- [ ] Projectplan opzetten
- [ ] Begroting / budgetraming maken (met budgeteigenaar)
- [ ] Stakeholderregister aanleggen
- [ ] RACI-matrix maken (wie beslist, uitvoert, raadpleegt, informeert)
- [ ] Risicoanalyse opzetten
- [ ] Beslislog starten

## 1. Concept (week 2 — Gate: Concept)

- [ ] Doel en doelgroep definiëren
- [ ] Datumopties bepalen
- [ ] Capaciteit inschatten (deelnemers)
- [ ] Budgeteigenaar aanwijzen
- [ ] Conceptnota schrijven → **Gate 1: Concept akkoord**

## 2. Locatie en toestemmingen (week 2–3 — Gate: Locatie)

- [ ] Lokaal identificeren (openingsuren, evacuatieroutes, toegankelijkheid, sanitair, toezicht)
- [ ] Fysiek plan maken: tafels, kabelroutes, labelconventie, nooduitgangen, helpdesk
- [ ] Lokaalplan / kabelplan documenteren
- [ ] Stuvo schriftelijk benaderen (voldoende doorlooptijd)
- [ ] Lokaalplanning / gebouwbeheer informeren
- [ ] Preventie raadplegen (veiligheid, evacuatie)
- [ ] **Gate 2: Locatie akkoord**

## 3. Netwerk en techniek (week 5 — Gate: Techniek)

- [ ] Toestemming uplink verlenen via IT/netwerkbeheer
- [ ] Netwerkontwerp maken op basis van IT-goedgekeurde uplink (geen eigen DHCP/router zonder akkoord)
- [ ] Beheerde switches selecteren en plannen (gescheiden beheersnetwerk)
- [ ] DHCP/routing-plan: IP-adressen, capaciteit, subnetten
- [ ] Bandbreedteplan / capaciteitsplan (deelnemers, bekabelde poorten, uplink)
- [ ] Stroomplan maken (aansluitingen, vermogen, back-up)
- [ ] Caching-strategie kiezen (bijv. LANCache) voor toegelaten platformen
- [ ] Lokale game-/ondersteunende servers plannen (licentieverzoek)
- [ ] Monitoring en dashboards plannen (uplink, poorten, latency, packet loss, cache)
- [ ] Netwerkdiagram + IP- en bandbreedteplan documenteren
- [ ] **Gate 3: Techniek akkoord**

## 4. Caching en technische laboproef (week 7)

- [ ] Proefopstelling opzetten (toegelaten omgeving)
- [ ] Scenario 1: nieuwe deelnemer aansluiten, adres + connectiviteit
- [ ] Scenario 2: onbekende/verkeerde DHCP of router detecteren zonder campusnet te raken
- [ ] Scenario 3: cache hit/miss meten + werkende fallback
- [ ] Scenario 4: gameserver bereiken + basisbelasting meten
- [ ] Scenario 5: kabel-, switchpoort- of gameserverstoring diagnosticeren
- [ ] Scenario 6: cache uitschakelen zonder internettoegang te breken
- [ ] Scenario 7: monitoringalarm ontvangen en per runbook behandelen
- [ ] Scenario 8: configuratie switch/service herstellen
- [ ] Cachebenchmark documenteren (opslag, hit ratio, DNS-impact, fallback)
- [ ] Switchconfiguratie back-up maken (zonder secrets)

## 5. Inschrijving en communicatie (week 5 en 9 — Gate: Communicatie)

- [ ] Inschrijfformulier maken (minimale gegevens)
- [ ] Privacytekst + bewaartermijn bepalen
- [ ] Deelnemersvoorwaarden en gedragscode opstellen
- [ ] Communicatieplan: aankondiging, praktische info, wijzigingen, incidenten
- [ ] Aankondigingsbericht laten goedkeuren
- [ ] Compatibiliteitschecklist voor deelnemers
- [ ] **Gate 4: Communicatie akkoord** (geen officiële communicatie vóór akkoord!)
- [ ] Inschrijving openen (alleen na akkoord)

## 6. Uitvoering voorbereiden (week 9–11 — Gate: Uitvoering)

- [ ] Crew werven en ploegenschema maken
- [ ] Draaiboek: opbouw → afbraak, per ploeg
- [ ] Servicedeskprocedure: triage, gekende problemen, escalatiepad
- [ ] Reservekabels en materialen inventariseren
- [ ] Noodnummers verzamelen (IT, gebouwbeheer, campus)
- [ ] Rollbackplan en noodplan (no-Go) maken
- [ ] Toernooischema + regels + verantwoordelijke
- [ ] Nevenactiviteiten voor niet-meespelende deelnemers
- [ ] Offline pakket: drivers, clients, documentatie (licentiekundig)
- [ ] Dry-run met meerdere clients
- [ ] Formele go/no-go-check → **Gate 5: Uitvoering akkoord**
- [ ] Opbouw- en afbraakvenster afspreken met gebouwbeheer

## 7. Het evenement

- [ ] Opbouw volgens draaiboek (binnen venster)
- [ ] Monitoring/dashboard live (intern)
- [ ] Servicedesk bemand
- [ ] Incidentlog bijhouden
- [ ] Afbraak en cleanup volgens draaiboek

## 8. Evaluatie (week 12)

- [ ] Metingen verzamelen (latency, packet loss, cache-effect, opkomst)
- [ ] Incidentlog analyseren
- [ ] Deelnemersfeedback verwerken
- [ ] Gemiddelde oplostijd support bepalen
- [ ] Gegevens verwijderen na retentieperiode
- [ ] Evaluatierapport schrijven
- [ ] Overdraagbaar draaiboek inleveren

## 9. Verplichte bewijsstukken (checklist)

- [ ] Goedgekeurde aanvragen / akkoordregistratie
- [ ] RACI-matrix
- [ ] Begroting
- [ ] Lokaal- en kabelplan
- [ ] Netwerkdiagram
- [ ] IP- en bandbreedteplan
- [ ] Cachebenchmark
- [ ] Switchconfiguratie (zonder secrets)
- [ ] Privacy- en communicatieplan
- [ ] Gedragscode
- [ ] Draaiboek
- [ ] Servicedeskprocedure
- [ ] Incidentlog
- [ ] Evaluatierapport
