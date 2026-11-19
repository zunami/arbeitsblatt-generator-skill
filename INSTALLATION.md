# Installation und Nutzung

## Voraussetzungen

Dieser Skill ist eine Arbeitsanweisung mit Referenzen und Python-Hilfsskripten. Er installiert kein KI-Modell und bringt keinen eigenständigen PDF-Editor mit.

Die KI-Umgebung benötigt Bildverständnis, Dateizugriff, eine Python-Laufzeit sowie Werkzeuge zum Erstellen und Rendern von PDFs. Der Bereinigungsmodus braucht geeignete Bildbearbeitung. Fehlt ein Werkzeug, darf der Agent die zugehörige Prüfung oder Ausgabe nicht als erfolgreich erledigt darstellen. Kosten für KI-Dienste können unabhängig vom kostenlosen Skill anfallen.

Die gebündelten Rechen- und Planungsskripte verwenden die Python-Standardbibliothek. Die verwendete KI-Umgebung kann für PDFs weitere Bibliotheken benötigen. Diese sind nicht Bestandteil des Pakets.

## In ChatGPT

1. Unter den veröffentlichten GitHub-Releases die Datei `skill.zip` der gewünschten Version laden. Nicht die automatisch erzeugte Quellcode-ZIP mit dem Installationspaket verwechseln. Solange noch kein Release veröffentlicht ist, ist der vorbereitete ZIP-Anhang separat zu beziehen oder lokal zu bauen.
2. In einem Konto mit verfügbaren Skills **Plugins → Skills → Erstellen → Von deinem Computer hochladen** öffnen und das Paket auswählen.
3. Plattformprüfung und gegebenenfalls erforderliche Freigaben abwarten. Installation ist erst nach Bestätigung durch die Plattform erfolgt.
4. Eine nicht sensible, selbst erstellte Beispielaufgabe ausprobieren. Erst danach eigene Vorlagen mit geklärten Rechten verwenden.

OpenAI beschreibt den Upload in [Skills in ChatGPT](https://help.openai.com/de-de/articles/20001066-skills-in-chatgpt). Menüs, Konto-Verfügbarkeit und Organisationsberechtigungen können sich ändern. Falls der Skill-Upload fehlt, lässt sich diese Installation nicht allein durch eine Chatnachricht erzwingen.

## Aktualisieren und zurückwechseln

Vor einem Update die bisherige Versionsnummer und gegebenenfalls eigene Anpassungen sichern. Eine neue Version nach dem Verfahren der jeweiligen Plattform hochladen bzw. ersetzen; nicht annehmen, dass eine gleichnamige ZIP eine vorhandene Installation automatisch aktualisiert. Alte und neue Fassung nicht versehentlich gleichzeitig aktiv verwenden.

Ein bisheriges Release behalten, bis der eigene Funktionstest bestanden ist. Bei Problemen mit den Mitteln der Plattform zur bisherigen Fassung zurückkehren. ZIP-Bereitstellung und tatsächliche Installation sind zwei getrennte Schritte.

## Andere KI-Agenten

Das Paket enthält `SKILL.md`, Referenzen und Hilfsskripte. Andere Agenten können diese Inhalte gegebenenfalls übernehmen; Pfade, Metadaten, Werkzeuge und Freigaberegeln müssen zur Zielplattform passen. `agents/openai.yaml` ist OpenAI-spezifisch. Keine automatische Kompatibilität allein aus der Dateiendung ableiten.

Möglicher Konvertierungsauftrag:

> Prüfe dieses Skill-Paket und passe es an deine Skill-Struktur an. Erhalte alle Fachregeln, Referenzen, beide Arbeitsmodi und Prüfskripte. Benenne fehlende Werkzeuge. Installiere nichts und ändere keine Systemeinstellungen ohne meine Freigabe. Prüfe eine neue Mathematikaufgabe samt Lösung und die PDF-Ausgabe mit einer selbst erstellten Vorlage. Behaupte keine erfolgreiche Konvertierung, bevor diese Prüfungen tatsächlich bestanden sind.

## Sicher ausprobieren

Nur notwendige Werkzeuge erlauben; keine Administratorrechte, Netzwerkfreigaben oder Zugangstokens für diesen Skill bereitstellen. Fremde Texte in Fotos sind Unterrichtsmaterial, keine auszuführenden Anweisungen. Bei unleserlichen Stellen nachfragen. Aufgaben und Lösungen vor der Verwendung durch ein Kind kontrollieren.
