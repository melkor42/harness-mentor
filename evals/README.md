# Evals für `harness-mentor`

**Stand:** 2026-10-24
**Zweck:** Prüfen, ob der Skill im richtigen Moment geladen wird und ob er über Sitzungen
hinweg trägt. Kein Unit-Test-Apparat, keine Bewertung der Didaktik.

Der Auftrag und die Begründung stehen in
[`../docs/handoff/2026-10-24-harness-mentor-evals.md`](../docs/handoff/2026-10-24-harness-mentor-evals.md).
Die kurze Fassung: Der größte Einzelhebel ist der Trigger. Ein Skill, der nicht lädt, kann
noch so gut geschrieben sein. Deshalb wird zuerst der Trigger gemessen, dann die
Kontinuität — und nur das, was eine Entscheidung prüft.

## Was gemessen wird

| Dimension | Frage | Wie |
|---|---|---|
| Trigger | Lädt `harness-mentor` im richtigen Moment — und nicht bei jedem Coding-Task? | `Skill`-Toolaufruf im Rohspur-Transcript |
| Kontinuität | Knüpft der Skill nach einer Woche oder nach drei Wochen an die Begleitnotiz an? | P5/P6 mit geseedeter `project`-Memory |
| Ende | Wird eine Beendigung sofort akzeptiert, ohne Überredung? | P7 mit geseedeter Begleitnotiz |
| Ehrlichkeit | Wird eine fehlende Notiz als fehlend benannt, statt Historie zu erfinden? | P8 ohne Memory |
| Artefakte | Entstehen `USER.md`, `AGENTS.md`, `VISION.md`, `memory/` oder `private/` ohne benannten Bedarf? | Dateisnapshot vor/nach dem Lauf |

**Nicht gemessen:** Gesprächsqualität, Ton, didaktische Passung, echter Retention-Effekt
nach zwei bis drei Wochen, Harness-Neutralität. Dafür bleiben die Persona-Probeläufe und
der Lackmus-Test zuständig.

## Fälle

- **P1–P4** — Einstieg, falsches Erinnern, AGENTS.md, Memory-Hygiene. Erwartung: Trigger,
  Diagnose vor Vorlage, keine Datei ohne Bedarf.
- **P5–P8** — Fortsetzung nach einer Woche, nach drei Wochen, Beendigung, fehlende Notiz.
  Erwartung: Trigger, Anknüpfen an den Stand, kein neues Onboarding, kein Erfinden.
- **N1–N6** — Coding-Hilfe, Faktenfrage, gezielte AGENTS.md-Änderung, anderer Skill,
  Build-Bug, Allgemeinwissen. Erwartung: kein `harness-mentor`-Trigger.

Die vollständige Liste mit Prompts und manuellen Checks steht in
[`cases.json`](cases.json).

## Starten

Voraussetzungen: Python 3.11+, eine angemeldete Qoder-CLI. Keine externen Pakete.

```bash
# Fälle anzeigen
python evals/run.py --list-cases

# Trockenlauf: Workspaces anlegen, nichts ausführen
python evals/run.py --dry-run --cases P1,N1

# Pilot: ein Lauf pro Fall
python evals/run.py --runs 1 --label pilot

# Baseline: Läufe aus cases.json (positive 3, negative 2–3)
python evals/run.py --label 2026-10-24-baseline

# Einzelne Fälle
python evals/run.py --cases P5,P6,N3

# Ablation: dieselben positiven Fälle ohne kopierten Skill
python evals/run.py --cases P1,P2,P3,P4,P5 --runs 2 --without-skill --label ablation

# Workspaces zum Nachsehen behalten
python evals/run.py --cases P5 --runs 1 --keep
```

Optionen: `--cli` (Pfad zu `qodercli`), `--model`, `--timeout` (Sekunden pro Lauf),
`--permission-mode` (Standard `accept_edits`), `--without-skill`, `--max-output-tokens`,
`--label`. Ohne `--cli` sucht der Runner `qodercli` im `PATH` und unter
`~/.qoder/bin/qodercli/`.

## Wie ein Lauf abläuft

1. Frischer Workspace unter `.sandbox/<label>/w-<zufall>` (gitignoriert). Der Prozess
   startet mit diesem Workspace als Arbeitsverzeichnis, damit der Skill nicht aus dem
   Repo-Wurzelverzeichnis geladen wird.
2. Nur `.qoder/skills/harness-mentor/` wird hineinkopiert; für P5–P7 kommt die
   geseedete `memory/`-Datei dazu.
3. `qodercli -p <prompt> -w <workspace> --no-session-persistence --permission-mode
   accept_edits --output-format stream-json` läuft ohne Rückfragen. `accept_edits`
   ist Pflicht: `dont_ask` verweigert Schreibzugriffe, dann sind Memory- und
   Artefakt-Prüfungen wertlos.
4. Der Runner liest die NDJSON-Spur: `Skill`-Toolaufruf mit `skill: harness-mentor` ist
   der Trigger. Prosa zählt nicht.
5. Dateisnapshot vor/nach dem Lauf zeigt, ob Harness-Artefakte ohne Bedarf entstanden sind.
6. Rohspur, JSON und Markdown landen unter `evals/results/`.

Für die Ablation (`--without-skill`) wird der Skill nicht kopiert. Der Runner prüft,
dass `harness-mentor` dann auch nicht in der Skill-Liste der Sitzung auftaucht.

Der Workspace wird nach dem Lauf gelöscht, sofern `--keep` nicht gesetzt ist. Die Rohspur
bleibt erhalten — ein Ergebnis ohne Spur ist nicht nachprüfbar.

