---
name: arbeitsblatt-generator
description: Erstellt kindgerechte schulnahe Übungen für Österreich aus Schulbuchfotos, Screenshots oder Stoffvorgaben, insbesondere Deutsch, Englisch und Mathematik, als A4-Schwarz-Weiß-PDF mit separatem Lösungsblatt, vorgeschriebenen Rechen- und Sichtprüfungen sowie ausgewiesenem Prüfstatus. Auch verwenden bei „bitte entferne die handschriftlichen Zeilen/Einträge“, um ausgefüllte fotografierte Arbeitsblätter zum erneuten Ausfüllen zu bereinigen.
---

# Arbeitsblatt-Generator

**Paketversion: 0.1.3** – erste versionierte Erprobungsfassung. Die Versionsdatei `VERSION` gehört zu diesem Paket.

**Vor Nutzung beachten:** [Rechte, Datenschutz und Plattformgrenzen](references/rechte-datenschutz-plattformen.md) gelten zusätzlich. Vorhandene Fachfunktionen und Prüfpflichten bleiben erhalten. Mathematik ist der Schwerpunkt; Deutsch und Englisch sind noch nicht ausreichend praktisch erprobt.

## Grundsätze

**Skill-Verbesserungen und neue Erfahrungen:** Bei Änderungswünschen zuerst [erfahrungslernen-und-versionierung.md](references/erfahrungslernen-und-versionierung.md) beachten. Bestehende installierte Skill-Struktur vollständig erhalten, Änderungen additiv durchführen und Regressionstests dokumentieren.

- **Österreichisches Sprach- und Darstellungsprofil ist verbindlich.** Vor jeder neuen Aufgabe [oesterreichische-schulsprache.md](references/oesterreichische-schulsprache.md) lesen; bei Mathematik zusätzlich [oesterreichische-matheverfahren.md](references/oesterreichische-matheverfahren.md). Die vom Nutzer gelieferten Muster für schriftliche Division und Winkelmarkierung haben Vorrang vor allgemeinen Standardgrafiken.
- **Nicht blind eindeutschen oder österreichisieren:** schulisch fachrichtige Begriffe verwenden, Nutzer-/Schulbuchnotation respektieren, widersprüchliche Begriffe kontextabhängig prüfen. Rasterzellen beim Rechnen und Zeichnen als **Kästchen** bezeichnen, nicht als Kacheln.
- Bei schriftlichen Divisionsaufgaben in der Volksschule die **vollständige schriftliche Division** mit korrekt ausgerichteten Zwischenschritten verwenden; kein stiller Wechsel zu Kurzdivision oder alternativer Notation. **Verbindlicher Pflichtschritt:** [schriftliche-division-rechenwege.md](references/schriftliche-division-rechenwege.md) lesen, jede Division untereinander notieren und mit `scripts/schriftliche_division.py` inklusive Layout-/Rest-Prüfung erzeugen. Ergebnisse und lose Teilgleichungen nebeneinander gelten ausdrücklich NICHT als fertige Lösung.
- Rechte Winkel in neu erzeugten Schulgeometrie-Grafiken standardmäßig mit **Viertelkreisbogen und Punkt im Winkelinneren** markieren, sofern die aktuelle Vorlage nichts anderes verlangt.

## Allgemeine Grundsätze

- Österreich immer als Schulsystem verwenden. Schulstufe variabel halten; Schulart und Schulstufe unterscheiden. Nicht allein aus einem Thema eine sichere Schulstufe behaupten.
- Pädagogisch sorgfältig arbeiten: Lernziel, Lernstand, eindeutige Aufgaben, verständliche Sprache und Schreibraum vor Menge und Dekoration stellen.
- Aktuelle Screenshots als Vorgabe für Aufgabenform, Anordnung, Notation, Rechenverfahren und Antwortflächen behandeln. Allgemeine Beispielbilder zeigen mögliche Formate, legen kein dauerhaftes Einheitslayout fest.
- Standardmäßig ähnliche neue Aufgaben mit anderen Zahlen bzw. neuen Sätzen erstellen; geübte Kompetenz und Schwierigkeit erhalten. Keine unbekannten Verfahren ungefragt einführen.
- Immer A4 und Schwarz-Weiß ausgeben. Struktur durch Linien, Kästchen, Abstände und Überschriften schaffen, keine farbabhängigen Aufgaben.
- Vorlagenfehler weder ungeprüft übernehmen noch still korrigieren: Stelle benennen und Vorgehen klären. Unleserliche Zeichen nicht erraten.
- Keine absolute Fehlerfreiheit versprechen. Nur tatsächlich ausgeführte Prüfungen als durchgeführt bezeichnen.

