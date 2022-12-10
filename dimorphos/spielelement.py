from pygame.math import Vector2
from nuetzliches import lade_bild, zufaellige_geschwindigkeit, zyklische_position

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
    
    def zeichne(self, oberflaeche):             # Alle SpielElement Klassen haben ebenfalls diese Mitglied Funktion
        pass
    
    def bewege(self, oberflaeche, zeitschritt): # Alle SpielElement Klassen haben ebenfalls diese Mitglied Funktion
        pass
    
    def kollidiert(self, anderes_element):      # Alle SpielElement Klassen haben ebenfalls diese Mitglied Funktion
        pass


AUFWAERTS = Vector2(0, -1)  # Globale Variable

'''
Die Klasse Raumschiff ist ein SpielElement
und hat andere Eigenschaften 
'''
class Raumschiff(SpielElement):
    def __init__(self, position, erzeuge_laser_rueckruf_funktion):      # Konstruktor Funktion
        super().__init__(position, lade_bild("raumschiff"), Vector2(0)) # Aufruf Basis Klassen Konstruktor Funktion
        # kopiere den originalen AUFWAERTS vector
        self.richtung = Vector2(AUFWAERTS)
        self.erzeuge_laser_rueckruf_funktion = erzeuge_laser_rueckruf_funktion
        self.bild_antrieb = lade_bild("laser")
        self.beschleunigt = False
        self.schuss_periode = 200
        self.letzter_schuss_zeitstempel = get_ticks()
        pass
    
    def zeichne(self, oberflaeche):         # Verändere Mitglied Funktion der Klasse SpielElement
        pass
    
    def drehe(self, uhrzeigersinn=True):    # Nur Raumschiff hat diese Mitglied Funktion
        pass
    
    def beschleunige(self):                 # Nur Raumschiff hat diese Mitglied Funktion
        pass
    
    def schiesse(self):                     # Nur Raumschiff hat diese Mitglied Funktion
        pass


'''
Die Klasse Asteroid ist ein SpielElement
und hat andere Eigenschaften 
'''
class Asteroid(SpielElement):
    def __init__(self, position):   # Konstruktor Funktion
        super().__init__(position, lade_bild("asteroid"), zufaellige_geschwindigkeit(1, 3)) # Aufruf Basis Klassen Konstruktor Funktion


'''
Die Klasse Laser ist ein SpielElement
und hat andere Eigenschaften 
'''
class Laser(SpielElement):
    def __init__(self, position, geschwindigkeit):  # Konstruktor Funktion
        super().__init__(position, lade_bild("laser"), geschwindigkeit) # Aufruf Basis Klassen Konstruktor Funktion
    
    def zeichne(self, oberflaeche):                 # Verändere Mitglied Funktion der Klasse SpielElement
        pass
    
    def bewege(self, oberflaeche, zeitschritt):     # Verändere Mitglied Funktion der Klasse SpielElement
        pass
