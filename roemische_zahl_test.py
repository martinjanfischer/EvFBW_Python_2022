# Teste das Programm "roemische_zahl" dass es funktioniert
#
# https://www.mathe-ist-einfach.de/Roemischezahlen/rom1000.html

import unittest
from roemische_zahl import berechne_roemische_zahl

class roemische_zahl_test(unittest.TestCase):   # Definiere die Test Klasse "roemische_zahl_test"
    
    def teste_roemische_zahl_0(self):           # Definiere die Testfunktion "teste_roemische_zahl_0"
        ergebnis = berechne_roemische_zahl(-1)  # Rufe die Funktion berechne_roemische_zahl mit -1 auf und speichere den Rückgabewert in der Variablen "ergebnis"
        self.assertEqual(ergebnis, '')          # Melde einen Fehler wenn die Variable ergebnis nicht den leeren Zeichenketten-Text enthält
        ergebnis = berechne_roemische_zahl(0)   # Rufe die Funktion berechne_roemische_zahl mit 0 auf und speichere den Rückgabewert in der Variablen "ergebnis"
        self.assertEqual(ergebnis, '')          # Melde einen Fehler wenn die Variable ergebnis nicht den leeren Zeichenketten-Text enthält
    
    def teste_roemische_zahl_1_bis_10(self):    # Definiere die Testfunktion "teste_roemische_zahl_1_bis_10"
        ergebnis = berechne_roemische_zahl(1)   # Rufe die Funktion berechne_roemische_zahl mit 1 auf und speichere den Rückgabewert in der Variablen "ergebnis"
        self.assertEqual(ergebnis, 'I')         # Melde einen Fehler wenn die Variable ergebnis nicht den Zeichenketten-Text I enthält
        ergebnis = berechne_roemische_zahl(2)   # Rufe die Funktion berechne_roemische_zahl mit 2 auf und speichere den Rückgabewert in der Variablen "ergebnis"
        self.assertEqual(ergebnis, 'II')        # Melde einen Fehler wenn die Variable ergebnis nicht den Zeichenketten-Text II enthält
        ergebnis = berechne_roemische_zahl(3)   # Rufe die Funktion berechne_roemische_zahl mit 3 auf und speichere den Rückgabewert in der Variablen "ergebnis"
        self.assertEqual(ergebnis, 'III')       # Melde einen Fehler wenn die Variable ergebnis nicht den Zeichenketten-Text III enthält
        ergebnis = berechne_roemische_zahl(4)   # Rufe die Funktion berechne_roemische_zahl mit 4 auf und speichere den Rückgabewert in der Variablen "ergebnis"
        self.assertEqual(ergebnis, 'IV')        # Melde einen Fehler wenn die Variable ergebnis nicht den Zeichenketten-Text IV enthält
        ergebnis = berechne_roemische_zahl(5)   # Rufe die Funktion berechne_roemische_zahl mit 5 auf und speichere den Rückgabewert in der Variablen "ergebnis"
        self.assertEqual(ergebnis, 'V')         # Melde einen Fehler wenn die Variable ergebnis nicht den Zeichenketten-Text V enthält
        ergebnis = berechne_roemische_zahl(6)   # Rufe die Funktion berechne_roemische_zahl mit 6 auf und speichere den Rückgabewert in der Variablen "ergebnis"
        self.assertEqual(ergebnis, 'VI')        # Melde einen Fehler wenn die Variable ergebnis nicht den Zeichenketten-Text VI enthält
        ergebnis = berechne_roemische_zahl(7)   # Rufe die Funktion berechne_roemische_zahl mit 7 auf und speichere den Rückgabewert in der Variablen "ergebnis"
        self.assertEqual(ergebnis, 'VII')       # Melde einen Fehler wenn die Variable ergebnis nicht den Zeichenketten-Text VII enthält
        ergebnis = berechne_roemische_zahl(8)   # Rufe die Funktion berechne_roemische_zahl mit 8 auf und speichere den Rückgabewert in der Variablen "ergebnis"
        self.assertEqual(ergebnis, 'VIII')      # Melde einen Fehler wenn die Variable ergebnis nicht den Zeichenketten-Text VIII enthält
        ergebnis = berechne_roemische_zahl(9)   # Rufe die Funktion berechne_roemische_zahl mit 9 auf und speichere den Rückgabewert in der Variablen "ergebnis"
        self.assertEqual(ergebnis, 'IX')        # Melde einen Fehler wenn die Variable ergebnis nicht den Zeichenketten-Text IX enthält
        ergebnis = berechne_roemische_zahl(10)  # Rufe die Funktion berechne_roemische_zahl mit 10 auf und speichere den Rückgabewert in der Variablen "ergebnis"
        self.assertEqual(ergebnis, 'X')         # Melde einen Fehler wenn die Variable ergebnis nicht den Zeichenketten-Text X enthält

if __name__ == '__main__':  # Die obigen Funktionen werden nur dann in der Kommandozeile ausgeführt...
    unittest.main()         # ... wenn man sie hier in der __main__ Funktion aufruft
