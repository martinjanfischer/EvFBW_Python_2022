import unittest
import roemische_zahl

class roemische_zahl_test(unittest.TestCase):
    def teste_roemische_zahl_0(self):               #definiere eine Testfunktion
        ergebnis = roemische_zahl.roemische_zahl(0) #Rufe die Funktion roemische_zahl mit der arabischen Zahl 0 auf und speichere das Ergebnis
        self.assertEqual(ergebnis, '')              #Vergleiche das ergebnis mit dem erwarteten Wert

    def teste_roemische_zahl_1(self):               #definiere eine Testfunktion
        ergebnis = roemische_zahl.roemische_zahl(1) #Rufe die Funktion roemische_zahl mit der arabischen Zahl 1 auf und speichere das Ergebnis
        self.assertEqual(ergebnis, 'I')             #Vergleiche das ergebnis mit dem erwarteten Wert

if __name__ == '__main__':
    unittest.main()
