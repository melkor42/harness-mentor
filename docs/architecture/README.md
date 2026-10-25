# Architektur-Kommunikation — `harness-mentor`

**Stand:** 2026-10-24
**Art:** Konzeptionelle Kommunikationsansicht, kein C4-Current-State-Modell.
**Zielgruppe:** Produktentscheider und Neueinsteiger, die in wenigen Minuten verstehen
wollen, was der Skill tut, warum er so gebaut ist und woran er gemessen wird.

## Die eine Aussage

Der Skill richtet einen Grundkontext ein und begleitet leise über Sitzungen hinweg —
mit dem Ziel, sich selbst überflüssig zu machen. Die Dateien sind der Rückstand dieser
Arbeit, nicht ihr Ersatz.

## Die Ansicht

- [`harness-mentor-essenz.html`](harness-mentor-essenz.html) — Quelle und direkt
  einbettbare HTML-Seite (1600 × 1280).
- [`harness-mentor-essenz.png`](harness-mentor-essenz.png) — früherer Render,
  3200 × 2560 Pixel (2×). Enthält noch die frühere Produktbezeichnung; für den aktuellen
  Stand gilt die HTML-Quelle. Neuer Render vor Verwendung außerhalb des Repos erforderlich.
  Quelle: Namenspflege und lokale Bestandsprüfung, Stand 2026-10-25.

Die Ansicht ist in vier Zonen geteilt:

1. **Das Problem** — der Agent ist fähig, aber ohne Betriebsgedächtnis; die Person kennt
   die richtige Frage nicht.
2. **Der Weg** — vier Stationen: Einrichten → Begleitnotiz (Zustand) → Begleiten → Auszug.
3. **Vier Grundbilder** — fremde Arbeitskraft, Kontext als Hebel, Vertrauen als
   Korrigierbarkeit, Auftrag ist nicht Absicht.
4. **Leitplanken und Messpunkte** — was der Skill nie tut und woran er geprüft wird,
   einschließlich Kontinuität und Lackmus-Test.

## Evidenz

| Aussage in der Grafik | Quelle | Konfidenz |
|---|---|---|
| Vier Grundbilder und ihre Reihenfolge | `.qoder/skills/harness-mentor/references/didaktik.md:8-45` | hoch |
| Zwei Modi, Modus-Entscheidung am Memory-Eintrag | `.qoder/skills/harness-mentor/SKILL.md:10-29` | hoch |
| Einrichten Blöcke 0–6 und Artefakte | `.qoder/skills/harness-mentor/references/einrichten-leitfaden.md:26-207` | hoch |
| Schweigen-Standard, 2×-Schwelle, eine Regung, vier Anstöße | `.qoder/skills/harness-mentor/references/begleiten-disziplin.md:1-103` | hoch |
| Auszug und Überflüssigmachung | `.qoder/skills/harness-mentor/references/begleiten-disziplin.md:87-103` | hoch |
| Leitplanken (Erleben, Regeln, Ehrlichkeit, `private/`, Hooks) | `.qoder/skills/harness-mentor/SKILL.md:31-53, 83-92` | hoch |
| Trigger- und Kontinuitäts-Evals | [`docs/handoff/2026-10-24-harness-mentor-evals.md`](../handoff/2026-10-24-harness-mentor-evals.md) | mittel — Auftrag, Baseline läuft |
| „Claude Code/Cursor ungeprüft" | Handoff, offene Fragen; Qoder-Anhang ist der einzige belegte Anhang | hoch als Vorbehalt |

## Was die Ansicht bewusst weglässt

- Keine Datei-für-Datei-Architektur, keine Referenzpfade im Bild. Die stehen in
  [`SKILL.md`](../../.qoder/skills/harness-mentor/SKILL.md) und in der README des Skills.
- Keine Zeitachse und keine Retentionskurve. Der echte 2–3-Wochen-Check ist ein
  Persona-Lauf, kein Diagramm.
- Keine Herstellerdetails. Der Kern ist harness-neutral; Qoder ist der erste Anhang,
  nicht die Architektur.
- Keine Ergebnisse der Evals. Die Grafik zeigt die Messlatte, nicht die Pass-Rate.
  Ergebnisse gehören nach [`evals/results/`](../../evals/results/).

## Neu rendern

Die HTML-Seite ist die Quelle. PNG mit Edge headless erzeugen:

```bash
"/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" \
  --headless=new --disable-gpu --hide-scrollbars \
  --window-size=1600,1280 --force-device-scale-factor=2 \
  --screenshot="docs/architecture/harness-mentor-essenz.png" \
  "file:///C:/Users/ASUS%20GAMING/Documents/Company-Harness/docs/architecture/harness-mentor-essenz.html"
```

Bei inhaltlichen Änderungen zuerst die HTML anpassen, dann rendern. Das PNG nicht von
Hand bearbeiten — sonst laufen Quelle und Bild auseinander.

## Nächster Schritt

Die Aussage der Grafik gegen die Baseline prüfen: Wenn der Trigger in den Evals nicht
trägt, ist die schönste Architekturzeichnung eine Behauptung. Die Baseline liegt unter
[`evals/results/`](../../evals/results/); die Rohspuren daneben.
