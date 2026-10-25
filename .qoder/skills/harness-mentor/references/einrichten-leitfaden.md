# Einrichten-Leitfaden — Grundkontext aufbauen und in die Begleitung übergeben

Der Aufbau läuft als geführtes Gespräch in Blöcken. Nur benötigte Blöcke bearbeiten;
ein Block kann mit der Bestätigung einer bereits passenden Datei enden. Der Nutzer
muss nicht wissen, was gebraucht wird — frage so,
dass Antworten leicht fallen. Wenn ein Inhalt wirklich ergänzt werden muss, einen
konkreten Vorschlag zur Bestätigung oder Korrektur zeigen.

## Gesprächsregeln

- **Takt: Bedarf vor Artefakt.** Nur fehlende Angaben fragen und kleine, bequem
  beantwortbare Runden bilden. Bestehendes verbessern, statt eine neue Datei zu erzwingen.
- **Zweckansage vor jeder Frage.** Vor dem Stellen sagen, welche Verhaltensänderung
  des Agenten die Antwort bewirkt. Antworten sind nur so gut wie das Verständnis
  dessen, was sie bewirken — ohne Zweck sind selbst gute Fragen Ratespiele.
- **Prüfstein für jede Frage.** Ändert sich je nach Antwort ein benennbares Verhalten
  des Agenten? Wenn nein, fliegt die Frage raus.
- **Vorschlagen statt abfragen.** Nach jeder Antwort den fertigen Dateiabschnitt
  zeigen: „Ich würde das so festhalten: … — passt das?"
- **Antworten wiederverwenden.** Was einmal gesagt wurde, nicht erneut fragen;
  höchstens bestätigen lassen.
- **Leere lassen dürfen.** Was der Nutzer nicht weiß, wird als „OFFEN — klären,
  sobald …" markiert, nicht erfunden.
- **Sprache des Nutzers spiegeln.** Diese Dateien sind persönlich; schreibe in der
  Sprache, in der das Gespräch läuft.

## Block 0 — Verständnis (keine Datei)

Zuerst `bestandsaufnahme.md` anwenden. Die folgenden Fragen nur stellen, soweit der
vorhandene Kontext sie nicht beantwortet. Ohne Begleitnotiz ist eine erfahrene Person
nicht automatisch neu. Alle Dateinamen der folgenden Blöcke an die tatsächlich
verwendeten Konventionen und Ladewege anpassen.

Klären, bevor etwas geschrieben wird:

1. Welchen Harness benutzt du? *(Entscheidet, welcher Anhang aus `anhaenge/` gilt.)*
2. Was machst du — Arbeit, Rolle, wichtigste Projekte?
3. Was soll der Agent für dich übernehmen?
4. Gibt es schon Dateien, Regeln, Entscheidungen oder Notizen, die weiter gelten
   sollen? *(Vorhandenes lesen und einbauen — nie plattmachen. Dazu gehören auch
   verworfene Wege und die Gründe früherer Entscheidungen.)*

**Arbeitskontext einordnen, nicht etikettieren.** Aus den Antworten ableiten, mit
welcher Passung der Mentor arbeitet: Eine Entwicklerin bekommt Vergleiche mit
Werkzeugen, die sie kennt, und mehr Anwenden; ein Unternehmer bekommt
Workflow-Beispiele und mehr Zeigen. Die Einordnung wählt Beispiele und Tempo —
sie steckt niemanden in eine Schublade, und sie ist korrigierbar, sobald die
Zusammenarbeit etwas anderes zeigt. Der Skill soll jedem helfen; die Passung macht
den Unterschied, wie er hilft.

## Grundbilder verankern (vor allen Dateien)

`didaktik.md` laden und die noch hilfreichen Grundbilder einführen — an einer Situation des
Nutzers, nicht als Vortrag: fremde Arbeitskraft mit begrenztem Gedächtnis; Kontext
als einzige Hebelstelle (sagen, anbieten, erlauben); Vertrauen als Korrigierbarkeit;
der Auftrag ist nicht die Absicht. Genau eine Rückfrage: „Was davon ist dir neu?"

## Block 1 — Die Person → `USER.md`

Prüfstein gilt: Zwei Fragen bestehen ihn (Zweckansagen nicht vergessen):

1. „Was hat dich an bisherigen KI-Antworten geärgert?" — *Zweck: Daraus werden die
   Punkte unter „Was ich nicht will" — Abbruchkriterien, die jede Antwort des
   Agenten betreffen.* Die ergiebigste Frage des Blocks.
2. „Woran erkennst du, dass erledigte Arbeit gut ist?" — *Zweck: Daraus wird der
   Maßstab, an dem der Agent eigene Arbeit prüft, bevor er sie vorlegt.*

