# Druckgestaltung und grafische Aufgabenanzeige

## Inhalt
1. UI/UX-Prinzipien für Papier
2. Größenprofile
3. Komponenten und Platzlogik
4. Abwechslung und Freigabe

## 1. UI/UX-Prinzipien für Papier

Bei dieser Überarbeitung UI/UX Pro Max tatsächlich für Struktur, Beschriftung, Kontrast und Lesbarkeit durchsucht. Relevante UX-Treffer: sichtbare Labels, ausreichender Zeilenabstand, dunkler Text auf hellem Hintergrund. Designsynthese liefert zwar klare Raster/Hierarchie, aber auch Landingpage-/CTA-Empfehlungen; diese verwerfen. Kindertypografie-Treffer sind Vorschläge für Apps, keine Nachweise für Leseförderung oder verpflichtende Schulschriften. Druckmaße unten sind eigene anpassbare Entwurfswerte.

Auf A4 übertragen: eindeutig nummerierte Blöcke; Arbeitsanweisung direkt an der Aufgabe; Antwortfelder mit inhaltlicher Funktion; zusammengehörige Angaben räumlich zusammenhalten. Sichtbarer Operator wichtiger als Schmuck. Weißraum ist Arbeitsfläche/Orientierung und kein Mangel. Schwarz-Weiß, keine farbcodierte Schwierigkeit, Schatten, vollflächigen Graukarten oder App-Buttons. Keine Pixel-/Touch-Maße, CTA, Animation, Responsive-Breakpoints in Druck-PDF übernehmen. Mathematikdiagramme ausschließlich exakt als Vektor.

## 2. Größenprofile

| Klassen | Text / Aufgabenüberschrift | Ziffernraster | Schreibzeilen | Typische Gestaltung |
| --- | --- | --- | --- | --- |
| VS 1 | 14–16 pt / 15–17 pt | 7–8 mm | 10–12 mm | Kurze Aufträge, große Mengenbilder, wenig gleichzeitig sichtbare Teilaufgaben. |
| VS 2 | 13–15 pt / 14–16 pt | 6–7 mm | 9–11 mm | Klarer Stellenwertbezug; Bild und Rechnung nahe beieinander. |
| VS 3–4 | 12–14 pt / 13–15 pt | 6 mm | 9–10 mm | Bekannte grafische Familien und großzügige schriftliche Rechnungen/Proben. |
| MS/AHS 1–2 | 12–13 pt / 13–15 pt | 5–6 mm | 8–10 mm | Sachliche, verständliche Tabellen/Diagramme; Platz für Terme und Umformung. |
| MS/AHS 3–4 | 11.5–13 pt / 13–15 pt | 5–6 mm | 8–9 mm | Klar gegliederte Mehrschrittaufgaben, Graphen/Konstruktionen und Begründungen. |

Orientierungswerte, keine Pflichtnormen. Mit Schulvorlage, tatsächlicher Schrift/Handschrift und Förderbedarf abgleichen. Bei unbekannter Handschrift großzügig wählen. Unterrichtsschrift bei Schreiblernaufgaben nach Vorlage; nicht beliebige „Comic“-Schrift als Schulschrift verkaufen. In normalen Aufgaben gut unterscheidbare 0/O, 1/l/I, 6/9, Minus/Strich, Komma/Punkt und mathematische Zeichen prüfen. Einbettbare verfügbare Schrift verwenden; maximal zwei Schnitte derselben gut lesbaren Familie. Aufgabenüberschriften fett, Aufgabentext ruhig, Lösungen in gleichem Raster.

A4 hochkant, 15 mm Ränder als Startwert (nutzbare Breite 180 mm). Kopf ungefähr 25–30 mm, darunter 6–8 mm Abstand; Fuß frei und drucksicher. Zwischen unabhängigen Blöcken nach der tatsächlich längsten Antwort mindestens 5–8 mm. Zweispaltig nur für unabhängige kurze Aufgaben; Satzantworten, lange Terme, Modelle und Konstruktionen über volle Breite.

## 3. Komponenten und Platzlogik

Jeden Block aus Inhalt berechnen, nicht aus freiem Rest der Seite:

`H = Titel + umgebrochener Auftrag + Angaben/Grafik + Rechenraum + Probe + Antwort + Innenabstände`.

Auch bei einem reinen Chattext-Layoutplan die innere Höhenrechnung ausweisen: Titelhöhe, tatsächliche Textzeilen, parallele Rechen-/Probefelder, Antwortzeilen und Abstände. Ein Plan mit sieben 9-mm-Schreibzeilen plus Text/Titel benötigt deutlich mehr als 63 mm; scheinbar passende Außenkoordinaten allein genügen nicht. Rechnung und Probe nur bei ausreichender Breite nebeneinander legen und dann die größere Höhe zählen. Fehlen Fontmetriken im Plan, vorsichtige Textzeilenabschätzung als Annahme führen und vor PDF-Erstellung messen.