## 1. Modus und fehlende Angaben klären

Zwischen **ähnliche Übungen erstellen** und **Handschrift entfernen** unterscheiden. Bei eindeutiger Bitte den passenden Modus automatisch wählen. Bereits vorhandene Antworten wiederverwenden.

Vor neuer Aufgabenerstellung **nur wirklich entscheidende, noch unbeantwortete Angaben** gebündelt erfragen. Die folgenden Punkte sind eine Prüfliste, kein verpflichtender Sechs-Fragen-Dialog. Bereits festgelegte Vorgaben aus diesem Chat und deutlich erkennbare Vorgaben der Vorlage ohne erneute Nachfrage übernehmen. Wenn ein sinnvoller Entwurf trotz einer offenen, nicht entscheidenden Präferenz möglich ist, eine vorsichtige Standardannahme ausdrücklich nennen und die Aufgabe fortsetzen:

1. Schulstufe: nur erfragen, wenn weder Chat noch Vorlage eine sichere Zuordnung erlauben und die Antwort den Schwierigkeitsgrad beeinflusst.
2. Umfang und Schwierigkeit: vorhandene Vorgaben verwenden; bei einer klaren Beispielvorlage ohne Umfangsangabe zunächst **ein A4-Blatt im Schwierigkeitsgrad der Vorlage** anbieten. Größere Serien nicht auf Verdacht festlegen.
3. Lösungen: standardmäßig ein **separates Lösungsblatt mit nachvollziehbaren Rechenwegen** erstellen, außer der Nutzer hat ausdrücklich nur Ergebnisse gewünscht.
4. Bei mehreren Vorlagenseiten und begrenztem Umfang ist die Auswahl wesentlich: **jede erkennbare nummerierte Aufgabenfamilie mindestens einmal** oder **bewusst gewählte Auswahl**. Nur wenn dies aus dem Auftrag nicht hervorgeht, gezielt klären.
5. Bei mehrseitigen Serien für die Prüfungs-/Schularbeitsvorbereitung den Blattaufbau klären, sofern nicht bereits festgelegt: **Themenschwerpunkt je Blatt** oder **gemischte Aufgabenfamilien**. Nicht ohne Auftrag still entscheiden.
6. Wenn keine Aufgabenform erkennbar und keine angegeben ist, zwei passende Formen kurz anbieten oder bei unkritischen Einzelfragen eine begründete Standardform wählen.

Höchstens drei gebündelte, für den Fortschritt tatsächlich notwendige Rückfragen stellen. Keine Abfrage oder Formularwand aus Routine. Unbekannte Schulstufen, verdeckte Druckzeichen und entscheidungsrelevante Widersprüche nicht erraten.

Wenn der Nutzer bereits klar sagt, dass die Vorlage als Vorbereitung auf Unterricht, Lernzielkontrolle oder Test dient, die Entscheidungen zu **Aufgabenfamilien-Abdeckung** und **Mischung je Blatt** besonders wichtig behandeln: Lehrer und verlagsnahe Testmaterialien behalten häufig die vertraute **Art der Aufgabenstellung, Darstellung und Bearbeitung** bei, während Zahlen, Figuren, Wörter und konkrete Inhalte verändert werden.

Alter, Hilfsmittel, besondere Lineatur oder Förderbedarf nur erfragen, wenn wesentlich. Aus Handschrift keine Diagnose ableiten. Englisch-Anweisungen an Schulstufe und Vorlage anpassen: bei Einstieg verständlich deutsch/zweisprachig, bei fortgeschrittenem Niveau passend englisch.

Bei eindeutiger Schulvorlage deren funktionalen Aufbau automatisch übernehmen, statt bereits erkennbare Darstellungswünsche erneut zu erfragen. Nur tatsächlich fehlende, relevante Angaben klären.

Bei reiner Handschriftentfernung keine Fragen nach Schwierigkeit, Umfang oder Schulstufe stellen. Nur unklare Entfernung, verdeckten Druck oder zusätzliche Lösungen klären.

## 2. Vorlage auswerten

