## Schriftliche Division: vollständige Rechenwege

Diese Version verbessert die Darstellung schriftlicher Divisionen in Mathematik-Arbeitsblättern und ihren Lösungsblättern. Anlass war ein praktischer Fehler: Zwischenschritte wurden nebeneinander statt untereinander dargestellt. Die Rechenwege sollen nun in der aus der Schulvorlage bekannten Form nachvollziehbar bleiben.

### Änderungen seit Version 0.1.2

- Vollständige schriftliche Division mit stellenrichtig untereinander angeordneten Teilzahlen, Minuszeilen und Zwischenresten.
- Nach jeder Subtraktion wird die nächste Ziffer zum verbleibenden Rest heruntergeholt; der daraus entstehende neue Teilwert ist sichtbar.
- Nullen im Quotienten sowie der letzte Rest werden ausdrücklich berücksichtigt. Ohne entsprechende Schulvorgabe wird eine Division mit Rest nicht stillschweigend als Dezimaldivision fortgesetzt.
- Neuer vektorbasierter Kästchenraster-Renderer für vollständige Divisionslösungen mit Platzprüfung; bei zu wenig Platz wird die Ausgabe abgebrochen statt ein Rechenschritt weggelassen.
- Zusätzliche Fach- und Layoutregeln sowie automatisierte Regressionstests für schriftliche Division.

### Tests und Grenzen

Lokal bestanden die neuen Divisionstests mit 1.000 zufälligen Beispielen, acht Referenzfällen, Renderer- und Negativprüfungen. Auch die bisherigen Mathematik-Prüftestgruppen wurden erneut erfolgreich ausgeführt. Eine vollständige praktische Abnahme aller erzeugbaren Arbeitsblätter, Bildbereinigungen und Skill-Installationen ist damit nicht nachgewiesen. Aufgaben, schriftliche Rechenwege und PDFs sind vor der Verwendung weiterhin zu kontrollieren.

### Bestehende Funktionen

Die bisherigen Arbeitsmodi und Fachmodule bleiben erhalten: neue Übungen aus Vorlagen, getrennte Lösungsblätter, Handschriftbereinigung sowie Mathematik, Deutsch und Englisch im österreichischen Schulkontext. Die konkrete Schulvorlage hat bei Rechenverfahren und Darstellung Vorrang.

### Download und Installation

Unter **Assets** `skill.zip` herunterladen; `SHA256SUMS` enthält die SHA-256-Prüfsumme. Das automatisch von GitHub angebotene Quellcode-ZIP ist nicht das installierbare Skill-Paket.

SHA-256 (`skill.zip`): `87ca401a0d58e517045af790f7ed6780a69491fe9ed681e23fdc130cb3233119`

Installation und Voraussetzungen: [INSTALLATION.md](https://github.com/zunami/arbeitsblatt-generator-skill/blob/main/INSTALLATION.md). Die Bereitstellung eines ZIP-Pakets aktualisiert keine bestehende Installation automatisch.

Kein eigenständiges Programm und kein offizielles Angebot von OpenAI oder einer Schule. Projektinhaber: zunami.

*Prepared with ChatGPT assistance in collaboration with zunami.*
