# LAN-party 26 — Todo-lijst

> Houd het beslislog bij voor elke beslissing, test en go/no-go-gate.

## Week 1 — Intake en projectsturing

- [x] Groepsrepository, eerste documentatie, checklist en logboek opzetten.
- [x] Eerste brainstorm uitvoeren.
- [x] Eerste contact met een stakeholder leggen.
- [x] Beslislog starten via het logboek.
- [ ] Groepsleden, rollen, toegang, projectboard en eerste issues vervolledigen.
- [x] Projectplan opzetten.
- [x] Risicoanalyse opzetten.

## Week 2 — Concept en haalbaarheid

- [ ] Doel en doelgroep definiëren.
- [ ] Datumopties en timing bepalen.
- [ ] Capaciteit inschatten voor deelnemers, tafels en netwerkpoorten.
- [ ] Begroting en budgeteigenaar bepalen.
- [ ] Stakeholderregister aanleggen.
- [ ] RACI-matrix maken: beslissen, uitvoeren, raadplegen en informeren.
- [ ] Conceptnota schrijven.
- [ ] **Gate 1: Concept akkoord** registreren.

## Week 3 — Locatie en toestemmingen

- [ ] Lokaal identificeren: openingsuren, evacuatie, toegankelijkheid, sanitair en toezicht.
- [ ] Fysiek plan maken met tafels, kabelroutes, labelconventie, nooduitgangen en helpdesk.
- [ ] Lokaal-, kabel- en stroomplan documenteren.
- [ ] Stuvo schriftelijk benaderen.
- [ ] Lokaalplanning en gebouwbeheer informeren.
- [ ] Preventie raadplegen over veiligheid en evacuatie.
- [ ] Aanvraag en akkoordregistratie bewaren.
- [ ] **Gate 2: Locatie akkoord** registreren.

## Week 4 — Ontwerp en proof-of-concept

- [ ] IT-goedgekeurde uplink en netwerkdiensten bevestigen.
- [ ] Netwerkdiagram en dataflow maken.
- [ ] IP-, DHCP-, bandbreedte- en capaciteitsplan opstellen.
- [ ] Beheerde switches, poorten, labels en beheer plannen.
- [ ] Grootste technische onzekerheid in een toegelaten proefopstelling testen.
- [ ] Technische keuzes, alternatieven, risico’s en resourcegebruik documenteren.

## Week 5 — Fundament en voorlopige plannen

- [ ] Voorlopig netwerk-, stroom-, veiligheids- en communicatieplan afronden.
- [ ] Cachingstrategie kiezen voor toegelaten platformen.
- [ ] Opslag, hitratio, DNS-impact en fallback van caching plannen.
- [ ] Lokale game- en ondersteunende servers plannen met aandacht voor licenties.
- [ ] Monitoring en dashboards plannen voor uplink, poorten, latency, packet loss en cache.
- [ ] Configuratieback-ups plannen zonder secrets.
- [ ] Inschrijfformulier en minimale gegevensbehoefte voorbereiden.
- [ ] Geen eigen DHCP, router, NAT of access point gebruiken zonder expliciet akkoord.
- [ ] **Gate 3: Techniek akkoord** voorbereiden en registreren.

## Week 6 — Kernfunctionaliteit en support

- [ ] Toegelaten proefopstelling opzetten.
- [ ] Aansluiten van een nieuwe deelnemer en connectiviteit testen.
- [ ] Gameserver met meerdere clients testen.
- [ ] Servicedeskprocedure maken met triage, gekende problemen en escalatiepad.
- [ ] Eerste technische runbooks schrijven.
- [ ] Reservekabels en hulpmateriaal inventariseren.
- [ ] Noodnummers van IT, gebouwbeheer en campus verzamelen.

## Week 7 — Security en technische laboproef

- [ ] Scenario 1: nieuwe deelnemer aansluiten en adres/connectiviteit verkrijgen.
- [ ] Scenario 2: verkeerde DHCP- of routerfunctie detecteren zonder campusnetwerk te raken.
- [ ] Scenario 3: cache hit en cache miss met werkende fallback meten.
- [ ] Scenario 4: gameserver bereiken en basisbelasting meten.
- [ ] Scenario 5: kabel-, switchpoort- of gameserverstoring diagnosticeren.
- [ ] Scenario 6: cache uitschakelen zonder algemene internettoegang te breken.
- [ ] Scenario 7: monitoringalarm ontvangen en volgens runbook behandelen.
- [ ] Scenario 8: switch- of serviceconfiguratie herstellen.
- [ ] Cachebenchmark documenteren: opslag, hitratio, DNS-impact en fallback.
- [ ] Switchconfiguratie back-uppen zonder secrets.
- [ ] Threat model en relevante dreigingen documenteren.
- [ ] Secretscontrole en negatieve securitytests uitvoeren binnen de projectscope.

