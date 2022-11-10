# Berechne die Römische Zahl aus einer Arabischen

def roemische_zahl(arabische_zahl): # Definiere Funktion roemische_zahl mit Parameter arabische_zahl
    if arabische_zahl==0:           # Wenn arabische_zahl gleich Null ist...
        return ''                   # ... dann gebe einen leeren Text aus
    elif arabische_zahl==1:         # Falls aber die arabische_zahl gleich Eins ist ...
        return 'I'                  # ... dann gebe die Römische Zahl I als Text aus

'''
if __name__ == '__main__':          # Die obigen Funktionen werden nur ausgeführt...
    import argparse
    parser = argparse.ArgumentParser(description = 'Berechne die Römische Zahl aus einer Arabischen Zahl')
    parser.add_argument('arabischezahl', type=int, help='Eine ganze Arabische Zahl')
    args = parser.parse_args()
    print(roemische_zahl(args.arabischezahl))   # ... wenn man sie hier in der main Funktion aufruft
'''
