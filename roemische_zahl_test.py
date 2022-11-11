# Teste das Programm "roemische_zahl" dass es funktioniert
#
# http://roemischezahlen.babuo.com/roemischen-ziffern-1-1000

import unittest
from roemische_zahl import roemische_zahl

class roemische_zahl_test(unittest.TestCase):   # Definiere die Test Klasse "roemische_zahl_test"
    
    def teste_roemische_zahl_0(self):           # Definiere die Testfunktion "teste_roemische_zahl_0"
        ergebnis = roemische_zahl(0)            # Rufe die Funktion roemische_zahl mit 0 auf und speichere den Rückgabewert in der Variablen "ergebnis"
        self.assertEqual(ergebnis, '')          # Vergleiche das Ergebnis mit der erwarteten Römischen Zahl
    
    def teste_roemische_zahl_1(self):           # Definiere die Testfunktion "teste_roemische_zahl_1"
        ergebnis = roemische_zahl(1)            # Rufe die Funktion roemische_zahl mit 1 auf und speichere den Rückgabewert in der Variablen "ergebnis"
        self.assertEqual(ergebnis, 'I')         # Vergleiche das Ergebnis mit der erwarteten Römischen Zahl

if __name__ == '__main__':  # Die obigen Funktionen werden nur dann in der Kommandozeile ausgeführt...
    unittest.main()         # ... wenn man sie hier in der __main__ Funktion aufruft
