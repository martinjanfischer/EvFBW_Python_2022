# Berechne die Römische Zahl aus einer Arabischen Zahl

# Definiere Klasse "RoemischeZahl"
# Wir können Objekte von diesem Typ erzeugen
# und in Variablen speichern
class RoemischeZahl:
    
    # Definiere Hilfs-Funktion "berechne_roemische_zahl_hilfs_funktion"
    # mit Parameter-Variablen "arabische_zahl"
    def berechne_roemische_zahl_hilfs_funktion(self, arabische_zahl, roemische_zahl, 
        roemische_ziffer_1, roemische_ziffer_4, roemische_ziffer_5, roemische_ziffer_9,
        arabische_ziffer_1, arabische_ziffer_4, arabische_ziffer_5, arabische_ziffer_9
        ):
        if (arabische_zahl >= arabische_ziffer_9):      # Wenn die Variable "arabische_zahl" größer oder gleich 9 ist ...
            roemische_zahl += roemische_ziffer_9        # ... dann hänge an die Variable "roemische_zahl" den Zeichenketten-Text 'IX' an
            arabische_zahl -= arabische_ziffer_9        # ... und ziehe von der Variablen "arabische_zahl" den Wert 9 ab
        elif (arabische_zahl >= arabische_ziffer_5):    # Wenn die Variable "arabische_zahl" größer oder gleich 5 ist ...
            roemische_zahl += roemische_ziffer_5        # ... und ziehe von der Variablen "arabische_zahl" den Wert 5 ab
            arabische_zahl -= arabische_ziffer_5        # ... und ziehe von der Variablen "arabische_zahl" den Wert 5 ab
        elif (arabische_zahl >= arabische_ziffer_4):    # Wenn die Variable "arabische_zahl" größer oder gleich 4 ist ...
            roemische_zahl += roemische_ziffer_4        # ... dann hänge an die Variable "roemische_zahl" den Zeichenketten-Text 'IV' an
            arabische_zahl -= arabische_ziffer_4        # ... und ziehe von der Variablen "arabische_zahl" den Wert 4 ab
        while (arabische_zahl >= arabische_ziffer_1):   # Schleife: Solange die Variable "arabische_zahl" größer oder gleich 1 ist ...
            roemische_zahl += roemische_ziffer_1        # ... dann hänge an die Variable "roemische_zahl" den Zeichenketten-Text 'I' an
            arabische_zahl -= arabische_ziffer_1        # ... und ziehe von der Variablen "arabische_zahl" den Wert 1 ab
        
        return arabische_zahl, roemische_zahl # Gebe zwei Werte zurück
    
    # Definiere Funktion "berechne_roemische_zahl"
    # mit Parameter-Variablen "arabische_zahl"
    def berechne_roemische_zahl(self, arabische_zahl):
        roemische_zahl = ''         # Definiere Variable "roemische_zahl" die einen leeren Zeichenketten-Text enthält
        
        # 1000 ist 'M'
        while arabische_zahl>=1000:
            roemische_zahl += 'M'
            arabische_zahl -= 1000
        
        # 100 ist 'C', 400 ist 'CD', 500 ist 'D', 900 ist 'CM'
        ergebnis = self.berechne_roemische_zahl_hilfs_funktion(arabische_zahl, roemische_zahl, 'C', 'CD', 'D', 'CM', 100, 400, 500, 900)
        arabische_zahl = ergebnis[0]
        roemische_zahl = ergebnis[1]
        
        # 10 ist 'X', 40 ist 'XL', 50 ist 'L', 90 ist 'XC'
        ergebnis = self.berechne_roemische_zahl_hilfs_funktion(arabische_zahl, roemische_zahl, 'X', 'XL', 'L', 'XC', 10, 40, 50, 90)
        arabische_zahl = ergebnis[0]
        roemische_zahl = ergebnis[1]
        
        # 1 ist 'I', 4 ist 'IV', 5 ist 'V', 9 ist 'IX'
        ergebnis = self.berechne_roemische_zahl_hilfs_funktion(arabische_zahl, roemische_zahl, 'I', 'IV', 'V', 'IX', 1, 4, 5, 9)
        arabische_zahl = ergebnis[0]
        roemische_zahl = ergebnis[1]
        
        return roemische_zahl       # Gebe den Wert von der Variablen "roemische_zahl" zurück
    
    # der Konstruktor-Funktion übergeben wir 
    # der Parameter-Variablen "arabische_zahl" 
    # den Anfangswert des RoemischeZahl Objektes, z.B.
    #  r = RoemischeZahl(7)
    #  r.roemische_zahl == 'VII'
    def __init__(self, arabische_zahl):
        if arabische_zahl < 0:
            arabische_zahl = 0
        self.arabische_zahl = arabische_zahl
        self.roemische_zahl = self.berechne_roemische_zahl(arabische_zahl)
    
    # Wir können zwei RoemischeZahl Objekte addieren, z.B.
    #  r_links = RoemischeZahl(7)
    #  r_rechts = RoemischeZahl(4)
    #  r_summe = r_links + r_rechts
    #  r_summe.roemische_zahl == 'XI'
    def __add__(self, rechte_roemische_zahl):
        summe_arabische_zahl = self.arabische_zahl + rechte_roemische_zahl.arabische_zahl
        return RoemischeZahl(summe_arabische_zahl)
    
    # Wir können zwei RoemischeZahl Objekte voneinander subtrahieren, z.B.
    #  r_links = RoemischeZahl(7)
    #  r_rechts = RoemischeZahl(4)
    #  r_differenz = r_links - r_rechts
    #  r_differenz.roemische_zahl == 'III'
    def __sub__(self, rechte_roemische_zahl):
        differenz_arabische_zahl = self.arabische_zahl - rechte_roemische_zahl.arabische_zahl
        return RoemischeZahl(differenz_arabische_zahl)
    
    # Wir können zwei RoemischeZahl Objekte multiplizieren, z.B.
    #  r_links = RoemischeZahl(7)
    #  r_rechts = RoemischeZahl(4)
    #  r_produkt = r_links * r_rechts
    #  r_produkt.roemische_zahl == 'XXVIII'
    def __mul__(self, rechte_roemische_zahl):
        produkt_arabische_zahl = self.arabische_zahl * rechte_roemische_zahl.arabische_zahl
        return RoemischeZahl(produkt_arabische_zahl)
    
    # Wir können zwei RoemischeZahl Objekte voneinander dividieren, z.B.
    #  r_links = RoemischeZahl(33)
    #  r_rechts = RoemischeZahl(11)
    #  r_quotient = r_links // r_rechts
    #  r_quotient.roemische_zahl == 'III'
    def __floordiv__(self, rechte_roemische_zahl):
        quotient_arabische_zahl = self.arabische_zahl // rechte_roemische_zahl.arabische_zahl
        return RoemischeZahl(quotient_arabische_zahl)
    
    # Wir können ein RoemischeZahl Objekt auf der Kommandozeile ausgeben
    def ausgabe(self):
        print(self.roemische_zahl)


if __name__ == '__main__':      # Definiere die __main__ Funktion
    import argparse
    parser = argparse.ArgumentParser(description = 'Berechne die Römische Zahl aus einer natürlichen Arabischen Zahl')
    parser.add_argument('arabische_zahl', type=int, help='Eine natürliche Arabische Zahl')
    args = parser.parse_args()
    
    # Die obige Funktion "berechne_roemische_zahl" 
    # wird nur dann in der Kommandozeile ausgeführt...
    # ... wenn man sie hier in der __main__ Funktion aufruft
    roemische_zahl = RoemischeZahl(args.arabische_zahl)
    roemische_zahl.ausgabe()
