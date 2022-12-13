# Implementierung eines Spiels
#    pygame.init()
#    while True:
#        _behandle_eingaben()
#        _behandle_spiele_logik()
#        _zeichne_spiele_elemente()

import pygame
from pygame.math import Vector2
from spielelement import SpielElement, Raumschiff, Asteroid
from nuetzliches import lade_bild, zufaellige_position

class Dimorphos:    # Diese Klasse ist das Spiel
    MIN_ASTEROIDEN_DISTANZ = 250
    
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
        
        self._initialisiere_spiel_elemente()        # Erzeuge Raumschiff, Asteroiden, Laser
        
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):          # Destruktor Funktion
        pygame.quit()           # Stoppe das pygame Modul
    
    def __del__(self):  # Destruktor Funktion
        pass
    
    def _hole_spiel_elemente(self):
        spiel_elemente = [*self.asteroiden]
        if self.raumschiff:
            spiel_elemente.append(self.raumschiff)
        return spiel_elemente
    
    def _initialisiere_spiel_elemente(self):
        self.anzahl_asteroiden = 6
        self.hintergrund = lade_bild("weltraum", False)
        pixel_waagerecht, pixel_senkrecht = self.leinwand.get_size()
        self.raumschiff = Raumschiff(Vector2(pixel_waagerecht / 2, pixel_senkrecht / 2), None)
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
    
    def _behandle_spiele_logik(self, zeitschritt):  # Private Mitglied Funktion für Spielelogik
        # Bewege alle SpielElemente pro Bild ein wenig weiter
        for spielelement in self._hole_spiel_elemente():
            spielelement.bewege(self.leinwand, zeitschritt)
    
    def _zeichne_spiele_elemente(self): # Private Mitglied Funktion für das Zeichnen
        # Zeichne Hintergrundbild neu
        self.leinwand.blit(self.hintergrund, (0, 0))
        
        # Zeichne alle SpielElemente in diesem Bild
        for spielelement in self._hole_spiel_elemente():
            spielelement.zeichne(self.leinwand)
        pygame.display.flip()           # Doppelpuffer: Zeichne in einem Nichtsichtbaren Speicher, während der andere Speicher dargestellt wird
