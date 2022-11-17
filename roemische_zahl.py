# Berechne die Römische Zahl aus einer Arabischen Zahl

# Definiere Funktion "berechne_roemische_zahl"
# mit Parameter-Variablen "arabische_zahl"
def berechne_roemische_zahl(arabische_zahl):
    roemische_zahl = ''         # Definiere Variable "roemische_zahl" die einen leeren Zeichenketten-Text enthält
    
    if arabische_zahl==10:      # Wenn die Variable "arabische_zahl" gleich 10 ist ...
        roemische_zahl = 'X'    # ... dann bekommt die Variable "roemische_zahl" den Zeichenketten-Text 'X'
    if arabische_zahl==9:       # Wenn die Variable "arabische_zahl" gleich 9 ist ...
        roemische_zahl = 'IX'   # ... dann bekommt die Variable "roemische_zahl" den Zeichenketten-Text 'IX'
    if arabische_zahl==8:       # Wenn die Variable "arabische_zahl" gleich 8 ist ...
        roemische_zahl = 'VIII' # ... dann bekommt die Variable "roemische_zahl" den Zeichenketten-Text 'VIII'
    if arabische_zahl==7:       # Wenn die Variable "arabische_zahl" gleich 7 ist ...
        roemische_zahl = 'VII'  # ... dann bekommt die Variable "roemische_zahl" den Zeichenketten-Text 'VII'
    if arabische_zahl==6:       # Wenn die Variable "arabische_zahl" gleich 6 ist ...
        roemische_zahl = 'VI'   # ... dann bekommt die Variable "roemische_zahl" den Zeichenketten-Text 'VI'
    if arabische_zahl==5:       # Wenn die Variable "arabische_zahl" gleich 5 ist ...
        roemische_zahl = 'V'    # ... dann bekommt die Variable "roemische_zahl" den Zeichenketten-Text 'V'
    if arabische_zahl==4:       # Wenn die Variable "arabische_zahl" gleich 4 ist ...
        roemische_zahl = 'IV'   # ... dann bekommt die Variable "roemische_zahl" den Zeichenketten-Text 'IV'
    if arabische_zahl==3:       # Wenn die Variable "arabische_zahl" gleich 3 ist ...
        roemische_zahl = 'III'  # ... dann bekommt die Variable "roemische_zahl" den Zeichenketten-Text 'III'
    if arabische_zahl==2:       # Wenn die Variable "arabische_zahl" gleich 2 ist ...
        roemische_zahl = 'II'   # ... dann bekommt die Variable "roemische_zahl" den Zeichenketten-Text 'II'
    if arabische_zahl==1:       # Wenn die Variable "arabische_zahl" gleich 1 ist ...
        roemische_zahl = 'I'    # ... dann bekommt die Variable "roemische_zahl" den Zeichenketten-Text 'I'
    
    return roemische_zahl       # Gebe den Wert von der Variablen "roemische_zahl" zurück

if __name__ == '__main__':      # Definiere die __main__ Funktion
    import argparse
    parser = argparse.ArgumentParser(description = 'Berechne die Römische Zahl aus einer natürlichen Arabischen Zahl')
    parser.add_argument('arabische_zahl', type=int, help='Eine natürliche Arabische Zahl')
    args = parser.parse_args()
    
    # Die obige Funktion "berechne_roemische_zahl" 
    # wird nur dann in der Kommandozeile ausgeführt...
    # ... wenn man sie hier in der __main__ Funktion aufruft
    print(berechne_roemische_zahl(args.arabische_zahl))
