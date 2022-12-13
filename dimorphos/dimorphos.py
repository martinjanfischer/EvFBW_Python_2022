# Implementierung eines Spiels
#    pygame.init()
#    while True:
#        _behandle_eingaben()
#        _behandle_spiele_logik()
#        _zeichne_spiele_elemente()

import pygame
from pygame.math import Vector2
from spielelement import SpielElement

class Dimorphos:    # Diese Klasse ist das Spiel
    
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
        del self.spielelement   # Lösche Dummy SpielElement Objekt der Mitglied Variablen
        pygame.quit()           # Stoppe das pygame Modul
    
    def __del__(self):  # Destruktor Funktion
        pass
    
    def _initialisiere_spiel_elemente(self):
        # Das ist nur ein Dummy SpielElement Objekt
        pixel_waagerecht, pixel_senkrecht = self.leinwand.get_size()
        self.spielelement = SpielElement(Vector2(pixel_waagerecht / 2, pixel_senkrecht / 2), None, Vector2(0))
    
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
    
    def _behandle_spiele_logik(self, zeitschritt):  # Private Mitglied Funktion für Spielelogik
        pass
    
    def _zeichne_spiele_elemente(self): # Private Mitglied Funktion für das Zeichnen
        pygame.display.flip()           # Doppelpuffer: Zeichne in einem Nichtsichtbaren Speicher, während der andere Speicher dargestellt wird