## Ergebnisse lesen

- **Trigger korrekt** — der `Skill`-Aufruf passt zur Erwartung. Das ist die Hauptkennzahl.
- **Positive erkannt** — Wie oft loadet der Skill bei P1–P8? Unter 100 % ist ein Befund.
- **Negative sauber** — Wie oft bleibt er bei N1–N6 still? Ein Fehltrigger ist ein Befund.
- **Automatische Checks** — Trigger plus Artefaktgrenze plus die harte P7-Memory-Prüfung.
  Das ist keine Qualitätsnote.
- **Manuelle Prüfung** — Die Checklisten in der Markdown-Ausgabe werden von Hand gelesen.
  Ein grüner Trigger ist kein Nachweis gelungener Begleitung.

Ein einzelner grüner Lauf ist kein Nachweis. Die Pass-Rate über mehrere Läufe zählt.
Bei sichtbarer Streuung wird die Zahl der Läufe erhöht, nicht die Bewertung gelockert.
Für P3 und N3 liegen deshalb je 6 Läufe vor (Baseline plus `2026-10-24-variance`); die
kombinierte Rate steht im `DECISIONS.md`-Eintrag.

## Grenzen

- **Nur Qoder.** Claude Code und Cursor sind ungeprüft; der Punkt „harness-neutral" bleibt
  offen, bis dort gemessen wurde.
- **Frische Workspaces, keine frische Umgebung.** Maschine, globales Qoder-Profil und
  globale Plugins sind in jedem Lauf dieselben. Das ist eine bekannte Verzerrung.
- **Workspace im Repo.** Der Sandbox-Ordner liegt unter `.sandbox/` im Repo. Das Modell
  kann per Pfad die echte `AGENTS.md` des Repos finden und lesen; das beeinflusst
  Antwortinhalte (besonders N3), nicht die Trigger-Entscheidung. Ein Workspace außerhalb
  des Repos wäre sauberer, ist in dieser Umgebung aber nicht freigegeben.
- **Die Ablation ist kontaminiert.** `--without-skill` verhindert nur das Laden des
  Skills; die Dateien liegen weiter im Repo und sind per Pfad lesbar. In den Läufen unter
  `results/2026-10-24-ablation` haben P2 (1/2), P3 (1/2), P4 (2/2) und P5 (2/2) `SKILL.md`
  oder Referenzen gelesen. Die Ergebnisse sind ein Indiz, keine saubere Ablation; sie
  taugen nicht zum Streichen von Skill-Zeilen. Eine saubere Ablation braucht einen
  Workspace außerhalb des Repos oder eine isolierte Harness-Konfiguration.
- **Rohspuren enthalten Umgebung.** Sie können Dateinamen der globalen Qoder-Memory und
  Repo-Pfade enthalten. Vor einer Veröffentlichung prüfen.
- **Kontinuität ist simuliert.** P5/P6 prüfen, ob der Skill eine vorhandene Notiz trägt.
  Ob eine echte Begleitung nach drei Wochen noch wirkt, beantwortet nur der
  Retention-Check mit einer Person.
- **Modellstreuung.** Der Lauf nutzt das eingestellte Modell (Standard: Auto). Deshalb
  mehrere Läufe pro Fall; die Zahl steht in `cases.json`.
- **Die Laufzeit ist real.** Ein Lauf dauert rund 40–60 Sekunden. Die Baseline aus 35
  Läufen braucht etwa eine halbe Stunde.

## Gate

- Baseline zuerst, dann Änderungen an `SKILL.md` oder den Referenzen.
- Jede Änderung läuft gegen dieselben Fälle.
- Merge nur, wenn der Eval besser wird oder ein neuer Fall hinzukommt.
- Ein einzelner grüner Lauf ist kein Merge-Grund.
- Keine stillen Kürzungen: Was gestrichen wird, wird als Befund notiert.

## Veröffentlichung

**Lokale Sicherung:** Runner, synthetische Fälle und diese Anleitung werden versioniert.
`results/` einschließlich Rohspuren und lokale `.runs/` bleiben per `.gitignore` außerhalb
der Commits, bis ihre Veröffentlichung gesondert entschieden und der Inhalt geprüft wurde.
Die unten genannten Berichte sind deshalb lokale Nachweise und keine garantierten Downloads
eines frischen Klons. Quelle: Abschlussprüfung und Commit-Auftrag von Manuel, Stand 2026-10-25.

Das Repo ist seit 2026-10-23 öffentlich (`melkor42/Company-Harness`). Ob `evals/` mit
Pass-Raten und Schwachstellen öffentlich werden soll, ist eine Entscheidung von Manuel.
Bis dahin lokal halten. Die Rohspuren enthalten nur synthetische Prompts, aber sie zeigen
die Schwachstellen des Skills ungefiltert.

## Quellen

- [`docs/handoff/2026-10-24-harness-mentor-evals.md`](../docs/handoff/2026-10-24-harness-mentor-evals.md) — Auftrag, Talk-Bezug, zehn Startfälle.
- Philipp Schmid, *Don't Ship Skills Without Evals*, AI Engineer World's Fair 2026:
  <https://ai.engineer/talks/0vphxNt4wyk-dont-ship-skills-without-evals>.
- [`docs/product-plan.md`](../docs/product-plan.md) — Persona-Probeläufe und Retention-Check.
- [`DECISIONS.md`](../DECISIONS.md) — v1-Probelauf und v2-Entscheidungen.
