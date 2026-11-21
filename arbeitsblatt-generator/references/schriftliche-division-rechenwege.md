# Schriftliche Division: vertikal lesbare Rechenwege (Pflicht)

## Anlass, Prioritaet, Geltung

Der reale Fehler im Loesungs-PDF `Loesungen_4x2.pdf` (4. und 8. Seite) war
nicht das Endergebnis, sondern die **falsche Darstellung**: Zwischenschritte
wurden als horizontale Teilgleichungen nebeneinander in dieselbe Zeile
gequetscht. Ein Kind kann dadurch weder die Stellenlage noch das Mitnehmen
des Rests verfolgen. Dieser Fehler ist ein hartes Freigabehindernis.

Bei jeder schriftlichen Division in Mathe-Arbeitsblaettern und insbesondere
im Loesungs-PDF gilt **ausnahmslos**, sofern die konkrete Schulvorlage
nicht ausdruecklich eine andere vollstaendige schriftliche Notation benutzt:

1. Erste teilbare Zifferngruppe bestimmen. Wenn eine Ziffer nicht reicht,
   die naechste dazunehmen.
2. Die Quotientenziffer hinter das Gleichheitszeichen schreiben.
3. Quotientenziffer mal Divisor rechnen. Das Produkt **stellenrichtig direkt
   unter die verwendete Teilzahl** schreiben, links ein Minus.
4. Sichtbare Linie und Differenz/Rest darunter notieren.
5. **Naechste Ziffer senkrecht herunterholen und rechts an den bisherigen
   Rest anhaengen**. Dadurch entsteht die naechste Teilzahl. Die neue
   Teilzahl in der naechsten Rasterzeile **unter** den vorigen Schritten
   notieren, nicht nebeneinander ueber das Blatt verteilen.
6. Die Schritte wiederholen. Falls eine Teilzahl kleiner als der Divisor ist,
   die **0 als Quotientenziffer** ausdruecklich erhalten und auch diesen
   Abschnitt nachvollziehbar darstellen.
7. Ist keine Ziffer mehr zum Herunterholen da, den letzten Rest unten
   stehen lassen. Bei Rest 0 ist die Division aufgegangen. Bei Rest > 0
   schreibe `Rest n`, nie unbemerkt in eine Kommazahl wechseln.
8. Schlussprobe: `Divisor * Quotient + Endrest = Dividend` und
   `0 <= Endrest < Divisor`.

### Schema der Stellenlage

Als lesbares *logisches Schema*, aus dem der PDF-Vektorrenderer einzelne
Rasterkaestchen erstellt (keine waagerechten Nebeneinander-Gleichungen):

```text
  6728 : 5 = 1345 Rest 3
 -5
  --
  17    <- Rest 1 und naechste Ziffer 7
 -15
  ---
   22   <- Rest 2 und naechste Ziffer 2
  -20
   --
    28  <- Rest 2 und naechste Ziffer 8
   -25
    --
     3  <- Endrest
```

Der Druckalgorithmus stellt dabei die Ziffern rechtsbuendig unter die
tatsaechlich verbrauchten Stellen der Ausgangszahl. Der Ausdruck `17`
steht also **nicht** beliebig links, sondern endet unter der Ziffer 7;
`22` endet unter der 2; `28` endet unter der 8. Das obige Textschema
stellt nur die Reihenfolge der Schritte dar, nicht die geometrische
Druckmassigkeit. Fuer die korrekte Platzierung immer den Renderer benutzen.

## Code und Datenschnittstelle

`scripts/schriftliche_division.py` bietet:

- `solution(dividend, divisor)` liefert (Quotient, Endrest, Step-Liste).
- Jeder Step enthaelt `end_col`, `partial`, `quotient_digit`,
  `product`, `remainder` und `next_digit`.
- `build_rows()` liefert die gedruckten Zeilen: Kopfzeile, untereinandergestellte
  Minuszeile, heruntergeholte neue Teilzahl, ..., letzte Restzeile.
