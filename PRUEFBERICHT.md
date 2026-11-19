# Prüfbericht - Version 0.1.1

## Historischer Ausgangsstand 0.1.0

Prüfdatum: 19.11.2026. Lokale isolierte Arbeitsumgebung, Python 3.13.5. Keine Ausführung auf einem Homelab oder im Konto eines anderen Nutzenden.

## Ausgangsbasis und Erhalt

Der vollständig vorhandene private Arbeitsblatt-Generator-Skill war die Ausgangsbasis: **21 Dateien**. Alle ursprünglichen Dateipfade und Fachfunktionen sind erhalten; **18 Dateien bytegleich**, **3 bewusst angepasst**, **5 hinzugefügt**. Die installierte Ausgangsfassung wurde nicht verändert.

Bewusst angepasst: `SKILL.md`, `agents/openai.yaml`, `assets/icon.svg`. Die Änderungen betreffen Versions-/Rechtehinweise, den Anzeigenamen und ein neu aufgebautes schlichtes Symbol ohne Übernahme eines undokumentierten Alt-Assets. Keines der vorhandenen Python-Rechenprogramme wurde funktional verändert.

Neue Paketdateien: `LICENSE`, `LIZENZ.md`, `RECHTLICHES.md`, `VERSION`, `references/rechte-datenschutz-plattformen.md`.

## Tatsächlich ausgeführt

| Prüfung | Ergebnis und Grenze |
| --- | --- |
| Vorhandenes `scripts/test_math_quality_gate.py` | Erfolgreich beendet. Prüft die enthaltenen konkreten positiven und negativen Rechenfälle. Keine vollständige Abdeckung aller denkbaren Eingaben. |
| Neue Tests in `tests/test_projekt.py` | 15 Tests bestanden: Schulprofil, Voraussetzungen, Zyklus, doppelte IDs, Themenkonflikt, Layoutflächen, Schreibraum und Paketbau. |
| Versionsabgleich | Repository-VERSION, Skill-VERSION und Versionszeile stimmen überein. |
| Python-Syntax und relative Markdown-Verweise | Erfolgreich geprüft. |
| Erhalt der Ausgangsdateien | Alle 21 Ausgangspfade vorhanden; unveränderte Dateien per SHA-256 verglichen. |
| ZIP-Bau | Deterministischer Aufbau lokal getestet. Gleiches Paket darf erneut gebaut werden; abweichende Bytes unter derselben Version werden abgewiesen. |

## Nicht durchgeführt und nicht zugesichert

Keine Installation in einem zweiten ChatGPT-Konto oder einem anderen Agenten. Keine neue vollständige Arbeitsblatt-Serie, PDF-Sichtabnahme oder Bildbereinigung in diesem Veröffentlichungsauftrag. Keine empirische Wirksamkeitsstudie, Lehrerfreigabe oder vollständige österreichische Lehrplanprüfung. Deutsch und Englisch sind nicht ausreichend praktisch erprobt. Kein anwaltlich geprüfter Haftungs- oder Lizenztext.

Die GitHub-Actions-Konfiguration ist ein vorbereiteter Prüfablauf mit ausschließlich lesenden Repository-Berechtigungen. Ein erfolgreicher Lauf auf GitHub ist mit diesem Bericht nicht nachgewiesen. Die Action-Referenzen wurden beim Vorbereiten gegen die offiziellen Repositories aufgelöst und als Commit-IDs festgehalten.

Die vorhandenen Matheprüfer setzen strukturierte Eingaben voraus. Sie prüfen weder ein hochgeladenes Foto noch den tatsächlich gedruckten PDF-Inhalt und sind kein allgemein abgesicherter Webdienst. Ein erfolgreiches Skriptergebnis ersetzt keine weitere Sicht- und Fachkontrolle.

## Reproduzieren

Im Repository mit Python 3.11 oder neuer:

```bash
python tools/pruefen.py
python tools/paket_bauen.py
```

Die Skripte verwenden die Python-Standardbibliothek und veröffentlichen nichts. Das Paket entsteht unter `dist/v0.1.0/skill.zip`. Für eine inhaltliche Prüfung neuer Mathematikblätter müssen zusätzlich die konkreten Aufgaben, Gegenproben und gerenderten PDF-Seiten geprüft werden.

## Erneute Prüfung der Korrekturfassung 0.1.1

Prüfdatum: 19.11.2026. Korrektur des vorbereiteten, noch nicht auf GitHub veröffentlichten Ausgangspakets.

Der zusammenhängende Ersatzentwurf der rechtlichen Hinweise wurde in beide `RECHTLICHES.md`-Dateien wortgleich übernommen. README und Skill-Beschreibung enthalten die freigegebenen redaktionellen Korrekturen. Alle 47 bisherigen Projektdateipfade und alle 26 Skill-Dateipfade sind erhalten. Die Python-Dateien und die MIT-Standardlizenz sind bytegleich zum Paket 0.1.0.

Erneut ausgeführt: Standard-Skill-Validator; bestehendes Mathe-Regressionsskript mit 3 ursprünglichen und 3 erweiterten Testgruppen; alle 15 Projekttests; Versions-, Struktur-, Syntax- und lokale Verweisprüfung. Alle genannten Prüfungen bestanden. Diese Ergebnisse belegen keine vollständige Arbeitsblatt-, Bildbereinigungs- oder Rechtsprüfung.

Nicht ausgeführt: GitHub-Veröffentlichung, GitHub-CI, Plattforminstallation und neue PDF-/Bildbereinigungsabnahme. Betreiberidentität, privater Kontaktweg und tatsächlicher Umgang mit Feedbackdaten wurden nicht erfunden oder als geklärt ausgegeben. Die bisherige Fassung 0.1.0 bleibt als unverändertes Ausgangsartefakt erhalten.
