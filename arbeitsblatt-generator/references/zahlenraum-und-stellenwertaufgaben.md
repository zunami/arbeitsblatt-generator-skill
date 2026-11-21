# Mathematik: Zahlenraum, Nachbarzahlen, Folgen und Stellenwerte

Dieses Modul bei Vorlagen zu Zahlenfolgen, Nachbarzehnern/-hundertern/-tausendern,
Zahlenordnungen, Stellenwerten, Ziffernkarten und einfachen schriftlichen
Rechenaufträgen verwenden. Es beschreibt **generative Regeln**, keine
abzuschreibenden Aufgaben aus Fotos. Schulvorlage und nachgewiesener Lernstand
entscheiden über Zahlenraum, Notation, Anzahl der Felder und Schwierigkeitsgrad.

## 1. Fotografierte Schularbeit als Datenquelle

- Gedruckte Aufgabenstellung, Startzahlen und Antwortfelder einzeln erfassen;
  handschriftliche Antworten sowie Lehrerhaken und -kreuze davon trennen.
- Handschriftliche Fehler sind Hinweise auf mögliche Übungsschwerpunkte, aber
  weder gesicherte Diagnosen noch automatische Soll-Lösungen. Die gedruckte
  Aufgabe immer unabhängig loesen und mit dem mathematischen Soll vergleichen.
- Bei einer angefragten Neubearbeitung keine Namen, Daten, Notizen, Korrekturzeichen,
  Figuren oder ausgefuellten Lösungen der Vorlage reproduzieren. Der funktionale
  Aufbau (Zahlenkette, Zeile, Zweispaltigkeit, Tabelle, Kästchenraster) darf
  nachgeahmt werden; neue Zahlen und Texte generieren.

## 2. Zahlenfolgen und Rechenmuster

- Jede Zahlenfolge als explizite Folge von Operationen modellieren: etwa
  konstanter Schritt `+d` oder alternierende Schritte `[d1,d2]`;
  Vorzeichen und Reihenfolge sind Bestandteil der Aufgabe.
- Bei alternierenden Schritten den Zyklus über **alle** sichtbaren Werte
  prüfen, nicht nur das letzte Differenzpaar. Die folgenden Leerstellen
  entsprechend Zyklusposition ausfuellen. Auch gemischte Plus-/Minusschritte
  und Hunderter-/Zehnerschritte koennen zusammen vorkommen.
- Der Generator waehlt Basis, Schritte, vorgegebene Glieder und Anzahl der
  Leerstellen so, dass **alle Zwischenwerte und Lösungen** im Zielzahlenraum
  liegen. Keine negativen Zahlen, sofern nicht unterrichtet.
- Beliebige endliche Anfangsglieder bestimmen eine Fortsetzungsregel
  mathematisch nicht eindeutig. Bei neuen alternierenden Folgen nach
  Moeglichkeit vier vorgegebene Glieder oder eine kurze Anweisung wie
  `Die zwei Schritte wechseln sich ab` verwenden. Wenn eine Vorlage exakt
  drei Anfangsglieder vorsieht, nur schulisch naheliegende Muster nutzen;
  keine ausschließlich eindeutige Fortsetzung behaupten.
- Anschlussmuster `immer +1`, `immer +10`, `immer +100`, `immer -10` und
  `immer -100` als eigene einfache Aufgabenfamilien fuehren. Zum Schluss
  Kontrollrechnung für jede vorgegebene und ausgefuellte Stelle.

## 3. Nachbarzehner, Nachbarhunderter, Nachbartausender

- `Basis b` ist 10, 100 oder 1000. Fuer eine natürliche Zahl `n > 0`
  sind die **unmittelbar darunter und darüber liegenden** Vielfachen
  dieser Basis gesucht: `unten = ((n-1)//b)*b` und
  `oben = (n//b+1)*b`. Beide Zahlen sind strikt kleiner bzw. groesser
  als `n`.
- Beispielhafte abstrakte Grenzpruefung: bei `n % b == 0` liegt `n`
  selbst NICHT in einem der Nachbarfelder. Bei `n = 10000, b = 100`
  ist die obere Nachbarzahl `10100`, nicht `11000`.
- Nachbarzahlen sind keine pauschalen Operationen `n-b` und `n+b`
  für Zahlen zwischen zwei Vielfachen. Die Anzahl der Stellen im
  Ergebnis kann sich an Grenzzahlen ändern; wenn die Vorlage nur Zahlen
  bis 10000 erlaubt, bei der Generierung entsprechende Werte auswählen.
- Darstellung gemaess Muster: `linker Nachbar | gegebene Zahl | rechter
  Nachbar`. Bei jeder Zeile unterschiedliche Schwierigkeitsmerkmale
  kontrollieren: nahe am Zehner/Hunderter, Nullen im Inneren,
  Wechsel eines Tausenders, exaktes Vielfaches.

## 4. Sortieren und fortlaufende Zahlenketten

- Eine Sortieraufgabe enthaelt eine **fest vorgegebene Menge von Zahlen**.
  Lösung bei `kleinste zuerst` aufsteigend, bei `größte zuerst`
  absteigend. Jede Ausgangszahl muss genau gleich oft wieder vorkommen;
  Gleichheits- oder Vergleichszeichen in der richtigen Richtung setzen.
