# Anhang Qoder — harness-abhängige Einzelheiten

*Datierte Orientierung aus dem bisherigen Qoder-Referenzsetup (Stand 2026-10-12),
keine Zusage über eine andere Installation. Pfade und Felder können sich mit Versionen
ändern — vor Änderungen in der tatsächlichen Umgebung prüfen. Die Konzepte
stehen in `../didaktik.md`; hier steht nur, wo sie bei Qoder konkret liegen. Gepflegt
wird diese Datei wie eine Abhängigkeit: datiert, und nur mit Geprüftem.*

## Pfade (Windows)

| Was | Wo |
|---|---|
| Globale Regeln (Ladung prüfen) | `<Benutzerprofil>\.qoder\agents.md` |
| Memory-Dateien + Index (falls vorhanden) | `<Benutzerprofil>\.qoder\memory\` und `MEMORY.md` dort |
| Projekt-Memory (Zuordnung prüfen) | `<Benutzerprofil>\.qoder\projects\<workspace-slug>\memory\` |
| Eigene Skills (Benutzerebene) | `<Benutzerprofil>\.qoder\skills\<name>\SKILL.md` |
| Skills (Projektebene) | `<workspace>\.qoder\skills\<name>\SKILL.md` |
| Hooks (falls unterstützt) | `<Benutzerprofil>\.qoder\hooks\`, Registrierung in der konkreten Version prüfen |

`<Benutzerprofil>` aus der aktuellen Umgebung ermitteln. Workspace-Slug und tatsächliche
Ladeorte nicht aus einem alten Rechnerpfad ableiten. Eine vorhandene Datei ist noch kein
Ladebeleg; das Verfahren in `../bestandsaufnahme.md` anwenden. Konfigurationsdateien mit
möglichen Credentials nicht vollständig einlesen.

## Skills in Qoder

- Ein Skill ist ein Ordner mit `SKILL.md`: YAML-Frontmatter (`name`, `description`
  — eine Zeile, max. 1024 Zeichen) plus Markdown-Rumpf; Referenzdateien daneben
  werden erst bei Bedarf geladen.
- Qoder kennt zusätzliche Frontmatter-Felder, u. a. `disable-model-invocation`
  (der Skill startet nur per explizitem Aufruf `/name`, nicht automatisch) und
  `argument-hint`.
- Nach dem Anlegen die Skill-Sichtbarkeit in der konkreten Installation prüfen.
  Session-Neustart sowie `/skills reload` und `/skills list` sind Kandidaten aus dem
  Referenzsetup; unbekannte Befehle nicht als sicher verfügbar versprechen.

## Memories in Qoder

- Im Referenzsetup: eine Datei je Eintrag, kebab-case-Name, YAML-Frontmatter mit `name`,
  `description`, `metadata.type` (`user`, `feedback`, `project`, `reference`);
  der Index `MEMORY.md` ist eine Zeile pro Eintrag, keine Inhalte.
- Praxis: Typ-Präfix im Dateinamen (`user-…`, `feedback-…`, `reference-…`),
  Verknüpfungen als `[[datei-name]]`, relative Daten immer absolut schreiben.

## Die Begleitung bei Qoder fortsetzen

- Den vorhandenen Memory-Ort ermitteln und die Begleitnotiz dort referenzieren.
  Ohne aktiven Ladeweg kann ein erneuter ausdrücklicher Skill-Aufruf nötig sein.
- Einen Session-Hinweis oder Hook nur nach Prüfung der unterstützten Ereignisse,
  tatsächlicher Registrierung und eines beobachteten Probelaufs anbieten. Eine
  Hook-Konfiguration allein belegt weder die Wiederaufnahme noch Hintergrundaktivität.
- Die Person wählt, ob sie solch einen Wiedereinstieg möchte. Ohne eingerichteten
  Auslöser bleibt die Fortsetzung bei ihrer nächsten Anfrage.
- Hooks dürfen keine Secrets ins Repo oder in Antworten leiten und sind für sich
  keine Sicherheitsgrenze.

## Modi bei Qoder

Qoder kennt u. a. einen **Planungsmodus**: Der Agent liefert zuerst einen prüfbaren
Plan und handelt erst nach Freigabe — die Antwort auf „erst übergriffig, dann
zögerlich". Für das Lernelement „Harness-Modi" (siehe `../didaktik.md`) ist er das
anschaulichste Beispiel. (Stand 2026-10-12; Bezeichnung und Tastenkürzel in der
eigenen Version prüfen.)

## Bekannte Grenzen (Stand 2026-10-12)

- Im Auto-Modus sind manche Schreibzugriffe außerhalb des Workspaces gesperrt —
  Dateien unter `~/.qoder` (Skills, Hooks) legt der Nutzer im Zweifel selbst an;
  der Agent bereitet den Inhalt vor.
- Rechte und externe Aktionsprüfung müssen Schutz für die konkrete Aktion und
  ihre Nutzlast durchsetzen. Markdown-Regeln und Hooks allein garantieren das nicht.

Quelle: frühere Fassung dieses Qoder-Anhangs in der Git-Historie, Stand
2026-10-12; Einordnung und Portabilitätskorrektur auf Manuels Auftrag, Stand 2026-10-25.
