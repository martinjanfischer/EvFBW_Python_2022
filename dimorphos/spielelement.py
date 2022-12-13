from pygame.math import Vector2

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
        return False


AUFWAERTS = Vector2(0, -1)  # Globale Variable

'''
Die Klasse Raumschiff ist ein SpielElement
und hat andere Eigenschaften 
'''
class Raumschiff(SpielElement):
    def __init__(self, position, erzeuge_laser_rueckruf_funktion):      # Konstruktor Funktion
        super().__init__(position, None, Vector2(0)) # Aufruf Basis Klassen Konstruktor Funktion
    
    def drehe(self, uhrzeigersinn=True):    # Nur Raumschiff hat diese Mitglied Funktion
        pass
    
    def beschleunige(self, zeitschritt):    # Nur Raumschiff hat diese Mitglied Funktion
        pass
    
    def schiesse(self):                     # Nur Raumschiff hat diese Mitglied Funktion
        pass


'''
Die Klasse Asteroid ist ein SpielElement
und hat andere Eigenschaften 
'''
class Asteroid(SpielElement):
    def __init__(self, position):   # Konstruktor Funktion
        super().__init__(position, None, Vector2(0, 0))


'''
Die Klasse Laser ist ein SpielElement
und hat andere Eigenschaften 
'''
class Laser(SpielElement):
    def __init__(self, position, geschwindigkeit):  # Konstruktor Funktion
        super().__init__(position, None, geschwindigkeit) # Aufruf Basis Klassen Konstruktor Funktion
