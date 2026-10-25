# Entscheidungen — Company Harness

Chronik dieses Workspaces. **Anhängen, nicht überschreiben.** Verworfene oder ersetzte Entscheidungen
bleiben stehen und werden als ersetzt markiert. Jede Zeile trägt Datum und Quelle.

Unterschied zum Delta-Weave-Hub: `D:\OneDrive\Delta Weave\decisions\log.md` ist die Chronik der Firma und
aller Projekte. Hier stehen nur Entscheidungen, die die Umsetzung des Company Harness betreffen.
Richtungsänderungen am Produktumfang werden zusätzlich im Hub-Knoten
`D:\OneDrive\Delta Weave\projects\company-harness.md` nachgezogen.

---

## 2026-09-19 — Workspace angelegt, Produktplan aus dem Hub verschoben

**Entscheidung:** Der Company Harness bekommt einen eigenen Workspace unter
`C:\Users\Admin\Documents\Company-Harness`; dort beginnt die initiale Umsetzung. Der recherchierte
Produktplan wurde aus `D:\OneDrive\Delta Weave\projects\company-harness.md` hierher **verschoben**, nicht
kopiert. Im Hub bleibt ein schlanker Verweisknoten. Manuels ursprüngliche Konzeptfassung wurde als
`docs/sources/konzept-ursprung-2026-09-19.md` gesichert, weil die Session-Anlage unter
`C:\Users\Admin\.qoder\tmp\` vergänglich ist.

**Grund:** Der Hub ist das Verzeichnis über Person, Firma und Projekte — nicht der Ort für
Umsetzungsunterlagen. Dieselbe Trennung gilt bereits für ATHA, FinanzMehrwert und den job-agent.
Quelle: Manuel, direkte Angabe im Chat, Stand 2026-09-19.

**Anwendung:** Neue Fakten zur Umsetzung gehören hierher. Neue Fakten zu Person, Firma, Vertrieb oder
Freigaben gehören in den Hub. Kein Duplikat an beiden Orten.

## 2026-09-19 — Git ohne Remote

**Entscheidung:** Der Workspace wird als lokales Git-Repo initialisiert, ohne Remote und ohne
Veröffentlichung. Quelle: Manuel, Auswahl im Chat, Stand 2026-09-19.

**Grund:** Umsetzung bekommt sofort Versionsgeschichte; über ein GitHub-Repo und dessen Sichtbarkeit
entscheidet Manuel später. Der Hub selbst ist privat und push-bedingt empfindlich — dieselbe Vorsicht
gilt hier, sobald echte Kundendaten ins Spiel kommen.

**Grenze:** Kein Push, kein öffentliches Repo, kein Hinzufügen von Kundendaten ohne Freigabe.

**Status: ersetzt** am selben Tag durch „Privates GitHub-Repo eingerichtet" (unten). Die Grenze zu
Kundendaten gilt unverändert weiter.

## 2026-09-19 — Vorschlag, nicht bestätigt: zwei Prüfprozesse vor jeder Plattform

**Entscheidungsvorschlag:** Kundenänderung → abgestimmter Lieferplan und erbrachte Leistung →
rechnungsbereite Nachweise werden als erste Prüfprozesse vorgeschlagen, zuerst in der vorhandenen
Qoder-/Datei-Arbeitsweise. Hexis und Oracle werden erst danach gegen dieselben Abnahmekriterien
verglichen. Quelle: Agentenanalyse, [`CONTEXT-SIGNOFF.md`](CONTEXT-SIGNOFF.md) §3 und §10, Stand 2026-09-19.

**Status: teils entschieden** am selben Tag, siehe „Prototyp-Plan" unten. Die Reihenfolge ist überholt;
der Vorrang der Datei-Baseline vor jeder Plattform bleibt bestehen und ist jetzt bestätigt.

## 2026-09-19 — Prototyp-Plan: Baseline zuerst, beide Prüfprozesse parallel

**Entscheidung:** Der erste Prototyp-Schritt ist die beaufsichtigte Baseline in der vorhandenen
Qoder-/Datei-Arbeitsweise; eine dauerhafte Case-Engine wird erst gebaut, wenn der Kontextnachweis erbracht
ist. Beide Prüfprozesse — Kundenänderung → Lieferplan und Leistung → rechnungsbereite Nachweise — laufen
von Anfang an parallel. Quelle: Manuel, zwei Auswahlangaben im Chat, Stand 2026-09-19.

**Grund:** Die Baseline liefert die Evidenz zu `CONTEXT-SIGNOFF.md` §10 Schritt 1–4, bevor Baukosten
entstehen. Parallele Prozesse prüfen die geteilte Architektur an zwei Fällen statt sie von einem Fall
hochzurechnen; der Preis ist doppeltes Fallmaterial pro Runde.
Quelle: Manuels Angabe; Abwägung in [`docs/prototype-plan.md`](docs/prototype-plan.md) §0.

**Anwendung:** Meilensteine M0–M5 mit je einer Abbruchbedingung stehen in
[`docs/prototype-plan.md`](docs/prototype-plan.md) §7. Die Reihenfolge-Empfehlung aus §3 des Sign-Offs
(Änderung zuerst) ist damit überholt und bleibt als Vorschlag stehen.

## 2026-09-19 — Fallmaterial synthetisch: abgeleitet, nicht entschieden

**Entscheidung:** Der Prototyp arbeitet durchgehend mit erfundenem Material, fiktive Firma „Nordwind
Betriebstechnik". **Status: aus dem Regelbestand abgeleitet, nicht von Manuel entschieden.**

**Grund:** `AGENTS.md` Regel 4 und `CONTEXT-SIGNOFF.md` §5 Regel 4 schließen echte Mail-, Kalender-,
Buchhaltungs- oder Kundenzugänge ohne ausdrückliche Freigabe aus; eine Freigabe liegt nicht vor.
Synthetisches Material ist der einzige Weg, der die Regel nicht berührt.

**Grenze:** Der Nachweis gilt damit für die Architektur, nicht für die Markthypothese. Welche echten
Quellen gelesen werden dürften, bleibt `OFFEN — Manuel` in §11 Punkt 3 des Sign-Offs.

## 2026-09-19 — Privates GitHub-Repo eingerichtet

**Entscheidung:** Der Workspace bekommt ein **privates** GitHub-Repo unter
`https://github.com/melkor42/Company-Harness` und wird dorthin gepusht. Quelle: Manuel,
Sichtbarkeitsangabe im Chat sowie eigene Anlage des Repos, Stand 2026-09-19.