- Jedes Bild visuell öffnen. OCR nur unterstützend einsetzen; Rechenzeichen, Hochzahlen, Kommas und Ziffernpositionen mit dem Bild vergleichen.
- Intern Vorlagenprofil festhalten: Fach, Thema, Lernziel, Aufgabenarten, Reihenfolge, Zahlenraum, Überträge, Rest, erlaubte Verfahren, Hilfsmittel und Antwortflächen.
- Druck, Handschrift und Korrekturen unterscheiden. Handschriftliche Lösungen nicht als Beweis übernehmen.
- Funktionalen Aufbau nachbilden; Quellenlogos und Verlagsfiguren bei neuen Übungen nicht als eigene Kennzeichnung übernehmen.
- **Das „Wie“ der Aufgabe ist ein eigener Lerngegenstand.** Erfassen, wie der Auftrag formuliert ist, welche Informationen wo stehen, welche Linien/Kästchen/Tabellen/Geometriehilfen vorhanden sind, in welcher Reihenfolge Teilschritte erwartet werden und **wie das Kind die Aufgabe ausfüllen soll** (z. B. einzeichnen, ergänzen, messen, Rechnung darunter notieren, Antwortsatz schreiben). Diese Bearbeitungslogik bei neuen Übungen erhalten.
- Vorlagentreue bedeutet nicht Kopieren: Zahlen, Maße, Figuren, Reihenfolge innerhalb zulässiger Grenzen und konkrete Inhalte deutlich verändern, aber **Aufgabenkontrakt, vertraute Darstellung, Notation und erwarteten Lösungsweg** beibehalten. Nicht bloß einzelne Zahlen in einer nahezu identischen Aufgabe austauschen.
- Bei Mathematik insbesondere die sichtbare **Ausfüll- und Rechenform** als prüfungsrelevant behandeln: Position von Einträgen, Tabellenstruktur, Kästchenraster, Beschriftungen, Rechenzeilen, Maßeinheiten und bekannte Lösungswege nicht ohne Grund verändern.
- Ohne Vorlage nach geklärten Vorgaben übersichtliches Layout frei entwickeln.

### Schulprofil, Lernlogik und Gestaltung

- Für Klassen-/Niveauplanung [schulstufen-und-niveau.md](references/schulstufen-und-niveau.md) lesen: Volksschule 1–4, Mittelschule 1–4 und AHS-Unterstufe 1–4 getrennt zuordnen. Jahresziele vom bereits behandelten Stoff unterscheiden. Niveau an belegtem Lernstand festmachen, nicht pauschal an Schulart.
- Vor Aufgabenentwicklung/Sortierung [aufgabenlogik-und-sortierung.md](references/aufgabenlogik-und-sortierung.md) lesen. Vollständige Aufgabenkontrakte, Voraussetzungen, deutliche Operatoren, zulässige Lösungen und Reihenfolge aus Lehrerstoff entwickeln. Aufgaben fachlich prüfen, dann nach Abhängigkeit, Thema und Schwierigkeit sortieren; Darstellungsvielfalt innerhalb des Schwerpunkts erhalten.
- Vor neuem/überarbeitetem Layout [druckdesign-und-grafik.md](references/druckdesign-und-grafik.md) lesen. Altersgerechte Druckprofile, Inhaltshöhen, Feldbeschriftung, Schriftmetrik und tatsächliche Schreibkapazität verwenden. UI/UX Pro Max bei explizitem Aufruf zusätzlich anwenden; ausschließlich geeignete Grundsätze für Papier übertragen.
- Die Rechen-/Fachprüfung, didaktisch-sprachliche Prüfung und gerenderte Layoutprüfung als drei separate Durchgänge durchführen. Korrekturen erneut prüfen; nicht „mehrfaches Reasoning“ ohne konkrete Prüfungen als Qualitätsnachweis ausgeben.

### Vollständige Erfassung und abwechslungsreiche Serien

Bei mehreren Vorlagen oder mehrtägiger Schularbeitsvorbereitung vor dem Entwurf [vorlagentreue-und-schreibraum.md](references/vorlagentreue-und-schreibraum.md) lesen.

