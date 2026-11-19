# Arbeitsblatt-Generator Skill

**Neue schulnahe Übungen aus Fotos erstellen – mit passenden Lösungsblättern.**

Version **0.1.1** · frühe Erprobungsfassung · Schwerpunkt Mathematik · österreichischer Schulkontext

## Warum ich diesen Skill gebaut habe

Ich habe mir diesen Arbeitsblatt-Generator mit Unterstützung von ChatGPT gebaut, um meiner Tochter beim Lernen für die Schule zu helfen.

Viele Eltern kennen die Situation: Man möchte mit seinem Kind üben, hat aber oft nur ein paar Arbeitsblätter, Buchseiten oder die Stoffangabe der Schule. Daraus selbst passende neue Übungen zu machen, kostet Zeit. Und einfach irgendwelche Aufgaben aus dem Internet zu nehmen, hilft nicht unbedingt, wenn sie anders aufgebaut sind oder einen anderen Rechenweg verlangen.

Bei unserer Vorbereitung auf Schularbeiten und Tests ist mir besonders wichtig, dass die Aufgabenart vertraut bleibt. Meine Tochter soll nicht an einer ungewohnten Darstellung scheitern, sondern das üben können, was in der Schule behandelt wurde – mit neuen Zahlen und neuen Beispielen, statt die Lösungen eines bereits ausgefüllten Blattes auswendig zu lernen.

Dafür ist dieser Skill entstanden. Er soll die schulische Vorgabe verstehen und daraus zusätzliche Übungsmöglichkeiten machen. Er ist eine Lernhilfe, kein Ersatz für Lehrkräfte oder die Begleitung durch Erwachsene.

## Was ist das genau?

Ein Skill ist ein Paket aus Anweisungen, Fachregeln und Hilfsskripten für einen KI-Assistenten. Dieser Skill ist **keine eigenständige App, keine Website und kein eigenes KI-Modell**. Die KI-Umgebung muss Bilder verstehen, Dateien erzeugen und für die Mathematikprüfung Python ausführen können. Für das Entfernen von Handschrift braucht sie zusätzlich geeignete Bildbearbeitungswerkzeuge.

Der Skill ist für österreichische Schulbegriffe und Darstellungen ausgelegt. Eine bestimmte Lehrplanabdeckung, Prüfungsnote oder Fehlerfreiheit wird nicht zugesichert.

## Was lässt sich damit machen?

### 1. Neue Übungsblätter aus Fotos erstellen

Ein oder mehrere schulische Arbeitsblätter fotografieren – ausgefüllt oder noch leer – und neue Übungen anfordern. Die KI soll Aufgabenarten, Zahlenraum, Schwierigkeitsgrad, Schreibflächen und den bekannten Rechenweg erkennen und bei der neuen Fassung berücksichtigen.

Bei Mathematik entstehen neue Aufgaben mit anderen Zahlen, bei Bedarf auch anderen Maßen, Figuren oder selbst formulierten Sachtexten. Es geht um die gleiche geübte Fähigkeit und eine vertraute Bearbeitung, **nicht um eine möglichst genaue Kopie einer fremden Buchseite**.

Neue Übungen werden als **Arbeitsblatt.pdf** und separates **Loesungen.pdf** angelegt. Beide Fassungen sollen dieselben Aufgaben in derselben Reihenfolge enthalten; Rechenwege oder Erklärungen können zusätzlich gewünscht werden.

### 2. Mehrere Vorlagen mischen

Mehrere Blätter oder Buchseiten lassen sich als Grundlage für eine neue Serie verwenden. Auf Wunsch werden Aufgabenfamilien gemischt, anders angeordnet oder auf Themenschwerpunkte verteilt.

Dabei soll nicht wahllos durcheinandergewürfelt werden: Der Schulstoff, notwendige Vorkenntnisse und der gewünschte Umfang bleiben maßgeblich. Bei vielen Vorlagen wird geklärt, ob jede Aufgabenfamilie vorkommen soll oder eine Auswahl reicht.

