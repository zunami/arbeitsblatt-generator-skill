Verbesserungen im Arbeitsblatt-Generator Skill: verlässlichere Rückfragen, bereinigte Anleitung und reproduzierbare Veröffentlichung. Die bestehenden Fachregeln, Skripte und die zwei Arbeitsmodi bleiben erhalten.

## Änderungen seit Version 0.1.1

- Fehlende Angaben zur Blattgestaltung nur noch dann erfragen, wenn sie für die Aufgabe tatsächlich nötig und im Chat noch offen sind. Bei klaren Vorgaben die Bearbeitung nicht durch wiederholte Rückfragen verzögern.
- Doppelte Abschnittsüberschrift im Skill bereinigt.
- Einheitlicher Ablauf für künftige GitHub-Releases: kurzer Titel `Version X.Y.Z`, ausführlicher Änderungsverlauf und richtige Kennzeichnung als regulärer Release oder ausdrücklich gewünschte Vorabversion.
- Vor Veröffentlichung Tests und SHA-256-Prüfsumme des Installationspakets prüfen; bestehende Releases nicht still ersetzen.

## Umfang und Grenzen

Schwerpunkt bleibt Mathematik im österreichischen Schulkontext. Deutsch und Englisch sind vorhanden, aber nicht ausreichend praktisch erprobt. Separate Lösungsblätter und die Handschriftbereinigung sind weiterhin vorgesehen. Ein erfolgreich getestetes Skript ist keine Zusicherung für fehlerfreie KI-Ergebnisse. Aufgaben und Lösungen vor der Verwendung kontrollieren.

## Versionsschema

- `0.1.x`: Korrekturen und präzisierte Abläufe ohne neue Fachfunktion.
- `0.2.0`: größere neue Aufgaben-/Prüffunktionen, einschließlich klar dokumentierter Änderungen im Erprobungsstadium.
- `1.0.0`: erst nach dokumentierter praktischer Abnahme als stabil eingestuft.

## Download und Versionspflege

Unter **Assets** `skill.zip` herunterladen; `SHA256SUMS` ist die zugehörige Prüfsummendatei. Nicht mit dem automatisch von GitHub erzeugten Quellcode-ZIP verwechseln. SHA-256 für die vorbereitete Version `0.1.2` (`skill.zip`): `7db22165e8eb0013884572036984cdb81ae019b1618496c66b8f4be3c18030e2`.

Die Versionsregeln stehen in [VERSIONIERUNG.md](https://github.com/zunami/arbeitsblatt-generator-skill/blob/main/VERSIONIERUNG.md), die Installation in [INSTALLATION.md](https://github.com/zunami/arbeitsblatt-generator-skill/blob/main/INSTALLATION.md).

Kein eigenständiges Programm und kein offizielles Angebot von OpenAI oder einer Schule. Projektinhaber: zunami. Dieses Release wird erst nach ausdrücklicher Freigabe der endgültigen Beschreibung und des Installationspakets veröffentlicht.
