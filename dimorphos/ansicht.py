import pygame
import random
from pygame.math import Vector2
from pygame.mixer import Sound
from level import Level
from spielelement import SpielElement, Asteroid, Explosion, AlienRaumschiff
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
        self.hintergrund = lade_bild("hintergrund.magenta", False)
        
        # Leere Raumschiff Liste
        self.ausgewaehltes_raumschiff = 0
        self.raumschiffe = []
        
        # Leere Asteroiden Liste
        self.bild_asteroid = lade_bild("asteroid")
        self.asteroiden = []
        self.anzahl_asteroiden = 6
    
    def initialisiere_spiel_elemente(self):
        # Raumschiffe
        self._positioniere_raumschiffe()
        
        # Neue Asteroiden mit zufälliger Platzierung und Geschwindigkeit
        self.asteroiden = []
        for _ in range(self.anzahl_asteroiden):
            # Finde eine zufällige Position für den Asteroiden
            position = zufaellige_position(self.leinwand)
            # Füge Asteroid zur Liste hinzu
            self.asteroiden.append(Asteroid(position, self.bild_asteroid, random.uniform(.5, 5)))
    
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
        position = Vector2(self.leinwand.get_size()) / 2
        zeige_text(self.leinwand, self.spiel_titel_text, self.spiel_titel_schrift, self.spiel_titel_farbe, position)
        position = Vector2(0, self.leinwand.get_height() * 1/4) + Vector2(self.leinwand.get_size()) / 2
        zeige_text(self.leinwand, self.spiel_start_text, self.spiel_start_schrift, self.spiel_start_farbe, position)
    
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
        self.score_text = str(self.score)
        
        # Text
        self.spiel_vorbei_schrift = pygame.font.Font(None, 64)
        self.spiel_vorbei_text = ""
        self.spiel_vorbei_farbe = pygame.Color(255, 255, 255, 255)
        
        # Weltraum
        self.hintergrund = lade_bild("hintergrund.magenta", False)
        
        # Leere Laser Liste
        self.laser = []
        
        # Kein Raumschiff
        self.raumschiff = None
        
        # Leere Asteroiden Liste
        self.bild_asteroid = lade_bild("asteroid")
        self.asteroiden = []
        
        # Leere Explosionen Liste
        self.bild_explosion = lade_bild("explosion")
        self.ton_explosion = lade_ton("explosion")
        self.explosionen = []
        
        # Leere Aliens Liste
        self.laser_bild = lade_bild("laser")
        self.ton_laser = lade_ton("laser")
        self.aliens = []
        
        # Leerer Text
        self.spiel_vorbei_text = ""
        
        # Leere Level Liste
        self.level = []
        self.aktuelles_level = 0
    
    def initialisiere_spiel_elemente(self):
        aktuelles_level = self.level[self.aktuelles_level]
        
        # Leere Laser Liste
        self.laser = []
        
        # Neue Asteroiden mit zufälliger Platzierung und Geschwindigkeit
        self.asteroiden = aktuelles_level.initialisiere_asteroiden(
            self.leinwand, self.bild_asteroid, self.raumschiff.position)
        
        # Neue Aliens mit zufälliger Platzierung und Geschwindigkeit
        self.aliens = aktuelles_level.initialisiere_aliens(
            self.leinwand, self.laser_bild, self.ton_laser, self.raumschiff.position)
        
        # Leere Explosionen Liste
        self.explosionen = []
        
        # Leerer Text
        self.spiel_vorbei_text = ""
    
    def _hole_spiel_elemente(self):
        # Liste mit allen Spiel Elementen
        if self.raumschiff:
            spiel_elemente = [*self.asteroiden, self.raumschiff, *self.laser, *self.explosionen, *self.aliens]
        else:
            spiel_elemente = [*self.asteroiden, *self.laser, *self.explosionen, *self.aliens]
        return spiel_elemente
    
    def behandle_eingabe_ereignis(self, event, zeitschritt):      # Öffentliche Mitglied Funktion für Eingabebehandlung
        if self.raumschiff:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                laser = self.raumschiff.schiesse()
                # Füge Laser in Liste hinzu
                for l in laser:
                    self.laser.append(l)
    
    def behandle_eingaben(self, zeitschritt):      # Öffentliche Mitglied Funktion für Eingabebehandlung
        # Hole Tastatur Eingaben
        wurde_taste_gedrueckt = pygame.key.get_pressed()
        
        # Raumschiff Steuerung
        if self.raumschiff:
            # Drehe Raumschiff
            if wurde_taste_gedrueckt[pygame.K_d]:
                self.raumschiff.drehe(uhrzeigersinn=True)
            # Drehe Raumschiff
            elif wurde_taste_gedrueckt[pygame.K_a]:
                self.raumschiff.drehe(uhrzeigersinn=False)
            # Schub nach vorne
            if wurde_taste_gedrueckt[pygame.K_w]:
                self.raumschiff.beschleunige(zeitschritt)
            # Schiesse
            if wurde_taste_gedrueckt[pygame.K_SPACE]:
                laser = self.raumschiff.schiesse()
                # Füge Laser in Liste hinzu
                for l in laser:
                    self.laser.append(l)
    
    def behandle_spiele_logik(self, zeitschritt):  # Öffentliche Mitglied Funktion für Spielelogik
        # Bewege alle SpielElemente pro Bild ein wenig weiter
        for spielelement in self._hole_spiel_elemente():
            spielelement.bewege(self.leinwand, zeitschritt)
        
        # Alle Aliens schiessen
        if self.raumschiff:
            for alien in self.aliens:
                laser = alien.schiesse(self.raumschiff.position)
                # Füge Laser in Liste hinzu
                for l in laser:
                    self.laser.append(l)
        
        # Treffer: Laser auf Asteroid/Alien/Raumschiff, entferne beide
        for laser in self.laser[:]:
            for asteroid in self.asteroiden[:]:
                if laser.von_spieler and asteroid.kollidiert(laser):
                    # Explosion
                    position = asteroid.position
                    geschwindigkeit = 0.5 * laser.geschwindigkeit + 0.5 * asteroid.geschwindigkeit
                    self.explosion(position, geschwindigkeit)
                    
                    # Entferne Laser und Asteroid
                    self.asteroiden.remove(asteroid)
                    self.laser.remove(laser)
                    self.score += 1
                    break
            
            if not laser:
                continue
            
            for alien in self.aliens[:]:
                if laser.von_spieler and alien.kollidiert(laser):
                    # Explosion
                    position = alien.position
                    geschwindigkeit = 0.5 * laser.geschwindigkeit + 0.5 * alien.geschwindigkeit
                    self.explosion(position, geschwindigkeit)
                    
                    # Entferne Laser und Alien
                    self.aliens.remove(alien)
                    self.laser.remove(laser)
                    break
            
            if not laser:
                continue
            
            if not laser.von_spieler and self.raumschiff and self.raumschiff.kollidiert(laser):
                # Explosion
                position = self.raumschiff.position
                geschwindigkeit = 0.5 * laser.geschwindigkeit + 0.5 * self.raumschiff.geschwindigkeit
                self.explosion(position, geschwindigkeit)
                
                # Entferne Laser und Raumschiff
                self.raumschiff = None
                self.spiel_vorbei_text = self.SPIEL_VORBEI_VERLOREN
                self.spiel_vorbei_farbe = pygame.Color("tomato")
                self.laser.remove(laser)
                break
        
        # Entferne Laser am Bildrand
        for laser in self.laser[:]:
            if not self.leinwand.get_rect().collidepoint(laser.position):
                self.laser.remove(laser)
        
        # Kollision: Raumschiff mit Asteroid/Alien, entferne Raumschiff
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
            
            for alien in self.aliens:
                if alien.kollidiert(self.raumschiff):
                    # Explosion
                    position = self.raumschiff.position
                    geschwindigkeit = 0.5 * self.raumschiff.geschwindigkeit + 0.5 * alien.geschwindigkeit
                    self.explosion(position, geschwindigkeit)
                    
                    # Entferne Raumschiff
                    self.raumschiff = None
                    self.spiel_vorbei_text = self.SPIEL_VORBEI_VERLOREN
                    self.spiel_vorbei_farbe = pygame.Color("tomato")
                    break
        
        # Gewonnen: Keine Asteroiden übrig
        if not self.asteroiden and not self.aliens and self.raumschiff:
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
            position = Vector2(self.leinwand.get_size()) / 2
            zeige_text(self.leinwand, self.spiel_vorbei_text, self.spiel_vorbei_schrift, self.spiel_vorbei_farbe, position)

        position = Vector2(self.leinwand.get_size()) / 16
        zeige_text(self.leinwand, str(self.score), self.spiel_vorbei_schrift, pygame.Color("tomato"), position)
    
    def level_gewonnen(self):
        # Du Gewinnst wenn das Raumschiff noch existiert und der Text anzeigt dass Du gewonnen hast
        # Du Verlierst wenn das Raumschiff nicht existiert oder der Text nicht anzeigt dass Du gewonnen hast
        return (self.raumschiff and self.spiel_vorbei_text == self.SPIEL_VORBEI_GEWONNEN)
    
    def explosion(self, position, geschwindigkeit):
        # Finde in der Explosionen Liste eine unbenutzte Explosion
        explosion = None
        for i, e in enumerate(self.explosionen):
            if e.explosion.beendet():
                e.explosion.reset()
                e.position = position
                e.geschwindigkeit = geschwindigkeit
                explosion = e
                break
        # Erzeuge eine neue Explosion wenn es keine unbenutzte Explosion gibt
        if not explosion:
            explosion = Explosion(position, geschwindigkeit, self.bild_explosion, self.ton_explosion)
            self.explosionen.append(explosion)
        # Spiele den Ton für die Explosion ab wenn Du eine Explosion hast
        if explosion:
            Sound.play(explosion.ton_explosion)