### 3. Handschrift entfernen, gedruckte Aufgaben beibehalten

Manchmal fehlt genau das Blatt, das das Kind noch bearbeiten soll. Ein typischer Anlass ist eine vergessene Hausübung: Andere Eltern können ein Foto ihrer bereits ausgefüllten Fassung schicken.

**Soweit die erforderlichen Nutzungsrechte oder eine passende gesetzliche Erlaubnis bestehen**, soll der Bereinigungsmodus daraus eine wieder ausfüllbare Kopie erstellen. Die gedruckten Zahlen, Aufgaben, Linien und Kästchen bleiben unverändert; entfernt werden nur die gewünschten handschriftlichen Einträge. Das Kind bearbeitet die Aufgaben anschließend selbst.

Verdeckte oder unleserliche Druckzeichen dürfen nicht erfunden werden. Wenn eine originalgetreue Bereinigung nicht gelingt, muss die KI das sagen. Das Original bleibt erhalten. In diesem Modus entsteht grundsätzlich nur die bereinigte PDF; ein Lösungsblatt gibt es auf ausdrücklichen Wunsch. Urheber-, Verlags- und Quellenhinweise werden nicht zur Verschleierung der Herkunft entfernt.

## Ehrlicher Entwicklungsstand

| Bereich | Aktueller Stand |
| --- | --- |
| **Mathematik** | Mein Schwerpunkt, weil wir hier am meisten üben. Dafür sind die Regeln und rechnerischen Prüfungen am umfangreichsten. Auch hier sind Fehler möglich. |
| **Deutsch** | Fachmodul vorhanden, aber in meiner bisherigen Nutzung fehlen ausreichende konkrete Beispiele und praktische Erprobung. Deshalb experimentell. |
| **Englisch** | Ebenfalls als Fachmodul vorgesehen, bisher aber nicht ausreichend praktisch erprobt. Deshalb experimentell. |
| **Handschrift entfernen** | Als eigener Arbeitsmodus beschrieben. Die Qualität hängt vom Foto und vom Bildbearbeitungswerkzeug ab; unveränderten Druck immer vergleichen. |

Der Skill verlangt rechnerische Gegenprüfungen sowie eine Sichtkontrolle der erzeugten PDFs. Das ist eine Arbeitsanweisung, **keine Garantie**, dass jedes KI-Modell sie vollständig und richtig ausführt. Vor dem Ausdrucken Aufgaben und Lösungen bitte selbst kontrollieren. Der tatsächliche Prüfumfang dieser Fassung steht in [PRUEFBERICHT.md](PRUEFBERICHT.md).

## Herunterladen und installieren

Die installierbare Datei heißt **skill.zip**. Für veröffentlichte Fassungen ist sie als eigener Anhang unter **Releases** vorgesehen. Die ZIP mit dem gesamten Repository ist nicht das Installationspaket.

In ChatGPT mit freigeschalteter Skill-Funktion: **Plugins → Skills → Erstellen → Von deinem Computer hochladen** und `skill.zip` auswählen. Verfügbarkeit und Bezeichnungen hängen vom Konto und der aktuellen Oberfläche ab. Die genaue Anleitung, Voraussetzungen und Hinweise zum Aktualisieren stehen in [INSTALLATION.md](INSTALLATION.md).

Andere KI-Agenten können die Anweisungen und Dateien gegebenenfalls ebenfalls nutzen. Eine KI kann bei der Anpassung helfen; **automatische Konvertierung und vollständige Kompatibilität sind aber nicht garantiert**. Bildverarbeitung, Python, PDF-Erzeugung und Dateizugriff müssen auch dort tatsächlich verfügbar sein. Ein reiner Text-Chat ersetzt diese Werkzeuge nicht.

## Drei Beispiele für den Auftrag

