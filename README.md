# EvFBW_Python_2022
Python Programmierkurs 2022 für Jugendliche beim Evangelischen Familienbildungswerk

## Zusatz Module
Unsere Python Skripte benötigen zusätzliche Software.
Wir installieren die Module über das Programm Pip.

Um alle in dem Kurs benötigten Module zu installieren
musst Du das folgende Kommando ausführen
```
    pip install -r zusatz_module.txt
```

Um alle in dem Kurs benötigten Module wieder zu deinstallieren
musst Du das folgende Kommando ausführen
```
    pip uninstall -r zusatz_module.txt
```

Ihr könnt jederzeit den Inhalt dieser Datei 
mit allen in dem Kurs aktuell benötigten Modulen ersetzen.
Dazu musst Du das folgende Kommando ausführen
```
    pip freeze > zusatz_module.txt
```


## 10. November 2022
Wir beginnen mit den Grundlagen
- Hallo Welt Programm
- Römische Zahl aus Arabischer Zahl

### hallo_welt_bunt.py
1. Kommandos ausführen
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
Kommandos ausführen
```
    python roemische_zahl.py
```
2. Wenn keine Arabische Zahl angegeben wird, wird ein Hilfetext angezeigt.
Kommandos ausführen
```
    python roemische_zahl.py 7
```
3. Das Programm zeigt die Römische Zahl VII an.

### roemische_zahl_test.py
Das Programm testet das eigentliche Programm zur Berechnung der Römischen Zahl.
Dieses Testprogramm ist Euer Sicherheitsnetz und meldet Euch
wenn das eigentliche Programm fehlerhaft arbeitet.

1. Kommandos ausführen
```
    python roemische_zahl_test.py
```