- Alle Dateien und alle unterschiedlichen Buchseiten einzeln visuell erfassen; Kontaktbögen nur zur Orientierung nutzen. Dubletten kennzeichnen. Pro Seite jede nummerierte Aufgabenfamilie, deren Rechenmethode, Darstellung und Schreibflächen inventarisieren. Ein Themenetikett wie „Multiplikation“ ersetzt diese Erfassung nicht.
- Eine Abdeckungsmatrix aus Lehrerstoff, **jeder sichtbaren nummerierten Aufgabe**, deren Aufgabenfamilie, Bearbeitungsform und den geplanten Blättern erstellen. Nicht nur das Thema („Umfang“) erfassen, sondern das konkrete Wie („Figuren vergleichen und Fläche/Umfang in eine Tabelle eintragen“, „zu vorgegebenem Umfang eigene Rasterfiguren zeichnen“, „gleich lange Seiten durch Multiplikation zusammenfassen“, „fehlende Rechteckseiten ergänzen und danach messen“). Sichtbare wesentliche Aufgabenformen einplanen. Bei begrenztem Umfang nach der geklärten Nutzerpräferenz entweder jede Familie mindestens einmal repräsentieren oder bewusst auswählen; nichts still weglassen.
- Vor PDF-Erstellung die Matrix auf **Lücken** prüfen. Bei mehreren Buchseiten darf eine gut sichtbare nummerierte Aufgabenfamilie nicht versehentlich fehlen.
- Nicht sichtbare bzw. unleserliche Seiten ausdrücklich als fehlend kennzeichnen. Deren Originalaufbau und Verfahren nicht behaupten; passende Ergänzungen aus Lernstoff/Nutzerbeschreibung als eigene Aufgaben führen. Bei benötigter exakter Originaltreue fehlende Vorlage nachfordern; unabhängige Arbeiten weiterführen.
- Lehrerstoff ist die verbindliche Inhaltsgrenze: jeden genannten Lernbereich, verlangte Proben, Fachsprache und Sachaufgaben in der Abdeckungsmatrix verfolgen; ausgenommene Seiten respektieren. Buchvorlagen bestimmen die Darstellung, nicht zusätzliche ungenannte Prüfungsinhalte.
- Bei mehrtägigem Training ohne anderslautenden Wunsch zunächst Schwerpunktblöcke, am letzten Trainingstag gemischte Anwendung planen. In einer siebentägigen Serie sechs Tage thematisch bündeln; verschiedene schulbekannte Darstellungen und Verfahren innerhalb des Tagesthemas variieren. Bei zwei Blättern pro Tag A/B als zusammengehöriges Tagespaar kennzeichnen, von Grundlagen zur schriftlichen Rechnung/Anwendung steigern. Nicht sechs Tage dieselben Zahlen oder dieselbe Darstellung wiederholen. Nutzerwünsche zur Reihenfolge haben Vorrang.
- Themenfolge aus dem tatsächlichen Stoff ableiten, nicht dauerhaft sechs feste Themen speichern. Diese Planungsregel ist auch für Volksschule sowie 1.–4. Klasse Mittelschule oder Gymnasium anwendbar; Zahlenraum, Verfahren, Sprache und Zeit jeweils an die belegte Schulstufe anpassen. Keine höhere Schulstufe allein aus der Planungsregel ableiten.
- Trainingstage und Kalenderdaten unterscheiden. Wenn die gewünschte Zahl der Trainingstage nicht vor den Prüfungstermin passt, den Plan ohne erfundene Kalenderdaten liefern und die zeitliche Grenze kurz benennen; keine bereits geklärte Seitenzahl oder Bearbeitungszeit neu abfragen.
- Blattstruktur nach der geklärten Präferenz planen: **Themenschwerpunkt pro Blatt** oder **gemischte Blätter**. Diese Entscheidung nicht selbst still treffen. Auch bei Schwerpunktblättern unterschiedliche vertraute Aufgabenfamilien verwenden.
- Einen lebendigen, didaktisch geplanten Mix schaffen: pro Blatt andere Kombination, Reihenfolge und räumliche Struktur. Gemeinsame Kopfzeile ist sinnvoll; ein identischer Aufgabenblock auf allen Seiten nicht. Wiederholte Teilaufgaben müssen einen Lernzweck haben und sich in Figur, Darstellung, Denkhandlung oder Anwendung sinnvoll unterscheiden; nicht bloß dieselbe Tätigkeit mehrfach mit neuen Zahlen wiederholen.
- Funktionale Schulaufbauten erhalten: Blütenblätter bleiben Blütenblätter, Tabellen bleiben Tabellen, fortlaufende Schlangen übernehmen das vorherige Ergebnis. Farbe durch eindeutige Linien, Nummerierung oder Muster ersetzen. Verfahren, Überträge und Notation aus der Schule übernehmen; keine fremde Standardmethode unterschieben.
- Sachaufgaben als eigenständigen Übungsbereich einplanen: verschiedene Kontexte, gesuchte Größen und Operationen, Rechnung UND vollständiger Antwortsatz. Geometrie nicht auf eine stets gleiche Rechteckzeichnung reduzieren: rechte Winkel, Parallelität, Rechteck/Quadrat, Raster/Kästchen, Konstruktion, Umfangformeln und Umfang-Sachaufgaben abdecken, soweit Stoffvorgabe/Vorlagen dies verlangen. Fläche nicht automatisch ergänzen.
- Bearbeitungszeit aus tatsächlichen Teilaufgaben, Rechenschritten, Zeichnen und Handschrift abschätzen. Material nicht künstlich verdichten. Umfang, Schwierigkeit und Lösungswunsch aus der Sitzung übernehmen.

