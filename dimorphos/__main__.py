from dimorphos import Dimorphos

if __name__ == "__main__":      # Hauptfunktion
    with Dimorphos() as dimorphos:  # Instanziiere Spielklasse und speichere Objekt in Variablen
        dimorphos.endlos_schleife() # Führe Endlos-Ereignis-Nachrichten-Schleife aus
        del dimorphos               # Lösche Objekt wenn Endlosschleife unterbrochen wurde

'''
Anforderungen

- Verschiedene Level mit aufsteigender Schwierigkeit
    - Dateibasierte Definition von Leveln
    - Erhöhe Anzahl und Geschwindigkeit der Asteroiden
    - Level
        - Letztes Level
        - Mehrere Level
        - Endlos Level
    - Zeit Tafel
    - Highscore: Höchstes Level, Kürzeste Zeit -> In Datei schreiben
    - Startbildschirm

- Mehr Grafik Effekte
    - Explosions Animationen
        - Raumschiff Zerstört
        - Asteroid Zerstört
        - Laser Einschlag auf Asteroid
    - Asteroiden zersplittern in Kleinere Brocken
        - Zwei Stufen mindestens
    - Raumschiff Animationen
        - Nachbrenner
        - Manövrierdüsen
        - Mündungsfeuer
        - Blinklichter
        - Ausfahrbare Flügel oder Geräte
        - (Schutzschild: Siehe Physik)

- Physik Effekte
    - Kollisionen
        - Asteroiden miteinander (teuer)
            - Asteroiden prallen ab in andere Flugbahn
            - Asteroiden Verändern Dreh-Impuls
        - Schutzschild mit Asteroid
            - Raumschiff und Asteroiden prallen ab in andere Flugbahn
            - Asteroiden Verändern Dreh-Impuls
    - Gravitation

- Ton
    - Laser Abschuss
    - Laser Einschlag auf Asteroid
    - Explosion Raumschiff Zerstört
    - Explosion Asteroid Zerstört
    - Nachbrenner
    - Manövrierdüsen
    - Schutzschild
    - Kollisionen
        - Asteroiden miteinander
        - Schutzschild mit Asteroid

- Erweiterungen
    - Raumschiff
        - Schaden aufnehmen, Zerstörung wenn vollständig beschädigt
        - Laser abkühlen, keine Abschussmöglichkeit wenn zu heiss
        - Gadgets einsammeln
            - Schaden reparieren
            - Ausdauernder Laser
            - Andere Waffen
            - Schutzschild
            - Helferlein Satellit
    - Asteroid
        - Schaden aufnehmen, Zerstörung wenn vollständig beschädigt
        - Verschiedene Größen
        - Gegnerische Raumschiffe

Links
- Coding with Russ
	- https://www.youtube.com/watch?v=nXOVcOBqFwM
	- https://github.com/russs123/pygame_tutorials
'''
