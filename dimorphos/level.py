from nuetzliches import zufaellige_position
from spielelement import Asteroid

class Level:
    def __init__(self):
        self.anzahl_asteroiden = 6
    def erzeuge_asteroid(self, oberflaeche, bild_asteroid):
        pass
class EndlosLevel(Level):
    def __init__(self):
        super().__init__() # Aufruf Basis Klassen Konstruktor Funktion

    def erzeuge_asteroiden(self, oberflaeche, bild_asteroid, anzahl):
        asteroiden = []
        for i in range(anzahl):
            position = zufaellige_position(oberflaeche, True)
            asteroiden.append(Asteroid(position, bild_asteroid))
        return asteroiden