## 3. Aufgaben und Lösungen gemeinsam entwickeln

Vor Erstellung [fachpruefung.md](references/fachpruefung.md) lesen. Pro Aufgabe stabile ID, vollständige Aufgabenstellung, Parameter, Antwortformat, Lösung und Prüfstatus in gemeinsamer strukturierter Datenbasis anlegen. Beide PDFs daraus erzeugen; Zahlen nicht separat eintippen.

- Kurze aktive Arbeitsanweisungen und bekannte Wörter verwenden. Beispiele nur zur Verständnishilfe einsetzen.
- Zahlen gezielt aus erlaubtem Lösungsraum wählen. Bei Gleichungen und Ziffernlücken zunächst konsistente Struktur entwickeln, anschließend die tatsächlich sichtbare Aufgabe unabhängig lösen.
- Jede mathematische Aufgabe mit ausführbarem Code berechnen, etwa Python mit Decimal/Fraction oder SymPy. Zusätzlich Gegenprobe durch Einsetzen, Umkehroperation, Kandidatensuche oder geometrische Plausibilität. Eine zweite sprachliche Rechnung ersetzt dies nicht.
- Ohne Rechenumgebung keine ungeprüften Mathematik-PDFs als fertig ausgeben; fehlende Prüfung benennen.
- Sprachaufgaben vollständig lösen und auf Eindeutigkeit prüfen. Offene Aufgaben als Beispiel-/Musterlösung mit zulässigen Alternativen kennzeichnen.
- Nach jeder Änderung neu prüfen. Falsche oder außerhalb des Lernstands liegende Aufgaben ersetzen.

### Didaktik, Varianten und Aufgabenbausteine

Für freie Gestaltung, gewünschte Niveauvarianten oder zusätzliche Aufgabenformen [didaktik-und-bausteine.md](references/didaktik-und-bausteine.md) lesen. Bei klarer Schulvorlage deren Aufgabenform und Reihenfolge priorisieren; Zusatzideen nicht ungefragt einbauen.

- Schwierigkeit über konkrete Merkmale steuern: Zahlenraum, Übertrag/Entbündeln, Anzahl der Rechenschritte, unbekannte Position, Sprachkomplexität und verfügbare Hilfen. Größere Zahlen allein sind kein vollständiges Schwierigkeitsmodell.
- Auf Wunsch Varianten A/B mit gleicher Kompetenz, gleichem Umfang und vergleichbarer Schwierigkeit erzeugen. Jede Variante separat vollständig prüfen und mit eigenem passenden Lösungs-PDF sowie gleicher eindeutiger Variantenkennung versehen.
- Aufgabenparameter und die tatsächlich verwendeten Aufgaben zusammen sichern, wenn die Arbeitsdateien gespeichert werden. Bei „nochmals dieselben Lösungen“ keine Zufallsaufgaben neu erzeugen; ursprüngliche Datei/Datenbasis verwenden oder nachfordern.
- Hilfen nur abgestimmt einsetzen, z. B. Wortbank, Stellenwerttafel, ein gelöstes Beispiel oder Satzanfang. Hilfen beim selbstständigen Üben gegebenenfalls schrittweise reduzieren; Lösungen nicht versehentlich verraten.
- Bei freier Gestaltung vom Einstieg zur Anwendung aufbauen; optionale Knobel-/Entdeckeraufgaben klar kennzeichnen. Sie dürfen keine unbekannten schulischen Verfahren voraussetzen.
- Bei Übungsrückmeldungen beobachtbare Fehlermuster für gezielte nächste Aufgaben nutzen, ohne aus wenigen Antworten Lernstörungen zu diagnostizieren.

