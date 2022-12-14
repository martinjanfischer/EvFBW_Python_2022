# EvFBW_Python_2022
Python Programmierkurs 2022 für Jugendliche beim Evangelischen Familienbildungswerk

## Software
Wir arbeiten auf Windows Computern.

Installiere das Python Übersetzer Programm von
[www.python.org](https://www.python.org/downloads/)

Installiere den Textbearbeitungs Programm Notepad++ von
[notepad-plus-plus.org](https://notepad-plus-plus.org/downloads/)

Installiere das Bildbearbeitungs Programm The Gimp von
[www.gimp.org](https://www.gimp.org/)

## Zusatz Module
Unsere Python Skripte benötigen zusätzliche Software.
Wir installieren die Module über das Programm Pip.

Um alle in dem Kurs benötigten Module zu installieren
musst Du das folgende Kommando ausführen
```
    pip install -r requirements.txt
```

Um alle in dem Kurs benötigten Module wieder zu deinstallieren
musst Du das folgende Kommando ausführen
```
    pip uninstall -r requirements.txt
```

Ihr könnt jederzeit den Inhalt dieser Datei 
mit allen in dem Kurs aktuell benötigten Modulen ersetzen.
Dazu musst Du das folgende Kommando ausführen
```
    pip freeze > requirements.txt
```

## 10. & 17. November & 8. Dezember 2022
Wir beginnen mit den Grundlagen
- Hallo Welt Programm
- Römische Zahl aus Arabischer Zahl

### hallo_welt_bunt.py
1. Führe folgende Kommandos aus
```
    pip install PyQt5
    python hallo_welt_bunt.py
```
2. Das Programm öffnet ein Fenster,
in dem der Text "Hallo Welt, mein Name ist ..." angezeigt wird.
1. Schließe das Programm.
1. Öffne das Python Skript im Programm notepad++.
1. Finde den Text und ergänze Deinen Namen.
1. Kommando ausführen
```
    python hallo_welt_bunt.py
```
7. Das Programm zeigt jetzt Deinen Namen.

### roemische_zahl.py
Das Programm erwartet ein eine Arabische Zahl als Argument.
1. Wenn keine Arabische Zahl angegeben wird, wird ein Hilfetext angezeigt.
Führe folgendes Kommando aus
```
    python roemische_zahl.py
```
2. Wenn eine Arabische Zahl angegeben wird, wird dafür eine Römische Zahl angezeigt.
Führe folgendes Kommando mit dem Argument 7 aus
```
    python roemische_zahl.py 7
```
3. Das Programm zeigt die Römische Zahl VII an.
```
    VII
```

### roemische_zahl_test.py
Das Programm testet das eigentliche Programm zur Berechnung der Römischen Zahl.
Dieses Testprogramm ist Euer Sicherheitsnetz und gibt Euch Roten Alarm
wenn das eigentliche Programm fehlerhaft arbeitet.

1. Führe folgendes Kommando aus
```
    python roemische_zahl_test.py
```
2. Wenn alle Tests erfolgreich ausgeführt wurden, erhält man folgende Ausgabe
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```
3. Wenn ein oder mehrere Tests fehlgeschlagen sind, erhält man folgende Ausgabe
```
.F
======================================================================
FAIL: teste_roemische_zahl_1_bis_10 (__main__.roemische_zahl_test)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Sources\EvFBW_Python_2022\roemische_zahl_test.py", line 30, in teste_roemische_zahl_1_bis_10
    self.assertEqual(ergebnis, 'VIII')       # Melde einen Fehler wenn die Variable ergebnis nicht den Zeichenketten-Text VII enthält
AssertionError: 'VII' != 'VIII'
- VII
+ VIII
?    +


----------------------------------------------------------------------
Ran 2 tests in 0.007s

FAILED (failures=1)
```

