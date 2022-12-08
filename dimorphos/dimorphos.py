# Implementierung eines Spiels
#    initialisiere_pygame()
#    while True:
#        behandle_eingaben()
#        behandle_spiele_logik()
#        zeichne_spiele_elemente()

import pygame

class Dimorphos:
    
    def __init__(self):     # Konstruktor Funktion: Bereite alle Mitglied-Variablen und Ressourcen dieser Klasse vor
        pygame.init()
        pygame.display.set_caption("Dimorphos")
        pygame.key.set_repeat(1, 10)    # Halte Taste Gedrückt für Wiederholte Dauer-Eingabe: benutze den Wert 10 als Intervall um den Ablauf zu beschleunigen.
        self.leinwand = pygame.display.set_mode((985, 570))
        self.clock = pygame.time.Clock()
        
        self._initialisiere_spiel_elemente()
    
    def __del__(self):      # Destruktor-Funktion
        pygame.quit()       # Beende pygame
    
    def _initialisiere_spiel_elemente(self):
        pass
    
    def endlos_schleife(self):      # Die wichtigste Funktion des Spiels
        
        self.laeuft_weiter = True   # Diese Mitglied-Variable kann durch Eingabe auf False gesetzt werden
        while self.laeuft_weiter:
            zeitschritt = pygame.time.get_ticks() / 1000
            self._behandle_eingaben()
            self._behandle_spiele_logik()
            self._zeichne_spiele_elemente()
    
    def _behandle_eingaben(self):
        for event in pygame.event.get():            # Durchlaufe alle Fenster-Eingabe-Ereignisse
            if event.type == pygame.QUIT or (       # Fensterknopf X geklickt oder
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE    # ESC-Taste gedrückt
            ):
                self.laeuft_weiter = False          # Breche die Endos-Schleife ab
    
    def _behandle_spiele_logik(self):
        pass
    
    def _zeichne_spiele_elemente(self):
        pygame.display.flip()   # Doppelpuffer: Zeichne in einem Nichtsichtbaren Speicher, während der andere Speicher dargestellt wird
        self.clock.tick(60)     # Bildwiederholrate: Zeichne alle 60 Millisekunden neu, das macht ca 16,66 Bilder pro Sekunde
