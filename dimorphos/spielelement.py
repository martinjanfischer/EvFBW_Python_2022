from pygame.locals import BLEND_ADD
from pygame.math import Vector2
from pygame.mixer import Sound
from pygame.time import get_ticks
from pygame.transform import rotozoom
from animiertebildsequenz import AnimierteBildSequenz
from nuetzliches import lade_bild, lade_ton, zufaellige_geschwindigkeit, zyklische_position

class SpielElement:
    """Diese Klasse ist eine Basis für Raumschiff, Asteroid, Laser und hat alle gemeinsamen Eigenschaften position, radius, geschwindigkeit, bild"""
    
    def __init__(self, position, bild, geschwindigkeit):    # Konstruktor Funktion: Bereite alle Mitglied Variablen und Ressourcen dieser Klasse vor
        self.position = Vector2(position)                   # Alle SpielElement Klassen haben ebenfalls diese Mitglied Variable: 2D Position
        self.geschwindigkeit = Vector2(geschwindigkeit)     # Alle SpielElement Klassen haben ebenfalls diese Mitglied Variable: 2D Geschwindigkeit
        self.bild = bild                                    # Alle SpielElement Klassen haben ebenfalls diese Mitglied Variable: Bild
        if bild is not None:
            self.radius = bild.get_width() / 2              # Alle SpielElement Klassen haben ebenfalls diese Mitglied Variable: Radius für Kollisionen
        else:
            self.radius = 1                                 # Alle SpielElement Klassen haben ebenfalls diese Mitglied Variable: Radius für Kollisionen
    
    def zeichne(self, oberflaeche, zeitschritt):            # Alle SpielElement Klassen haben ebenfalls diese Mitglied Funktion
        blit_position = self.position - Vector2(self.radius)
        oberflaeche.blit(self.bild, blit_position)
    
    def bewege(self, oberflaeche, zeitschritt):             # Alle SpielElement Klassen haben ebenfalls diese Mitglied Funktion
        schritt = self.geschwindigkeit * zeitschritt
        self.position = zyklische_position(self.position + schritt, oberflaeche)
    
    def kollidiert(self, anderes_element):                  # Alle SpielElement Klassen haben ebenfalls diese Mitglied Funktion
        if anderes_element:
            distanz = self.position.distance_to(anderes_element.position)
            return distanz < self.radius + anderes_element.radius
        else:
            return False


AUFWAERTS = Vector2(0, -1)  # Globale Variable