- `required_height()` rechnet die **gesamte** Hoehe vor der Aufteilung.
- `draw_division(canvas, x, top, dividend, divisor, cell=20,
  total_cols=22, min_bottom=...)` zeichnet die vollstaendige Loesung
  mit echten ReportLab-Vektorkaestchen und wirft bei Platzmangel einen
  Fehler, statt Schritte zu unterdruecken.
- `scripts/math_quality_gate.py` prueft weiterhin die Werte des
  `division_written`-Datensatzes. Die geometrische/vertikale
  Vollstaendigkeit prueft zusaetzlich `scripts/schriftliche_division.py`.

**Nie** einen anderen Renderer verwenden, der die Ausgabe zu einer einzigen
Ergebniszeile oder verstreuten Zwischenrechnungen vereinfacht. Ein
`9864 : 6 = 1644 Rest 0` und daneben `9-6=3 | 38-36=2 | ...`
ist trotz rechnerisch richtiger Werte **keine gueltige Loesung**.

## Raster und Platzregel

- Je Ziffer ein Kaestchen: Standard ca. 6-7 mm Breite/Hoehe in VS 4.
- Eine Kopfzeile und fuer jeden tatsaechlichen Divisionsschritt
  **eine Produkt/Minus-Zeile plus eine Rest/Herunterhol-Zeile**:
  mindestens `1 + 2 * N` Zeilen fuer N Quotientenziffern.
- Zusaetzlich Randabstand, ggf. Beschriftungen und Schlussprobe.
  Mit vier Teilungen mindestens 9 Rasterzeilen; nicht nur 3-4.
- Fehlender Platz: mehr Schreibraum vorsehen oder Loesung als
  **weitere eindeutig zugeordnete A4-Seite** ausgeben. Weder Ziffern
  stapeln noch Schrift verkleinern, um einen Rechenweg zu verbergen.
- Loesung und Schuelerblatt verwenden denselben Aufgabentext und dieselben
  Zahlen. Im Schuelerblatt ist genug Platz zum Nachrechnen vorzusehen.
- Die Loesung exakt wie eine Schuelerrechnung senkrecht lesen koennen:
  Produkte unter Teilzahlen, naechste Ziffer herunter, Rest mitnehmen.

## Pflichtpruefungen und Regression

Bei jedem Generatordurchlauf:

1. Alle gedruckten Divisionen aus derselben Aufgabenbasis entnehmen.
2. Algorithmen fuer jeden Step sowie `Quotient * Divisor + Rest` pruefen.
3. `scripts/test_schriftliche_division.py` ausfuehren. Enthalten sind
   Restaufgaben, Aufgaben ohne Rest, erste zu kleine Ziffer,
   mittlere Quotientennullen, mehrere Zwischenreste und unzulaessig
   kleine Antwortflaechen; zudem 1000 seeded Zufallsfaelle.
4. Loesungs-PDF rendern. Jede Divisionsstelle **visuell** kontrollieren:
   Ziffern vertikal ausgerichtet? Alle Teilprodukte und Reste sichtbar?
   Keine abgeschnittenen Zeilen? Passender Endrest?
5. Eine Seite mit horizontal verstreuten Zwischenrechnungen oder
   fehlender Minus-/Rest-Zeile **nicht freigeben**.

## Beispielquellen (kein ungepruefter Transfer anderer Schulsysteme)

- Baden-Wuerttemberg Lehrerfortbildung: `https://www.lehrerfortbildung-bw.de/u_matnatech/mathematik/bs/bej/bej1/grund/anl_divi/`
- Sivakids: `https://www.sivakids.de/schriftlich-dividieren-division/`
- Studyflix: `https://studyflix.de/mathematik/schriftlich-dividieren-3138`

Diese Quellen unterstuetzen die vertikale Schreibweise, das Subtrahieren
und das senkrechte Herunterholen. **Abweichung zum Schulfoto:** Einige
Webbeispiele fuehren den Endrest zu Dezimalstellen weiter. Auf Leas
Schulblattern ist dagegen `Rest n` vorgesehen; die schriftliche Rechnung
endet hier beim ganzzahligen Ergebnis mit Rest. Eine Umwandlung in Dezimalzahl
nur auf ausdruecklichen Auftrag.