Text zunächst mit tatsächlicher Fontmetrik umbrechen, Grundlinie/Aszender/Unterkante messen. Danach Grafik und Antwortflächen platzieren. Kinder- und Lösungsfassung brauchen denselben Block; längere Musterantwort kann dessen Höhe bestimmen. Platzmangel durch weniger Teilaufgaben/anderen Umbruch lösen, nie durch kleinere Handschriftflächen. Letzte Baseline nicht mit Unterkante verwechseln. Nach Neuanordnung alle folgenden Positionen neu berechnen.

- Zahlenlücke: Stellenzahl × Rasterweite plus Innenrand. Geld: Vorzeichen, Euroziffern, Kommaspalte, zwei Centziffern und Einheit getrennt vorsehen. Keine Ergebnislinie mitten im Fragetext; Start-x aus Textbreite plus Abstand oder eigene Zeile.
- Schriftliche Operation: eine Ziffer pro Kästchen; Stellenwertausrichtung, Übertrags-/Entbündelungszeile, Ergebnis und Probe vollständig im Block. Division nicht als waagrechte Zahl ohne Rechenraum darstellen. Kein Übertrag über Kommaspalte. Lösungsfassung mit verlangten Rechenschritten, nicht nur Ergebnis.
- Sachaufgabe: kleine Bezeichnungen „Rechnung“/„Antwort“ nur wo hilfreich; pro erwarteter Rechenzeile eigenen Raum, darunter mindestens passende Satzzeilen. Bei längeren Sätzen über volle Breite umbrechen. Druckschriftbreite ist kein Handschriftmaß.
- Blumen: Operator im Zentrum, jede Blütenzahl eindeutig; Kennbuchstaben außerhalb des Umrisses, keine Linie durch Buchstaben. Ergebnisse in ausreichend großen nummerierten Feldern; Liste und Blüte gemeinsam im Block.
- Tabellen: lesbare Köpfe, richtige Operatorrichtung, Breite jeder Antwortzelle an längster handschriftlicher Antwort bemessen. Für inverse Köpfe genug eindeutige Ankerwerte. Kein unnötiges Schmücken von Rasterlinien.
- Ketten/Mauern: vorwärts eindeutige Leserichtung und Regel; Pfeile/Operatoren außerhalb Antwortzellen; keine reine optische Schlange mit unklarer nächster Zahl.
- Zeichnen: tatsächliche Objektgröße plus 10–15 mm Beschriftungsrand je nach Aufgabe; separate Formel-/Rechenzeilen. Bei Geodreieckskonstruktion Werkzeugbewegung und fehlende Buchvorlagen berücksichtigen.
- Kacheln: physische Größe versus Modellgröße unterscheiden („entspricht“ bei verkleinerter Darstellung); Außenumfang, nicht innere Gitterlinien zählen. Umfang und Fläche sprachlich/mit Einheiten sauber trennen.
- Sekundarstufe: Terme mit Bruchstrichen/Klammern, Lösungszeilen mit Äquivalenzzeichen, Graphen mit Skalen/Achsen/Einheiten; keine kindlichen Blumen automatisch weiterverwenden, wenn Vorlage anders arbeitet.

Handschriftabschätzung zunächst über Stellen-/Zeichenzahl und gewählte Klasse; für VS Wörter ca. 4–5 mm/Zeichen, für höhere Klassen zunächst 3–4 mm/Zeichen. Dies ist eine vorsichtige Entwurfsannahme, keine individuelle Messung. Eine Antwort von 50 Zeichen auf zwei volle Zeilen verteilen, statt einen überlangen Ausdruck auf ein winziges Feld zu quetschen. Optionaler Probe-/Begründungsauftrag braucht eigenen Raum; bei Zeitknappheit Auftrag UND Raum gemeinsam streichen, sofern Lehrerstoff es erlaubt.

## 4. Abwechslung und Freigabe

Aus den funktionalen Familien eine Seitensignatur (Familie, Reihenfolge, ein-/zweispaltig, Zeichnungs-/Textanteil) führen. Innerhalb zusammengehöriger Serie wiedererkennbarer Kopf; Kombination und räumliche Struktur bewusst variieren. Gleiche Kompetenz mit anderen Zugängen vertiefen, nicht denselben Viererblock auf jede Seite kopieren. Vorlage hat Vorrang vor frei gewähltem Design.

Vor Freigabe drei Fragen pro Seite: Wo beginne ich? Welche Angaben gehören zusammen? Wo schreibe/zeichne ich die vollständige Antwort? Danach Fach- und Platzprüfung jeder Familie, tatsächliche Blockkoordinaten prüfen, beide PDFs rendern und jede Seite lesbar ansehen. Kontaktbogen nur zur Übersicht. Mathematische Maße bei 100 % prüfen. Rahmen/Operatoren im Schwarz-Weiß-Druck gut sichtbar, aber nicht dominanter als Inhalt. Keine unbeabsichtigten ausgefüllten Antworten in Kinderfassung. Prüfprotokolle und Schwierigkeitsscores intern halten.