class Raumschiff(SpielElement):
    """Die Klasse Raumschiff ist ein SpielElement und hat andere Eigenschaften"""
    
    MANEUVRIERFAEHIGKEIT = 3
    BESCHLEUNIGUNG = 100
    SCHWARZ = (0, 0, 0)
    
    def __init__(self, position, raumschiff_bilddatei_name, positionen_laser):      # Konstruktor Funktion
        super().__init__(position, lade_bild(raumschiff_bilddatei_name), Vector2(0)) # Aufruf Basis Klassen Konstruktor Funktion
        
        # kopiere den originalen AUFWAERTS vector
        self.richtung = Vector2(AUFWAERTS)
        self.bild_antrieb = lade_bild("nachbrenner")
        self.beschleunigt = False
        
        # Positionslichter
        self.bild_positionslichter = lade_bild("positionslichter")
        self.positionslichter = AnimierteBildSequenz(self.bild_positionslichter, 8, 2, 64, 64)
        self.positionslichter.zyklisch = True
        
        # Laser
        self.schuss_periode = 200
        self.letzter_schuss_zeitstempel = get_ticks()
        self.positionen_laser = positionen_laser            # In Pixel Koordinaten
        self.ton_laser = lade_ton("laser")
        
        # Mündungsfeuer
        self.bild_muendungsfeuer = lade_bild("muendungsfeuer")
        self.zeichne_muendungsfeuer = False
    
    def zeichne(self, oberflaeche, zeitschritt):         # Verändere Mitglied Funktion der Klasse SpielElement
        # Raumschiff
        winkel = self.richtung.angle_to(AUFWAERTS)
        gedrehte_oberflaeche = rotozoom(self.bild, winkel, 1.0)
        gedrehte_oberflaeche_groesse = Vector2(gedrehte_oberflaeche.get_size())
        blit_position = self.position - gedrehte_oberflaeche_groesse * 0.5
        oberflaeche.blit(gedrehte_oberflaeche, blit_position)
        # Antrieb
        if self.beschleunigt == True:
            gedrehte_oberflaeche_antrieb = rotozoom(self.bild_antrieb, winkel, 1.0)
            gedrehte_oberflaeche_antrieb_groesse = Vector2(gedrehte_oberflaeche_antrieb.get_size())
            blit_position_antrieb = self.position - gedrehte_oberflaeche_antrieb_groesse * 0.5
            oberflaeche.blit(gedrehte_oberflaeche_antrieb, blit_position_antrieb, special_flags=BLEND_ADD)
            self.beschleunigt = False
        # Positionslichter
        self.positionslichter.zeichne_einzel_bild(oberflaeche, self.position, winkel, self.radius, 1, self.SCHWARZ, True)
        # Mündungsfeuer
        if self.zeichne_muendungsfeuer:
            self.zeichne_muendungsfeuer = False
            gedrehte_oberflaeche_muendungsfeuer = rotozoom(self.bild_muendungsfeuer, winkel, 1.0)
            gedrehte_oberflaeche_muendungsfeuer_groesse = Vector2(gedrehte_oberflaeche_muendungsfeuer.get_size())
            blit_position_muendungsfeuer = self.position - gedrehte_oberflaeche_muendungsfeuer_groesse * 0.5
            oberflaeche.blit(gedrehte_oberflaeche_muendungsfeuer, blit_position_muendungsfeuer, special_flags=BLEND_ADD)
    
    def bewege(self, oberflaeche, zeitschritt):                  # Verändere Mitglied Funktion der Klasse SpielElement
        super().bewege(oberflaeche, zeitschritt)                 # Aufruf Basis Klassen Funktion
        
        # Nächste Einzelbild Nummer
        self.positionslichter.naechste_einzel_bild_nummer(zeitschritt)
    
    def drehe(self, uhrzeigersinn=True):    # Nur Raumschiff hat diese Mitglied Funktion
        vorzeichen = 1 if uhrzeigersinn else -1
        winkel = self.MANEUVRIERFAEHIGKEIT * vorzeichen
        self.richtung.rotate_ip(winkel)
    
    def beschleunige(self, zeitschritt):    # Nur Raumschiff hat diese Mitglied Funktion
        self.geschwindigkeit += self.richtung * self.BESCHLEUNIGUNG * zeitschritt
        self.beschleunigt = True
    
    def schiesse(self):                     # Nur Raumschiff hat diese Mitglied Funktion
        # Laser Liste
        if get_ticks() - self.letzter_schuss_zeitstempel > self.schuss_periode:
            self.letzter_schuss_zeitstempel = get_ticks()
            self.zeichne_muendungsfeuer = True
            Sound.play(self.ton_laser)
            winkel = self.richtung.angle_to(AUFWAERTS)
            laser = []
            for position_laser in self.positionen_laser:
                laser.append(Laser(self.position + position_laser.rotate(-winkel), self.richtung, True))
            return laser
        # Leere Liste
        else:
            return []


class Asteroid(SpielElement):
    """Die Klasse Asteroid ist ein SpielElement und hat andere Eigenschaften"""
    
    def __init__(self, position,
        groesse=1,
        geschwindigkeit_minimum=30,
        geschwindigkeit_maximum=100,
        dreh_geschwindigkeit_maximum=300
        ):   # Konstruktor Funktion
        geschwindigkeit = zufaellige_geschwindigkeit(
            geschwindigkeit_minimum, geschwindigkeit_maximum)
        dreh_geschwindigkeit = zufaellige_geschwindigkeit(
            - dreh_geschwindigkeit_maximum, dreh_geschwindigkeit_maximum)
        self.dreh_geschwindigkeit = dreh_geschwindigkeit.x
        self.groesse = groesse
        self.winkel = 0
        super().__init__(position, lade_bild("asteroid"), geschwindigkeit)
    
    def bewege(self, oberflaeche, zeitschritt):          # Verändere Mitglied Funktion der Klasse SpielElement
        super().bewege(oberflaeche, zeitschritt)
        self.winkel += self.dreh_geschwindigkeit * zeitschritt
    
    def zeichne(self, oberflaeche, zeitschritt):         # Verändere Mitglied Funktion der Klasse SpielElement
        gedrehte_oberflaeche = rotozoom(self.bild, self.winkel, self.groesse)
        gedrehte_oberflaeche_groesse = Vector2(gedrehte_oberflaeche.get_size())
        blit_position = self.position - gedrehte_oberflaeche_groesse * 0.5
        oberflaeche.blit(gedrehte_oberflaeche, blit_position)


