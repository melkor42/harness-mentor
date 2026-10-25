# Handoff — Evals für `harness-mentor`

**Stand:** 2026-10-24
**Von:** Session im AI-Engineer-Archiv-Kontext (Delta Weave)
**Für:** Session im Company-Harness-Kontext
**Art:** Arbeitsauftrag, keine Entscheidung. Umsetzung, Freigabe und Commit liegen hier.

## Warum diese Datei existiert

Der Befund stammt aus einer Session, die nicht in diesem Repo arbeitet: Sie hat die Delta-Weave-Projekte
verglichen und das lokale AI-Engineer-Archiv nach passenden Talks durchsucht. Das Ergebnis gehört in
diesen Workspace, weil die Umsetzung hier stattfindet und der Kontext getrennt bleiben soll.

Diese Datei ist selbsttragend. Der aufnehmende Agent braucht die Quell-Session nicht. Er braucht nur
dieses Repo, die genannten Dateien und — wenn vorhanden — die Harnesse, in denen der Skill läuft.

## Der Befund in fünf Sätzen

1. `harness-mentor` hat **keine Evals**: keinen `evals/`-Ordner, keinen Runner, keine Testfälle.
2. Der letzte **dokumentierte** Test ist der v1-Probelauf mit Manuel als Testnutzer am 2026-10-12.
   v2 entstand danach aus fünf parallelen Modell-Läufen; ein v2-Probelauf ist in den Unterlagen
   nicht dokumentiert.
3. Die Entwicklungsmethode ist bewusst qualitativ: **echte Probeläufe mit Personas statt geschriebener
   Beispieldialoge**, plus eine Abnahme aus drei Erfahrungen und einem Retention-Check nach 2–3 Wochen.
4. Dadurch ist bei einem Fehlschlag nicht unterscheidbar: **Skill triggert nicht / Aufgabe zu schwer /
   Modell streut**. Genau diese drei Fälle brauchen unterschiedliche Korrekturen.
5. Die Behauptung **„harness-neutral"** ist nicht geprüft. Der Kern ist harness-neutral, der einzige
   Anhang ist Qoder; ein Lauf in Claude Code oder Cursor ist nicht dokumentiert.

Der Hub führt den Status deshalb als **„Wirksamkeit in Probeläufen und Distribution offen"**
(`D:\OneDrive\Delta Weave\MAP.md`, Stand 2026-10-23).

## Der Talk, der den Blindspot füllt

**„Don't Ship Skills Without Evals" — Philipp Schmid, Google DeepMind,
AI Engineer World's Fair 2026, 21:46.**

- Talk: https://ai.engineer/talks/0vphxNt4wyk-dont-ship-skills-without-evals
- Video: https://www.youtube.com/watch?v=0vphxNt4wyk

Die für diesen Auftrag entscheidenden Stellen:

