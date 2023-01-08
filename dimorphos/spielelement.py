from pygame.locals import BLEND_ADD
from pygame.math import Vector2
from pygame.time import get_ticks
from pygame.transform import rotozoom
from animiertebildsequenz import AnimierteBildSequenz
from nuetzliches import lade_bild, lade_ton, zufaellige_geschwindigkeit, zyklische_position

'''
Diese Klasse ist eine Basis für 
Raumschiff, Asteroid, Laser 
und hat alle gemeinsamen Eigenschaften 
position, radius, geschwindigkeit, bild
'''
class SpielElement:
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
        distanz = self.position.distance_to(anderes_element.position)
        return distanz < self.radius + anderes_element.radius


AUFWAERTS = Vector2(0, -1)  # Globale Variable

'''
Die Klasse Raumschiff ist ein SpielElement
und hat andere Eigenschaften 
'''
class Raumschiff(SpielElement):
    MANEUVRIERFAEHIGKEIT = 3
    BESCHLEUNIGUNG = 100
    LASER_GESCHWINDIGKEIT = 500
    
    def __init__(self, position, erzeuge_laser_rueckruf_funktion):      # Konstruktor Funktion
        super().__init__(position, lade_bild("raumschiff"), Vector2(0)) # Aufruf Basis Klassen Konstruktor Funktion
        
        # kopiere den originalen AUFWAERTS vector
        self.richtung = Vector2(AUFWAERTS)
        self.bild_antrieb = lade_bild("nachbrenner")
        self.beschleunigt = False
        
        # Laser
        self.erzeuge_laser_rueckruf_funktion = erzeuge_laser_rueckruf_funktion
        self.schuss_periode = 200
        self.letzter_schuss_zeitstempel = get_ticks()
    
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
    
    def drehe(self, uhrzeigersinn=True):    # Nur Raumschiff hat diese Mitglied Funktion
        vorzeichen = 1 if uhrzeigersinn else -1
        winkel = self.MANEUVRIERFAEHIGKEIT * vorzeichen
        self.richtung.rotate_ip(winkel)
    
    def beschleunige(self, zeitschritt):    # Nur Raumschiff hat diese Mitglied Funktion
        self.geschwindigkeit += self.richtung * self.BESCHLEUNIGUNG * zeitschritt
        self.beschleunigt = True
    
    def schiesse(self):                     # Nur Raumschiff hat diese Mitglied Funktion
        if get_ticks() - self.letzter_schuss_zeitstempel > self.schuss_periode:
            self.letzter_schuss_zeitstempel = get_ticks()
            laser_geschwindigkeit = self.richtung * self.LASER_GESCHWINDIGKEIT #+ self.geschwindigkeit
            laser = Laser(self.position, laser_geschwindigkeit)
            self.erzeuge_laser_rueckruf_funktion(laser)


'''
Die Klasse Asteroid ist ein SpielElement
und hat andere Eigenschaften 
'''
class Asteroid(SpielElement):
    GESCHWINDIGKEIT_MINIMUM = 30
    GESCHWINDIGKEIT_MAXIMUM = 100
    DREH_GESCHWINDIGKEIT_MAXIMUM = 300
    
    def __init__(self, position, groesse=1):   # Konstruktor Funktion
        geschwindigkeit = zufaellige_geschwindigkeit(
            self.GESCHWINDIGKEIT_MINIMUM, self.GESCHWINDIGKEIT_MAXIMUM)
        dreh_geschwindigkeit = zufaellige_geschwindigkeit(
            - self.DREH_GESCHWINDIGKEIT_MAXIMUM, self.DREH_GESCHWINDIGKEIT_MAXIMUM)
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


'''
Die Klasse Laser ist ein SpielElement
und hat andere Eigenschaften 
'''
class Laser(SpielElement):
    def __init__(self, position, geschwindigkeit):  # Konstruktor Funktion
        super().__init__(position, lade_bild("laser"), geschwindigkeit) # Aufruf Basis Klassen Konstruktor Funktion
    
    def zeichne(self, oberflaeche, zeitschritt):    # Verändere Mitglied Funktion der Klasse SpielElement
        winkel = self.geschwindigkeit.angle_to(AUFWAERTS)
        gedrehte_oberflaeche = rotozoom(self.bild, winkel, 1.0)
        gedrehte_oberflaeche_groesse = Vector2(gedrehte_oberflaeche.get_size())
        blit_position = self.position - gedrehte_oberflaeche_groesse * 0.5
        oberflaeche.blit(gedrehte_oberflaeche, blit_position, special_flags=BLEND_ADD)
    
    def bewege(self, oberflaeche, zeitschritt):     # Verändere Mitglied Funktion der Klasse SpielElement
        schritt = self.geschwindigkeit * zeitschritt
        self.position = self.position + schritt


'''
Die Klasse Explosion ist ein SpielElement
und hat andere Eigenschaften 
'''
class Explosion(SpielElement):
    BLACK = (0, 0, 0)
    
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
        self.explosion.zeichne_einzel_bild(oberflaeche, self.position, self.radius, 4, self.BLACK, True)
    
    def bewege(self, oberflaeche, zeitschritt):                  # Verändere Mitglied Funktion der Klasse SpielElement
        super().bewege(oberflaeche, zeitschritt)                 # Aufruf Basis Klassen Funktion
        
        # Nächste Einzelbild Nummer
        self.explosion.naechste_einzel_bild_nummer(zeitschritt)