## Week 8 — Operations en herstel

- [ ] Monitoringdashboard inrichten.
- [ ] Twee of drie meetbare SLI’s en SLO’s bepalen.
- [ ] Alertmatrix maken met drempel, ernst, eigenaar en runbookactie.
- [ ] Logging, privacy, retentie en tijdsynchronisatie instellen.
- [ ] Back-upstrategie, RPO en RTO bepalen.
- [ ] Restore testen op een aparte VM of testomgeving.
- [ ] Runbooks maken voor update, storing, back-up/restore, credentialrotatie en uitschakeling.

## Week 9 — Communicatie, automatisering en draaiboek

- [ ] Privacytekst en bewaartermijn toevoegen aan de inschrijving.
- [ ] Deelnemersvoorwaarden en gedragscode opstellen.
- [ ] Communicatieplan maken voor aankondiging, praktische info, wijzigingen en incidenten.
- [ ] Compatibiliteitschecklist voor deelnemers opstellen.
- [ ] Aankondigingsbericht laten goedkeuren.
- [ ] **Gate 4: Communicatie akkoord** registreren.
- [ ] Inschrijving openen, alleen na akkoord.
- [ ] Crew werven en ploegenschema maken.
- [ ] Belangrijke deployment- of beheertaak automatiseren.
- [ ] Definitief draaiboek maken van opbouw tot afbraak.
- [ ] Rollbackplan en noodplan voor een no-go-situatie maken.
- [ ] Toernooischema, regels en verantwoordelijke bepalen.
- [ ] Nevenactiviteiten voor niet-meespelende deelnemers plannen.
- [ ] Offline pakket met drivers, clients en documentatie voorbereiden waar licenties dit toelaten.

## Week 10 — Gebruikerstest en generale repetitie

- [ ] Dry-run met meerdere clients uitvoeren.
- [ ] Opbouw, netwerk, monitoring, support, incidenten en afbraak simuleren.
- [ ] Capaciteit, latency, packet loss en cachegedrag meten.
- [ ] Servicedesk en escalatiepad testen.
- [ ] Openstaande risico’s en verbeteracties registreren.
- [ ] Draaiboek, crewplanning en contactlijst aanpassen.

## Week 11 — Stabilisatie en uitvoerings-gate

- [ ] Kritieke fouten oplossen.
- [ ] Rollback en herstel opnieuw testen.
- [ ] Noodnummers, reservekabels en materialen controleren.
- [ ] Opbouw- en afbraakvenster met gebouwbeheer bevestigen.
- [ ] Alle technische en organisatorische bewijsstukken reviewen.
- [ ] Formele go/no-go voor uitvoering registreren.
- [ ] Bij no-go overschakelen naar een goedgekeurde tabletopoefening of dry-run.
- [ ] **Gate 5: Uitvoering akkoord** registreren.

## Evenement — Uitvoering en cleanup

- [ ] Opbouw volgens draaiboek uitvoeren.
- [ ] Monitoringdashboard intern live zetten.
- [ ] Servicedesk bemannen.
- [ ] Incidentlog en supportvragen bijhouden.
- [ ] Latency, packet loss, cache-effect, opkomst en oplostijden meten.
- [ ] Afbraak en cleanup volgens draaiboek uitvoeren.

## Week 12 — Evaluatie en overdracht

- [ ] Metingen en incidentlog analyseren.
- [ ] Deelnemersfeedback verwerken.
- [ ] Gemiddelde oplostijd van support bepalen.
- [ ] Gegevens verwijderen na de afgesproken retentieperiode.
- [ ] Aanbevelingen en verbeterpunten documenteren.
- [ ] Evaluatierapport schrijven.
- [ ] Overdraagbaar draaiboek opleveren.
- [ ] Bewijsstukken compleet controleren: aanvragen, RACI, begroting, plannen, diagram, benchmark, configuratie, privacy, gedragscode, draaiboek, servicedesk, incidentlog en evaluatie.
