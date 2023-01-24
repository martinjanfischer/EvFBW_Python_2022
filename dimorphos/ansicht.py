import pygame
import random
from pygame.math import Vector2
from pygame.mixer import Sound
from spielelement import SpielElement, Asteroid, Explosion
from nuetzliches import lade_bild, zufaellige_position, zeige_text

class Ansicht:
    def __init__(self):
        self.leinwand = pygame.display.set_mode((1280, 720)) # Anzahl Bildpunkte/Pixel waagerecht und senkrecht
    
    def initialisiere_spiel_elemente(self):
        pass
    
    def behandle_eingaben(self, zeitschritt):      # Öffentliche Mitglied Funktion für Eingabebehandlung
        pass
    
    def behandle_spiele_logik(self, zeitschritt):  # Öffentliche Mitglied Funktion für Spielelogik
        pass
    
    def zeichne_spiele_elemente(self, zeitschritt): # Öffentliche Mitglied Funktion für das Zeichnen
        pass

AUFWAERTS = Vector2(0, -1)  # Globale Variable

class StartAnsicht(Ansicht):
    def __init__(self):
        super().__init__() # Aufruf Basis Klassen Konstruktor Funktion
        
        # Text
        self.spiel_titel_schrift = pygame.font.Font(None, 64)
        self.spiel_titel_text = "DIMORPHOS"
        self.spiel_titel_farbe = pygame.Color(255, 255, 255, 255)
        
        self.spiel_start_schrift = pygame.font.Font(None, 32)
        self.spiel_start_text = "Drücke Enter zum Start oder ESC zum Verlassen"
        self.spiel_start_farbe = pygame.Color(0, 255, 0, 255)
        
        # Weltraum
        self.hintergrund = lade_bild("weltraum", False)
        
        # Raumschiffe
        self.ausgewaehltes_raumschiff = 0
        self.raumschiffe = []
        
        # Asteroiden
        self.asteroiden = []
        self.anzahl_asteroiden = 6
    
    def initialisiere_spiel_elemente(self):
        # Raumschiffe
        self._positioniere_raumschiffe()
        
        # Asteroiden
        self.asteroiden = []
        self.anzahl_asteroiden = 6
        for _ in range(self.anzahl_asteroiden):
            position = zufaellige_position(self.leinwand)
            self.asteroiden.append(Asteroid(position, random.uniform(.5, 5)))
    
    def _hole_spiel_elemente(self):
        if self.asteroiden and self.raumschiffe:
            spiel_elemente = [*self.asteroiden, *self.raumschiffe]
            return spiel_elemente
        else:
            return []
    
    def behandle_eingabe_ereignis(self, event, zeitschritt):      # Öffentliche Mitglied Funktion für Eingabebehandlung
        # Raumschiff wählen
        if event.type == pygame.KEYUP:
            # Raumschiff wählen
            if (event.key == pygame.K_RIGHT):
                if self.ausgewaehltes_raumschiff < len(self.raumschiffe) - 1:
                    self.ausgewaehltes_raumschiff += 1
                    self._positioniere_raumschiffe()
            elif (event.key == pygame.K_LEFT):
                if self.ausgewaehltes_raumschiff > 0:
                    self.ausgewaehltes_raumschiff -= 1
                    self._positioniere_raumschiffe()
        
    def behandle_eingaben(self, zeitschritt):      # Öffentliche Mitglied Funktion für Eingabebehandlung
        pass
    
    def behandle_spiele_logik(self, zeitschritt):  # Öffentliche Mitglied Funktion für Spielelogik
        # Bewege alle SpielElemente pro Bild ein wenig weiter
        for spielelement in self._hole_spiel_elemente():
            spielelement.bewege(self.leinwand, zeitschritt)
    
    def zeichne_spiele_elemente(self, zeitschritt): # Öffentliche Mitglied Funktion für das Zeichnen
        # Zeichne Hintergrundbild neu
        self.leinwand.blit(self.hintergrund, (0, 0))
        
        # Zeichne alle SpielElemente in diesem Bild
        for spielelement in self._hole_spiel_elemente():
            spielelement.zeichne(self.leinwand, zeitschritt)
        
        # Zeichne Text
        zeige_text(self.leinwand, self.spiel_titel_text, self.spiel_titel_schrift, self.spiel_titel_farbe)
        position = Vector2(0, self.leinwand.get_height() * 1/4)
        zeige_text(self.leinwand, self.spiel_start_text, self.spiel_start_schrift, self.spiel_start_farbe, position)
    
    def kann_ansicht_wechseln(self):
        return True
    
    def _positioniere_raumschiffe(self):
        pixel_waagerecht, pixel_senkrecht = self.leinwand.get_size()
        for i in range(0, len(self.raumschiffe)):
            self.raumschiffe[i].position = Vector2(
                (0.5 + (i - self.ausgewaehltes_raumschiff) * 0.1) * pixel_waagerecht,
                0.6 * pixel_senkrecht
                )
            self.raumschiffe[i].geschwindigkeit = Vector2(0, 0)
            self.raumschiffe[i].richtung = Vector2(AUFWAERTS)