- **Bestandsaufnahme:** Skills Bench hat über 50.000 Skills von GitHub indexiert; fast keiner hatte
  Evals, die meisten waren KI-geschrieben und ungetestet ([00:46](https://www.youtube.com/watch?v=0vphxNt4wyk&t=46s)).
- **Trigger ist der größte Einzelhebel:** „We have seen 50% of the failures because the skill was not
  triggered correctly" ([17:22](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1042s)).
- **Umfang:** 10–20 Prompts reichen für den Anfang, davon 5 für den Happy Path und 5 für „soll nicht
  triggern" ([10:31](https://www.youtube.com/watch?v=0vphxNt4wyk&t=631s)).
- **Outcomes, nicht Pfade:** Nicht prüfen, ob der Skill im ersten Turn lädt; prüfen, ob die Aufgabe
  erreicht wird ([18:20](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1100s)).
- **Wiederholung:** 3–6 Läufe pro Fall, weil Modelle nicht deterministisch sind
  ([18:59](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1139s)).
- **Isolation:** Frischer Workspace pro Lauf; Agents suchen sonst in vorherigen Chats nach Kontext
  ([18:33](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1113s)).
- **Harnesse:** Über verschiedene Harnesse testen, nicht nur einen
  ([19:12](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1152s)).
- **Ablation:** Immer mit und ohne Skill laufen lassen. Trägt das Modell die Leistung ohne Skill, kann
  der Skill (oder die betreffende Zeile) weg; der Eval bleibt
  ([21:03](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1263s)).
- **Gate:** Bei Google DeepMind liegen Evals neben jedem Skill, laufen bei jeder Änderung und ein Merge
  erfolgt nur, wenn der Eval besser wird oder ein neuer Fall dazukommt
  ([16:41](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1001s)).

**Der eine Hinweis, nicht die ganze Liste:** Der Skill wird nicht daran scheitern, dass ihm eine Idee
fehlt. Er wird daran scheitern, dass niemand misst, ob er im richtigen Moment geladen wird und ob er
das Verhalten ändert. **Trigger-Evals sind der erste Check, nicht der letzte.**

Das ersetzt die Persona-Läufe nicht. Persona-Läufe beantworten „fühlt sich das richtig an?".
Trigger-Evals beantworten „feuert der Skill, und zwar reproduzierbar?". Beides ist nötig.

## Aufgabe

Baue eine **minimale, wiederholbare Evaluationsschicht** für `harness-mentor`. Kein Produktumbau, keine
neue Skill-Funktion, keine Distribution. Zuerst wird der Ist-Stand gemessen, dann werden Änderungen
vorgeschlagen.

### Lieferungen

1. `evals/cases.json` — 10–20 Fälle, mindestens 5 positive und 5 negative. Jeder Fall hat:
   `id`, `prompt`, `should_trigger`, `mode` (`einrichten` / `begleiten` / `keiner`), `checks`.
2. `evals/run.py` — stdlib-only Runner, falls ein headless Lauf möglich ist. Wenn Qoder keinen
   headless Skill-Runner anbietet: `evals/PROTOKOLL.md` mit demselben Aufbau als manuelles Protokoll.
3. `evals/README.md` — wie man die Fälle startet, was gemessen wird, was ein Ergebnis bedeutet.
4. `evals/results/2026-10-24-baseline.md` oder `.json` — Trigger-Quote, Outcome-Quote, Rohspuren,
   Abweichungen. Keine geschönten Zusammenfassungen.
5. Ein Eintrag in `DECISIONS.md` mit Datum, Ergebnis und nächstem Schritt. Keine stillen Änderungen an
   `SKILL.md` vor der Baseline.

### Die zehn Startfälle

Die Prompts sind Beispiele; sie dürfen sprachlich angepasst werden, aber die Abdeckung muss bleiben.

| ID | Prompt (gekürzt) | soll triggern? | Modus | Was der Fall prüft |
|---|---|---|---|---|
| P1 | „Ich fange gerade mit Qoder an und habe noch nie mit einem Agenten gearbeitet." | ja | Einrichten | Keine Datei vor benanntem Bedarf; fragt zuerst, wer da sitzt; vier Grundbilder |
| P2 | „Mein Agent versteht meine Aufträge falsch und erinnert sich nach jeder Sitzung an nichts." | ja | Einrichten | Diagnose vor Template; Kontext als Hebel; keine vorschnelle AGENTS.md |
| P3 | „Ich will eine AGENTS.md für mein Projekt aufsetzen." | ja | Einrichten | Absicht fragen; führende Regel mit Umkehrbedingung; keine Vorlage ohne Bedarf |
| P4 | „Wie richte ich ein Memory-System ein, das nicht zumüllt?" | ja | Einrichten | Schreibregeln; `private/`; kein Extra-Apparat |
| P5 | „Wir haben letzte Woche angefangen; ich will die Begleitung fortsetzen." | ja | Begleiten | Memory-Eintrag lesen; Schweigen als Standard; max. eine Regung |
| N1 | „Schreib mir eine Python-Funktion, die eine CSV liest." | nein | keiner | Normal antworten, kein Mentor |
| N2 | „Was ist der Unterschied zwischen Qoder und Cursor?" | nein | keiner | Faktische Antwort, kein Onboarding |
| N3 | „Ich habe schon alles eingerichtet; ändere eine Regel in meiner AGENTS.md." | nein | keiner | Direkte Hilfe, kein Mentor |
| N4 | „Ich arbeite mit einem anderen Skill an einer Landingpage." | nein | keiner | Nicht übernehmen |
| N5 | „Mein Agent hat einen Bug in der Build-Pipeline." | nein | keiner | Coding-Hilfe, kein Mentor |

Für P5 muss ein `project`-Memory-Eintrag vorbereitet werden, sonst testet der Fall den Einrichten-Modus.
Für die negative Seite ist wichtig, dass der Skill nicht aus Höflichkeit „helfend" einsteigt.

### Outcome-Checks

Nicht den Pfad prüfen („hat der Skill im ersten Turn geladen?"), sondern das Ergebnis:

- Entstehen `USER.md`, `AGENTS.md`, `VISION.md`, `private/` und `MEMORY.md` nur nach benanntem Bedarf?
- Hat jede Frage eine Zweckansage und ändert ein benennbares Agentenverhalten?
- Werden Fähigkeiten nur aus der Live-Tool-Liste behauptet; wird Ungeprüftes als ungeprüft benannt?
- Beginnt eine lange Antwort mit TL;DR und endet mit den To-dos der Person?
- Bleibt `private/` privat; steht kein Inhalt daraus außerhalb?
- Wird im Begleiten höchstens einmal eingegriffen; ist Schweigen das protokollierte Standardergebnis?
- Wird der Auszug angeboten, wenn die Person ihn signalisiert?

### Runner-Anforderungen

- **Frischer Workspace pro Lauf.** Kein Vorzustand, kein vorheriger Chat, kein `MEMORY.md` außer dem
  für P5 präparierten Eintrag.
- **3 Läufe pro Fall**, bei sichtbarer Streuung 6. Die Pass-Rate wird pro Fall ausgewiesen, nicht nur
  als Gesamtzahl.
- **Trigger-Erkennung** aus der Spur (Tool-/Skill-Ladeereignis) oder aus dem expliziten Aufruf. Wenn
  weder noch verfügbar: manuell protokollieren, aber nicht als „automatisch gemessen" ausgeben.
- **Deterministische Checks zuerst.** Artefakte, Dateinamen, Regelform, TL;DR, `private/`-Grenze.
  Ein Rubric-Judge nur für Gesprächsverhalten, das sich nicht deterministisch prüfen lässt.
- **Rohspuren aufbewahren.** Ein Ergebnis ohne Spur ist nicht nachprüfbar.
- **Keine echten Konten, keine Zugänge, keine personenbezogenen Daten.** Nur synthetische Personas.

### Harnesse

- **Qoder zuerst.** Dort liegt der Skill, dort ist der primäre Anhang.
- **Claude Code und Cursor nur, wenn verfügbar.** Wenn nicht: den Punkt „harness-neutral" ausdrücklich
  als **ungeprüft** stehen lassen, nicht als bestanden.
- Der Kern-Skill muss ohne Qoder-Anhang funktionieren. Wenn er das nicht tut, ist das ein Befund, kein
  Testfehler.

### Ablation

- Dieselben positiven Fälle einmal **mit** und einmal **ohne** Skill laufen lassen.
- Wenn das Modell die Zweckansage, das TL;DR oder die Regel-Lehre ohnehin schon liefert, ist die
  entsprechende Zeile ein **No-op**. Vorschlag zum Kürzen machen; nicht ohne Manuels Freigabe ändern.
- Den Eval behalten, auch wenn die Zeile gestrichen wird. Sonst merkt man nicht, wenn die Leistung
  später zurückfällt.

### Gate

- Baseline zuerst, dann Änderungen.
- Jede Änderung an `SKILL.md` oder den Referenzen läuft gegen die Cases.
- Merge nur, wenn der Eval besser wird oder ein neuer Fall hinzukommt.
- Ein einzelner grüner Lauf ist kein Nachweis; die Pass-Rate über 3–6 Läufe zählt.

## Definition of Done

- [ ] 10 Fälle in `evals/cases.json`, 5 positiv, 5 negativ.
- [ ] Runner oder manuelles Protokoll, mit frischem Workspace pro Lauf.
- [ ] 3 Läufe pro Fall; Rohspuren und Pass-Raten dokumentiert.
- [ ] Qoder getestet; Claude Code/Cursor getestet oder ausdrücklich als ungeprüft markiert.
- [ ] Ablation mit/ohne Skill für mindestens die fünf positiven Fälle.
- [ ] Keine Änderung an `SKILL.md` vor der Baseline.
- [ ] `DECISIONS.md`-Eintrag mit Ergebnis und nächstem Schritt.
- [ ] Hub nur nachziehen, wenn sich der Produktumfang ändert; sonst reicht der Repo-Eintrag.

## Nicht-Ziele

- Keine neuen Skill-Funktionen, keine Umbenennung, kein Redesign.
- Keine Distribution, keine Auffindbarkeit, kein Marketplace.
- Keine Entscheidung über öffentliche Sichtbarkeit der Evals.
- Keine echten Geschäftskonten, keine Kundendaten, keine externen Dienste.
- Kein LLM-Judge, wo deterministische Checks reichen.

## Repo-Stand und Grenzen

**Wichtig:** Im Repo liegen bereits uncommittete Änderungen (Stand 2026-10-24, `git status`):
`SKILL.md`, `README.md`, `DECISIONS.md`, `docs/product-plan.md`, die Vorlagen `AGENTS.md` und
`VISION.md` sowie `references/didaktik.md` und `references/einrichten-leitfaden.md`.
Diese Änderungen **nicht zurücksetzen, nicht überschreiben und nicht ungefragt mitcommitten**. Sie sind
der aktuelle Arbeitsstand.

Es gelten die Regeln aus [`AGENTS.md`](../../AGENTS.md):

- Nichts aus `D:\OneDrive\Delta Weave\private\` hierher kopieren oder zitieren.
- Keine echten Konten oder Zugänge für Tests.
- Jede Zahl und jedes Datum mit Quelle und Stand.
- Herstellerangaben sind kein Funktionsnachweis; Ungetestetes bleibt ungeprüft.
- Credentials nie in Dateien dieses Repos.

**Öffentlichkeit:** Das Repo ist seit 2026-10-23 öffentlich (`melkor42/Company-Harness`). Ob `evals/`
mit Pass-Raten und Schwachstellen öffentlich werden soll, ist eine Entscheidung von Manuel, keine
Nebenwirkung dieses Auftrags. Bis dahin lokal halten oder ausdrücklich freigeben.

## Offene Fragen — Manuel

1. Welche Harnesse stehen für den Test zur Verfügung: nur Qoder, oder auch Claude Code/Cursor?
2. Gibt es einen headless Qoder-Lauf, oder wird der erste Durchlauf manuell protokolliert?
3. Was gilt als Baseline-Schwelle: nur messen und festhalten, oder ein Mindestwert (z. B. 9/10
   Trigger korrekt, 8/10 Outcome-Checks)?
4. Soll in der ersten Runde ein Rubric-Judge für Gesprächsverhalten eingesetzt werden, oder reichen
   deterministische Artefakt-Checks?
5. Soll `evals/` öffentlich committet werden oder lokal bleiben?
6. Wer führt den Lauf aus: diese Session oder Manuel selbst?

## Reihenfolge für die aufnehmende Session

1. `AGENTS.md`, `CONTEXT-SIGNOFF.md`, `docs/product-plan.md` (Zeilen 35–60),
   `DECISIONS.md` (Zeilen 255–325) und `.qoder/skills/harness-mentor/SKILL.md` lesen.
2. Baseline einfrieren: Hash von `SKILL.md` und den Referenzen notieren.
3. `evals/cases.json` mit den zehn Fällen anlegen.
4. Runner oder Protokoll bauen; einen Trockenlauf mit einem Fall machen.
5. Qoder-Baseline: 3 Läufe pro Fall, frische Workspaces, Rohspuren sichern.
6. Ablation ohne Skill für die fünf positiven Fälle.
7. Ergebnisse in `evals/results/2026-10-24-baseline.md` festhalten.
8. Erst danach Änderungen vorschlagen; keine stillen Kürzungen.
9. `DECISIONS.md` ergänzen; Hub nur bei geändertem Produktumfang nachziehen.

## Quellen

- `D:\OneDrive\Delta Weave\MAP.md`, Stand 2026-10-23 — Status „Wirksamkeit in Probeläufen und
  Distribution offen".
- `D:\OneDrive\Delta Weave\projects\company-harness.md`, Stand 2026-10-23 — Produktidee, öffentliche
  Freigabe, Abgrenzung zum Hub.
- `docs/product-plan.md`, Zeilen 47 und 53, Stand 2026-10-12 — Abnahme aus drei Erfahrungen plus
  Retention-Check; Entwicklungsmethode mit Persona-Probeläufen statt geskripteter Dialoge.
- `DECISIONS.md`, Zeilen 269–303, Stand 2026-10-12 — v1-Probelauf, zwei Konstruktionsfehler, v2-Bau
  aus fünf Modell-Läufen, offene Distribution.
- `.qoder/skills/harness-mentor/SKILL.md`, 92 Zeilen, 118-Wort-Beschreibung, geprüft 2026-10-24.
- Talk: `https://ai.engineer/talks/0vphxNt4wyk-dont-ship-skills-without-evals`,
  AI Engineer World's Fair 2026, 21:46; Zitate gegen die lokale Segmenttabelle des AI-Engineer-Archivs
  geprüft, Stand 2026-10-24.
- Lokales AI-Engineer-Archiv: 1.346 Talks, 221.467 Segmente, 373 Talks mit Topic Evals
  (`aie stats`, Stand 2026-10-24).
