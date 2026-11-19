# Erfahrungslernen, Erhalt bestehender Funktionen und Versionspflege

## Verbindliche Änderungsstrategie
- Bei jeder Aufforderung wie „verbessere den Skill“, „lerne daraus“ oder „baue diese Erfahrung ein“ zuerst die installierte Originalfassung bzw. vom Nutzer bereitgestellte vollständige ZIP als Ausgangsbasis verwenden. Niemals aus Gesprächszusammenfassungen eine kleinere Ersatzfassung erstellen und als Update bezeichnen.
- Vor Änderung ein Inventar aller vorhandenen Dateien, Fachfunktionen, Vorlagenmodi, Skripte und Referenzen anlegen. Nach Änderung auf Dateiebene und anhand einer Funktionsmatrix kontrollieren, dass nichts ohne ausdrücklichen Auftrag entfernt wurde.
- Neue Erkenntnisse nach Typ einordnen: (a) verbindliche Nutzerkonvention, (b) konkret beobachteter Fehler, (c) didaktische Verbesserung, (d) noch ungetestete Idee. Beobachtungen nicht als allgemein gültige österreichische Lehrplanregel ausgeben.
- Bei widersprechenden Regeln die jüngste ausdrückliche Nutzeranweisung für die konkrete Vorlage bevorzugen; Abweichung transparent machen.
- Lernregeln in passende Fachreferenz schreiben, nicht alles in SKILL.md duplizieren. SKILL.md nur um kurze Navigations-/Aktivierungsanweisung ergänzen.
- Vor Freigabe Regressionstests für Mathe, Deutsch, Englisch, Handschriftentfernung, A4-Schwarz-Weiß, getrennte Lösungen, Vorlagenabdeckung und Drucklayout planen. Nur tatsächlich ausgeführte Tests als bestanden melden.
- Installierten Skill nicht als aktualisiert bezeichnen, solange keine bestätigte Installation stattgefunden hat. Paketbereitstellung und Installation sind getrennte Schritte.

## Erfahrungen aus dieser Gesprächsserie
- Arbeitsblatt-Generator als EIN Skill mit drei eigenständigen Fachmodulen; Mathematik erhält besonders tiefe algorithmische Prüfungen.
- Für fünf fotografierte Buchseiten alle nummerierten Aufgabenfamilien inventarisieren, sinnvoll mischen und fünf neue Blätter plus vollständige Lösungsfassungen erzeugen, sofern vom Nutzer so beauftragt.
- Beispielbilder des Nutzers sind autoritative Muster für Schreibweise und Geometriezeichen: 704 : 4 mit allen Teilschritten; rechter Winkel mit Viertelkreisbogen und Punkt.
- Für Rasterkästchen niemals pauschal „Kacheln“ verwenden. Bundesdeutsche und österreichische Schulformulierungen differenziert redigieren.
- Wenn Nutzer mehr Logik oder bessere GUI verlangt, tatsächliche PDF-Bedienbarkeit verbessern: verständliche Überschriften, eindeutige Nummerierung, Schreibraum, Rasterpräzision, visuelle Abwechslung und getrennte Lösungen. Keine Web-UI vortäuschen.

## Wiederverwendbare Erkenntnisse aus GitHub-Veröffentlichungen

- Für öffentliche Releases einen **knappen sichtbaren Titel** wie `Version X.Y.Z` von der **ausführlichen Beschreibung** trennen. Unterschiedliche Oberflächen der Plattform separat kontrollieren: Release-Liste, Detailseite, Anzeige „Latest“, Tag und Download unter „Assets“.
- Den Status `prerelease` nur nach ausdrücklicher Entscheidung setzen, nicht automatisch aus `0.x` oder „Erprobungsphase“ ableiten. Ein fachlich experimenteller Inhalt kann als regulärer GitHub-Release erscheinen.
- Ein GitHub-Tag allein ist kein Release und eine Datei im Repository kein Release-Anhang. Abschluss erst nach erneuter Prüfung der veröffentlichten Asset-Namen, SHA-256-Werte und des vollständigen Wortlauts melden.
- Bei fehlender direkter Release-API eine **einmalige, geprüfte Veröffentlichung über GitHub Actions** nur mit ausdrücklicher Genehmigung des konkreten Inhalts vorsehen; keine neuen Token anfordern, Token-Rechte klein halten, bei Timeouts vor jedem Wiederholungsversuch den tatsächlichen Plattformstand lesen.
- Eine Korrektur einzelner Release-Metadaten (z. B. Titel oder Pre-release-Flag) darf keine ZIP-Dateien, Tag-Ziele oder bestehende Release-Texte ändern. Korrekturwirkung und Nebenwirkungsfreiheit getrennt verifizieren.
- Zukunftsworkflows versionunabhängig halten und nur nach manuell bestätigter Release-Freigabe auslösen. Bereits veröffentlichte Pakete nicht still überschreiben.

## Prüfbericht für Skill-Updates
Kurz ausweisen: Ausgangsbasis, erhaltene Dateien/Funktionen, neue Dateien, veränderte Dateien, tatsächlich ausgeführte Tests, verbleibende Risiken und Status der Installation.