**Neue Mathematikübungen:**
> Erstelle aus diesen Fotos zwei neue Mathematik-Arbeitsblätter mit anderen Zahlen. Behalte die Aufgabenarten, die bekannte Rechenweise und den Schwierigkeitsgrad bei. Ich brauche auch passende separate Lösungsblätter.

**Gemischtes Training:**
> Erstelle aus diesen drei Vorlagen ein gemischtes Übungsblatt. Jede erkennbare Aufgabenfamilie soll mindestens einmal vorkommen. Verwende neue Zahlen und kontrolliere alle Lösungen.

**Nur Handschrift entfernen:**
> Entferne aus einer Kopie nur die handschriftlichen Antworten. Verändere keine gedruckten Zahlen, Aufgaben, Quellenhinweise oder Linien. Gib mir eine wieder ausfüllbare A4-PDF. Falls Druck verdeckt oder unleserlich ist, frage nach, statt etwas zu erfinden.

## Weiterentwicklung und Rückmeldungen

Ich möchte den Skill anhand unserer Erfahrungen weiter verbessern und neue Versionen veröffentlichen. Das passiert in meiner Freizeit, ohne feste Termine oder Supportzusage. Ein Versionsverlauf zeigt, was geändert wurde; bereits veröffentlichte Pakete werden nicht still ausgetauscht.

Rückmeldungen sind willkommen, besonders zu unklaren Aufgaben, falschen Lösungen und zu wenig Schreibraum. Bitte Versionsnummer, verwendete KI-Umgebung, Fach und eine **selbst erstellte, anonymisierte** Beispielaufgabe nennen. Keine echten Kinderfotos, Namen, Schulangaben oder fremden Schulbuchscans in öffentliche Issues laden. Mehr dazu in [BEITRAGEN.md](BEITRAGEN.md) und [DATENSCHUTZ.md](DATENSCHUTZ.md).

## Rechte, Haftung und Grenzen

Mit diesen Projektinformationen werden keine zusätzlichen vertraglichen Garantien für bestimmte Noten, einen bestimmten Lernerfolg, die vollständige Abdeckung eines Lehrplans oder dauerhafte Kompatibilität abgegeben. Die Lernhilfe ersetzt nicht die Begleitung durch Erwachsene oder die fachliche Beurteilung durch Lehrkräfte.

Diese Projektinformationen enthalten keinen zusätzlichen pauschalen Haftungsausschluss und verlangen keinen generellen Verzicht auf gesetzliche Ansprüche. Ob und in welchem Umfang die Regelungen der MIT-Lizenz im konkreten Fall wirksam sind, richtet sich nach dem anwendbaren Recht. Gesetzlich nicht abdingbare Ansprüche werden durch das Projekt nicht aufgehoben.

Die Projektlizenz betrifft nur die vom Projekt rechtmäßig bereitgestellten eigenen Inhalte. Sie erteilt **keine Rechte an fremden Arbeitsblättern, Schulbüchern, Bildern, Logos oder hochgeladenen Dateien**. Privatgebrauch ist nicht automatisch eine Erlaubnis, Material an einen Cloud-Dienst zu übermitteln oder im Internet zu veröffentlichen. Das Ändern von Zahlen oder Entfernen von Handschrift macht fremdes Material nicht automatisch frei nutzbar.

Vorlagen nur mit ausreichender Berechtigung verwenden. Bei unklaren Rechten stattdessen Thema, Aufgabenart und Lernziel beschreiben und eigenständige neue Beispiele erstellen lassen. Vollständige Hinweise: [RECHTLICHES.md](RECHTLICHES.md), [LIZENZ.md](LIZENZ.md) und [LICENSE](LICENSE).

---
Von **zunami** mit Unterstützung von **ChatGPT** entwickelt. Eigenständiges Privatprojekt; kein offizielles Angebot und keine Freigabe von OpenAI, einer Schule oder einem Schulbuchverlag.
