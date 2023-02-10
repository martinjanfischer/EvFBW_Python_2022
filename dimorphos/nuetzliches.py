import os
import random
from pygame.image import load
from pygame import Color
from pygame.math import Vector2
from pygame.mixer import Sound

def lade_bild(datei_name, mit_transparenz=True):
    datei_pfad = os.path.dirname(__file__) + f'\\bilder\\{datei_name}.png'
    geladenes_bild = load(datei_pfad)
    if mit_transparenz:
        return geladenes_bild.convert_alpha()
    else:
        return geladenes_bild.convert()

def lade_ton(datei_name):
    datei_pfad = os.path.dirname(__file__) + f'\\ton\\{datei_name}.wav'
    geladener_ton = Sound(datei_pfad)
    return geladener_ton

def zyklische_position(position, oberflaeche):
    x, y = position
    pixel_waagerecht, pixel_senkrecht = oberflaeche.get_size()
    return Vector2(x % pixel_waagerecht, y % pixel_senkrecht)   # Modulo Operator % ist der Divisionsrest

def zufaellige_position(oberflaeche, am_rand):
    zufaellig_x = random.randrange(oberflaeche.get_width())
    zufaellig_y = random.randrange(oberflaeche.get_height())
    if not am_rand:
        return Vector2(zufaellig_x, zufaellig_y)
    else:
        return random.choice(
            [
                Vector2(zufaellig_x, 0), Vector2(zufaellig_x, oberflaeche.get_height() - 1),
                Vector2(0, zufaellig_y), Vector2(oberflaeche.get_width() - 1, zufaellig_y)
            ]
        )

def zufaellige_geschwindigkeit(min_geschwindigkeit, max_geschwindigkeit):
    geschwindigkeit = random.uniform(min_geschwindigkeit, max_geschwindigkeit)
    winkel = random.uniform(0, 360)
    return Vector2(geschwindigkeit, 0).rotate(winkel)

def zeige_text(oberflaeche, text, schrift, farbe=Color("tomato"), position=Vector2(0,0)):
    text_oberflaeche = schrift.render(text, True, farbe)
    rechteck = text_oberflaeche.get_rect()
    rechteck.center = position
    oberflaeche.blit(text_oberflaeche, rechteck)
