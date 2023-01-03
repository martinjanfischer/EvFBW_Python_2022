import pygame

class AnimierteBildSequenz():
	def __init__(self, animierte_bild_sequenz):
		self.animierte_bild_sequenz = animierte_bild_sequenz

	def einzel_bild(self, einzel_bild_nummer, anzahl_pixel_horizontal, anzahl_pixel_vertikal, skalierung, farbe):
		einzel_bild = pygame.Surface((anzahl_pixel_horizontal, anzahl_pixel_vertikal)).convert_alpha()
		einzel_bild.blit(self.animierte_bild_sequenz, (0, 0), ((einzel_bild_nummer * anzahl_pixel_horizontal), 0, anzahl_pixel_horizontal, anzahl_pixel_vertikal))
		einzel_bild = pygame.transform.scale(einzel_bild, (anzahl_pixel_horizontal * skalierung, anzahl_pixel_vertikal * skalierung))
		einzel_bild.set_colorkey(farbe)
		return einzel_bild