class Laser(SpielElement):
    """Die Klasse Laser ist ein SpielElement und hat andere Eigenschaften"""
    
    GESCHWINDIGKEIT = 500
    
    def __init__(self, position, richtung, von_spieler):  # Konstruktor Funktion
        super().__init__(position, lade_bild("laser"), richtung * self.GESCHWINDIGKEIT) # Aufruf Basis Klassen Konstruktor Funktion
        
        self.von_spieler = von_spieler
    
    def zeichne(self, oberflaeche, zeitschritt):    # Verändere Mitglied Funktion der Klasse SpielElement
        winkel = self.geschwindigkeit.angle_to(AUFWAERTS)
        gedrehte_oberflaeche = rotozoom(self.bild, winkel, 1.0)
        gedrehte_oberflaeche_groesse = Vector2(gedrehte_oberflaeche.get_size())
        blit_position = self.position - gedrehte_oberflaeche_groesse * 0.5
        oberflaeche.blit(gedrehte_oberflaeche, blit_position, special_flags=BLEND_ADD)
    
    def bewege(self, oberflaeche, zeitschritt):     # Verändere Mitglied Funktion der Klasse SpielElement
        schritt = self.geschwindigkeit * zeitschritt
        self.position = self.position + schritt


class Explosion(SpielElement):
    """Die Klasse Explosion ist ein SpielElement und hat andere Eigenschaften"""
    
    SCHWARZ = (0, 0, 0)
    
    def __init__(self, position, geschwindigkeit):  # Konstruktor Funktion
        super().__init__(position, lade_bild("explosion"), geschwindigkeit) # Aufruf Basis Klassen Konstruktor Funktion
        
        # Animierte Bild Sequenz einer Explosion
        self.explosion = AnimierteBildSequenz(self.bild, 5, 8, 64, 64)
        
        if self.bild is not None:
            self.radius = self.explosion.anzahl_pixel_horizontal / 2
        else:
            self.radius = 1
        
        self.ton_explosion = lade_ton("explosion")
    
    def zeichne(self, oberflaeche, zeitschritt):                 # Verändere Mitglied Funktion der Klasse SpielElement
        self.explosion.zeichne_einzel_bild(oberflaeche, self.position, 0, self.radius, 4, self.SCHWARZ, True)
    
    def bewege(self, oberflaeche, zeitschritt):                  # Verändere Mitglied Funktion der Klasse SpielElement
        super().bewege(oberflaeche, zeitschritt)                 # Aufruf Basis Klassen Funktion
        
        # Nächste Einzelbild Nummer
        self.explosion.naechste_einzel_bild_nummer(zeitschritt)


class AlienRaumschiff(SpielElement):
    """Die Klasse AlienRaumschiff ist ein SpielElement und hat andere Eigenschaften"""
    
    SCHWARZ = (0, 0, 0)
    
    def __init__(self, position):   # Konstruktor Funktion
        geschwindigkeit = zufaellige_geschwindigkeit(50, 100)
        super().__init__(position, lade_bild("raumschiff"), geschwindigkeit)
        
        # Positionslichter
        self.bild_positionslichter = lade_bild("positionslichter")
        self.positionslichter = AnimierteBildSequenz(self.bild_positionslichter, 8, 2, 64, 64)
        self.positionslichter.zyklisch = True
        
        # Laser
        self.schuss_periode = 2000
        self.letzter_schuss_zeitstempel = get_ticks()
        self.ton_laser = lade_ton("laser")
    
    def zeichne(self, oberflaeche, zeitschritt):         # Verändere Mitglied Funktion der Klasse SpielElement
        super().zeichne(oberflaeche, zeitschritt)                 # Aufruf Basis Klassen Funktion
        
        # Positionslichter
        self.positionslichter.zeichne_einzel_bild(oberflaeche, self.position, 0, self.radius, 1, self.SCHWARZ, True)
    
    def bewege(self, oberflaeche, zeitschritt):                  # Verändere Mitglied Funktion der Klasse SpielElement
        super().bewege(oberflaeche, zeitschritt)                 # Aufruf Basis Klassen Funktion
        
        # Nächste Einzelbild Nummer
        self.positionslichter.naechste_einzel_bild_nummer(zeitschritt)
    
    def schiesse(self, ziel_position):                     # Nur AlienRaumschiff hat diese Mitglied Funktion
        # Laser Liste
        if get_ticks() - self.letzter_schuss_zeitstempel > self.schuss_periode:
            self.letzter_schuss_zeitstempel = get_ticks()
            Sound.play(self.ton_laser)
            richtung = ziel_position - self.position
            laser = []
            laser.append(Laser(self.position, richtung.normalize(), False))
            return laser
        # Leere Liste
        else:
            return []