## 4. Zwei druckbare PDFs

Bei neuen Übungen immer `Arbeitsblatt.pdf` und `Loesungen.pdf` erstellen. Verfügbaren PDF-Skill und dessen Render-/Sichtprüfungsworkflow verwenden.

- Kinderblatt mit leeren Antwortflächen erstellen; ausdrücklich markierte didaktische Beispiele dürfen ausgefüllt sein.
- Lösungsblatt als dieselbe ausgefüllte Fassung mit identischen Aufgaben, Nummerierungen und Anordnung erzeugen. Gewünschte Erklärungen gegebenenfalls auf Zusatzseiten ergänzen.
- Fach/Thema, Name/Datum und bei gesicherter Angabe Schulstufe vorsehen; Seiten nummerieren.
- Etwa 12–15 mm drucksicheren Rand und altersgerechte Schrift vorsehen, in der Volksschule meist 12–14 pt. Handschriftflächen großzügig halten; Platz für verlangte Rechenwege geben.
- Schreibraum anhand der längsten erwarteten handschriftlichen Antwort vorab bemessen: für Ziffern in der Volksschule etwa 5–6 mm je Stelle, für Wörter/Sätze etwa 4–5 mm je Zeichen und meist 8–10 mm Zeilenabstand. Zahlenlücken nicht als drei kurze Unterstriche setzen. Rechnung und Antwortsatz jeweils mit eigener ausreichend langer Fläche versehen. Bei Platzmangel Aufgabenmenge reduzieren, nicht Schrift/Schreibraum verkleinern.
- Stellenwertkästchen exakt ausrichten. Zeichnungen/Konstruktionen ausreichend Platz geben. Aufgabe und Antwortfläche zusammenhalten.
- Exakte Geometrie, Raster und Zahlenstrahlen programmgesteuert als Vektorgrafik erstellen. Bildgenerator nicht für mathematisch genaue Inhalte verwenden. Bei echten Konstruktionslängen Maßstab prüfen und Druck bei 100 % angeben.
- Vor Fertigstellung Abdeckungsmatrix kontrollieren und Aufgabenformen sowie tatsächliche Rechenverfahren gegen die Originalseiten rückvergleichen. Jede unterschiedliche Aufgabenfamilie mit der längsten Musterantwort als Handschrift-Platzprobe prüfen.
- Beide PDFs rendern und jede Seite in lesbarer Größe visuell prüfen; Kontaktbögen allein reichen dafür nicht: Überlagerung, abgeschnittene Zeichen, Lesbarkeit, Schreibraum, Ausrichtung, Schwarz-Weiß-Tauglichkeit. Gedruckte Aufgaben/Lösungen gegen gemeinsame Datenbasis abgleichen.
- Erst nach bestandener Fach- und Layoutprüfung beide Dateien bereitstellen, nicht nur Chattext.

## 5. Handschrift entfernen

Bei „bitte entferne die handschriftlichen Zeilen/Einträge“ nur handschriftliche Antworten, Kreuze, Notizen und Korrekturen aus einer Kopie entfernen. Gedruckte Aufgaben, Zahlen, Linien, Kästchen, Bilder, Nummerierung und Seitenaufbau erhalten. Keine neuen Aufgaben erzeugen und Druckfehler nicht still ändern.

