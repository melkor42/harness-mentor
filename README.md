# Harness Mentor

Ein persönlicher Onboarding- und Begleit-Skill für die Arbeit mit KI-Agenten.
Er hilft dir, deinen Arbeitsrahmen zu verstehen, passend einzurichten und zunehmend
selbstständig weiterzuentwickeln.

- **Einrichten:** vorhandene Konfiguration prüfen, passende Arbeitsweisen entwickeln
  und nur den fehlenden Kontext ergänzen.
- **Begleiten:** konkrete Reibung aufgreifen, Korrekturen nachvollziehbar machen und
  die Unterstützung schrittweise zurücknehmen. Du kannst pausieren oder beenden.

## Installation

Lade dieses Repository herunter. Kopiere den gesamten Ordner
[`.qoder/skills/harness-mentor/`](.qoder/skills/harness-mentor/SKILL.md) einschließlich
`references/` und `assets/` in `.qoder/skills/` deines Qoder-Workspaces.
Wenn der Ordner schon existiert, sichere deine Anpassungen und vergleiche die Dateien vor dem Ersetzen.
Prüfe anschließend in deiner Installation, ob `harness-mentor` als Skill erkannt wird;
gegebenenfalls die Sitzung neu starten.

Aufruf: `/harness-mentor`. Zum Beispiel:

> Prüfe zuerst mein vorhandenes Setup. Ich möchte wissen, welcher Kontext tatsächlich
> geladen wird und welche kleine Verbesserung mir bei meiner Arbeit hilft.

Für einen neuen Einstieg kannst du stattdessen um eine gemeinsame Einrichtung bitten.
Der Skill arbeitet als Anleitung für deinen Agenten; er ist kein eigenständig laufender Dienst.

## Voraussetzungen und Grenzen

Der Agent benötigt Zugriff auf die von dir freigegebenen relevanten Workspace-Dateien und,
wenn du Anpassungen möchtest, passende Schreibrechte. Zugangsdaten gehören nicht in den Skill.
Welche Funktionen, Dateinamen und Ladewege verfügbar sind, hängt von deinem Harness ab.
Der enthaltene Qoder-Anhang ist datierte Orientierung, kein Kompatibilitätsnachweis für
jede Version. Andere Harnesses müssen ihre tatsächlichen Konventionen prüfen; allein
die Übernahme einer Vorlage stellt noch keine automatische Ladung her.

Die Begleitung setzt bei einem erneuten Aufruf fort, sofern ihr gespeicherter Stand
zugänglich ist. Erinnerungen oder automatische Sitzungshinweise werden nur mit einem
tatsächlich vorhandenen, geprüften Mechanismus und deiner Zustimmung eingerichtet.
Eine langfristige Wirkung ist noch nicht unabhängig nachgewiesen.

Quelle: mitgelieferter Skill und Manuels freigegebene Weiterentwicklung, Stand 2026-10-25.