**Bestehende Freigaben gelten weiter.** Eine Setup-Prüfung setzt weder Autonomie
noch vorhandene Regeln zurück. Nur bei einem neuen Setup ohne entsprechende
Festlegung *eng führen* als Start vorschlagen: Entwürfe vorlegen, Handlungen mit
Außenwirkung nach konkreter Freigabe. Den Lockerungsmechanismus in zwei
Sätzen erklären: „Wenn der Agent etwas wiederholt gut macht, sag einmal: Das darfst
du künftig ohne Rückfrage. Genau das wird dann als Regel festgehalten." Lockerungen
wandern als datierte Regeln in die `AGENTS.md` (Block 3).

Aus den Antworten und aus Block 0 die vier Abschnitte der Vorlage
`assets/vorlagen/USER.md` füllen.

## Block 2 — Absicht und Ziel → `VISION.md`

**Auftrag und Absicht sind nicht dasselbe.** Der Auftrag nennt das Wie („ein
Dashboard"), die Absicht das Warum und Für-wen. Frage zuerst nach der Absicht —
so, dass das genannte Produkt noch hinterfragbar bleibt; reicht die Antwort
nicht, wird sie als OFFEN markiert, nicht erfunden.

Fragen:

1. „Was soll sich für wen verändern, wenn das hier funktioniert?" — *Zweck: der
   Nordstern für Vorschläge und Prioritäten des Agenten.*
2. „Woran würdest du merken, dass es gut ist — und was würde sich falsch
   anfühlen?" — *Zweck: daraus wird der Qualitätsmaßstab; das „falsch" ist oft
   konkreter als das „gut".*
3. „Was ist nicht verhandelbar, und was ist nur deine erste Vermutung?" —
   *Zweck: Festlegung und Hypothese bleiben unterscheidbar; die Hypothese darf
   durch Erfahrung überholt werden.*
4. „Was ist jetzt mühsam — und woran könnte das Ganze scheitern?" — *Zweck:
   Herausforderungen und Risiken; daraus werden Schutzregeln für spätere Blöcke.*

Vorhandenes aus Block 0 — Entscheidungen, Regeln, verworfene Wege — fließt als
Hintergrund ein, damit der Agent Neues gegen den Stand prüft, statt ihn zu
wiederholen oder rückgängig zu machen.

Was offen ist, bleibt offen: Unklarheit bei Begriffen und Zuständigkeit klären;
Fragen, die nur das Ausprobieren beantwortet, als Experiment notieren. Ein Dokument,
das alle Fragen beantwortet, ist verdächtig.

Vorlage: `assets/vorlagen/VISION.md`. Die Absicht in einem Satz festhalten; die
Details darunter.

## Block 3 — Regeln → `AGENTS.md`

**Regeln führen oder sie blockieren — dazwischen gibt es nichts.** Eine führende
Regel verbessert jede Antwort, ohne einen einzigen Workflow einzuschränken; Muster:
„Fasse lange Ergebnisse am Anfang in wenigen Sätzen zusammen und hebe meine To-dos
sichtbar hervor." Eine Regel, die einen Weg vorschreibt, steht bald im Weg. Und am
schlimmsten ist die veraltete Regel: Sie wird mit gutem Grund befolgt — sie steht ja
schwarz auf weiß da — und produziert mit voller Überzeugung das Falsche. Deshalb
gelten hier drei Maßstäbe: **wenige** Regeln (jede kostet in jeder Session Kontext),
**nur führende** (gelten für viele Fälle und lassen dem Agenten den Weg frei;
vorschreibende Regeln nur bei einem benannten Schaden dahinter), **jede
verfallsanfällige mit Umkehrbedingung** (Block 5 zeigt das Muster).

Die bestehende Freigaberegel aus Block 1 übernehmen oder den gemeinsam vereinbarten
Start festhalten. Geltungsbereich und Quelle der Erlaubnis nennen. Spätere Änderungen
haben einen eindeutigen aktuellen Stand; wichtige frühere Gründe bleiben knapp
nachvollziehbar. Widersprüchliche Freigaben nicht nebeneinander als gültig stehen lassen.

Zusammen mit ihr kommt die Absichts-Regel in die Datei — die zweite führende
Regel: „Beginne beim Warum: Wenn ein Auftrag nur das Wie nennt, frag nach der
Absicht — was soll sich für wen ändern —, bevor du umsetzt." Sie führt, weil sie
jede Aufgabe verbessert, ohne einen Weg vorzuschreiben.

Fragen: Was soll der Agent **nie** tun? Was soll er **immer** tun? Jede Antwort an
den drei Maßstäben messen, bevor sie in die Datei darf.

## Block 4 — Ablage → Ordnerstruktur

Fragen: Was davon ist privat (Notizen, Kontakte, Finanzen, Zugänge)? Arbeitest du
an mehr als einem Gerät?

Grundmuster:

```
<workspace>/
├── AGENTS.md            # Beispiel für eine native Regeldatei; Ladeweg prüfen
├── USER.md              # Beispiel: Profil nur bei Bedarf, mit wirksamem Ladeweg
├── docs/
│   └── VISION.md        # Absicht, offene Fragen, Stand
├── memory/              # Memory-Dateien + MEMORY.md (falls harness-seitig nicht vorgegeben)
└── private/             # privat, nie an Dritte, nie pushen — in .gitignore eintragen
```

Prinzip **agent-first**: eindeutige Namen, ein Einstiegsdokument, keine Duplikate.
Privates ausschließlich in `private/`; der Agent darf verweisen, aber Inhalte nie
nach außen geben. Bei mehreren Geräten: Git vs. Sync-Ordner gemeinsam festlegen und
als Memory-Eintrag notieren.

## Block 5 — Gedächtnis → `memory/` + `MEMORY.md`

Erklären, was Memories sind und wo sie bei *seinem* Harness liegen (Bestandsaufnahme
und Anhang). Ein vorhandenes natives System erhalten. Nur bei Bedarf `MEMORY.md`
aus der Vorlage anlegen und passende erste Einträge gemeinsam schreiben: ein `user-`-Eintrag
(Arbeitsweise), ein `feedback-`-Eintrag (die wichtigste Regel aus Block 3, mit
**Why:** und **How to apply:**), ein `reference-`-Eintrag (wo die Memory-Dateien
liegen).

Fünf Schreibregeln mitgeben — sie verhindern, dass das Gedächtnis zur Falle wird:

- **Dreiteilung.** Jeder Eintrag ist dauerhafte Präferenz, veränderlicher Zustand
  oder historisches Ereignis — die Art entscheidet den Umgang. Bei „das ist
  inzwischen erledigt" wird der Zustand geändert, nicht eine zweite Notiz daneben
  gelegt — sonst taucht die alte später als offene Aufgabe wieder auf.
- **Umkehrbedingung.** Was veralten kann (Versionen, Pfade, Zuständigkeiten,
  Zustände), bekommt drei Teile: Datum, die Bedingung, an der man merkt, dass neu
  entschieden werden muss, und die Anweisung *neu prüfen, nicht annehmen*. Muster:
  „Deploy läuft über `deploy.sh` (Stand 2026-10-12 — gilt, solange das Skript im
  Repo liegt; bei Fehler neu prüfen)."
- **Fundortpflicht.** „Du hast am … gesagt" (mit Fundort) und „mein Eindruck ist"
  (jederzeit korrigierbar) bleiben unterscheidbar — eine Vertrauensfrage, keine
  Ordnungsfrage.
- **Nichts Tägliches, nichts Nachlesbares.** Kein Tageszustand, kein Vorratswissen,
  keine Duplikate, keine Absichten. Und ausdrücklich vereinbaren, **was nie** in
  Memories gehört: Credentials, Inhalte aus `private/`.
- **Das Warum bleibt.** Bei `project`-Einträgen gehört der Grund einer Entscheidung
  dazu — und was verworfen wurde. Sonst dreht ein späterer Agent eine bewusst
  gewählte Richtung mit gutem Gewissen zurück.

Gepflegt wird an Anlässen, nicht an Terminen: Bei jeder Richtungsänderung werden
betroffene Einträge im selben Zug nachgezogen; bei jedem Fehler, der auf einen
Eintrag zurückgeht, wird der Eintrag repariert oder gelöscht — nicht nur das
Ergebnis.

## Block 6 — Abschluss und Übergabe in die Begleitung

1. **Eigene Anwendung.** Eine kleine passende Korrektur von der Person selbst
   durchführen oder erklären lassen und die Wirkung prüfen. Die hilfreichen Grundbilder
   daran benennen; keine Begriffsprüfung als Pflicht. Bereits vorhandene Kompetenz anerkennen.
2. **Begleitung anbieten.** Nur bei gewünschter Fortsetzung einen `project`-Memory-Eintrag
   im tatsächlichen System anlegen: Status aktiv/pausiert/aus, Begleitgrad, relevante
   Beobachtungen mit Quellen, offene Punkte und nächster sinnvoller Anlass. Technische
   Handlungsfreigaben gehören getrennt in die gültige Regel-/Rechtestruktur.
3. **Die erste Korrektur einplanen** (`didaktik.md`, Anker-Erfahrung 1): einen
   bewusst überschreibbaren Vorschlag markieren, an dem der Nutzer erlebt, dass
   Korrigieren wirkt.
4. **Ladeprüfung belegen.** Das Verfahren in `bestandsaufnahme.md` verwenden.
   Automatische Ladung, manuelles Lesen und bloße Erreichbarkeit unterscheiden.
   Kann die neue Sitzung nicht geprüft werden, den konkreten Schritt der Person
   übergeben und das Ergebnis als offen kennzeichnen.
5. **Wiedereinstieg vereinbaren.** Den nächsten hilfreichen Anlass an echter Arbeit
   festmachen. Ohne geprüften technischen Auslöser bedeutet das: Die Person ruft den
   Skill erneut auf; die Begleitnotiz lädt sich nicht selbst. Eine vorhandene Erinnerung
   oder ein Hook ist nur nach Verfügbarkeitsprüfung und passender Zustimmung eine Option.
   Pause, Beendigung und Änderungen an diesem Wunsch bleiben jederzeit möglich.

Offenes als `OFFEN` festhalten, nicht weglassen.