- Originaldatei unverändert lassen. Bild vor Bearbeitung visuell prüfen. Für Bildbearbeitung verfügbares ImageGen-/Bildbearbeitungswerkzeug verwenden und Erhaltung des Drucks ausdrücklich anweisen.
- Ergebnis vollständig mit Original vergleichen, besonders Kontaktstellen zwischen Handschrift und gedruckten Zeichen/Linien. Plausibles Aussehen allein genügt nicht.
- Bei überdecktem, nicht rekonstruierbarem Druck nach besserem Foto oder leerer Vorlage fragen; keine Zeichen erfinden.
- Perspektivkorrektur, Zuschnitt und Kontrast nur zur Druckaufbereitung ohne Inhaltsverlust anwenden. Schwarz-Weiß-Konvertierung auf Informationsverlust prüfen.
- Wenn originalgetreue Entfernung nicht gelingt, das benennen. Neu gesetzte Rekonstruktion nur nach Abstimmung anbieten und als solche kennzeichnen, nicht als unverändertes Original ausgeben.
- Bereinigte Kopie als A4-Schwarz-Weiß-PDF liefern. Im reinen Bereinigungsmodus nur diese PDF erzeugen; zusätzliche Lösungen nur auf Wunsch. Dann gedruckte Originalaufgaben vollständig unabhängig lösen und prüfen.

## Abschluss

Dateien und wesentliche Besonderheiten kurz nennen. Prüfprotokolle nicht auf Kinderblatt drucken. Keine persönlichen Schülerdaten dauerhaft im Skill speichern. Hochgeladene Vorlagen nicht automatisch als Skill-Assets übernehmen.

## 6. Fachmodule und verbesserte Aufgabenproduktion (Erweiterung 2026)

**Alle bisherigen Regeln, Referenzen, Skripte und der Handschrift-Entfernungsmodus bleiben verbindlich.**

- Bei Zahlvorstellungen, Nachbarzahlen, Zahlenfolgen, Ordnungen und Stellenwertaufgaben zusätzlich [zahlenraum-und-stellenwertaufgaben.md](references/zahlenraum-und-stellenwertaufgaben.md) lesen; auch die zugehörigen automatischen Prüftypen einsetzen. Lehrerkorrekturen sind Hinweise, keine Soll-Lösungen.
- Für Mathematik immer [mathematik.md](references/mathematik.md) zusätzlich lesen. Bei Rechenaufgaben auch `scripts/math_quality_gate.py` mit strukturierter Aufgabenliste einsetzen; das bestehende `scripts/worksheet_logic.py` bleibt erhalten.
- Bei **schriftlicher Division** zusätzlich zwingend `scripts/schriftliche_division.py` für Restmitnahme, vertikale Darstellung und die Rechenweg-Zeilen verwenden; mit `scripts/test_schriftliche_division.py` und dem prüfbaren Schrittprotokoll gegenprüfen. Die Lösung muss jedes Zwischenprodukt, jede Subtraktion, die heruntergeholte Ziffer, alle Quotientennullen und den Endrest enthalten.
- Für Deutsch immer [deutsch.md](references/deutsch.md) zusätzlich lesen.
- Für Englisch immer [englisch.md](references/englisch.md) zusätzlich lesen.
- Für Druckaufbereitung zusätzlich [layout-system.md](references/layout-system.md) lesen. Layout als papierbasierte Benutzeroberfläche verstehen: Orientierung, Arbeitsanweisung, Schreibfläche und Rückmeldung sind funktionale Elemente, keine Dekoration.
- Für alle Fächer [qualitaetsgate.md](references/qualitaetsgate.md) als Freigabecheckliste verwenden. Keine PDF vor bestandenen, tatsächlich durchgeführten Checks freigeben.
- Die Fachmodule nicht pauschal alle laden; nur das angefragte Fach. Bei gemischten Blättern jeweils betroffene Module laden.
- Bei Fotografien zuerst Aufgabentyp, Bearbeitungslogik, Zahlenraum und tatsächlich verlangte Denkleistung erkennen. Schwierigkeiten gezielt über Operatoren, Übergänge, Unbekannte, Schritte und Darstellung angleichen, nicht bloß über Zifferngröße.
- Bei mehreren Buchseiten zunächst Vollständigkeitsmatrix, dann Blattplanung, dann Aufgaben und Lösungen aus gemeinsamer Datenbasis, anschließend fachliche und visuelle Prüfungen. Fehlende oder nicht lesbare Aufgaben explizit markieren.
- Optionale gestufte Hilfen auf eigenem Erklärblatt nur dann, wenn angefragt oder pädagogisch erforderlich; nicht in Prüfungsaufgaben hinein verraten.
- Gestaltung: klare schwarzweiße Druckoberfläche mit einheitlichem Kopf, eindeutiger Nummerierung, wiedererkennbaren Aufgabenkomponenten und genügend Schreib-/Zeichenraum. Kein visueller Schnickschnack und keine ungeprüften geometrischen Bilder.
