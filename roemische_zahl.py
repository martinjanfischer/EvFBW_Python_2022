# Berechne die Römische Zahl aus einer Arabischen Zahl

def roemische_zahl(arabische_zahl): # Definiere Funktion "roemische_zahl" mit Parameter-Variablen "arabische_zahl"
    if arabische_zahl==0:           # Wenn Variable arabische_zahl gleich Null ist ...
        return ''                   # ... dann gebe einen leeren Zeichenketten-Text zurück
    elif arabische_zahl==1:         # Ansonsten, wenn die Variable arabische_zahl gleich Eins ist ...
        return 'I'                  # ... dann gebe die Römische Zahl I als Zeichenketten-Text zurück

'''
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description = 'Berechne die Römische Zahl aus einer Arabischen Zahl')
    parser.add_argument('arabischezahl', type=int, help='Eine ganze Arabische Zahl')
    args = parser.parse_args()
    
    # Die obige Funktion "roemische_zahl" wird nur dann in der Kommandozeile ausgeführt...
    # ... wenn man sie hier in der __main__ Funktion aufruft
    print(roemische_zahl(args.arabischezahl))
'''
