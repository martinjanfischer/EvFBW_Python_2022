# Teste das Programm "roemische_zahl" dass es funktioniert
#
# https://www.mathe-ist-einfach.de/Roemischezahlen/rom1000.html

import unittest
from roemische_zahl import berechne_roemische_zahl

class roemische_zahl_test(unittest.TestCase):   # Definiere die Test Klasse "roemische_zahl_test"
    
    def teste_roemische_zahl_0(self):           # Definiere die Testfunktion "teste_roemische_zahl_0"
        ergebnis = berechne_roemische_zahl(0)   # Rufe die Funktion berechne_roemische_zahl mit 0 auf und speichere den Rückgabewert in der Variablen "ergebnis"
        self.assertEqual(ergebnis, '')          # Melde einen Fehler wenn die Variable ergebnis nicht den leeren Zeichenketten-Text enthält
    
    def teste_roemische_zahl_1(self):           # Definiere die Testfunktion "teste_roemische_zahl_1"
        ergebnis = berechne_roemische_zahl(1)   # Rufe die Funktion berechne_roemische_zahl mit 1 auf und speichere den Rückgabewert in der Variablen "ergebnis"
        self.assertEqual(ergebnis, 'I')         # Melde einen Fehler wenn die Variable ergebnis nicht den Zeichenketten-Text I enthält

if __name__ == '__main__':  # Die obigen Funktionen werden nur dann in der Kommandozeile ausgeführt...
    unittest.main()         # ... wenn man sie hier in der __main__ Funktion aufruft
