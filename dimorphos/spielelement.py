from pygame.math import Vector2

AUFWAERTS = Vector2(0, -1)

class SpielElement:
    def __init__(self, position, sprite, geschwindigkeit):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.geschwindigkeit = Vector2(geschwindigkeit)
    
    def zeichne(self, oberflaeche):
        pass
    
    def bewege(self, oberflaeche):
        pass
    
    def kollidiert(self, anderes_element):
        pass


class Raumschiff(SpielElement):
    def __init__(self, position, erzeuge_laser_rueckruf_funktion):
        pass
    
    def drehe(self, uhrzeigersinn=True):
        pass
    
    def zeichne(self, oberflaeche):
        pass
    
    def beschleunige(self):
        pass
    
    def schiesse(self):
        pass


class Asteroid(SpielElement):
    def __init__(self, position):
        pass


class Laser(SpielElement):
    def __init__(self, position, geschwindigkeit):
        pass
    
    def bewege(self, oberflaeche):
        pass
    
    def zeichne(self, oberflaeche):
        pass
