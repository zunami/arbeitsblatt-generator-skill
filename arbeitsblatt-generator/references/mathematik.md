# Fachmodul Mathematik – Österreich

Bei österreichischen Aufgaben zuerst [oesterreichische-matheverfahren.md](oesterreichische-matheverfahren.md) und [oesterreichische-schulsprache.md](oesterreichische-schulsprache.md) berücksichtigen.

Für Aufgaben im Zahlenraum (Folgen, Nachbarzahlen, Sortieren, Stellenwerte, Ziffernkarten) zusätzlich [zahlenraum-und-stellenwertaufgaben.md](zahlenraum-und-stellenwertaufgaben.md) verwenden.

## Aufgabenerkennung

Jede Vorlage zuerst als Aufgabenfamilie klassifizieren: Kopfrechnen, Rechenpäckchen, Umkehraufgabe, Zahlenmauer, Rechenschlange, Zahlenstrahl, Stellenwerttafel, schriftliche Grundrechenart, Lückenrechnung, Gleichung, Sachaufgabe, Tabelle, Diagramm, Bruch-/Dezimaldarstellung, Größen/Messen, Geometrie/Konstruktion, Muster/Entdecken. Auftragswortlaut, Beispiel, Ausfüllrichtung, Kästchenzahl, Linien und Teilaufgaben einzeln erfassen. Neue Aufgaben dürfen gleiche Denkleistung, aber nicht einfach identische Zahlen und Figuren übernehmen.

## Schwierigkeitsfingerabdruck

Für jede Familie notieren: Zahlenraum (inklusive Zwischenwerte), Operationen, Überträge/Entbündelungen, Anzahl Schritte, Nullfälle, Rest, unbekannte Position, Notation, Textlast, notwendige Umrechnung, erwartete Bearbeitungszeit, Hilfsmittel, Schreibraum und Vertrautheit des Lösungsverfahrens. Schwierigkeitsgleichheit anhand dieser Merkmale prüfen, nicht nur Ergebnisgrößen. Lehrerstoff und sichtbare Vorlage haben Vorrang vor generischen Lehrplanannahmen.

## Aufgabengenerator

1. Aufgabenfamilien-Matrix mit IDs erstellen; alle sichtbaren nummerierten Aufgaben inventarisieren.
2. Aufgabenparameter aus Lernstand und Fingerabdruck ableiten. Zuerst gültige Lösung wählen, daraus konsistente Lücken-/Umkehraufgaben bilden; danach unabhängig zurücklösen.
3. Jede Zahl, Rechenoperation, Einheit und erwartete Antwort aus gemeinsamer Datenbasis generieren; Lösungen nicht manuell in PDF übertragen.
4. Beim schriftlichen Rechnen Stellenwertspalten, Übertrag, Rest, Divisionsschreibweise und schulübliche Verfahren explizit abbilden. Nicht still zu anderen Verfahren wechseln.
5. Bei Sachaufgaben reale Größen plausibilisieren, relevante und irrelevante Angaben bewusst steuern, Einheit in Ergebnis und vollständigen Antwortsatz vorsehen.
6. Geometrie mit vektorbasierten, maßhaltigen Zeichnungen; Linienlängen/Skalierung kontrollieren. Bei Rasterfiguren Kästchenmaße und Platz zum Einzeichnen prüfen. Umfang und Fläche nicht vermengen.
7. Bei Zahlenfolgen und Mustern ausreichende Eingrenzung geben; andernfalls mehrere mögliche Regeln als zulässig kennzeichnen.
8. Jede Aufgabe algorithmisch kontrollieren. `scripts/math_quality_gate.py` für unterstützte Typen ausführen, andere Typen durch eigenes ausführbares Prüfprogramm und unabhängige Gegenprobe absichern. Bei Nichtunterstützung nicht als geprüft ausweisen.
9. Bei Serien Lernprogression planen: Einstieg, vertraute Verfahren, Anwendung, Transfer; innerhalb der Blattvorgabe Aufgabenformen abwechseln. Keine unbeauftragte Erhöhung der Schwierigkeit.

## Qualitätssicherung

- Keine führende Null in natürlichen Zahlendarstellungen; Divisor ungleich 0; Rest 0 <= r < Divisor; bei ohne Rest explizit r=0.
- Lücken mit eindeutigem Lösungssatz oder explizit zugelassenen Mehrfachlösungen; systematische Kandidatenprüfung.
- Geometrieangaben konsistent, Maßeinheiten korrekt, Zwischenwerte im erlaubten Bereich.
- Jede Ergebniszahl gegen Ausgangsaufgabe rückeinsetzen; Lösungsblatt identische Aufgabe und Reihenfolge.
- Bearbeitungszeit und Schreibraum auf die längste plausible Schülerlösung dimensionieren.

## Quellen und Inspiration

Didaktische Prinzipien aus PIKAS (Aufgabenvariationen und mathematische Beziehungen), IQS Österreich (Kompetenzorientierung und Musteraufgaben) und Worksheet Crafter (Aufgabenfamilien, Lösungen, visuelle Strukturen) als Anregung nutzen. Keine urheberrechtlich geschützten Seiten, Logos oder Aufgaben wortgetreu übernehmen. Quellen sind keine automatische Freigabe für österreichischen Unterrichtsstoff.
