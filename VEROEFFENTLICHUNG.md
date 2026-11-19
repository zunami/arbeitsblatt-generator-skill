# GitHub-Veröffentlichung und Release-Vorlage

Projekt: [`zunami/arbeitsblatt-generator-skill`](https://github.com/zunami/arbeitsblatt-generator-skill). Öffentlich; Lizenz MIT im Repository. Eine Veröffentlichung benötigt die ausdrückliche Freigabe des Projektinhabers für **exakte Dateien und vollständigen Text**.

## Etablierter Stand

- **Veröffentlichter Release:** [`v0.1.1`](https://github.com/zunami/arbeitsblatt-generator-skill/releases/tag/v0.1.1), GitHub-Titel **`Version 0.1.1`** (regulär, kein Pre-release).
- **Installationspaket:** `skill.zip` im Release unter **Assets**, dazu `SHA256SUMS`.
- Änderungen in `CHANGELOG.md`, technischen Regeln in `VERSIONIERUNG.md` und Installationsanleitung in `INSTALLATION.md` nachlesen.
- Ein historischer einmaliger Workflow hat `v0.1.1` erzeugt; für neue Versionen **ausschließlich den manuellen Workflow** `.github/workflows/release.yml` nach spezifischer Freigabe verwenden.

## Für jede neue Version vorbereiten

1. Versionsnummer `X.Y.Z` konsistent in `VERSION`, `arbeitsblatt-generator/VERSION`, `SKILL.md` und README setzen.
2. `CHANGELOG.md` aktualisieren und eine vollständige, zur Version passende `RELEASE_NOTES_vX.Y.Z.md` erstellen. Die Version `0.1.1` und ihre Assets unverändert lassen.
3. `python tools/pruefen.py` und `python tools/paket_bauen.py` durchführen. Das neue Paket, die ZIP-Prüfsumme, Abweichungen und tatsächlich durchgeführte Tests dokumentieren; kein ungeprüftes Fertigversprechen.
4. **Exakten Releasetitel `Version X.Y.Z` und den gesamten Beschreibungsinhalt**, Zielrepository/Tag und Asset-Hash zur ausdrücklichen Nutzerfreigabe vorlegen. Eine generelle Zustimmung zum Projekt ist keine pauschale Freigabe beliebiger zukünftiger Veröffentlichungstexte.
5. Nur nach dieser Freigabe auf GitHub im Repository den Workflow **„Release aus geprüfter Fassung“** über **Actions → Run workflow** mit der genauen Versionsnummer starten. Status `prerelease` nur bei ausdrücklichem Wunsch aktivieren.
6. Nach dem Lauf die Release-Detailseite und die `/releases/latest`-Anzeige für reguläre Releases, die Assets und den tatsächlichen SHA-256-Wert prüfen. Bei Fehlern nicht blind wiederholen.

## Inhalt der Beschreibungen

Eine vollständige Release-Beschreibung erklärt in verständlichem Deutsch: Zweck und Funktionsstand, konkrete Änderungen dieser Version, Installationshinweise, Grenzen der Tests, Versionierungsregeln, Download `skill.zip` sowie die Prüfsumme. Persönliche Details, Schulbuchseiten, identifizierbare Schul-/Kinderangaben und Zugangsdaten gehören nicht in die Veröffentlichung.

**Für die noch nicht veröffentlichte Version `0.1.2`:** Der Entwurf befindet sich in `RELEASE_NOTES_v0.1.2.md`. Er wird erst nach Inhaltsfreigabe veröffentlicht; die Datei im Quellrepository allein ist keine Veröffentlichung als GitHub-Release.