- Zur gezielten Schwierigkeit Zahlen mit gleichen Tausendern oder
  Hundertern, nahen Einerstellen und Nullen mischen; bei nicht gewuenschter
  Mehrdeutigkeit nur unterschiedliche Zahlen verwenden.
- Fortlaufende Ketten um eine bereits eingetragene Ankerzahl mit festen
  Schritten ergaenzen. Anzahl links/rechts und notwendige Start-/Endwerte
  vorab berechnen. Die Ankerzahl nicht unabsichtlich mitdrucken oder
  erneut als Antwort ausgeben.

## 5. Stellenwerte und Ziffern zu Zahlen

- Fuer vierstellige Zahlen gelten `T=1000`, `H=100`, `Z=10`, `E=1`.
  Gemischt angeordnete Angaben wie `...H ...E ...T ...Z` erst den
  Stellen zuordnen, dann `1000*T+100*H+10*Z+E` berechnen.
  Die Reihenfolge der Angaben ändert den Wert nicht.
- Fuer `Bilde aus den Ziffern die größte vierstellige Zahl` die vier
  erlaubten Ziffern **genau einmal** absteigend sortieren. Die andere
  Zahl ist nur dann die Ziffernfolge in der gegebenen Reihenfolge,
  wenn die Vorlage diese Rechenpartner-Rolle erkennbar festlegt. Bei
  neuer Aufgabenstellung explizit sagen, welche beiden Zahlen addiert
  oder subtrahiert werden.
- Keine fuehrende Null bei vierstelligen Zahlen. Bei Subtraktion
  `größte minus Ausgangszahl` muss der Unterschied nichtnegativ sein.
  Auch Überträge und Stellenwertwechsel im schriftlichen Verfahren
  und die erlaubte Ergebnisgroesse vorab festlegen.
- Aufgaben auf Zifferneindeutigkeit, vierstellige Ausgangszahl,
  Vervollstaendigung der vier Stellen und korrekte Ergebniswerte prüfen.

## 6. Schriftliche Verfahren und Antwortflaechen

- `Addiere immer 1/100` und `Subtrahiere immer 10/100` als Tabellenform
  mit gedruckter Ausgangszahl links und leerem Ergebnisfeld rechts
  erzeugen. Bei verschiedenen Anfangszahlen auch Zehner-/Hunderter-
  oder Tausenderübergaenge einplanen, aber nur im belegten Zahlenraum.
- Bei schriftlicher Addition, Subtraktion und Multiplikation stellenrichtig
  eintragen, Rechenstriche und ggf. Überträge darstellen. Bei Division
  vollständige Teilrechnungen samt Herunterholen, Quotient und Rest.
- Bei Division muss gelten `Dividend = Divisor*Quotient + Rest` und
  `0 <= Rest < Divisor`. Auch Teilquotienten mit 0 abbilden.
- Grosse kästchenbasierte Freiflächen für alle Zwischenrechnungen
  vorsehen; bei Tabellen und Reihen mindestens für die laengste Zahl
  ausreichend Platz. Im Lösungs-PDF exakt dieselbe Darstellung nutzen.

## 7. Automatische Prüfungen und Negativtests

Fuer unterstuetzte Typen `scripts/math_quality_gate.py` einsetzen:
`sequence_alternating`, `neighbors`, `order_numbers`, `consecutive_chain`,
`place_value`, `digit_rearrangement`, `step_value`, `division_written` sowie die bisherigen
Typen. `math_quality_gate.py` validiert das Ergebnis und relevante
Eingabebedingungen, nicht das fotografierte Original oder die Druckoptik.
Bei fehlendem Typ eine eigene unabhängige Berechnung implementieren,
nicht eine ungeprüfte Lösung als bestaetigt melden.

Regressionen gezielt als Negativfaelle prüfen: falscher Wechsel im
alternierenden Muster; `n +/- 100` statt echte Nachbarhunderter;
falsche Ziffernreihenfolge; eine Zahl doppelt beim Sortieren; falscher
Stellenwert bei gemischter Notation; fehlender Divisionsrest;
zu kleiner Schreibraum für die vollständige schriftliche Rechnung.

Bei `division_written` zusaetzlich jeden einzelnen Zwischenwert als
`partial`, `quotient_digit`, `subtracted` und `remainder` pruefen.
Nullen im Quotienten muessen als eigene Zwischenstufe erhalten bleiben;
die auf dem Papier erlaubte Notationsvariante weiterhin an die Vorlage anpassen.


## Pflichtform der schriftlichen Division im Loesungs-PDF

`division_written` allein sichert Zahlen, nicht ein benutzbares Rechenbild. Nach dem numerischen Check fuer jede schriftliche Division `scripts/schriftliche_division.py` einsetzen und das vertikale Rechenverfahren mit Restmitnahme aus [schriftliche-division-rechenwege.md](schriftliche-division-rechenwege.md) beachten. **Jede** Teilzahl, Produktzeile, Subtraktion und heruntergeholte Ziffer untereinander; Endrest unten und ggf. hinter dem Ergebnis.
