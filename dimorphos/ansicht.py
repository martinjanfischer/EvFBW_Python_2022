import pygame
import random
from pygame.math import Vector2
from spielelement import SpielElement, Asteroid, Explosion, Banana_Alien
from nuetzliches import lade_bild, lade_ton, zufaellige_position, zeige_text

class Ansicht:
    """Diese Klasse ist eine Basis für StartAnsicht und LevelAnsicht und hat alle gemeinsamen Eigenschaften leinwand"""
    
    def __init__(self):
        self.leinwand = pygame.display.set_mode((1280, 720)) # Anzahl Bildpunkte/Pixel waagerecht und senkrecht
    
    def initialisiere_spiel_elemente(self):         # Öffentliche Mitglied Funktion für Vorbereitung
        pass
    
    def behandle_eingaben(self, zeitschritt):       # Öffentliche Mitglied Funktion für Eingabebehandlung
        pass
    
    def behandle_spiele_logik(self, zeitschritt):   # Öffentliche Mitglied Funktion für Spielelogik
        pass
    
    def zeichne_spiele_elemente(self, zeitschritt): # Öffentliche Mitglied Funktion für das Zeichnen
        pass


class StartAnsicht(Ansicht):
    """Die Klasse StartAnsicht ist eine Ansicht und hat andere Eigenschaften"""
    
    AUFWAERTS = Vector2(0, -1)
    
    def __init__(self, highscore):
        super().__init__() # Aufruf Basis Klassen Konstruktor Funktion
        
        # Text
        self.spiel_titel_schrift = pygame.font.Font(None, 64)
        self.spiel_titel_text = "DIMORPHOS"
        self.spiel_titel_farbe = pygame.Color(255, 255, 255, 255)
        
        self.spiel_start_schrift = pygame.font.Font(None, 32)
        self.spiel_start_text = "Drücke Enter zum Start oder ESC zum Verlassen"
        self.spiel_start_farbe = pygame.Color(0, 255, 0, 255)
        
        self.spiel_level_schrift = pygame.font.Font(None, 48)
        self.spiel_level_farbe = pygame.Color(255, 255, 0, 255)
        
        self.spiel_highscore_schrift = pygame.font.Font(None, 32)
        self.spiel_highscore_farbe = pygame.Color('tomato')
        
        self.highscore = highscore
        
        # Weltraum
        self.hintergrund = None
        
        # Leere Raumschiff Liste
        self.ausgewaehltes_raumschiff = 0
        self.raumschiffe = []
        
        # Leere Asteroiden Liste
        self.bilder_asteroiden = []
        self.asteroiden = []
        self.anzahl_asteroiden = 6
        
        # Leeres Level Wörterbuch
        self.level = {}
        self.level_zyklisch = None
        self.ausgewaehltes_level = None
    
    def initialisiere_spiel_elemente(self):
        # Raumschiffe
        self._positioniere_raumschiffe()
        
        # Neue Asteroiden mit zufälliger Platzierung und Geschwindigkeit
        self.asteroiden = []
        for _ in range(self.anzahl_asteroiden):
            # Finde eine zufällige Position für den Asteroiden
            position = zufaellige_position(self.leinwand, False)
            # Füge Asteroid zur Liste hinzu
            bild_asteroid = self.bilder_asteroiden[random.randrange(len(self.bilder_asteroiden))]
            self.asteroiden.append(Asteroid(position, bild_asteroid, random.uniform(.5, 5)))
    
    def _hole_spiel_elemente(self):
        # Liste mit allen Spiel Elementen
        if self.asteroiden and self.raumschiffe:
            spiel_elemente = [*self.asteroiden, *self.raumschiffe]
            return spiel_elemente
        # Leere Liste
        else:
            return []
    
    def behandle_eingabe_ereignis(self, event, zeitschritt):      # Öffentliche Mitglied Funktion für Eingabebehandlung
        # Raumschiff wählen
        if event.type == pygame.KEYUP:
            # Bewege Raumschiffe nach Links wenn die Rechte Pfeiltaste gedrückt wurde
            if (event.key == pygame.K_RIGHT):
                if self.ausgewaehltes_raumschiff < len(self.raumschiffe) - 1:
                    self.ausgewaehltes_raumschiff += 1
                    self._positioniere_raumschiffe()
            # Bewege Raumschiffe nach Rechts wenn die Linke Pfeiltaste gedrückt wurde
            elif (event.key == pygame.K_LEFT):
                if self.ausgewaehltes_raumschiff > 0:
                    self.ausgewaehltes_raumschiff -= 1
                    self._positioniere_raumschiffe()
            # Wechsele Level wenn die Pfeiltaste Rauf oder Runter gedrückt wurde
            if (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
                if self.level and self.level_zyklisch:
                    self.ausgewaehltes_level = next(self.level_zyklisch)
        
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
        
        # Auswahlrechteck
        ausgewaehltes_raumschiff = self.raumschiffe[self.ausgewaehltes_raumschiff]
        rechteck = ausgewaehltes_raumschiff.bild.get_rect()
        rechteck.center = ausgewaehltes_raumschiff.position
        pygame.draw.rect(self.leinwand, pygame.Color("tomato"), rechteck,  2)
        
        # Zeichne Titel Text
        position = Vector2(self.leinwand.get_size()) / 2
        position.y *= 3/4
        zeige_text(self.leinwand, self.spiel_titel_text, self.spiel_titel_schrift, self.spiel_titel_farbe, position)
        position = Vector2(0, self.leinwand.get_height() * 1/4) + Vector2(self.leinwand.get_size()) / 2
        zeige_text(self.leinwand, self.spiel_start_text, self.spiel_start_schrift, self.spiel_start_farbe, position)
        
        # Sortiere nach Punkten
        scores = list(self.highscore.keys())
        scores.sort(reverse=True)
        highscore = {i: self.highscore[i] for i in scores}
        
        # Zeige Highscore mit zehn Einträgen
        position = Vector2(self.leinwand.get_size())
        position.x *= 1/ 8
        position.y *= 1/ 16
        zeige_text(self.leinwand, 'Top Ten Highscore', self.spiel_level_schrift, self.spiel_highscore_farbe, position)
        position.y += 32
        for index, (score, name) in enumerate(highscore.items()):
            text = name + " " + str(score)
            zeige_text(self.leinwand, text, self.spiel_highscore_schrift, self.spiel_highscore_farbe, position)
            position.y += 24
            if index >= 9:
                break
        
        # Zeichne Level Text
        position = Vector2(self.leinwand.get_size()) / 2
        zeige_text(self.leinwand, self.ausgewaehltes_level, self.spiel_level_schrift, self.spiel_level_farbe, position)
    
    def kann_ansicht_wechseln(self):
        return True
    
    def _positioniere_raumschiffe(self):
        # Anzahl Raumschiffe minus Nummer des Aktuell Ausgewählten Raumschiffes
        # gibt die Verschiebungsrichtung vor
        pixel_waagerecht, pixel_senkrecht = self.leinwand.get_size()
        for i in range(0, len(self.raumschiffe)):
            self.raumschiffe[i].position = Vector2(
                (0.5 + (i - self.ausgewaehltes_raumschiff) * 0.1) * pixel_waagerecht,
                0.6 * pixel_senkrecht
                )
            self.raumschiffe[i].geschwindigkeit = Vector2(0, 0)
            self.raumschiffe[i].richtung = Vector2(self.AUFWAERTS)


class LevelAnsicht(Ansicht):
    """Die Klasse LevelAnsicht ist eine Ansicht und hat andere Eigenschaften"""
    
    SPIEL_VORBEI_GEWONNEN = "Gewonnen!"
    SPIEL_VORBEI_VERLOREN = "Verloren!"
    
    def __init__(self):
        super().__init__() # Aufruf Basis Klassen Konstruktor Funktion

        # spielpunkte
        self.score = 0
        
        # Text
        self.spiel_vorbei_schrift = pygame.font.Font(None, 64)
        self.spiel_vorbei_text = ""
        self.spiel_vorbei_farbe = pygame.Color(255, 255, 255, 255)
        
        # Leerer Text
        self.spiel_vorbei_text = ""
        
        # Leere Level Liste
        self.level = []
        self.aktuelles_level = 0
    
    def _aktuelles_level(self):
        if len(self.level) <= 0 or self.aktuelles_level < 0 or self.aktuelles_level >= len(self.level):
            return None
        
        return self.level[self.aktuelles_level]
    
    def initialisiere_spiel_elemente(self, raumschiff):
        # Leerer Text
        self.spiel_vorbei_text = ""
        
        aktuelles_level = self._aktuelles_level()
        if aktuelles_level:
            aktuelles_level.initialisiere_spiel_elemente(self.leinwand, raumschiff)
    
    def _hole_spiel_elemente(self):
        aktuelles_level = self._aktuelles_level()
        if aktuelles_level:
            spiel_elemente = aktuelles_level.hole_spiel_elemente()
        return spiel_elemente
    
    def behandle_eingabe_ereignis(self, event, zeitschritt):      # Öffentliche Mitglied Funktion für Eingabebehandlung
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            aktuelles_level = self._aktuelles_level()
            if aktuelles_level and aktuelles_level.raumschiff:
                laser = aktuelles_level.raumschiff.schiesse()
                # Füge Laser in Liste hinzu
                aktuelles_level.laser.extend(laser)
    
    def behandle_eingaben(self, zeitschritt):      # Öffentliche Mitglied Funktion für Eingabebehandlung
        # Hole Tastatur Eingaben
        wurde_taste_gedrueckt = pygame.key.get_pressed()
        
        # Raumschiff Steuerung
        aktuelles_level = self._aktuelles_level()
        if aktuelles_level and aktuelles_level.raumschiff:
            # Drehe Raumschiff
            if wurde_taste_gedrueckt[pygame.K_d] or wurde_taste_gedrueckt[pygame.K_RIGHT]:
                aktuelles_level.raumschiff.drehe(uhrzeigersinn=True)
            # Drehe Raumschiff
            elif wurde_taste_gedrueckt[pygame.K_a] or wurde_taste_gedrueckt[pygame.K_LEFT]:
                aktuelles_level.raumschiff.drehe(uhrzeigersinn=False)
            # Schub nach vorne
            if wurde_taste_gedrueckt[pygame.K_w] or wurde_taste_gedrueckt[pygame.K_UP]:
                aktuelles_level.raumschiff.beschleunige(zeitschritt)
            # Schiesse
            if wurde_taste_gedrueckt[pygame.K_SPACE]:
                laser = aktuelles_level.raumschiff.schiesse()
                # Füge Laser in Liste hinzu
                aktuelles_level.laser.extend(laser)
    
    def behandle_spiele_logik(self, zeitschritt):  # Öffentliche Mitglied Funktion für Spielelogik
        aktuelles_level = self._aktuelles_level()
        if aktuelles_level:
            self.score += aktuelles_level.behandle_spiele_logik(self.score, self.leinwand, zeitschritt)
        
        if aktuelles_level:
            # Gewonnen: Keine Asteroiden übrig
            if aktuelles_level.gewonnen():
                self.spiel_vorbei_text = self.SPIEL_VORBEI_GEWONNEN
                self.spiel_vorbei_farbe = pygame.Color("gold")
            # Verloren: Kein Raumschiff
            elif aktuelles_level.verloren():
                self.spiel_vorbei_text = self.SPIEL_VORBEI_VERLOREN
                self.spiel_vorbei_farbe = pygame.Color("tomato")
    
    def zeichne_spiele_elemente(self, zeitschritt): # Öffentliche Mitglied Funktion für das Zeichnen
        aktuelles_level = self._aktuelles_level()
        if aktuelles_level:
            aktuelles_level.zeichne_spiele_elemente(self.leinwand, zeitschritt)
        
        # Zeichne Text
        if self.spiel_vorbei_text:
            position = Vector2(self.leinwand.get_size()) / 2
            zeige_text(self.leinwand, self.spiel_vorbei_text, self.spiel_vorbei_schrift, self.spiel_vorbei_farbe, position)
        
        position = Vector2(self.leinwand.get_size()) / 16
        zeige_text(self.leinwand, str(self.score), self.spiel_vorbei_schrift, pygame.Color("tomato"), position)
    
    def level_gewonnen(self):
        # Du Gewinnst wenn das Raumschiff noch existiert und der Text anzeigt dass Du gewonnen hast
        # Du Verlierst wenn das Raumschiff nicht existiert oder der Text nicht anzeigt dass Du gewonnen hast
        aktuelles_level = self._aktuelles_level()
        if aktuelles_level:
            return (aktuelles_level.gewonnen())
        else:
            return True
