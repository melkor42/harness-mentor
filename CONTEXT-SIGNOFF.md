# Context Sign-Off — Harness Mentor

**Aktueller Vorrang:** Der Produktname bleibt **Harness Mentor**, technisch `harness-mentor`.
Manuel hat den zunächst gewünschten Namen Set Me Up zurückgenommen. Es handelt sich um einen
persönlichen Onboarding- und Begleit-Skill mit dem Ziel der eigenständigen Harness-Nutzung.
Der aktuelle Einstieg liegt in [`.qoder/skills/harness-mentor/SKILL.md`](.qoder/skills/harness-mentor/SKILL.md).
Der [Funktionsabgleich](docs/product-plan.md#funktionsabgleich-und-änderungsplan) trennt vorhandene
Anweisungen, beobachtete Wirkung und noch vorgeschlagene Erweiterungen. Funktionale Erweiterungen
sind nicht freigegeben und wurden bei der Namensangleichung nicht implementiert.
Die älteren Abschnitte unten bleiben Vorgeschichte. Quelle: Manuels Auftrag und Namenskorrektur
im aktuellen Chat, Stand 2026-10-25.

**Historischer Stand 2026-10-11 — durch den aktuellen Vorrang oben präzisiert.** Das Produkt ist nicht mehr der
Messprüfstand, sondern ein **Skill**: ein geführtes Setup, das eine Person an die Hand nimmt, die zum
ersten Mal einen Harness benutzt — Erklärung, was ein Harness ist, dann Aufbau des Grundkontexts.
Entscheidung und Begründung stehen in [`DECISIONS.md`](DECISIONS.md), Einträge vom 2026-10-11. Der
Prüfstand (`prototype/`, `schema/`, `docs/prototype-plan.md`) ist an diesem Tag gelöscht; der letzte Stand
liegt in der Git-Historie (Commit `d14365a` und davor). Die Abschnitte 1, 3, 7, 8, 10 und 11 beschreiben
den ersetzten Weg und bleiben als Vorgeschichte stehen; §2 (soweit nicht kollidierend), §4, §5, §6 und §9
gelten weiter. Dieses Dokument wird zu gegebener Zeit als Projektseite des Skills neu geschrieben — bis
dahin gilt zuerst dieser Hinweis.

**Stand 2026-09-19.** Neue Sessions starten hier, nicht bei null. Dieses Dokument übergibt den Stand
der Produktidee **Company Harness Product Idea** an den Workspace
`C:\Users\Admin\Documents\Company-Harness`, in dem die initiale Umsetzung beginnt.

Es ist eine Übergabe, keine Freigabe. Was Manuel entschieden hat, steht unter *Bestätigt*. Was ein
Agent vorgeschlagen hat, steht unter *Vorschlag*. Was niemand belegt hat, steht unter *Unbelegt* oder
*OFFEN*. Diese Trennung ist die nützlichste Information in diesem Bestand — sie nicht verwischen.
Eine Ablehnung wird als neuer Eintrag festgehalten, nicht als stille Änderung dieses Dokuments.

**Sprache:** Dieses Dokument ist Deutsch. Der recherchierte Produktplan
[`docs/product-plan.md`](docs/product-plan.md) ist Englisch, weil er aus der Recherche-Sitzung stammt
und seine Quellenverweise dort stehen. Beides ist Absicht, kein Versehen.

---

## 1. Was das ist

Ein **Company Harness** ist eine AI-Arbeitsschicht über einem kleinen oder mittleren Unternehmen. Sie
verbindet zwei Dinge, die heute meist getrennt verkauft werden: den Kontext des Unternehmens (was
vereinbart wurde, was gilt, was fehlt, wer entscheidet) und eine ausführende Agentenschleife, die daraus
einen abgeschlossenen, geprüften Arbeitsvorgang macht.

Der Unterschied zu „AI-Mitarbeitern" ist bewusst gewählt: Es wird **keine menschliche Rolle** nachgebildet.
Abgebildet wird die Arbeits- und Prozessebene — Auslöser, Evidenz, erlaubte Aktionen, Prüfpunkt,
Abbruchbedingung. Der Agent ist eine Komponente, nicht das Produkt.

Quelle für die Idee: Manuels Diktat, verdichtet in
[`docs/sources/konzept-ursprung-2026-09-19.md`](docs/sources/konzept-ursprung-2026-09-19.md),
Stand 2026-09-19. Die dortigen Marktaussagen sind seine Einschätzung, keine belegten Befunde.

## 2. Bestätigt (von Manuel, 2026-09-19)

- Der Titel lautet **Company Harness Product Idea**.
- Es geht um ausführbare, unternehmensweite Prozesse statt um AI in Menschenrollen.
- Es braucht eine Verkaufsstrategie: Ein Harness, den niemand kauft, ist kein Produkt.
- Zielgruppe sind kleine und mittlere Unternehmen; der eigene Betrieb ist erstes Versuchslabor.
- Qoder ist die priorisierte Harness-Seite, Oracle AI Database 26ai die angedachte Kontextseite —
  **beide ausdrücklich austauschbar**, nicht Teil des Produktkerns.
- Dass ähnliche Angebote existieren, ist keine Überraschung und kein Gegenargument. Entscheidend sind:
  vollständige Ersetzbarkeit, Wiederverwendbarkeit und der praktische Einstieg im vorhandenen Setup.
- White-Label ist die langfristige Richtung; Dienstleistung soll in Produkt übergehen.

Ebenfalls von Manuel, am 2026-09-19 als spätere Angabe in denselben drei Punkten — diese Überarbeitung
ersetzt die Vorschläge aus §3, soweit sie kollidieren:

- **Baseline zuerst, dann Engine.** Es wird nichts gebaut, bevor der Kontextnachweis in der
  Qoder-/Datei-Arbeitsweise erbracht ist. Das ist Bestätigung zu §10 Schritt 1–4, keine Vorwegnahme.
- **Beide Prüfprozesse parallel**, nicht nacheinander. Die Empfehlung „Änderung zuerst" aus §3 ist überholt.
- **Privates GitHub-Repo**, von Manuel selbst angelegt; siehe §11 Punkt 9.

## 3. Vorschlag (Agent, 2026-09-19 — nicht bestätigt)

Die folgenden Punkte sind Empfehlungen aus der Analyse. Sie gelten, solange Manuel sie nicht verwirft.

**Die zwei Prüfprozesse.** Nicht „mehr Kontext", sondern zwei Abläufe, an denen sich zeigt, ob Kontext
die Entscheidung überhaupt verändert:

1. **Kundenänderung → abgestimmter Lieferplan.** Eine Änderungswünsche-Mail trifft auf den vereinbarten
   Umfang, die aktuelle Kapazität, frühere Kulanzfälle und die kaufmännischen Regeln. Das System trennt
   Wunsch von Zusage, zeigt betroffene Arbeit und entwickelt Optionen (Umfang reduzieren, Termin ändern,
   Zusatzangebot). Ein Mensch entscheidet; danach werden die freigegebenen Aktualisierungen vorbereitet
   oder ausgeführt, und der Fall bleibt offen, bis Vereinbartes und operative Daten übereinstimmen.
2. **Erbrachte Leistung → rechnungsbereite Nachweise.** Ein Meilenstein gilt als fertig, die Rechnung
   hängt aber an Abnahme, Zeiterfassung, Bestellnummer oder kundenspezifischer Dokumentation. Das System
   vergleicht Nachweise mit Vereinbarung, benennt den fehlenden Punkt, fragt beim richtigen Eigentümer nach
   und setzt fort, sobald die Antwort da ist. Buchung, Steuerklassifikation und Versand bleiben außen.

Beide brauchen dieselbe Architektur — geteilten Kontext, dauerhaften Fallzustand, begrenzte Aktionen,
menschliche Freigabe, Wiederaufnahme nach Unterbrechung. Sie sind der Prüfstand, nicht das Endprodukt.

**Erster Einstieg:** die vorhandene Qoder-/Datei-Arbeitsweise als beaufsichtigte Baseline nutzen, bevor
eine Plattform bereitgestellt wird. Erst danach entscheidet der Vergleich, ob Hexis oder ein gehostetes
Produkt etwas ersetzt oder nur einen Baustein liefert.

**Verkaufsansatz:** Ein benanntes Ergebnis verkaufen, keine Infrastruktur. Mögliche Botschaft:
*„Kundenänderungen klären, bevor daraus unbezahlte Arbeit wird."* Zielgruppe zunächst inhabergeführte
B2B-Dienstleister mit wiederkehrender Projektlieferung; Käufer ist, wer für die Lieferökonomie
verantwortet. Das ist eine zu prüfende Segmentwahl, kein belegter Markt.

## 4. Unbelegt / ausdrücklich nicht nachgewiesen

- **Zahlungsbereitschaft.** Keine Quelle in diesem Bestand zeigt, dass jemand für einen Company Harness
  bezahlt. Öffentliche Studien belegen Verwaltungslast und KI-Hemmnisse, nicht die Nachfrage nach
  diesem Produkt (siehe §9).
- **„Gibt es so noch nicht."** Nicht belegt und nicht behauptbar. Die Recherche hat Überschneidungen
  gefunden, keine Marktlücke bewiesen. Fehlen eines Angebots auf einer Landingpage ist kein Beleg.
- **Qoder als Produktruntime.** Die interaktive Sitzung funktioniert; unbelegt bleiben unbeaufsichtigte
  Integration, strukturierte Ereignisse, Wiederaufnahme, Nebenläufigkeit, gehosteter Betrieb und
  kommerzielle Weitergabe-/White-Label-Rechte.
- **Oracle AI Database 26ai.** Edition, relevante Funktionen, Treiber, Kosten und Lizenzbedingungen sind
  nicht geprüft. Es liegt kein Test der geplanten Retrieval-Last vor.
- **Hexis im Betrieb.** Installationsanforderungen wurden aus einem README-Spiegel gelesen, nicht
  ausgeführt. Quelltext und Lizenz wurden nicht direkt eingesehen (GitHub-CLI fehlte auf dem PATH).
  **Nachtrag 2026-09-19:** Die Begründung ist überholt — `gh` fehlt weiterhin, aber HTTPS-Klonen und
  -Pushen funktionieren über den systemweit konfigurierten Git Credential Manager. Eine Lizenzprüfung am
  Quelltext ist also sofort möglich und liegt noch immer nicht vor. Siehe
  [`DECISIONS.md`](DECISIONS.md), Vorgeschichte zum Repo-Eintrag.
- **Alle Herstellerangaben.** Sie belegen, was dokumentiert oder beworben wird — nicht, dass es im
  Kundeneinsatz zuverlässig läuft. Kein Kandidat wurde gegen unsere Abnahmekriterien getestet.
- **Vollständige Ersetzbarkeit.** Offen. Genau dafür ist der Vergleich in §8 vorgesehen.

## 5. Harte Regeln für diesen Workspace

1. **`private/`-Inhalte des Delta-Weave-Hubs kommen nicht hierher.** Nicht kopieren, nicht zitieren,
   nicht in Prompts an Dritte geben. Verweis mit Pfad genügt.
2. **Jede Zahl und jedes Datum braucht Quelle und Stand.** Ohne Quelle gehört es als `OFFEN — Manuel`
   markiert, nicht geraten.
3. **Keine Herstellerbehauptung ohne geprüfte Quelle.** Marketingtext ist kein Funktionsnachweis.
   Schweigen einer Dokumentationsseite ist kein Beweis für ein fehlendes Feature.
4. **Keine echten Geschäftskonten ohne ausdrückliche Freigabe.** Keine Mail-, Kalender-, Buchhaltungs-
   oder Kundenzugänge für einen Demo-Test verbinden. Erst synthetische oder ausdrücklich freigegebene
   Fälle.
5. **Zugriff wird außerhalb des Modells erzwungen.** Prompt-Guardrails und Hooks sind keine
   Sicherheitsgrenze. Freigaben binden an die konkrete Aktion und ihre Nutzlast.
6. **Kein Auto-Commit eines Kontextservers in den Delta-Weave-Hub.** Ein Hexis-Versuch läuft in einem
   separaten, isolierten Repo.
7. **Credentials nie in Dateien dieses Repos.** Kein `.env` committen; Bedarf als Entscheidung melden.

## 6. Was hier liegt

| Pfad | Inhalt | Status |
|---|---|---|
| [`CONTEXT-SIGNOFF.md`](CONTEXT-SIGNOFF.md) | Dieses Dokument; Einstieg für jede neue Session | Stand 2026-09-19 |
| [`AGENTS.md`](AGENTS.md) | Arbeitsregeln für Agents in diesem Workspace | neu, 2026-09-19 |
| [`docs/product-plan.md`](docs/product-plan.md) | Produktthese, Prozessbeispiele, Architektur, Wettbewerbs- und Ersetzbarkeitsvergleich, Marktansatz, Build-or-Reuse-Experiment — mit 16 Quellenbelegen | verschoben aus dem Delta-Weave-Hub, 2026-09-19 |
| [`docs/sources/konzept-ursprung-2026-09-19.md`](docs/sources/konzept-ursprung-2026-09-19.md) | Manuels ursprüngliche Konzeptfassung (Sicherung der Session-Anlage) | Kopie der Anlage, Quelltext unverändert |
| [`docs/manifest.md`](docs/manifest.md) | Manuels Position in neun Abschnitten: Ziel ist die Evaluierung; Presets statt Harness; Domänenwissen als Kern; Kontext kuratieren; drei Arbeitsweisen; Core Loop; deterministisch/urteilend getrennt; Oberfläche als Prüfmittel | aus Diktat 2026-10-09; **bestätigte Position**, kein Agentenvorschlag |
| [`docs/manifest-gegenlese.md`](docs/manifest-gegenlese.md) | Einwände eines Agenten mit Web-Recherche: vier Punkte belegt, drei Widersprüche, vier blinde Flecken, fünf Planänderungen vorgeschlagen | Agent, 2026-10-09; von Manuel **angenommen** 2026-10-10 (DECISIONS.md); die Pläne, in die nachgezogen worden wäre, sind 2026-10-11 ersetzt |
| [`docs/manifest.html`](docs/manifest.html) | Beide Teile als eigenständige HTML-Seite, ohne externe Abhängigkeiten | erzeugt 2026-10-10; bei Abweichung gelten die Markdown-Dateien |
| [`docs/recherche-kontext-verwaltung.md`](docs/recherche-kontext-verwaltung.md) | Recherche gegen Primärquellen: dateibasierte kuratierte Kontext-Setups vs. RAG — Minimum, das funktioniert; gemessene Grenzen beider Extreme; wann Retrieval nötig wird; Nachvollziehbarkeit | Agent, 2026-10-10; 19 Quellen mit Datum, Herstellerangaben gekennzeichnet; Schwellwerte Datei→RAG bleiben OFFEN |

**Gelöscht am 2026-10-11** (Richtungsänderung zum Skill, siehe Banner oben; letzter Stand in der
Git-Historie, Commit `d14365a` und davor): `docs/prototype-plan.md`, `schema/` (fünf JSON-Schemas),
`prototype/` (Korpus Nordwind, Kontextdatensätze, Prozessdefinitionen, vier Fälle, Sandbox-Systeme,
Validator, Messprotokoll).

**Außerhalb dieses Workspaces, aber relevant:**

- `D:\OneDrive\Delta Weave` — der Kontext-Hub: Person, Firma, Projekte, Kontakte, Entscheidungen.
  Dort liegt weiterhin der schlanke Knoten `projects/harness-mentor.md` als Verweis auf diesen
  Workspace. Hub-Regeln: erst `MAP.md`, dann der betroffene Knoten.
- `D:\OneDrive\Delta Weave\company\vision.md` — Methode und Anspruch von Delta Weave; die offene Frage,
  ob Delta Weave Auftragsarbeit oder ein eigenes Produkt ist, betrifft dieses Projekt direkt.
- `D:\OneDrive\Delta Weave\company\oeffentlichkeit.md` — Freigabeliste. **Nichts aus diesem Workspace
  geht nach außen, ohne dort gegengeprüft zu haben.**
- `C:\Users\Admin\Documents\ATHA` und `...\finanzmehrwert` — die zwei belegten Produktarchitekturen
  (Firecrawl-Ingest → Neo4j-Graph → Zwei-Agenten-Compose → Renderer mit Allowlist). Relevant als
  Vergleichsmaßstab für „was bereits zweimal funktioniert hat".

## 7. Technik-Kandidaten und ihre ungeprüften Punkte

| Kandidat | Rolle im Vorschlag | Vor dem Einsatz zu klären |
|---|---|---|
| **Qoder** | Operator-Workbench jetzt; mögliche Ausführungs-Komponente später | Unterstützte unbeaufsichtigte Schnittstelle, Ereignisformate, Abbruch/Neustart, Werkzeugbeschränkung, Modellwahl, Nebenläufigkeit, gehosteter Betrieb, White-Label-Rechte |
| **Oracle AI Database 26ai** | Kandidat für Kontext, Beziehungen, Retrieval-Index, Fallzustand | Edition/Betriebsform, tatsächlich benötigte Funktionen, Treiber, Durchsetzung von Berechtigungen, Backup/Export, Region, Kosten, Lizenz |
| **Hexis (Bevel)** | Wiederverwendbare Kontext-/Steuerungsschicht, Git-gestützt, über MCP | Eigene Bereitstellung (Docker Compose, PostgreSQL, Secrets), Lizenz direkt am Quelltext prüfen, Qoder-Anbindung testen, Aufwand für Verwaltung und Migration |
| **Lindy** | Gehostete Alternative für die eigene Tagesarbeit, Vergleichsmaßstab | Leistung auf denselben Fällen, Datenhaltung/Export, kommerzielle Rechte; dokumentierter Einstiegsweg führt über Slack |
| **Rocketlane / Scoro / Accelo** | Bestehende operative Systeme als Vergleichsmaßstab | Ob der Zielkunde eines davon bereits führt; dann ist Ausbau oft billiger als eine neue Schicht |

**Konkreter Befund zum Hexis-Entwicklungsweg:** Der gelesene README-Spiegel nennt als Engine-Bereich
`>=22.13 <23`. Auf diesem Rechner liegt Node 24 (bash-Pfad meldet `v24.16.0`). Der Entwicklungsweg
`pnpm dev` würde damit an der Engine-Prüfung scheitern; der dokumentierte Produktivweg über
`docker compose up -d` ist unabhängig davon — **Docker war auf dem PATH und an den geprüften
Standardorten nicht vorhanden.** Quelle: lokale Prüfungen und README-Spiegel in dieser Sitzung,
Stand 2026-09-19. Nicht exhaustiv; ein Docker Desktop an anderer Stelle ist nicht ausgeschlossen.

Verfügbar auf diesem Rechner (gleiche Prüfung): Git 2.54.0, Node 24, Python 3.14.5. Nicht gefunden:
`docker`, `gh`, `uv`, `firecrawl`.

**Austauschbarkeit heißt nicht kostenlos.** Quelldokumente, kanonische Sätze, Prozessdefinitionen und
Evaluationsfälle müssen exportierbar bleiben. Hersteller spezifische Abfragen gehören hinter eine kleine
Dienstgrenze. Ein Datenbankwechsel kann trotzdem Query-Änderungen, Neuindexierung und neue Embeddings
bedeuten.

## 8. Das Experiment, das Bauen oder Wiederverwenden entscheidet

Derselbe Änderungsfall und derselbe Rechnungsbereitschafts-Fall laufen in der Qoder-/Datei-Baseline und
in einem ausgewählten bestehenden Kandidaten. Beide müssen: die richtige Evidenz finden, Wunsch von
Zusage trennen, eine erlaubte Folgeaktion entwickeln, auf eine Entscheidung warten, nach Unterbrechung
fortsetzen und den resulting business state prüfen. Dazu gehören Fehlerfälle: geänderte Evidenz nach
Freigabe, verweigerte Aktion, fehlendes Dokument, entzogener Zugriff, Wiederholung.

**Gemessen wird:** Aufwand des Eigentümers einschließlich Kontexterklärung, Korrektur und laufender
Pflege; Dauer bis Fallabschluss; unbelegte Behauptungen; falsche oder doppelte Aktionen; Gesamtkosten.
Vergleichsmaßstab ist eine einfache Regel oder das bestehende operative Werkzeug — nicht der schlechteste
denkbare Zustand.

Um den Nutzen des Kontexts isoliert zu zeigen, läuft dieselbe Aufgabe einmal **nur mit der eingehenden
Anfrage** und einmal **mit freigegebenem Unternehmenskontext**. Ändert der Kontext die Entscheidung nicht
wesentlich, ist der Ablauf kein gutes Flaggschiff für dieses Produkt.

**Ersetzbarkeit, getrennt betrachtet:**
- *Vollständiger Ersatz des internen Nutzens* — wenn ein bestehendes Produkt dieselben Ergebnisse mit
  geringerem Gesamtaufwand liefert. Dann kann Delta Weave integrieren oder konfigurieren statt bauen.
- *Vollständiger Ersatz des Verkaufsangebots* — wenn Zielkunden es einführen, dieselben Ergebnisse
  erreichen und es einfacher betreiben können, zu vertretbaren Kosten.
- *Nur Baustein* — wenn es die Kontextschicht ersetzt, aber Ausführung, Fallzustand, Freigabe oder
  Vertrieb offen bleiben. Das ist der wahrscheinlichste Ausgang für Hexis.

Eigenentwicklung ist gerechtfertigt durch eine beobachtete fehlende Fähigkeit oder deutlich bessere
Betriebsökonomie — nicht durch die Vorliebe für den eigenen Stack.

## 9. Marktkontext — was die Quellen tragen und was nicht

Die Studien belegen wiederkehrende Belastung und Hemmnisse, **nicht** die Nachfrage nach diesem Produkt.

- **KfW Research (2025-04-25):** Steuer-, Aufbewahrungs-, Dokumentations- und Rechnungswesenpflichten
  sind benannte, wiederkehrende Belastungen; die Last ist ungleich verteilt, nicht jeder Betrieb trägt sie.
  Kein Beleg für einsparbare AI-Anteile.
- **EU Payment Observatory (Bericht 2025, veröffentlicht 2025-12-15, Zahlungsjahr 2024):** Das Verfolgen
  überfälliger Zahlungen ist eine erhebliche Verwaltungslast. Zahlungsziele, tatsächliche Zahlungsdauer
  und Ursachen sind verschiedene Dinge — nicht vermischen.
- **Eurostat (Daten 2025):** Erfasst sind Betriebe ab 10 Beschäftigten in den genannten Branchen; die
  Hemmnis-Angaben beziehen sich auf Unternehmen, die AI erwogen, aber nicht eingesetzt haben.
  Nicht auf Kleinstbetriebe verallgemeinern.
- **Bitkom (2026-03-11):** 604 deutsche Unternehmen ab 20 Beschäftigten; Beleg für ungenutzte eigene
  Daten und Zeit-/Datenschutz-/Fachkräftehemmnisse, kein Beleg für diesen Anwendungsfall.

**Konsequenz für den Vertrieb:** Ein Angebot verkaufen, das Einarbeitungsaufwand verringert und Vertrauen
aufbaut — nicht die Plattform. Discovery startet mit einem konkreten zurückliegenden Fall: Wo lag die
Evidenz, wer hat es bemerkt, was ist passiert, wie viel Zeit kostete es, warum hat die vorhandene
Software es nicht gelöst? Das ist ergiebiger als die Frage, ob jemand einen AI-Assistenten möchte.

**Kosten, die in jede Rechnung gehören:** Kontextbereinigung pro Kunde, menschliche Prüfung der
Ergebnisse, laufende Pflege bei sich ändernden Quellen — und die Stunden des Kunden beim Einrichten.
Bei knapper Zeit ist der Einrichtungsaufwand ein Verkaufseinwand, nicht nur unsere Kosten.

## 10. Nächste Schritte für die initiale Umsetzung

**Stand 2026-10-11: ersetzt** durch die Skill-Richtung ([`DECISIONS.md`](DECISIONS.md)); der Messprüfstand
und seine Dateien sind gelöscht. Die Liste unten bleibt als ursprüngliche Fassung der Vorgeschichte stehen.

Reihenfolge, nicht Termine. Jeder Schritt hat eine erkennbare Abbruchbedingung.

**Stand 2026-09-19:** Diese Liste ist in [`docs/prototype-plan.md`](docs/prototype-plan.md) §7 zu
Meilensteinen M0–M5 mit je einer Abbruch- und einer Fertig-Bedingung ausgearbeitet; Schritt 5 und 6 sind
dort M5 und M4. Die Liste unten bleibt als ursprüngliche Fassung stehen.

**Stand 2026-09-20:** Schritt 1 und 2 sind gebaut. Schritt 1 erfüllt, soweit ein Agent ihn erfüllen kann:
vier Fälle, zwanzig Datensätze, sechs Quelldokumente, erwartete Ergebnisse vor jedem Lauf geschrieben. Sein
Fertig-Kriterium — *ein Prüfer ohne Vorwissen sagt, ob das Ergebnis stimmt* — ist damit **nicht** erreicht,
weil der Schreiber nicht der Prüfer sein darf; die Bedingung steht offen im Messprotokoll §2. Schritt 2 ist
erfüllt: beide Prozesse liegen als versionierte Dateien mit Allowlist unter `prototype/processes/`, und die
Allowlist wird maschinell geprüft, nicht nur beschrieben. Schritt 3 ist der nächste und braucht nichts außer
einer Qoder-Sitzung.

1. **Fallmaterial anlegen.** Zwei synthetische oder ausdrücklich freigegebene Fälle je Prozess:
   eingehende Änderung, vereinbarter Umfang, Kapazität, kaufmännische Regeln, erwartetes Ergebnis.
   *Fertig, wenn* ein Prüfer ohne Vorwissen sagen kann, ob das Ergebnis stimmt.
2. **Prozessdefinition schreiben.** Auslöser, benötigte Evidenz, erlaubte Aktionen, Prüfpunkte,
   Abbruchbedingungen, Eskalation. Als Datei versionierbar, nicht als Prompt-Fragment.
3. **Baseline in Qoder laufen lassen.** Fallzustand, Entscheidungen und Freigaben außerhalb des Chats
   dauerhaft ablegen. *Abbruch, wenn* der Chat selbst als Zustandspeicher missbraucht wird.
4. **Kontextnutzen isoliert messen.** Gleicher Fall mit und ohne Unternehmenskontext (§8).
   *Abbruch, wenn* kein wesentlicher Unterschied messbar ist — dann ist der Ablauf falsch gewählt.
5. **Ersatzkandidat vergleichen.** Erst dann Hexis bereitstellen oder ein gehostetes Produkt prüfen,
   mit denselben Abnahmekriterien. *Abbruch, wenn* ein Kandidat mit geringerem Gesamtaufwand besteht.
6. **Nur fehlende Bausteine bauen.** Kontextdienst, Fallzustand, begrenzte Aktionen, Wiederaufnahme.
   Oracle erst, wenn reale Daten- und Retrieval-Anforderungen es begründen.

**Bis dahin ausdrücklich nicht:** Software installieren, externe Geschäftskonten verbinden,
`private/`-Inhalte übernehmen, etwas veröffentlichen, Preise nennen oder Liefertermine zusagen.

## 11. OFFEN — Manuel

1. **Reihenfolge der zwei Prüfprozesse.** Änderung → Lieferplan zuerst, oder Rechnungsbereitschaft?
   Empfehlung im Vorschlag: Änderung zuerst, weil dort der Kontext die Entscheidung sichtbar verändert.
   **Erledigt 2026-09-19:** Manuel lässt beide parallel laufen; die Empfehlung bleibt als Vorschlag stehen.
   Siehe [`DECISIONS.md`](DECISIONS.md) und [`docs/prototype-plan.md`](docs/prototype-plan.md) §0.
2. **Zielsegment.** Inhabergeführte B2B-Dienstleister mit Projektlieferung als Einstieg — bestätigen,
   oder ein anderes Segment aus dem vorhandenen Umfeld wählen? Für den Prototyp nicht nötig; vor dem
   Ersetzungskandidaten-Vergleich (M5) braucht die Frage eine Antwort.
3. **Fallmaterial.** Synthetisch, oder ausdrücklich freigegebene echte Fälle? Welche Quellen dürfen
   gelesen werden? Bisher keine Freigabe für Kunden- oder Mailzugänge. **Vorläufig geklärt, nicht
   entschieden:** der Prototyp nutzt synthetisches Material, weil Regel 4 keine andere Wahl lässt. Die
   Frage, welche echten Quellen gelesen werden dürfen, bleibt offen.
4. **Hexis-Bereitstellung.** Docker auf diesem Rechner einrichten, einen separaten Sandbox-Host nutzen,
   oder erst ohne Hexis arbeiten? Lizenzprüfung am Quelltext steht in jedem Fall aus.
5. **Oracle.** Weiter als Kandidat führen oder zurückstellen, bis die Prozesse laufen? Im Prototyp nicht
   vorgesehen; eine Begründung wäre ein realer Retrieval-Fall aus M3.
6. **Qoder-Rechte.** Wer klärt gehosteten Betrieb und White-Label-Fähigkeit — Herstelleranfrage nötig?
7. **Erster bezahlter Pilot.** Mit wem, und auf welcher Grundlage? Die vorhandenen Projektkontakte
   stehen laut Hub ohne Vertrag und ohne Preis; Interesse ist keine Beauftragung. Keine Grundlage vor M3.
8. **Sprache der Kundendokumente.** Deutsch, englisch, oder beides? Intern ist die Mischung bewusst.
9. **Repo-Sichtbarkeit.** Git ist ohne Remote initialisiert. Wann und ob ein privates GitHub-Repo
   folgt, ist offen. **Erledigt 2026-09-19:** privates Repo
   `https://github.com/melkor42/Company-Harness`, von Manuel angelegt; Einzelheiten und der korrigierte
   Befund zum GitHub-Zugang stehen in [`DECISIONS.md`](DECISIONS.md).

## 12. Wie dieser Stand zustande kam

Erstellt in einer Qoder-Sitzung am 2026-09-19 auf Manuels Auftrag: Idee schärfen, Architektur
skizzieren, dann Prozesse, Verkauf und tatsächliche Ersetzbarkeit recherchieren. Drei parallele
Recherche-Aufträge lieferten Herstellerbelege (Microsoft/Glean/Dust, Lindy/Relevance/Bevel/Fig/Relay,
öffentliche KMU-Studien); die Haupt-Sitzung prüfte die belastungsrelevanten Aussagen selbst nach,
darunter die Installationswege von Hexis, Lindy und Fig. Die Firecrawl-CLI war nicht installiert;
die Recherche lief über die verfügbaren Web-Werkzeuge. Alle externen Quellen wurden am 2026-09-19
abgerufen; vollständiges Verzeichnis mit Abrufdatum und Grenzen:
[`docs/product-plan.md`](docs/product-plan.md), Abschnitt *Sources and evidence limits*.

Ein früherer Versuch, externe Recherche zu starten, wurde von der Rechteprüfung blockiert; das erklärt
den Hinweis auf „blockierte Recherche" im älteren Teil des Plans. Sie wurde anschließend nachgeholt.

---

**Nicht Teil dieses Sign-Offs:** Preise, Umsatzannahmen, Liefertermine, Teamzusagen,
Veröffentlichungsfreigaben. Was fehlt, steht in §11 — nicht als Lücke versteckt.
