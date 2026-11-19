# Versionierung und Veröffentlichung

## Ausgangspunkt

`0.1.0` ist die erste versionierte Erprobungsfassung dieses Projekts. Die zuvor privat verwendete Fassung hatte keine konkrete Versionsnummer; es wird keine erfundene historische Versionsfolge angelegt. Die installierte private Fassung wird durch das Erstellen des Pakets nicht verändert.

## Eine maßgebliche Versionsnummer

`VERSION` im Repository ist die maßgebliche Quelle. `arbeitsblatt-generator/VERSION` und die Versionszeile in `SKILL.md` müssen damit übereinstimmen. Das Bauwerkzeug bricht bei Abweichungen ab. Die YAML-Kopfdaten von `SKILL.md` bleiben auf Name und Beschreibung beschränkt; die Versionsnummer ist eine separate Paketangabe.

Der sichtbare Titel aller künftigen Releases lautet standardmäßig `Version X.Y.Z`; die eigentlichen Änderungen stehen im Beschreibungsfeld. Das Schema orientiert sich an [Semantic Versioning 2.0.0](https://semver.org/lang/de/). Zum Funktionsvertrag gehören die zwei Arbeitsmodi, A4-Schwarz-Weiß, die getrennten passenden Lösungen bei neuen Übungen, die Fachreferenzen sowie die dokumentierten JSON-Eingaben der Hilfsskripte. Es gibt keine eigene Web-API.

- `0.1.x`: Korrekturen ohne neue oder entfernte Funktion, auch korrigierte Anleitung, Fragenlogik oder Release-Workflow.
- `0.2.0`: neue Aufgabenfamilien, neue kompatible Prüfungen oder deutliche Erweiterungen; während `0.x` auch mögliche Brüche ausdrücklich dokumentieren.
- `1.0.0`: erste als stabil festgelegte Fassung nach dokumentierter praktischer Abnahme. Das ist kein Versprechen für absolute Fehlerfreiheit.
- Nach `1.0.0`: inkompatible Änderungen an diesem Funktionsvertrag erhöhen die Hauptversion, kompatible Erweiterungen die mittlere, reine Korrekturen die letzte Stelle.

## Ablauf für ein Release

1. Ausgangsinventar und bisherige Funktionen prüfen; keine Referenzen oder Arbeitsmodi unbeabsichtigt verlieren.
2. Änderungen und vorhandene Tests ausführen. Fach-, Layout-, Bildbereinigungs- und Installationstests getrennt dokumentieren. Nicht ausgeführte Tests offen lassen.
3. Versionsnummer konsistent aktualisieren; `CHANGELOG.md` und Versionshinweise ergänzen.
4. `python tools/pruefen.py` und `python tools/paket_bauen.py` im Repository ausführen.
5. Das erzeugte `dist/v<VERSION>/skill.zip`, die Prüfsumme und den genauen Veröffentlichungstext prüfen und vom Projektinhaber freigeben lassen.
6. **Erst nach Freigabe des exakten Titels, vollständigen Beschreibungstextes und der Paket-Prüfsumme** den manuellen GitHub-Actions-Workflow `release.yml` auslösen. Der Release heißt sichtbar **`Version X.Y.Z`**; die ausführliche Änderungsbeschreibung gehört in den Release-Body. Bei nicht ausdrücklich gewünschter Vorabveröffentlichung **regulären Release** erstellen (nicht aus `0.x` auf `prerelease` schließen).
7. Den fertigen Tag `v<VERSION>`, den Status „Latest“ (nur reguläre Releases), den unveränderten Body und **beide hochgeladenen Assets** (`skill.zip`, `SHA256SUMS`) über GitHub erneut lesen. ZIP-Hash mit dem freigegebenen Paket vergleichen; nur so den Release als verifiziert bezeichnen. Bei Tool-Timeout zuerst den tatsächlichen Stand prüfen, nicht blind erneut auslösen.

Die Version `v0.1.1` ist bereits als regulärer GitHub-Release mit dem Titel `Version 0.1.1` veröffentlicht. Der einmalige Workflow von damals bleibt historisch, wird aber für kommende Versionen nicht wiederverwendet. Keine automatische Veröffentlichung durch diesen Skill; das manuelle Auslösen ersetzt nicht die vorherige Freigabe. Ein geändertes Paket erhält eine neue Version. Alte Tags oder Anhänge nicht heimlich überschreiben. Sicherheitsbedingt zurückgezogene Versionen sichtbar als zurückgezogen markieren.

GitHub-Releases und die interne Versionsverwaltung eines KI-Anbieters sind verschieden. Eine Plattform kann eigene Versionsnummern vergeben; entscheidend für dieses Projekt bleiben `VERSION`, Tag und SHA-256 des Pakets.
