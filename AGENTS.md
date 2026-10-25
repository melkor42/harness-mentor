# Harness Mentor — Arbeitsregeln für Agents

Dieser Workspace gehört zum Skill **Harness Mentor** von Delta Weave. Er ist der
Ort für die Umsetzung; der Unternehmenskontext liegt außerhalb.

## Lies in dieser Reihenfolge

1. [`CONTEXT-SIGNOFF.md`](CONTEXT-SIGNOFF.md) — Stand, was bestätigt ist, was Vorschlag ist, was offen ist.
2. [`docs/product-plan.md`](docs/product-plan.md) — Produktthese, Prozesse, Architektur, Quellen.
3. Bei Fragen zu Person, Firma, Projekten oder Freigaben: `C:\Users\ASUS GAMING\OneDrive\Delta Weave\MAP.md`.

## Harte Regeln

**Nichts aus `D:\OneDrive\Delta Weave\private\` kommt hierher.** Nicht lesen und kopieren, nicht
zitieren, nicht in Prompts an dritte Dienste geben. Verweis mit Pfad genügt.

**Keine echten Geschäftskonten ohne ausdrückliche Freigabe.** Kein Mail-, Kalender-, Buchhaltungs- oder
Kundenzugang für einen Test. Erst synthetische oder ausdrücklich freigegebene Fälle.

**Jede Zahl und jedes Datum braucht Quelle und Stand.** Format: `Quelle: <Pfad oder URL>, Stand JJJJ-MM-TT`.
Ohne Quelle gehört es als `OFFEN — Manuel` markiert, nicht geraten.

**Herstellerangaben sind kein Funktionsnachweis.** Marketingtext belegt Werbung. Schweigen einer
Dokumentationsseite belegt kein fehlendes Feature. Was nicht getestet ist, bleibt als ungeprüft stehen.

**Zugriff wird außerhalb des Modells erzwungen.** Freigaben binden an die konkrete Aktion und ihre
Nutzlast. Prompt-Guardrails und Hooks sind keine Sicherheitsgrenze.

**Credentials nie in Dateien dieses Repos.** Kein `.env` committen. Wer einen Wert braucht, meldet es
als Entscheidung, statt zu lesen oder zu patchen.

**Kein externer Kontextserver darf in den Delta-Weave-Hub schreiben.** Ein Versuch mit Hexis oder einem
anderen Tool läuft in einem separaten, isolierten Repo.

## Pflegen

- Neuer Fakt → in die zuständige Datei, nicht in eine neue.
- Entscheidung oder Richtungsänderung → **anhängen** in [`DECISIONS.md`](DECISIONS.md), mit Datum.
  Verworfene Vorschläge bleiben stehen und werden als ersetzt markiert.
- Geändert hat sich etwas am Produktumfang? Dann auch den Delta-Weave-Knoten
  `C:\Users\ASUS GAMING\OneDrive\Delta Weave\projects\harness-mentor.md` und `MAP.md` nachziehen — der Hub ist das
  Verzeichnis über alle Projekte.
- Vor irgendetwas, das nach außen geht: `C:\Users\ASUS GAMING\OneDrive\Delta Weave\company\oeffentlichkeit.md` gegenprüfen.
