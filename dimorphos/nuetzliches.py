import os
import random
from pygame.image import load
from pygame import Color
from pygame.math import Vector2

def lade_bild(datei_name, mit_transparenz=True):
    datei_pfad = os.path.dirname(__file__) + f'\\bilder\\{datei_name}.png'
    geladenes_bild = load(datei_pfad)
    if mit_transparenz:
        return geladenes_bild.convert_alpha()
    else:
        return geladenes_bild.convert()

def zyklische_position(position, oberflaeche):
    x, y = position
    pixel_waagerecht, pixel_senkrecht = oberflaeche.get_size()
    return Vector2(x % pixel_waagerecht, y % pixel_senkrecht)   # Modulo Operator % ist der Divisionsrest

def zufaellige_position(oberflaeche):
    return Vector2(
        random.randrange(oberflaeche.get_width()),
        random.randrange(oberflaeche.get_height()),
    )

def zufaellige_geschwindigkeit(min_geschwindigkeit, max_geschwindigkeit):
    geschwindigkeit = random.uniform(min_geschwindigkeit, max_geschwindigkeit)
    winkel = random.uniform(0, 360)
    return Vector2(geschwindigkeit, 0).rotate(winkel)

def zeige_text(oberflaeche, text, schrift, farbe=Color("tomato"), position=Vector2(0,0)):
    text_oberflaeche = schrift.render(text, True, farbe)
    rechteck = text_oberflaeche.get_rect()
    rechteck.center = position + Vector2(oberflaeche.get_size()) / 2
    oberflaeche.blit(text_oberflaeche, rechteck)