**Grund:** `CONTEXT-SIGNOFF.md` §11 Punkt 9 war offen („Wann und ob ein privates GitHub-Repo folgt").
Zwei GitHub-Konten sind auf diesem Rechner im Gebrauch — `ManuelOnemundi` für ATHA und FinanzMehrwert,
`melkor42` für Delta-Weave, Held, MMC-Delta und job-agent. Die Wahl fiel auf `melkor42`, das Konto des
Hub-Repos.

**Vorgeschichte, damit der Irrtum nicht wiederholt wird:** Ein erster Prüflauf hatte ergeben, es sei kein
GitHub-Zugang vorhanden. Das war falsch: `gh` fehlt zwar, aber Git Credential Manager ist **systemweit**
konfiguriert (`C:/Program Files/Git/etc/gitconfig`, `credential.helper = manager`) und funktioniert über
HTTPS. Wer nur `git config --global` liest, übersieht es. Der vorhandene SSH-Schlüssel ist dagegen bei
GitHub nicht hinterlegt.

**Grenze:** Privat, nicht öffentlich. `oeffentlichkeit.md` liegt außerhalb dieses Workspaces und konnte in
dieser Sitzung nicht gegengeprüft werden; ein Screenshot oder Zitat aus dem Repo gilt bereits als nach
außen und ist zurückgestellt. Kein Kundenmaterial, keine Credentials, kein automatischer Push.

**Korrektur am selben Tag:** Der Halbsatz „konnte nicht gegengeprüft werden" war falsch und ist durch eine
Prüfung ersetzt. Eine Verzeichnisauflistung des Hubs über die Shell wird von der Rechteprüfung abgewiesen,
das gezielte Lesen einer benannten Datei dagegen nicht. `MAP.md` und `company/oeffentlichkeit.md` wurden
nachgelesen: Company Harness steht auf keiner der drei Listen der Freigabeliste, und `MAP.md` führt den
Knoten mit „intern, keine Veröffentlichungsfreigabe". Am Ergebnis ändert sich nichts — privates Repo
zulässig, jedes Zitat nach außen nicht. Festzuhalten bleibt der Fehler: **Nicht aus einem geblockten `ls`
auf unlesbare Inhalte schließen.**

## 2026-09-20 — M0 und M1 gebaut; der Validator ist die Durchsetzungsstelle

**Entscheidung:** Die vier Verträge liegen als JSON-Schema unter `schema/` und als Beispieldateien unter
`prototype/`. Der Korpus ist eine erfundene Firma mit sechs Quelldokumenten, zwanzig Kontextdatensätzen,
zwei Prozessen, vier Fällen und vier Sandbox-Schreibzielen. `node prototype/tools/validate.mjs` prüft den
Bestand; jede Prüfung ist mit einem Negativbeleg verifiziert.

**Fünf Punkte, die beim Bauen anders kamen als im Plan und hier nachgezogen sind:**

1. **Ein fünftes Schema.** Der Fallvertrag hat zwei Dateien: `fall.json` (unveränderlich) und
   `runs/<fall>/state.json` (der wandernde Zustand). Ohne eigenes Schema wäre der Zustand — die eigentliche
   Behauptung des Produkts — der einzige ungeprüfte Teil des Bestands geblieben.
2. **Ein viertes Sandbox-System.** `postausgang.json` kam dazu, weil die Kundennachricht die Aktion ist, an
   der sich Duplikat-Schutz und nutzlastgebundene Freigabe zeigen muss. Drei Dateien hätten das nicht
   geprüft, sondern behauptet.
3. **Die Laufprüfungen sitzen im Validator, nicht erst in der Engine.** Eine Aktion, die ihre
   Prozessdefinition nicht vorsieht, ein abweichendes Schreibziel, `ausgeführt` ohne Freigabeeintrag, ein
   Idempotenzschlüssel zweimal: Das wird jetzt ab M1 abgewiesen, obwohl die Engine erst in M4 entsteht. Eine
   Allowlist, die nur im Kopf des späteren Programms existiert, ist keine Grenze.
4. **Ein Muster ist kein Kalender.** `stand` war gegen `\d{4}-\d{2}-\d{2}` geprüft und ließ `2026-02-30`
   durch. Seither prüft der Validator den Kalenderdatum-Wert, nicht nur seine Form.
5. **`supersedes` war ein Feld ohne Benutzung.** Die Störung „Evidenz ändert sich nach der Freigabe" war nur
   im erwarteten Ergebnis beschrieben. Jetzt liegt der Nachfolger-Datensatz mit `supersedes` real im Korpus
   (`kap-kest-frei-bis-termin-2026-09-21`, 0,8 PT statt 2,3 PT) — sonst könnte M2 die Störung nicht setzen.

**Zwei eigene Fehler, aufgeschrieben damit sie sich nicht wiederholen:** Der Verzeichnisläufer des
Validators hatte bei verschachtelten Ordnern den Präfix doppelt gesetzt; dadurch liefen die
Fallordner-Prüfungen in M0 nie an, obwohl der Lauf „OK" meldete. Entdeckt wurde er erst, als Fälle
existierten — **ein Prüfer, der nichts findet, weil er nichts sieht, ist kein Prüfstand.** Und die
Anordnung `/aktion.*\.json$/` hätte eine `state.json` in `runs/` still übersprungen; seither fällt jede
JSON-Datei dort, die auf keine Zuordnung passt, als Fehler auf.

## 2026-09-20 — M1 heißt „gebaut", nicht „bestanden"

**Entscheidung:** In der Meilensteintabelle des Prototyp-Plans steht M1 auf **gebaut, nicht bestanden**. Der
Prüferspruch — ein Mensch ohne Vorwissen sagt je Fall „stimmt" oder „stimmt nicht" — steht aus.

**Grund:** Die Fälle, ihre erwarteten Ergebnisse und dieser Bestand stammen aus einer Hand (Agent,
2026-09-19/20). Die Regel „wer den Fall geschrieben hat, darf ihn nicht ausgewertet haben" gilt auch gegen
den eigenen Befund: Ein vorab geschriebenes Ergebnis ist nur dann ein Maßstab, wenn jemand anderes es
gegenlesen hat. M2 gegen einen unbestätigten Maßstab laufen zu lassen wäre ein Nachweis ins Leere.

**Anwendung:** Vor dem ersten A/B-Lauf ist `prototype/cases/*/erwartet.md` von einer Person ohne
Sitzungsvorwissen gegenzulesen; das Ergebnis kommt in `prototype/evaluation/MESSPROTOKOLL.md` §2 und diese
Zeile gilt als erledigt.

## 2026-10-09 — Das Ziel dieser Phase heißt Evaluierung; Manifest und Gegenlese getrennt

**Entscheidung (Manuel, Diktat 2026-10-09):** Das Ziel der laufenden Arbeit ist die **Evaluierung**, nicht
das Produkt. Seine Haltung dazu steht in [`docs/manifest.md`](docs/manifest.md) und gilt als bestätigte
Position — neben §2 des Sign-offs, nicht darunter.

**Entscheidung (Agent, 2026-10-09):** Die Gegenlese liegt als eigene Datei
[`docs/manifest-gegenlese.md`](docs/manifest-gegenlese.md), nicht als Abschnitt im Manifest.

**Grund:** Standpunkt und Kritik aus einer Datei lassen sich später nicht mehr trennen; dann ist nicht mehr
erkennbar, was Manuel gesagt hat und was ein Agent eingewandt hat. Dieselbe Trennung, die der Sign-off
zwischen *Bestätigt* und *Vorschlag* zieht.

**Anwendung:** Die fünf Planänderungen aus der Gegenlese §5 (Rückfragen zweigeteilt zählen; Bedingung C mit
Minimalkontext; Rückführungsregel für Ergebnisdokumente; Fallansicht in M2; Kontextbeschaffung als
Prüfpunkt) sind **Vorschläge**. Was Manuel davon annimmt, wird hier als eigener Eintrag festgehalten und
dann in Messprotokoll und Prototyp-Plan nachgezogen — nicht vorher.

## 2026-10-10 — Gegenlese angenommen; Recherche zur Kontext-Verwaltung angesetzt

**Entscheidung (Manuel, 2026-10-10):** Er stimmt der Gegenlese in
[`docs/manifest-gegenlese.md`](docs/manifest-gegenlese.md) überein — „absolut der gleichen Meinung". Damit
gelten die fünf Planänderungen aus deren §5 als **angenommene Richtung** (Rückfragen zweigeteilt zählen;
Bedingung C mit Minimalkontext; Rückführungsregel; Fallansicht in M2; Kontextbeschaffung als Prüfpunkt).
Der Nachzug in Messprotokoll und Prototyp-Plan steht noch aus und ist eigener Arbeitsschritt.

**Zusatz (Manuel, 2026-10-10):** Die große Arbeit liegt im Verwalten des Kontexts. Er verwaltet seinen
eigenen Agenten-Kontext lokal als kleine Markdown-Dateien, die der Agent findet und benutzt; eine Lösung
muss an den Kontext der bestehenden Umgebung angepasst werden. Dazu ist eine Recherche angesetzt:
Best Practices für dateibasierte kuratierte Kontext-Setups gegenüber RAG-Systemen, Grenzen von RAG-only,
wann Retrieval nötig wird. Ergebnis wird in `docs/recherche-kontext-verwaltung.md` erwartet.

## 2026-10-11 — Ziel neu gefasst: Brauchbarkeit über Unternehmen hinweg; Messbetrieb zurückgestellt

**Entscheidung (Manuel, 2026-10-11):** Das Ziel ist neu gefasst: herausfinden, **was relevant ist, um einen
Harness für unterschiedliche Unternehmen nützlich und hilfreich zu machen**. Der große Hebel ist die
**Kontext-Kuration** — an ihr hängt, ob Ergebnisse effizient erzielt werden. Die bisherige Prototyp-Arbeit
(Testläufe, synthetische Firmendaten, M0/M1-Messapparat) hatte nach seiner Einschätzung kein echtes, von
ihm vorgegebenes Ziel und stört die Konzeptdiskussion eher, als dass sie sie trägt. Er erwägt die Löschung;
die Entscheidung darüber steht aus.

**Anwendung:** Die acht Fragen der laufenden M2-Runde sind hinfällig und werden nicht beantwortet. Die
Arbeit läuft auf der Konzeptebene weiter; Grundlage bleiben Manifest, Gegenlese und die
Kontext-Recherche. Der Umgang mit dem Prototyp-Bestand (löschen, einfrieren, teilweise übernehmen) wird
als eigene Entscheidung geklärt und hier festgehalten.

## 2026-10-11 — Company Harness wird ein Skill: geführter Einstieg statt Messprüfstand

**Entscheidung (Manuel, 2026-10-11):** Das Produkt wird ein **Skill**: ein geführtes Setup, das eine Person
an die Hand nimmt, die zum ersten Mal einen Harness benutzt — der Skill soll der erste Aufruf beim Einstieg
sein können. Inhalt zwei Seiten: erstens Erklärung, was ein Harness ist und wie diese Systeme funktionieren
(sein eigener Einstieg war schwer, weil „Harness" ein Konzept ist und nirgends lag, was wie wo funktioniert);
zweitens und wichtiger: **Grundkontext abfragen und aufbauen** — Personenprofil (USER.md, Muster ist sein
delta-profile-Skill), AGENTS.md (was soll der Agent erfüllen), Workspace-Vision und Herausforderungen,
Dateistruktur (agent-first abgelegt, privater Bereich getrennt, über Geräte teilbar), Regeln mit
Verfallsdisziplin (veraltete Regeln richten mehr Schaden an als sie nutzen), Memory-System (wo die Dateien
liegen, wie sie funktionieren, was dort abgelegt wird — harness-abhängig, muss dem Nutzer erklärt werden).
Inhaltsquelle: seine eigenen Monate Agentenarbeit und sein bestehendes Setup. Zielgruppe: Anwender aus der
Chatfenster-Welt, denen „Harness" ein Fremdwort ist; der Einstieg muss nicht schwierig sein, und der Harness
soll proaktiv unterstützen, ohne dass man fragen muss. Soul-Files hält er für unbewiesen — allenfalls als
optionaler, skeptisch kommentierter Baustein.

**Repo-Bestand:** Die bestehenden Artefakte sollen weg (seine Worte: „besitzen keinen Wert"; Sicherung ist
die Git-Historie). Der Umfang der Löschung wird vor Ausführung bestätigt.

**Anwendung:** Der Messprüfstand (M0–M5, A/B-Pläne) ist ersetzt; die Einträge davor bleiben als Vorgeschichte
stehen. Nächste Schritte: Inventur seines Setups, dann Aufbau des Skills mit dem skill-creator.

## 2026-10-11 — Skill-Parameter: neutraler Kern mit Qoder-Anhang, Name „company-harness"

**Entscheidung (Manuel, 2026-10-11):** Der Skill wird **harness-neutral im Kern** aufgebaut — Grundkontext,
Regeln, Memory, Dateistruktur werden herstellerübergreifend erklärt — mit einem **Qoder-Anhang** als
erstem konkreten Anhang (echte Pfade, settings.json, Besonderheiten). Weitere Harness-Anhänge (Claude
Code, Cursor) kommen später. Begründung: Viele Erklärungen sind harness-abhängig und müssen dem Nutzer
als solche erkennbar sein; reine Neutralität würde den Einstieg wieder schwer machen.

**Name:** `company-harness` (Produktname, Aufruf `/company-harness`).

**Anwendung:** Referenzdateien des Skills trennen neutrale Konzepte von Anhängen je Harness; jede
herstellerspezifische Angabe steht in einem Anhang, nie im Kern.

## 2026-10-12 — harness-mentor auf Essenz reduziert (16 → 10 Dateien)

**Entscheidung (Manuel, 2026-10-12):** Nach dem Bau wird der Skill gegen die Frage geprüft „ist das
notwendig und hilfreich, oder kann es im Weg stehen" — und auf die Essenz reduziert. Begründung in
seinen Worten: keine Regeln aufstellen, die im Weg stehen, keine Workflows ohne Notwendigkeit, keine
Einschränkung der Kreationsvielfalt. Aus seiner eigenen Harness-Arbeit: Es wurden kaum Regeln
dokumentiert, weil alte entschiedene Regeln den Agenten oft aufhalten statt zu führen — Regeln, die
führen, sind wichtig; Regeln, die blockieren, sind der Feind.

**Getilgt als Apparat:** `BEGLEITSTAND.md` samt Format-Referenz und Einladungs-Snippet — der Stand
der Begleitung lebt jetzt als `project-`-Memory-Eintrag (der Mentor benutzt das Gedächtnis, das er
einrichtet); `auszug.md` — die Führungsgrade waren ohnehin die Vertrauensrampe in der AGENTS.md,
Übergänge und die letzte Geste stehen jetzt als Absatz in der Begleiten-Disziplin;
`ehrlichkeit-und-verifikation.md` — Essenz in SKILL-Grundhaltung (Regel ist Bitte, keine Sperre)
und Block 6 (Ladeprüfung); `gedaechtnis-hygiene.md` — Essenz in Block 5 (Dreiteilung,
Umkehrbedingung, Fundortpflicht, was nie in den Bestand gehört).

**Quelle better-harness (v0.2.21), gelesen am selben Tag:** Der Skill bleibt separat und wird separat
aufgerufen. Übernommen nur drei Schärfungen: Schweigen als protokolliertes Standardergebnis mit
Stufen (drohender Verlust durchbricht das Eine-Regung-Limit); „festgehalten ist nicht angekommen"
als sechste Spur; die Zwei-Vorkommen-Schwelle deckt sich mit deren 2-Episoden-Disziplin.

**Neu integriert:** „Regeln führen oder blockieren" als Lehre in Block 3; das TL;DR-Verhalten
(lange Ergebnisse: Kern in wenigen Sätzen zuerst, To-dos der Person sichtbar hervorgehoben) als
Musterbeispiel einer führenden Regel in Block 3 und der AGENTS.md-Vorlage — und als eigene
Ausgabedisziplin des Mentors in der Grundhaltung. Quelle: Manuel, Diktat 2026-10-12.

**Anwendung:** Persona-Probeläufe prüfen künftig auch, ob die Essenz-Fassung trägt. Der Delta-Weave-
Hub-Knoten braucht keinen Nachzug — Produktumfang unverändert, nur schlanker umgesetzt.

## 2026-10-12 — Probelauf des v1-Skills: zwei Konstruktionsfehler, sofortige Korrektur

**Befund (Manuel als Testnutzer, 2026-10-12):** Der v1-Skill lief als Probelauf in diesem Workspace.
Zwei Fehler: erstens waren die Block-1-Fragen flach — ohne Zweckansage kann der Nutzer nicht wissen,
was seine Antwort bewirkt; zweitens fragte die Delegier-Frage („selbst entscheiden oder delegieren?")
eine stabile Präferenz ab, die ein Neueinsteiger gar nicht haben kann — ob jemand delegiert, hängt am
Vertrauen, und Vertrauen wächst durch Gebrauch, nicht durch Interviewantwort.

**Korrektur (mit Manuels Freigabe, 2026-10-12):** Delegier-Frage gestrichen; Autonomie wird
voreingestellt (*eng führen*, Lockerungen als datierte Regeln — „Vertrauensrampe"); Zweckansage und
Prüfstein („ändert die Antwort ein benennbares Agentenverhalten?") als Gesprächsregeln; Block 3 beginnt
die AGENTS.md mit der datierten Startregel. Eingebaut in
`.qoder/skills/company-harness/references/interview-leitfaden.md` und in den v2-Leitfaden übernommen.

## 2026-10-12 — Fünf Linsen synthetisiert; neuer Skill harness-mentor (v2) angenommen

**Entscheidung (Manuel, 2026-10-12):** Der Plan aus der Synthese der fünf parallelen
Modell-Explorationsläufe vom selben Tag ist angenommen; v2 entsteht als neuer Skill
`.qoder/skills/harness-mentor/`. Architektur: zwei Modi (**Einrichten**/**Begleiten**), entschieden an
`BEGLEITSTAND.md`; Dreiteilung **Einladung** (≤3 Zeilen immer geladen, mit Ausschalter) / **Programm**
(der Skill) / **Stand** (BEGLEITSTAND.md); Didaktik-Kern aus drei Grundbildern (fremde Arbeitskraft mit
begrenztem Gedächtnis, Kontext als einzige Hebelstelle, Vertrauen als Korrigierbarkeit); Anstoß-Disziplin
(Schweigen-Standard, fünf Reibungsspuren ab zweitem Vorkommen, vier zulässige Anstöße, max. eine Regung
pro Sitzung); Auszug in Stufen mit Abnahmeprüfung; Ehrlichkeits-Regeln (Fähigkeiten nur aus der echten
Werkzeugliste, Ladeprüfung) und Gedächtnis-Hygiene (Dreiteilung, Umkehrbedingung, Fundortpflicht).

**Grund:** Die fünf Läufe konvergieren unabhängig auf dieselben Mechanismen (Vertrauen operationalisiert
als Prüf-/Vorhersag-/Korrigierbarkeit; Begleitstand als Persistenzmuster; Mentor mit eigenem Ende).
Stärkstes Validierungssignal: Zweckansage/Prüfstein (Probelauf) und ccaabs „doppelte Ertrag-Regel" sind
unabhängig dieselbe Regel. Quelle: die fünf Qoder-Sessions vom 2026-10-12, Destillation durch vier
parallele Agenten, Synthese in dieser Session.

**Anwendung:** v1 (`company-harness`) bleibt als Artefakt erhalten; v2 führt die Linie weiter.
Entwicklungsmethode: echte Probeläufe mit Personas (Chat-Neueinsteiger, erfahrene Entwicklerin,
stale-memory-Frust) statt geschriebener Beispieldialoge; Befunde werden wie am 2026-10-12 eingebaut.
Offen: Distribution/Auffindbarkeit (v2 bleibt manueller Aufruf); die Gabel aus Lauf fa76, ob der
erklärende Teil dauerhaft zum Produkt gehört — vorerst ja, als Didaktik-Kern.

## 2026-10-12 — Zielgruppe universell; Einordnung wird Teil des Kennenlernens

**Entscheidung (Manuel, 2026-10-12):** Der Skill hilft nicht nur der Chat-Welt, sondern jedem, der mit
einem Harness arbeiten will — Vorbild grill-me von Matt Pocock: für Entwickler gedacht, hilft bei
besseren Entscheidungen aber jedem. Entwickler werden definitiv abgefangen; Early Adopter sind
neugierige, selbstmotivierte Unternehmer breiten Spektrums. Die Einordnung (Arbeitskontext, Ziele) ist
Teil von Block 0 des Einrichtens: Sie wählt Beispiele und Tempo (Passung), steckt aber niemanden in eine
Schublade.

**Zusatz (Manuel, 2026-10-12):** Der Planungsmodus und die Intention des Planens im Vergleich zum Chat
war selbst eine Lernhürde — aufgenommen als Lernelement „Harness-Modi" in
`.qoder/skills/harness-mentor/references/didaktik.md`.

## 2026-10-24 — Absicht vor Auftrag: Intent-Driven Creation im Mentor verankert

**Entscheidung (Manuel, 2026-10-24):** Die Ideen aus *Die Architektur der Intention* fließen in den
aktuellen Skill `harness-mentor` ein — nicht als Essay-Logik, sondern als vierte Grundhaltung: Der
Agent fragt nach der Absicht hinter einem Auftrag, sucht das große Ganze und nutzt vorhandenes Wissen,
Entscheidungen und verworfene Wege als Hintergrund. Absicht und Auftrag bleiben unterscheidbar;
Festlegungen und Vermutungen auch. Umsetzung: viertes Grundbild, Block 2 des Einrichten-Leitfadens
(Absicht und Ziel), VISION- und AGENTS-Vorlage, Abschluss-Gegenprobe.

**Grund:** In einem unbekannten Frontier-Umfeld ist die Umsetzung billig geworden; der Engpass ist die
Wahl der richtigen Richtung. Ein Harness, der nur Aufträge ausführt, optimiert das Falsche mit großer
Sicherheit — je schneller, desto teurer. Quelle: Manuels Essay
`C:\Users\ASUS GAMING\OneDrive\Delta Weave\paper\Die_Architektur_der_Intention.md`, Stand
2026-10-23; Idee im Chat vorgetragen am 2026-10-24.

**Grenze:** Keine Übernahme der vollständigen Essay-Argumentation (Zeitdimension, Anreizsysteme,
Computerarchitektur). Der Skill bleibt ein Einstiegs-Guide; die Vertiefung gehört in den Essay, nicht
in den Grundkontext. v1 (`company-harness`) bleibt Artefakt und wird nicht nachgezogen.

## 2026-10-24 — Evals für harness-mentor: Baseline, Trigger-Konkurrenz, kontaminierte Ablation

**Entscheidung (Manuel, 2026-10-24):** `harness-mentor` bekommt eine schmale Evalschicht unter
`evals/` — kein Unit-Testing um des Testens willen, gemessen wird nur, was das Verhalten ändert:
Trigger (feuert der Skill im richtigen Moment, nicht bei jedem Coding-Task), Kontinuität (bleibt die
Begleitung nach Wochen aktiv), verfrühte Harness-Artefakte. 14 Fälle (P1–P8 positiv, N1–N6 negativ),
stdlib-Runner, frischer Workspace je Lauf, Rohspuren als NDJSON, Bericht als Markdown und JSON.
Läufe je Fall 2–3 wegen Modellstreuung; Baseline mit Skill-Hash eingefroren.

**Ergebnis Baseline:** 35 Läufe, Trigger 34/35 (21/22 positiv, 13/13 negativ), Auto-Modus 34/35,
18,48 Credits. Einziger Fehlschlag: P3, in allen drei Baseline-Läufen lud zuerst `writing-for-agents`,
`harness-mentor` in 2/3. Varianzläufe (P3 und N3 je 3): P3 3/3, N3 3/3, 3,02 Credits; kombiniert P3
5/6, gesamt 40/41 (97,6 %). Gültige Messung: 25,65 Credits. Kontinuität trägt: P5/P6 lesen die
Workspace-`memory/`, P7 setzt den Grad auf „aus", P8 benennt die fehlende Notiz statt Historie zu
erfinden. P1–P4 und alle Negativfälle legen keine Harness-Artefakte an. Bericht:
`evals/results/2026-10-24-baseline.md`, `…-variance.md`.

**Ablation:** 10 Läufe, 4,15 Credits — als Aussage unbrauchbar. Ohne kopierten Skill konnte das
Modell die echten Skill-Dateien per Pfad lesen (P2 Lauf 2, P3 Lauf 1, P4 2/2, P5 2/2; sauber nur P1,
P2 Lauf 1, P3 Lauf 2). Der Test prüft „Skill nicht geladen", nicht „Skill unerreichbar". Ergebnis
dokumentiert in `evals/results/2026-10-24-ablation.md`; keine Kürzung des Skill-Textes darauf gestützt.

**Behobene Runner-Fehler:** cp1252-Spuren (zeilenweise UTF-8/cp1252 dekodieren, danach UTF-8
normalisieren); `--permission-mode dont_ask` blockiert alle Schreibzugriffe (→ `accept_edits`);
`cwd` auf Repo-Wurzel ließ die echte `AGENTS.md` durchsickern (→ Workspace als cwd). Verworfene
Baselines (17,23 und 19,27 Credits) sind keine Ergebnisse und stehen nicht in den Berichten.

**Grenzen:** Der Workspace liegt im Repo — das Modell kann die Repo-`AGENTS.md` per Pfad lesen; das
beeinflusst Antwortinhalte, nicht die Trigger-Entscheidung (N3 6/6). P5s Seed behauptet USER.md,
AGENTS.md und `private/`, legt aber nur `memory/` an — P5 Lauf 3 fragte korrekt nach. P7 prüft grob
auf „aus" (trifft auch „Pause"); maßgeblich ist die Sichtprüfung. Rohspuren enthalten Umgebung
(globale Memory-Dateinamen, Pfade); das Repo ist öffentlich — Veröffentlichung von `evals/results/`
entscheidet Manuel. Kontinuität ist über geseedete Notizen simuliert, nicht über echte Wochen.

**Anwendung:** Baseline eingefroren (Skill-Hash
`99a043a4cad8af773d0aded0d3b02dc193a06f0524afbdb5c67d6c69a4d47b9e`). Jede Änderung an `SKILL.md`
läuft mindestens gegen P3 und den geänderten Fall; keine unbewerteten Kürzungen. Ablation erst nach
sauberem Aufbau (Workspace außerhalb des Repos oder isolierte Konfiguration).

**Nächster Schritt:** (1) P3-Beschreibung annehmen oder schärfen (Konkurrenz zu `writing-for-agents`),
(2) saubere Ablation, (3) P5-Seed vervollständigen, (4) echter Retention-Check über Wochen,
(5) Veröffentlichung der Evals entscheiden. Hub nicht nachgezogen — der Produktumfang ist unverändert,
die Evalschicht ist Prüfung, kein Produktbestandteil.


## 2026-10-25 — Harness Mentor bleibt; Namensangleichung und Funktionsabgleich

**Entscheidung von Manuel:** Der zunächst gewünschte Name Set Me Up ist ersetzt durch
**Harness Mentor**. Der vorhandene aktuelle Skill und sein technischer Name `harness-mentor`
bleiben erhalten. Ziel ist persönliches Onboarding und zurückhaltende Begleitung bis zur
Eigenständigkeit. Funktionale Erweiterungen sind nur zu analysieren und vorzuschlagen.
Quelle: Auftrag und anschließende Namenskorrektur im aktuellen Chat, Stand 2026-10-25.

**Durchgeführt:** GitHub-Repository nach `melkor42/harness-mentor` umbenannt; Admin-Recht,
neuer Name und Weiterleitung der alten Adresse über GitHub CLI/API geprüft. Lokales `origin`
aktualisiert. Aktuelle Titel, Repository-README, Website-Texte und Links in beiden Sprachen
angeglichen. Hub-Knoten nach `projects/harness-mentor.md` verschoben und MAP, Projektregister,
Querverweise, aktuelle Regel und Freigabeliste aktualisiert. Der Hub liegt auf diesem Rechner
unter `C:/Users/ASUS GAMING/OneDrive/Delta Weave`. Historische Quellen, ältere Entscheidungseinträge,
Eval-Berichte und der als Vorgänger dokumentierte `company-harness`-Skill bleiben als damaliger
Bestand erhalten. Keine Funktionsänderung am aktuellen Skill vorgenommen.
Quelle: lokale Dateiprüfung, GitHub-CLI/API und Hub-Linkprüfung dieser Sitzung, Stand 2026-10-25.

**Bild:** Auf Manuels Rückmeldung ein neues Thumbnail passend zum Skill und zur bestehenden
Galerie-Bildsprache erzeugt, statt das verworfene Set-Me-Up-Motiv einzubauen. Im Website-Repo:
`assets/exhibits/harness-mentor.png` als Master und `harness-mentor.webp` für die Galerie.
Werkzeug: integriertes Imagegen; Motiv: offenes Tor, goldener Weg in die Eigenständigkeit,
Kontext-/Profil-/Orientierungssymbole, dunkles Blau und Gold. Der vollständige Prompt liegt
lokal unter `.scratch/thumbnail-prompt.txt`. Quelle: Manuels Bildauftrag und Imagegen-Ausgabe
in dieser Sitzung, Stand 2026-10-25.

**Analyse:** `docs/product-plan.md`, Abschnitt „Funktionsabgleich und Änderungsplan“ ist die
zuständige Stelle. Kernintention bereits vorhanden; prioritäre Lücken sind Bestandsdiagnose,
tatsächliche Dateikonventionen/Ladebelege, korrekte Sicherheitsgrenzen und verlässliche,
nutzergesteuerte Wiederaufnahme. Die bestehende Architektur bleibt vorgeschlagenes Fundament.
Quelle: statischer Abgleich von Skill, Referenzen, Vorlagen und vorhandenen Evals, Stand 2026-10-25.

**Prüfung:** Skill-Validator erfolgreich; Eval-Fallliste unverändert ausführbar. Website-Build
und vorhandene Website-Tests erfolgreich; Hub-Prüfung erfolgreich. Desktop-Galerie und
Detaildialog im lokalen Browser kontrolliert, mobiler Text und Links ebenfalls sichtbar.
Impeccable-Detektor ohne Befund, aber nur Regex-Fallback; keine vollständige Kontrastprüfung.
Kein neuer verhaltensbezogener oder langfristiger Skill-Test durchgeführt.
Quelle: lokale Tool-Ausgaben und Browserprüfung dieser Sitzung, Stand 2026-10-25.

### Konkrete offene Handgriffe

- **Workspace-Ordner koordiniert umstellen:** Nach Ende laufender Chats/Prozesse
  `C:/Users/ASUS GAMING/Documents/Company-Harness` in
  `C:/Users/ASUS GAMING/Documents/Harness-Mentor` umbenennen. Projekt in Codex/Qoder am neuen
  Ort öffnen, workspacegebundene Memory-Zuordnung prüfen und aktuellen Arbeitsort im Hub
  (`projects/harness-mentor.md`, `infra/weitere-workspaces.md`, `MAP.md`, `decisions/rules.md`)
  nachziehen. Danach Git-Remote und Skill-Erkennung prüfen. Kein automatischer Umzug während
  dieses aktiven Chats und keine Junction als Ersatzlösung.
- **Veröffentlichung abstimmen:** Website und Skill-Dokumentation liegen lokal; noch kein Push
  und kein Website-Deploy. Bereits vor dieser Aufgabe vorhandene Änderungen in denselben Repos
  getrennt prüfen. Die Veröffentlichung der lokalen Eval-Ergebnisse bleibt eine eigene offene
  Entscheidung; sie nicht versehentlich mit veröffentlichen. Anschließend freigegebene Änderungen
  committen/pushen und beide Live-Sprachfassungen samt Bild und GitHub-Link prüfen.
- **Ältere Architektur-PNG erneuern:** `docs/architecture/harness-mentor-essenz.html` trägt den
  aktuellen Namen; die bestehende PNG ist noch der frühere Render. Vor Veröffentlichung der
  Architekturansicht nach der Anleitung in `docs/architecture/README.md` neu rendern und prüfen.
- **Andere Rechner und externe Verzeichnisse:** Nicht erreichbare Arbeitskopien, Bookmarks und
  installierte Vorgängerversionen auf alte Repo-/Workspace-Adressen prüfen. GitHub-Weiterleitung
  ist verifiziert, eine globale Prüfung aller Geräte ist nicht erfolgt. Die aktuelle lokale
  Skill-ID bleibt unverändert; dafür ist keine neue Installation nötig.
- **Änderungsplan entscheiden:** Nur die gewünschten funktionalen Punkte freigeben, anschließend
  gezielt gegen die betroffenen Szenarien testen. Bis dahin bleibt das Verhalten unverändert.

Quelle für Status und Pfade: lokale Bestandsaufnahme und Ausführung dieser Sitzung;
Veröffentlichungsgrenze zusätzlich `evals/README.md`, Stand 2026-10-25.


**Abschlussnachtrag:** Die Namenspflege im Hub ist lokal als Commit `53d0008` gesichert;
andere vorgefundene Änderungen sind nicht enthalten. Aktuelle README-Linkziele und die
geänderten Diff-Abschnitte sind geprüft. Die alte Architektur-PNG bleibt offen, weil die
Browser-Sicherheitsrichtlinie das Öffnen der lokalen HTML-Datei zum Rendern abgelehnt hat;
kein Umgehungsversuch. Quelle: Git-/Linkprüfung und Browser-Toolausgabe, Stand 2026-10-25.


## 2026-10-25 — Abschlussprüfung und lokale Commits des Gesamtstands

**Auftrag:** Manuel verlangt den Abschluss einschließlich der vorgefundenen Änderungen anderer,
Qualitätsprüfung und Bericht; „quitten“ wurde ausdrücklich zu „committen“ korrigiert. Funktionale
Erweiterungen aus dem Gap-Plan bleiben Vorschläge. Quelle: aktueller Chat, Stand 2026-10-25.

**Übernommene Vorarbeiten:** Das vierte Grundbild „Auftrag ist nicht Absicht“ ist konsistent in
Skill-Beschreibung, Didaktik, Einrichten-Leitfaden, AGENTS-/VISION-Vorlagen und Produktplan
verankert. Diese Änderungen waren bereits vor der Namensaufgabe vorhanden; die Aussage „keine
Funktionsänderung“ in deren Eintrag bezeichnet nur die damalige Namenspflege, nicht den gesamten
jetzt gesicherten Diff gegenüber HEAD. Eval-Runner, synthetische Fälle, Handoff und
Architekturansicht wurden mitgeprüft und lokal gesichert. Quelle: Git-Diff und Dateiprüfung,
Stand 2026-10-25.

**Website fertiggestellt:** Harness Mentor und Delta Profile haben eigene Galerie-Einträge,
Bilder, deutsche/englische Detailtexte und jeweils ihren Repository-Link. Die bisherigen
Mentor-Anker `skills-h` und `skills-story` bleiben erreichbar; Delta Profile hat eigene Anker.
Die Mentor-Bildvariante zeigt Begleitung am Tor und eigenständiges Weitergehen. Die bereits
vorhandenen Änderungen der anderen an Essay-Titel, Ausgabenbezeichnung und Harness-Erklärung
sind übernommen. Das gelieferte deutsche Essay-Bild ist im deutschen Teaser und auf der
Essay-Seite eingebunden. Überholte Bildentwürfe sind lokal unter
`../Delta-Weave/.scratch/asset-drafts/` erhalten. Quelle: Website-Dateien und Browserprüfung,
Stand 2026-10-25.

**Qualitätskorrekturen:** Dokumentation des früher gemeinsamen Skill-Eintrags aktualisiert;
widersprüchlichen Vorrang im Sign-Off beseitigt. Die Galerie korrigiert nun das automatische
horizontale Scrollen ihres verdeckten Containers bei Fragmentnavigation. Versionierte CSS-/JS-URLs
verhindern die Mischung von neuen HTML-Inhalten mit alten Styles oder alter Galerie-Logik.
Der bestehende Runtime-Test prüft weiter die tatsächlichen Skriptpfade und akzeptiert deren
Versionsparameter. Quelle: `../Delta-Weave/js/main.js`, HTML-/CSS-Dateien,
`../Delta-Weave/tests/learning.test.mjs`, Browserbefund, Stand 2026-10-25.

**Prüfergebnis:** Website-Build und alle vorhandenen Website-Tests erfolgreich. Beide Skill-
Detaildialoge, direkte Galerie-Anker, Bildladung, englische Repository-Zuordnung und mobile
Darstellung ohne horizontalen Seitenüberlauf im Browser geprüft. Die vollständigen Mentor- und
Delta-Profile-Bilder bleiben sichtbar. Skill-Validator und Python-Syntaxprüfung erfolgreich.
Der mechanische Design-Check fand im Regex-Fallback nichts; eine vollständige automatische
Kontrastanalyse ist damit nicht belegt. Quellen: lokale Prüfprotokolle unter `.scratch/`,
Website-Tests und Screenshots `.scratch/final-mentor-desktop.png`,
`.scratch/final-delta-profile-desktop.png`, `.scratch/final-mentor-mobile.png`, Stand 2026-10-25.

**Verhaltensprüfung mit Grenze:** Der erste P3/N3-Versuch konnte wegen Sandbox-EPERM nicht
starten und ist kein Verhaltensbefund. Im freigegebenen Wiederholungslauf erkannte P3 den Skill,
überschritt jedoch das Zeitlimit; N3 beendete sich ohne unerwünschten Trigger und bestand die
automatischen Checks. Daraus wird kein vollständig bestandener positiver End-to-End-Test und
keine neue Aussage zur Langzeitwirkung abgeleitet. Quelle:
`evals/results/2026-10-25-final-review-authorized.md` und zugehörige JSON/Rohspuren (lokal),
Stand 2026-10-25.

**Commit-Grenze:** Die geprüften Quellen werden in getrennten lokalen Repository-Commits gesichert.
`evals/results/`, lokale `.runs/`, Sandboxes und `.scratch/` bleiben gitignoriert. Die Rohspuren
werden erhalten; keine unbewertete Veröffentlichung. Kein Push und kein Deploy gehören zu diesem
Abschluss. Quelle: Manuels Commit-Auftrag, bestehende Veröffentlichungsentscheidung und `.gitignore`,
Stand 2026-10-25.

**Offen nach dem Commit:** Freigabe und Umsetzung des priorisierten funktionalen Änderungsplans;
belastbarer positiver Verhaltenslauf sowie echte Nutzungs-/Retention-Prüfung; gesonderte Freigabe
von Eval-Ausgaben und Veröffentlichung der Quellen; koordinierter Workspace-Umzug. Der ältere
Architektur-PNG-Render ist ausdrücklich als veraltet gekennzeichnet und vor externer Verwendung
neu zu erzeugen; seine aktuelle HTML-Quelle ist maßgeblich. Diese offenen Produkt- und
Veröffentlichungsschritte verhindern die lokale Sicherung des geprüften Arbeitsstands nicht.
Quelle: `docs/product-plan.md`, Architektur-README und diese Abschlussprüfung, Stand 2026-10-25.


**Commit-Nachweis Website:** `6ddbcde` — „Separate skill exhibits and finish Harness Mentor
presentation“. Website-Arbeitsverzeichnis nach Commit sauber; kein Push. Der eigene
Harness-Mentor-Commit enthält diesen Bericht. Quelle: lokale Git-Prüfung, Stand 2026-10-25.


## 2026-10-25 — Erweiterungen freigegeben; dev für Entwicklung, main für Installation

**Manuel hat freigegeben:** die vorgeschlagenen gezielten Erweiterungen des vorhandenen Skills.
Auf seine Frage zu den vielen Unterlagen folgt seine Entscheidung: bisherige öffentliche
Historie behalten; Entwicklung und Evals auf `dev`, aktueller Installationsstand auf `main`.
Quelle: Freigabe, Antwort zur Historie und Dev-Branch-Vorschlag im Chat, Stand 2026-10-25.

**Umgesetzt:** Bestandsdiagnose vor Einrichtung mit vorhandenen Dateien, Werkzeugen und
Ladewegen; Vorlagen an tatsächliche native Konventionen anpassen; vorhandene Freigaben
nicht zurücksetzen; ungelöste Konflikte mit Quelle/Geltungsbereich prüfen und Reparatur
anbieten. Aktuellen Memory-Zustand aktualisieren, Gründe kompakt erhalten und Routine-
Schweigeprotokolle vermeiden. Begleitstatus aktiv/pausiert/aus von Begleitgrad und externen
Handlungsrechten trennen; Pause und Ende respektieren. Wiedereinstieg nur durch erneute
Anfrage oder einen konkret verfügbaren, gewünschten und geprüften Mechanismus. Selbstständige
Anwendung ersetzt eine Pflichtprüfung des Begriffswortlauts. Hooks sind ausdrücklich keine
eigenständige Sicherheitsgrenze. Quelle: aktueller Skill unter `.qoder/skills/harness-mentor/`,
Stand 2026-10-25.

**Öffentliche Installation:** Nutzer-README, aktueller Skill, benötigte Referenzen und Vorlagen
stehen in der expliziten Dateiliste `scripts/package_skill.py`. Vorgänger-Skill, Evals,
Entscheidungsprotokolle, Planungsunterlagen und Entwicklungswerkzeuge gelangen nicht in den
aktuellen `main`-Baum. Die alte öffentliche Historie bleibt zugänglich. `dev` ist nach einem
Push in das öffentliche Repository ebenfalls öffentlich und daher kein Vertraulichkeitsort.
Persönliche Ausgaben/Rohspuren bleiben lokal ausgeschlossen. Quelle: Manuels Entscheidung und
Exportscript, Stand 2026-10-25.

**Branch-Verfahren:** Der bisherige lokale Entwicklungsstand heißt jetzt `dev` und ist nicht
mehr versehentlich an `origin/main` gekoppelt. `scripts/prepare_release.py` bereitet nach einem
geprüften Dev-Commit den lokalen `main` ausschließlich aus der Dateiliste über einen separaten
Git-Index vor; sein Parent ist der vorherige öffentliche beziehungsweise freigegebene Main-Stand.
Kein vollständiger Merge aus `dev`, kein Force-Push, keine History-Umschreibung. Der aktive
Dev-Checkout und sein Index werden nicht ersetzt. Das Verfahren ist in einem wegwerfbaren
synthetischen Git-Repo auf History-Erhalt, Installationsbaum und Idempotenz geprüft.
Quelle: `scripts/prepare_release.py`, `tests/test_prepare_release.py`, Stand 2026-10-25.

**Prüfung und Grenzen:** Paketgrenzen, nicht überschreibender Export, vollständige Pflichtdateien,
Ergebnis-Gate und Branch-Verfahren bestehen die lokalen synthetischen Tests. Skill-Frontmatter
und Python-Syntax werden geprüft. In Qoder erkannten die neuen Szenarien P9/P10/P11 den Skill;
P9/P11 beendeten sich mit bestandenen automatischen Checks, P10 endete im Zeitlimit. Manuell
waren globale Kontext-/Hook-Einflüsse sichtbar. Deshalb keine saubere Isolation oder
Freigabebehauptung aus diesen Läufen. Die zusätzliche Regression wurde abgebrochen; auch dort
ist der positive Fall nicht vollständig grün. Quelle: lokale Ergebnisse und Rohspuren unter
`evals/results/2026-10-25-vnext*`, `tests/`, Stand 2026-10-25.

**Konsequenz für künftige Tests:** Live-Läufe verlangen ein separat eingerichtetes Testprofil;
kein stiller Rückgriff auf das persönliche Qoder-Profil, keine Credential-Kopie. Ein Profil
allein erzwingt keine Dateisicherheitsgrenze. Der Runner meldet einen nicht erfolgreichen
Lauf auch dann als Fehler, wenn dessen Trigger erkannt wurde. Ein sauber isolierter
Verhaltenslauf und eine echte längere Nutzung bleiben offene Nachweise.
Quelle: `evals/run.py`, `evals/README.md`, Stand 2026-10-25.

**Auslieferung:** Installationsarchiv und lokaler Main-Branch werden zur Prüfung vorbereitet.
Kein Upload wird aus einer lokalen Vorbereitung abgeleitet; bisher weder Push noch Deploy
der Erweiterung. Hub-Knoten, MAP und Regelregister sind um Umfang und Branch-Entscheidung
nachgezogen. Quelle: lokale Ausführung und Hub-Prüfung, Stand 2026-10-25.
