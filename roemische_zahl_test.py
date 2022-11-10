# Teste roemische_zahl auf Korrektheit
#
# http://roemischezahlen.babuo.com/roemischen-ziffern-1-1000

import unittest
import roemische_zahl

class roemische_zahl_test(unittest.TestCase):       # Definiere eine Test Klasse
    
    def teste_roemische_zahl_0(self):               # Definiere eine Testfunktion
        ergebnis = roemische_zahl.roemische_zahl(0) # Rufe die Funktion roemische_zahl mit einer Arabischen Zahl auf und speichere das Ergebnis
        self.assertEqual(ergebnis, '')              # Vergleiche das Ergebnis mit der erwarteten Römischen Zahl
    
    def teste_roemische_zahl_1(self):               # Definiere eine Testfunktion
        ergebnis = roemische_zahl.roemische_zahl(1) # Rufe die Funktion roemische_zahl mit einer arabischen Zahl auf und speichere das Ergebnis
        self.assertEqual(ergebnis, 'I')             # Vergleiche das Ergebnis mit der erwarteten Römischen Zahl

if __name__ == '__main__':  # Die obigen Funktionen werden nur ausgeführt...
    unittest.main()         # ... wenn man sie hier in der main Funktion aufruft
