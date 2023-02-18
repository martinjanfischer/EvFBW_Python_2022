from pygame.time import get_ticks
from spielelement import AlienRaumschiff, Asteroid
from nuetzliches import zufaellige_position

class Level:
    MIN_ASTEROIDEN_DISTANZ = 250
    
    def __init__(self,
        asteroiden_anzahl = 6,
        asteroiden_groesse = 1,
        asteroiden_geschwindigkeit_minimum = 30,
        asteroiden_geschwindigkeit_maximum = 100,
        asteroiden_dreh_geschwindigkeit_maximum = 300,
        aliens_anzahl = 0
    ):
        self.asteroiden_anzahl = asteroiden_anzahl
        self.asteroiden_groesse = asteroiden_groesse
        self.asteroiden_geschwindigkeit_minimum = asteroiden_geschwindigkeit_minimum
        self.asteroiden_geschwindigkeit_maximum = asteroiden_geschwindigkeit_maximum
        self.asteroiden_dreh_geschwindigkeit_maximum = asteroiden_dreh_geschwindigkeit_maximum
        self.aliens_anzahl = aliens_anzahl
    
    def initialisiere_asteroiden(self, oberflaeche, bild_asteroid, raumschiff_position):
        asteroiden = []
        for _ in range(self.asteroiden_anzahl):
            # Finde eine zufällige Position für den Asteroiden
            # mit einem gewissen Abstand zum Raumschiff
            while True:
                position = zufaellige_position(oberflaeche, False)
                distanz = position.distance_to(raumschiff_position)
                if (distanz > self.MIN_ASTEROIDEN_DISTANZ):
                    break
            # Füge Asteroid zur Liste hinzu
            asteroiden.append(
                Asteroid(
                    position,
                    bild_asteroid,
                    self.asteroiden_groesse,
                    self.asteroiden_geschwindigkeit_minimum,
                    self.asteroiden_geschwindigkeit_maximum,
                    self.asteroiden_dreh_geschwindigkeit_maximum
                )
            )
        return asteroiden
    
    def initialisiere_aliens(self, oberflaeche, bild_laser, ton_laser, raumschiff_position):
        aliens = []
        for _ in range(self.aliens_anzahl):
            # Finde eine zufällige Position für das Alien
            # mit einem gewissen Abstand zum Raumschiff
            while True:
                position = zufaellige_position(oberflaeche, False)
                distanz = position.distance_to(raumschiff_position)
                if (distanz > self.MIN_ASTEROIDEN_DISTANZ):
                    break
            # Füge Asteroid zur Liste hinzu
            aliens.append(
                AlienRaumschiff(position, bild_laser, ton_laser)
            )
        return aliens
    
    def erzeuge_asteroiden(self, oberflaeche, bild_asteroid, anzahl):
        return None
    
    def erzeuge_alien(self, oberflaeche, bild_laser, ton_laser):
        return None

class EndlosLevel(Level):
    def __init__(self,
        erzeugungs_rate = 1000,
        asteroiden_anzahl = 6,
        asteroiden_groesse = 1,
        asteroiden_geschwindigkeit_minimum = 30,
        asteroiden_geschwindigkeit_maximum = 100,
        asteroiden_dreh_geschwindigkeit_maximum = 300,
        aliens_anzahl = 0
    ):
        super().__init__(
            asteroiden_anzahl,
            asteroiden_groesse,
            asteroiden_geschwindigkeit_minimum,
            asteroiden_geschwindigkeit_maximum,
            asteroiden_dreh_geschwindigkeit_maximum,
            aliens_anzahl
        ) # Aufruf Basis Klassen Konstruktor Funktion
        
        self.erzeugungs_rate = erzeugungs_rate
        self.letzter_erzeugter_zeitstempel = get_ticks()
    
    def erzeuge_asteroiden(self, oberflaeche, bild_asteroid, anzahl):
        # Asteroiden Liste
        asteroiden = []
        for i in range(anzahl):
            position = zufaellige_position(oberflaeche, True)
            asteroiden.append(
                Asteroid(
                    position,
                    bild_asteroid,
                    self.asteroiden_groesse,
                    self.asteroiden_geschwindigkeit_minimum,
                    self.asteroiden_geschwindigkeit_maximum,
                    self.asteroiden_dreh_geschwindigkeit_maximum
                )
            )
        return asteroiden
    
    def erzeuge_alien(self, oberflaeche, bild_laser, ton_laser):                     # Nur Raumschiff hat diese Mitglied Funktion
        # Laser Liste
        if get_ticks() - self.letzter_erzeugter_zeitstempel > self.erzeugungs_rate:
            self.letzter_erzeugter_zeitstempel = get_ticks()
            # Finde eine zufällige Position für das Alien
            position = zufaellige_position(oberflaeche, True)
            # Füge Asteroid zur Liste hinzu
            return AlienRaumschiff(position, bild_laser, ton_laser)
        # Leere Liste
        else:
            return None