class LevelAnsicht(Ansicht):
    MIN_ASTEROIDEN_DISTANZ = 250
    SPIEL_VORBEI_GEWONNEN = "Gewonnen!"
    SPIEL_VORBEI_VERLOREN = "Verloren!"
    
    def __init__(self):
        super().__init__() # Aufruf Basis Klassen Konstruktor Funktion
        
        # Text
        self.spiel_vorbei_schrift = pygame.font.Font(None, 64)
        self.spiel_vorbei_text = ""
        self.spiel_vorbei_farbe = pygame.Color(255, 255, 255, 255)
        
        # Weltraum
        self.hintergrund = lade_bild("weltraum", False)
        
        # Laser
        self.laser = []
        
        # Raumschiff
        self.raumschiff = None
        
        # Asteroiden
        self.asteroiden = []
        self.anzahl_asteroiden = 6
        
        # Explosionen
        self.explosionen = []
        
        # Text
        self.spiel_vorbei_text = ""
    
    def initialisiere_spiel_elemente(self):
        # Laser
        self.laser = []
        
        # Asteroiden
        self.asteroiden = []
        for _ in range(self.anzahl_asteroiden):
            while True:
                position = zufaellige_position(self.leinwand)
                distanz = position.distance_to(self.raumschiff.position)
                if (distanz > self.MIN_ASTEROIDEN_DISTANZ):
                    break
            self.asteroiden.append(Asteroid(position))
        
        # Explosionen
        self.explosionen = []
        
        # Text
        self.spiel_vorbei_text = ""
    
    def _hole_spiel_elemente(self):
        spiel_elemente = [*self.asteroiden, *self.laser, *self.explosionen]
        if self.raumschiff:
            spiel_elemente.append(self.raumschiff)
        return spiel_elemente

    def behandle_eingabe_ereignis(self, event, zeitschritt):      # Öffentliche Mitglied Funktion für Eingabebehandlung
        pass
    
    def behandle_eingaben(self, zeitschritt):      # Öffentliche Mitglied Funktion für Eingabebehandlung
        # Hole Tastatur Eingaben
        wurde_taste_gedrueckt = pygame.key.get_pressed()
        
        # Raumschiff Steuerung
        if self.raumschiff:
            if wurde_taste_gedrueckt[pygame.K_RIGHT]:
                self.raumschiff.drehe(uhrzeigersinn=True)
            elif wurde_taste_gedrueckt[pygame.K_LEFT]:
                self.raumschiff.drehe(uhrzeigersinn=False)
            if wurde_taste_gedrueckt[pygame.K_UP]:
                self.raumschiff.beschleunige(zeitschritt)
            if wurde_taste_gedrueckt[pygame.K_SPACE]:
                laser = self.raumschiff.schiesse()
                if laser:
                    self.laser.append(laser)
    
    def behandle_spiele_logik(self, zeitschritt):  # Öffentliche Mitglied Funktion für Spielelogik
        # Bewege alle SpielElemente pro Bild ein wenig weiter
        for spielelement in self._hole_spiel_elemente():
            spielelement.bewege(self.leinwand, zeitschritt)
        
        # Treffer: Laser auf Asteroid, entferne beide
        for laser in self.laser[:]:
            for asteroid in self.asteroiden[:]:
                if asteroid.kollidiert(laser):
                    self.asteroiden.remove(asteroid)
                    self.laser.remove(laser)
                    break
        
        # Entferne Laser am Bildrand
        for laser in self.laser[:]:
            if not self.leinwand.get_rect().collidepoint(laser.position):
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
                    self.spiel_vorbei_text = self.SPIEL_VORBEI_VERLOREN
                    self.spiel_vorbei_farbe = pygame.Color("tomato")
                    break
        
        # Gewonnen: Keine Asteroiden übrig
        if not self.asteroiden and self.raumschiff:
            self.spiel_vorbei_text = self.SPIEL_VORBEI_GEWONNEN
            self.spiel_vorbei_farbe = pygame.Color("gold")
    
    def zeichne_spiele_elemente(self, zeitschritt): # Öffentliche Mitglied Funktion für das Zeichnen
        # Zeichne Hintergrundbild neu
        self.leinwand.blit(self.hintergrund, (0, 0))
        
        # Zeichne alle SpielElemente in diesem Bild
        for spielelement in self._hole_spiel_elemente():
            spielelement.zeichne(self.leinwand, zeitschritt)
        
        # Zeichne Text
        if self.spiel_vorbei_text:
            zeige_text(self.leinwand, self.spiel_vorbei_text, self.spiel_vorbei_schrift, self.spiel_vorbei_farbe)
    
    def level_gewonnen(self):
        return (self.raumschiff and self.spiel_vorbei_text == self.SPIEL_VORBEI_GEWONNEN)
    
    def explosion(self, position, geschwindigkeit):
        explosion = None
        for i, e in enumerate(self.explosionen):
            if e.explosion.beendet():
                e.explosion.reset()
                e.position = position
                e.geschwindigkeit = geschwindigkeit
                explosion = e
                break
        if not explosion:
            explosion = Explosion(position, geschwindigkeit)
            self.explosionen.append(explosion)
        if explosion:
            Sound.play(explosion.ton_explosion)

