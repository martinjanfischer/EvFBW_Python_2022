from nuetzliches import zufaellige_position
from spielelement import Asteroid
import random

class Level:
    def __init__(self):
        self.anzahl_asteroiden = 6
    
    def erzeuge_asteroiden(self, oberflaeche, bild_asteroid, anzahl):
        pass

class EndlosLevel(Level):
    def __init__(self):
        super().__init__() # Aufruf Basis Klassen Konstruktor Funktion
    
    def erzeuge_asteroiden(self, oberflaeche, bild_asteroid, anzahl):
        asteroiden = []
        for i in range(anzahl):
            position = zufaellige_position(oberflaeche, True)
            asteroiden.append(Asteroid(position, bild_asteroid, 2))
        return asteroiden

    # Behandle spiele logig
    def behandle_spielelogik(self, score, asteroiden, anzahl_asteroiden, bilder_asteroiden, leinwand):
        if score % 2 == 1 and asteroiden and len(asteroiden) < anzahl_asteroiden:
            bild_asteroid = bilder_asteroiden[random.randrange(len(bilder_asteroiden))]
            neue_asteroiden = self.erzeuge_asteroiden(leinwand, bild_asteroid, 3)
            asteroiden.extend(neue_asteroiden)

        return len(asteroiden)



