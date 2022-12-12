# Implementierung eines Spiels
#    pygame.init()
#    while True:
#        _behandle_eingaben()
#        _behandle_spiele_logik()
#        _zeichne_spiele_elemente()

import pygame
from pygame.math import Vector2
from spielelement import SpielElement, Raumschiff, Asteroid
from nuetzliches import lade_bild, zufaellige_position, zeige_text

class Dimorphos:    # Diese Klasse ist das Spiel
    MIN_ASTEROIDEN_DISTANZ = 250
    SPIEL_VORBEI_GEWONNEN = "Gewonnen!"
    SPIEL_VORBEI_VERLOREN = "Verloren!"
    
    def __init__(self):     # Konstruktor Funktion: Bereite alle Mitglied Variablen und Ressourcen dieser Klasse vor
        pass
    
    def __enter__(self):    # Konstruktor Funktion: Bereite alle Mitglied Variablen und Ressourcen dieser Klasse vor
        pygame.init()       # starte das pygame Modul
        pygame.display.set_caption("Dimorphos") # Text am oberen Fenster Rahmen
        pygame.key.set_repeat(1, 10)            # Halte Taste Gedrückt für Wiederholte Dauer-Eingabe: benutze den Wert 10 als Intervall um den Ablauf zu beschleunigen.
        
        self.endlos_schleife_laeuft_weiter = True   # Diese Mitglied Variable kann durch Eingabe auf False gesetzt werden
        self.leinwand = pygame.display.set_mode((1280, 720)) # Anzahl Bildpunkte/Pixel waagerecht und senkrecht
        self.clock = pygame.time.Clock()            # Zeitgeber
        self.letzte_zeit = pygame.time.get_ticks() / 1000
        
        self.spiel_vorbei_schrift = pygame.font.Font(None, 64)
        self.spiel_vorbei_text = ""
        self.spiel_vorbei_farbe = pygame.Color(255, 255, 255, 255)
        
        self.hintergrund = lade_bild("weltraum", False)
        self._initialisiere_spiel_elemente()        # Erzeuge Raumschiff, Asteroiden, Laser
    
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):          # Destruktor Funktion
        pygame.quit()           # Stoppe das pygame Modul
    
    def __del__(self):  # Destruktor Funktion
        pass
    
    def _hole_spiel_elemente(self):
        spiel_elemente = [*self.asteroiden, *self.laser]
        if self.raumschiff:
            spiel_elemente.append(self.raumschiff)
        return spiel_elemente
    
    def _initialisiere_spiel_elemente(self):
        self.spiel_vorbei_text = ""
        self.anzahl_asteroiden = 6
        self.laser = []
        w, h = self.leinwand.get_size()
        self.raumschiff = Raumschiff(Vector2(w / 2, h / 2), self.laser.append)
        self.asteroiden = []
        for _ in range(self.anzahl_asteroiden):
            while True:
                position = zufaellige_position(self.leinwand)
                distanz = position.distance_to(self.raumschiff.position)
                if (distanz > self.MIN_ASTEROIDEN_DISTANZ):
                    break
            self.asteroiden.append(Asteroid(position))
    
    def endlos_schleife(self):          # Die wichtigste öffentliche Mitglied Funktion des Spiels
        # Implementierung eines Spiels
        while self.endlos_schleife_laeuft_weiter:
            aktuelle_zeit = pygame.time.get_ticks() / 1000  # Millisekunden umrechnen in Sekunden
            zeitschritt = aktuelle_zeit - self.letzte_zeit
            self.letzte_zeit = aktuelle_zeit
            self._behandle_eingaben(zeitschritt)
            self._behandle_spiele_logik(zeitschritt)
            self._zeichne_spiele_elemente()
            self.clock.tick(60)         # Bildwiederholrate: Zeichne alle 60 Millisekunden neu, das macht ca 16,66 Bilder pro Sekunde
    
    def _behandle_eingaben(self, zeitschritt):      # Private Mitglied Funktion für Eingabebehandlung
        # Programm Schließen?
        for event in pygame.event.get():            # Durchlaufe alle Fenster-Eingabe-Ereignisse
            if event.type == pygame.QUIT or (       # Fensterknopf X geklickt oder
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE    # ESC-Taste gedrückt
            ):
                self.endlos_schleife_laeuft_weiter = False # Breche die Endos-Schleife ab
        
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
                self.raumschiff.schiesse()
        
        # Neues Spiel?
        if wurde_taste_gedrueckt[pygame.K_RETURN]:
            if (
                (self.raumschiff == None and self.spiel_vorbei_text == self.SPIEL_VORBEI_VERLOREN)
                or (self.raumschiff and self.spiel_vorbei_text == self.SPIEL_VORBEI_GEWONNEN)
                ):
                self._initialisiere_spiel_elemente()
    
    def _behandle_spiele_logik(self, zeitschritt):  # Private Mitglied Funktion für Spielelogik
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
                   self.raumschiff = None
                   self.spiel_vorbei_text = self.SPIEL_VORBEI_VERLOREN
                   self.spiel_vorbei_farbe = pygame.Color("tomato")
                   break
        
        # Gewonnen: Keine Asteroiden übrig
        if not self.asteroiden and self.raumschiff:
            self.spiel_vorbei_text = self.SPIEL_VORBEI_GEWONNEN
            self.spiel_vorbei_farbe = pygame.Color("gold")
    
    def _zeichne_spiele_elemente(self): # Private Mitglied Funktion für das Zeichnen
        self.leinwand.blit(self.hintergrund, (0, 0))
        for spielelement in self._hole_spiel_elemente():
            spielelement.zeichne(self.leinwand)
        if self.spiel_vorbei_text:
            zeige_text(self.leinwand, self.spiel_vorbei_text, self.spiel_vorbei_schrift, self.spiel_vorbei_farbe)
        pygame.display.flip()           # Doppelpuffer: Zeichne in einem Nichtsichtbaren Speicher, während der andere Speicher dargestellt wird
