# Berechne die Römische Zahl aus einer Arabischen Zahl

# Definiere Funktion "berechne_roemische_zahl"
# mit Parameter-Variablen "arabische_zahl"
def berechne_roemische_zahl(arabische_zahl):
    roemische_zahl = ''         # Definiere Variable "roemische_zahl" die einen leeren Zeichenketten-Text enthält
    if arabische_zahl==0:       # Wenn Variable "arabische_zahl" gleich Null ist ...
        roemische_zahl = ''     # ... dann bekommt die Variable "roemische_zahl" einen leeren Zeichenketten-Text
    elif arabische_zahl==1:     # Ansonsten, wenn die Variable "arabische_zahl" gleich Eins ist ...
        roemische_zahl = 'I'    # ... dann bekommt die Variable "roemische_zahl" den Zeichenketten-Text 'I'
    return roemische_zahl       # Gebe den Wert von der Variablen "roemische_zahl" zurück

'''
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description = 'Berechne die Römische Zahl aus einer natürlichen Arabischen Zahl')
    parser.add_argument('arabische_zahl', type=int, help='Eine natürliche Arabische Zahl')
    args = parser.parse_args()
    
    # Die obige Funktion "berechne_roemische_zahl" wird nur dann in der Kommandozeile ausgeführt...
    # ... wenn man sie hier in der __main__ Funktion aufruft
    print(berechne_roemische_zahl(args.arabische_zahl))
'''
