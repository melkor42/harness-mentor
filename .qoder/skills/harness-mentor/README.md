# Harness Mentor

Interaktiver Mentor für die Arbeit mit einem KI-Agenten-Harness — auf Deutsch,
harness-neutral im Kern, mit Anhang pro Harness (erster: Qoder).

Für alle, die mit dem Agenten arbeiten statt nur chatten wollen — Entwicklerin,
Unternehmer oder Neugierige. Der Einstieg setzt nichts voraus: Die Person muss
nicht wissen, wonach sie fragen müsste, der Mentor führt.

## Zwei Modi

- **Einrichten** — geführtes Erst-Setup per Interview. Zuerst werden vier
  Grundbilder verankert (der Harness als fremde Arbeitskraft mit begrenztem
  Gedächtnis; Kontext als einzige Hebelstelle; Vertrauen als Korrigierbarkeit;
  der Auftrag ist nicht die Absicht), dann entsteht Block für Block der
  Grundkontext als Dateien: `USER.md`, `AGENTS.md`, `docs/VISION.md` mit Absicht
  und offenen Fragen, Ablage mit `private/`, Memory-System mit `MEMORY.md` und
  ersten Einträgen.
- **Begleiten** — leiser Mentor über Sitzungen hinweg. Beobachtet
  Reibungsspuren, regt sich höchstens einmal pro Sitzung und nur, wenn Schweigen
  etwas kostet. Lockerungen laufen über die Vertrauensrampe (datierte Regeln in
  der AGENTS.md); Ziel ist die eigene Überflüssigmachung.

Der Stand der Begleitung lebt als `project`-Memory-Eintrag — kein eigener Apparat,
keine Extra-Datei.

## Aufruf

`/harness-mentor` — oder einfach sagen, dass man neu mit einem Harness anfängt;
die Skill-Beschreibung trägt den Rest.

## Aufbau

- `SKILL.md` — Einstieg, Modus-Entscheidung, Grundhaltung, Grenzen
- `references/didaktik.md` — die vier Grundbilder, Anker-Erfahrungen, Lackmus-Test
- `references/einrichten-leitfaden.md` — Interview-Blöcke 0–6, Regel-Lehre
  (führend vs. blockierend), Gedächtnis-Schreibregeln
- `references/begleiten-disziplin.md` — Schweigen-Standard, Reibungsspuren, vier
  zulässige Anstöße, Lockerung und Auszug
- `references/anhaenge/qoder.md` — Qoder-Pfade und -Formate, datiert
- `assets/vorlagen/` — USER.md, AGENTS.md, VISION.md, MEMORY.md, memory-eintrag.md

## Stand

2026-10-12: Gebaut aus der Synthese von fünf parallelen Modell-Läufen und einem
Probelauf des Vorgänger-Skills `company-harness` (v1, liegt weiterhin unter
`.qoder/skills/company-harness/`). Am selben Tag auf Essenz reduziert
(16 → 10 Dateien).

2026-10-24: Absicht vor Auftrag aus *Die Architektur der Intention* ergänzt
(viertes Grundbild, Block 2, VISION-/AGENTS-Vorlagen). Keine Essay-Logik
übernommen. Quelle und Begründung: [`DECISIONS.md`](../../../DECISIONS.md).

Produktkontext: [`docs/product-plan.md`](../../../docs/product-plan.md).
