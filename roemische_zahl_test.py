import unittest
import roemische_zahl

class roemische_zahl_test(unittest.TestCase):
    def teste_roemische_zahl_0(self):
        ergebnis = roemische_zahl.roemische_zahl(0)
        self.assertEqual(ergebnis, '')

    def teste_roemische_zahl_1(self):
        ergebnis = roemische_zahl.roemische_zahl(1)
        self.assertEqual(ergebnis, 'I')

if __name__ == '__main__':
    unittest.main()
