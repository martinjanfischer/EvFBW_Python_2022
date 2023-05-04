import random
from pygame.mixer import Sound
from nuetzliches import zufaellige_position
from spielelement import Asteroid, Banana_Alien, Explosion

class Level:
    MIN_ASTEROIDEN_DISTANZ = 250
    
    def __init__(self):
        # Leere Asteroiden Liste
        self.asteroiden = []
        self.anzahl_asteroiden = 6
        
        # Weltraum
        self.hintergrund = None#lade_bild("hintergrund.magenta", False)
        
        # Leere Laser Liste
        self.laser = []
        
        # Kein Raumschiff
        self.raumschiff = None
        
        # Leere Asteroiden Liste
        self.bilder_asteroiden = []
        
        # Leere Explosionen Liste
        self.bild_explosion = None
        self.ton_explosion = None
        self.explosionen = []
        
        # Alien
        self.bild_Banana_alien = None
        self.bild_Laser = None
    
    def initialisiere_spiel_elemente(self, leinwand, raumschiff):
        # Kein Raumschiff
        self.raumschiff = raumschiff
        
        # Leere Laser Liste
        self.laser = []
        
        # Leere Explosionen Liste
        self.explosionen = []
        
        # Alien
        position = zufaellige_position(leinwand, True)
        self.alien=Banana_Alien(position, self.bild_Banana_alien,self.bild_Laser)
        
        # Leere Asteroiden Liste
        self.asteroiden = []
        
        # Neue Asteroiden mit zufälliger Platzierung und Geschwindigkeit
        for _ in range(self.anzahl_asteroiden):
            # Finde eine zufällige Position für den Asteroiden
            # mit einem gewissen Abstand zum Raumschiff
            while True:
                position = zufaellige_position(leinwand, False)
                distanz = position.distance_to(self.raumschiff.position)
                if (distanz > self.MIN_ASTEROIDEN_DISTANZ):
                    break
            # Füge Asteroid zur Liste hinzu
            bild_asteroid = self.bilder_asteroiden[random.randrange(len(self.bilder_asteroiden))]
            self.asteroiden.append(Asteroid(position, bild_asteroid))
    
    def hole_spiel_elemente(self):
        # Liste mit allen Spiel Elementen
        spiel_elemente = [*self.asteroiden]
        if self.alien:
            spiel_elemente.append(self.alien)
        if self.raumschiff:
            spiel_elemente.append(self.raumschiff)
        spiel_elemente.extend([*self.laser, *self.explosionen])
        return spiel_elemente
    
    def behandle_spiele_logik(self, score, leinwand, zeitschritt):
        score = 0
        
        # Bewege alle SpielElemente pro Bild ein wenig weiter
        for spielelement in self.hole_spiel_elemente():
            spielelement.bewege(leinwand, zeitschritt)
        
        # Treffer: Laser auf Asteroid, entferne beide
        for laser in self.laser[:]:
            for asteroid in self.asteroiden[:]:
                if asteroid.kollidiert(laser):
                    # Entferne Laser und Asteroid
                    self.asteroiden.remove(asteroid)
                    self.laser.remove(laser)
                    
                    # Punkte
                    score += 1
                    break
        
        # Treffer: Laser auf Banana_alien entferne beide
        for laser in self.laser[:]:
            if self.alien and self.alien.kollidiert(laser):
                # Entferne Laser und Asteroid
                self.alien= None
                self.laser.remove(laser)
                
                # Punkte
                score += 1
                break
        
        # Entferne Laser am Bildrand
        for laser in self.laser[:]:
            if not leinwand.get_rect().collidepoint(laser.position):
                self.laser.remove(laser)
        
        # Kollision: Raumschiff mit Asteroid, entferne Raumschiff
        if self.raumschiff:
            for asteroid in self.asteroiden:
                if asteroid.kollidiert(self.raumschiff):
                    # Explosion
                    position = self.raumschiff.position
                    geschwindigkeit = 0.5 * self.raumschiff.geschwindigkeit + 0.5 * asteroid.geschwindigkeit
                    self.explosion(position, geschwindigkeit)
                    
                    # Entferne Raumschiff
                    self.raumschiff = None
                    break
        
        # banana alien schießt: Laser trifft Raumschiff, entferne Raumschiff
        if self.alien and self.raumschiff:
             laser = self.alien.schiesse()
             # Füge Laser in Liste hinzu
             self.laser.extend(laser)
        
        return score
    
    def zeichne_spiele_elemente(self, leinwand, zeitschritt): # Öffentliche Mitglied Funktion für das Zeichnen
        # Zeichne Hintergrundbild neu
        leinwand.blit(self.hintergrund, (0, 0))
        
        # Zeichne alle SpielElemente in diesem Bild
        for spielelement in self.hole_spiel_elemente():
            spielelement.zeichne(leinwand, zeitschritt)
    
    def gewonnen(self):
        # Du Gewinnst wenn das Raumschiff noch existiert und der Text anzeigt dass Du gewonnen hast
        # Du Verlierst wenn das Raumschiff nicht existiert oder der Text nicht anzeigt dass Du gewonnen hast
        return (self.raumschiff and not self.asteroiden)
    
    def verloren(self):
        return (not self.raumschiff)
    
    def explosion(self, position, geschwindigkeit):
        # Finde in der Explosionen Liste eine unbenutzte Explosion
        explosion = None
        for i, e in enumerate(self.explosionen):
            if e.explosion.beendet():
                e.explosion.reset()
                e.position = position
                e.geschwindigkeit = geschwindigkeit
                explosion = e
                break
        # Erzeuge eine neue Explosion wenn es keine unbenutzte Explosion gibt
        if not explosion:
            explosion = Explosion(position, geschwindigkeit, self.bild_explosion, self.ton_explosion)
            self.explosionen.append(explosion)
        # Spiele den Ton für die Explosion ab wenn Du eine Explosion hast
        if explosion:
            Sound.play(explosion.ton_explosion)

class EndlosLevel(Level):
    def __init__(self):
        super().__init__() # Aufruf Basis Klassen Konstruktor Funktion
    
    def _erzeuge_asteroiden(self, oberflaeche, bild_asteroid, anzahl):
        asteroiden = []
        for i in range(anzahl):
            position = zufaellige_position(oberflaeche, True)
            asteroiden.append(Asteroid(position, bild_asteroid, 2))
        return asteroiden

    # Behandle spiele logik
    def behandle_spiele_logik(self, score, leinwand, zeitschritt):
        newscore = super().behandle_spiele_logik(score, leinwand, zeitschritt) # Aufruf Basis Klassen Funktion
        
        if score % 2 == 1 and self.asteroiden and len(self.asteroiden) < self.anzahl_asteroiden:
            bild_asteroid = self.bilder_asteroiden[random.randrange(len(self.bilder_asteroiden))]
            neue_asteroiden = self._erzeuge_asteroiden(leinwand, bild_asteroid, 3)
            self.asteroiden.extend(neue_asteroiden)
        
        self.anzahl_asteroiden = len(self.asteroiden)
        
        return newscore
