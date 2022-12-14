import pygame
from pygame.locals import BLEND_ADD
from pygame.math import Vector2

class AnimierteBildSequenz():
    zyklisch = False
    
    def __init__(self, animierte_bild_sequenz, anzahl_einzel_bilder, bilder_pro_sekunde, anzahl_pixel_horizontal, anzahl_pixel_vertikal):
        self.animierte_bild_sequenz = animierte_bild_sequenz
        self.anzahl_einzel_bilder = anzahl_einzel_bilder
        self.anzahl_pixel_horizontal = anzahl_pixel_horizontal
        self.anzahl_pixel_vertikal = anzahl_pixel_vertikal
        
        self.einzel_bilder = []
        for einzel_bild_nummer in range(self.anzahl_einzel_bilder):
            self.einzel_bilder.append(self.erstelle_einzel_bild(einzel_bild_nummer))
        
        self.reset()
        if bilder_pro_sekunde <= 0:
            bilder_pro_sekunde = 1
        self.zeitschritt_einzel_bild_schwelle = 1 / bilder_pro_sekunde
    
    def erstelle_einzel_bild(self, einzel_bild_nummer):
        einzel_bild = pygame.Surface((self.anzahl_pixel_horizontal, self.anzahl_pixel_vertikal)).convert_alpha()
        einzel_bild.blit(self.animierte_bild_sequenz, (0, 0), ((einzel_bild_nummer * self.anzahl_pixel_horizontal), 0, self.anzahl_pixel_horizontal, self.anzahl_pixel_vertikal))
        return einzel_bild
    
    def naechste_einzel_bild_nummer(self, zeitschritt):
        if (self.zeitschritt_einzel_bild <= self.zeitschritt_einzel_bild_schwelle):
            self.zeitschritt_einzel_bild += zeitschritt
        else:
            self.zeitschritt_einzel_bild = 0
            self.einzel_bild_nummer += 1
            if self.zyklisch:
                self.einzel_bild_nummer %= self.anzahl_einzel_bilder
            else:
                if self.einzel_bild_nummer >= self.anzahl_einzel_bilder:
                    self.einzel_bild_nummer = self.anzahl_einzel_bilder - 1
    
    def zeichne_einzel_bild(self, oberflaeche, position, winkel, radius, skalierung, farbe, additive_farbmischung):
        einzel_bild = self.einzel_bilder[self.einzel_bild_nummer]
        einzel_bild.set_colorkey(farbe)
        einzel_bild = pygame.transform.scale(einzel_bild, (self.anzahl_pixel_horizontal * skalierung, self.anzahl_pixel_vertikal * skalierung))
        einzel_bild = pygame.transform.rotozoom(einzel_bild, winkel, 1.0)
        blit_position = position - Vector2(einzel_bild.get_size()) * 0.5
        if additive_farbmischung:
            oberflaeche.blit(einzel_bild, blit_position, special_flags=BLEND_ADD)
        else:
            oberflaeche.blit(einzel_bild, blit_position)
    
    def beendet(self):
        if self.zyklisch:
            return False
        else:
            return self.einzel_bild_nummer < self.anzahl_einzel_bilder
    
    def reset(self):
        if not self.zyklisch:
            self.einzel_bild_nummer = 0
            self.zeitschritt_einzel_bild = 0
