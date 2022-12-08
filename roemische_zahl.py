# Berechne die Römische Zahl aus einer Arabischen Zahl

# Definiere Funktion "berechne_roemische_zahl"
# mit Parameter-Variablen "arabische_zahl"
def berechne_roemische_zahl(arabische_zahl):
    roemische_zahl = ''         # Definiere Variable "roemische_zahl" die einen leeren Zeichenketten-Text enthält
    
    # 1000 ist 'M'
    while arabische_zahl>=1000:
        roemische_zahl += 'M'
        arabische_zahl -= 1000
    
    # 100 ist 'C', 400 ist 'CD', 500 ist 'D', 900 ist 'CM'
    if arabische_zahl>=900:
        roemische_zahl += 'CM'
        arabische_zahl -= 900
    if arabische_zahl>=500:
        roemische_zahl += 'D'
        arabische_zahl -= 500
    if arabische_zahl>=400:
        roemische_zahl += 'CD'
        arabische_zahl -= 400
    while arabische_zahl>=100:
        roemische_zahl += 'C'
        arabische_zahl -= 100
    
    # 10 ist 'X', 40 ist 'XL', 50 ist 'L', 90 ist 'XC'
    if arabische_zahl>=90:
        roemische_zahl += 'XC'
        arabische_zahl -= 90
    if arabische_zahl>=50:
        roemische_zahl += 'L'
        arabische_zahl -= 50
    if arabische_zahl>=40:
        roemische_zahl += 'XL'
        arabische_zahl -= 40
    while arabische_zahl>=10:
        roemische_zahl += 'X'
        arabische_zahl -= 10
    
    # 1 ist 'I', 4 ist 'IV', 5 ist 'V', 9 ist 'IX'
    if arabische_zahl>=9:       # Wenn die Variable "arabische_zahl" größer oder gleich 9 ist ...
        roemische_zahl += 'IX'  # ... dann hänge an die Variable "roemische_zahl" den Zeichenketten-Text 'IX' an
        arabische_zahl -= 9     # ... und ziehe von der Variablen "arabische_zahl" den Wert 9 ab
    if arabische_zahl>=5:       # Wenn die Variable "arabische_zahl" größer oder gleich 5 ist ...
        roemische_zahl += 'V'   # ... dann hänge an die Variable "roemische_zahl" den Zeichenketten-Text 'V' an
        arabische_zahl -= 5     # ... und ziehe von der Variablen "arabische_zahl" den Wert 5 ab
    if arabische_zahl>=4:       # Wenn die Variable "arabische_zahl" größer oder gleich 4 ist ...
        roemische_zahl += 'IV'  # ... dann hänge an die Variable "roemische_zahl" den Zeichenketten-Text 'IV' an
        arabische_zahl -= 4     # ... und ziehe von der Variablen "arabische_zahl" den Wert 4 ab
    while arabische_zahl>=1:    # Schleife: Solange die Variable "arabische_zahl" größer oder gleich 1 ist ...
        roemische_zahl += 'I'   # ... dann hänge an die Variable "roemische_zahl" den Zeichenketten-Text 'I' an
        arabische_zahl -= 1     # ... und ziehe von der Variablen "arabische_zahl" den Wert 1 ab
    
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
