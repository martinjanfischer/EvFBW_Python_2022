# Implementierung eines Spiels
#    pygame.init()
#    while True:
#        _behandle_eingaben()
#        _behandle_spiele_logik()
#        _zeichne_spiele_elemente()

import os
import pygame
import itertools
from pygame.math import Vector2
from ansicht import StartAnsicht, LevelAnsicht
from level import EndlosLevel, Level
from nuetzliches import lade_bild, lade_ton
from spielelement import Raumschiff
from level import EndlosLevel

class Dimorphos:
    """Diese Klasse ist das Spiel"""
    
    DIMORPHOS_APPDATA_PATH = os.path.join(os.getenv('APPDATA'), 'EvFBW_dimorphos_2022')
    TIME_CLOCK_TICK_FPS_60 = 60 # Maximale Bildwiederholrate für pygame.time.Clock.tick
    START_ANSICHT = 0
    LEVEL_ANSICHT = 1
    
    def __init__(self):     # Konstruktor Funktion: Bereite alle Mitglied Variablen und Ressourcen dieser Klasse vor
        pass
    
    def __enter__(self):    # Konstruktor Funktion: Bereite alle Mitglied Variablen und Ressourcen dieser Klasse vor
        # pygame Vorbereitung
        pygame.init()       # starte das pygame Modul
        pygame.display.set_caption("Dimorphos") # Text am oberen Fenster Rahmen
        pygame.key.set_repeat(1, 10)            # Halte Taste Gedrückt für Wiederholte Dauer-Eingabe: benutze den Wert 10 als Intervall um den Ablauf zu beschleunigen.
        
        # Steuerung der Endlos Schleife und der FPS Bildwiederholrate
        self.endlos_schleife_laeuft_weiter = True   # Diese Mitglied Variable kann durch Eingabe auf False gesetzt werden
        self.uhr = pygame.time.Clock()              # Zeitgeber
        self.letzte_zeit = pygame.time.get_ticks() / 1000
        
        # Ansichten
        start_ansicht = StartAnsicht()
        level_ansicht = LevelAnsicht()
        
        # Füge neue Raumschiffe in die Raumschiff-Liste der Start Ansicht hinzu
        self.laser_bild = lade_bild("laser")
        self.ton_laser = lade_ton("laser")
        start_ansicht.raumschiffe.append(Raumschiff(Vector2(0, 0), "raumschiff", self.laser_bild, self.ton_laser, [Vector2(0, -25)]))
        start_ansicht.raumschiffe.append(Raumschiff(Vector2(0, 0), "raumschiff_sui", self.laser_bild, self.ton_laser, [Vector2(-11, -1),Vector2(11, -1)]))
        start_ansicht.raumschiffe.append(Raumschiff(Vector2(0, 0), "raumschiff_von_konrad", self.laser_bild, self.ton_laser, [Vector2(16, -25),Vector2(-16, -25), Vector2(39,-12), Vector2(-39,-12)]))
        start_ansicht.raumschiffe.append(Raumschiff(Vector2(0, 0), "raumschiff.perfect_grafic", self.laser_bild, self.ton_laser, [Vector2(0, -25)]))
        
        
        # Füge neue Asteroidenbilder in die Liste der Ansichten hinzu
        bild_asteroid_1 = lade_bild("asteroid")
        bild_asteroid_2 = lade_bild("asteroid")
        start_ansicht.bilder_asteroiden.append(bild_asteroid_1)
        start_ansicht.bilder_asteroiden.append(bild_asteroid_2)
        level_ansicht.bilder_asteroiden.append(bild_asteroid_1)
        level_ansicht.bilder_asteroiden.append(bild_asteroid_2)
                # Die Level Ansicht bekommt das ausgewählte Raumschiff der Start Ansicht
        level_ansicht.raumschiff = start_ansicht.raumschiffe[start_ansicht.ausgewaehltes_raumschiff]
        
        # Bereite Level vor
        zerstoere_was_du_kannst_level = [EndlosLevel(1000,6,1,30,100,300,1)]
        karriere_level = []
        karriere_level.append(Level(3,0.5,10,50,200,1))
        karriere_level.append(Level(6,1,40,100,300,2))
        karriere_level.append(Level(9,1.5,80,150,400,3))
        start_ansicht.level = {}
        start_ansicht.level['Zerstöre was Du kannst'] = zerstoere_was_du_kannst_level
        start_ansicht.level['Karriere'] = karriere_level
        start_ansicht.level_zyklisch = itertools.cycle(start_ansicht.level)
        start_ansicht.ausgewaehltes_level = next(start_ansicht.level_zyklisch)
        
        # Bereite Start Anischt vor
        start_ansicht.initialisiere_spiel_elemente()
        
        # Füge die Ansichten in die Ansicht Liste der Spiele Klasse Dimorphos hinzu
        self.ansichten = []
        self.ansichten.append(start_ansicht)
        self.ansichten.append(level_ansicht)
        self.aktuelle_ansicht = self.START_ANSICHT
        
        # Highsore
        self.highscore = {}
        self._lade_highscore()
        
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):          # Destruktor Funktion
        self._schreibe_highscore()
        pygame.quit()           # Stoppe das pygame Modul
    
    def __del__(self):  # Destruktor Funktion
        pass
    
    def endlos_schleife(self):          # Die wichtigste öffentliche Mitglied Funktion des Spiels
        # Implementierung eines Spiels
        #    while True:
        #        _behandle_eingaben()
        #        _behandle_spiele_logik()
        #        _zeichne_spiele_elemente()
        while self.endlos_schleife_laeuft_weiter:
            aktuelle_zeit = pygame.time.get_ticks() / 1000  # Millisekunden umrechnen in Sekunden
            zeitschritt = aktuelle_zeit - self.letzte_zeit
            self.letzte_zeit = aktuelle_zeit
            self._behandle_eingaben(zeitschritt)
            self._behandle_spiele_logik(zeitschritt)
            self._zeichne_spiele_elemente(zeitschritt)
            self.uhr.tick(self.TIME_CLOCK_TICK_FPS_60)  # Bildwiederholrate
    
    def _behandle_eingaben(self, zeitschritt):      # Private Mitglied Funktion für Eingabebehandlung
        # Eingabebehandlung Programm
        for event in pygame.event.get():            # Durchlaufe alle Fenster-Eingabe-Ereignisse
            # Programm Schließen?
            if event.type == pygame.QUIT:           # Fensterknopf X geklickt
                self.endlos_schleife_laeuft_weiter = False # Breche die Endos-Schleife ab
            elif event.type == pygame.KEYUP:
                # Programm Schließen?
                if (self.aktuelle_ansicht == self.START_ANSICHT
                    and event.key == pygame.K_ESCAPE# ESC-Taste gedrückt
                ):
                    self.endlos_schleife_laeuft_weiter = False # Breche die Endos-Schleife ab
                # Aktuelles Spiel abbrechen
                elif (self.aktuelle_ansicht == self.LEVEL_ANSICHT
                    and event.key == pygame.K_ESCAPE# ESC-Taste gedrückt
                ):
                    start_ansicht = self.ansichten[self.START_ANSICHT]
                    level_ansicht = self.ansichten[self.LEVEL_ANSICHT]
                    level_ansicht.aktuelles_level = 0
                    self.aktuelle_ansicht = self.START_ANSICHT
                    self.ansichten[self.aktuelle_ansicht].initialisiere_spiel_elemente()
                # Starte Spiel
                elif (self.aktuelle_ansicht == self.START_ANSICHT
                    and event.key == pygame.K_RETURN # Enter-Taste gedrückt
                ):
                    start_ansicht = self.ansichten[self.START_ANSICHT]
                    level_ansicht = self.ansichten[self.LEVEL_ANSICHT]
                    level_ansicht.raumschiff = start_ansicht.raumschiffe[start_ansicht.ausgewaehltes_raumschiff]
                    level_ansicht.level = start_ansicht.level[start_ansicht.ausgewaehltes_level]
                    level_ansicht.aktuelles_level = 0
                    self.aktuelle_ansicht = self.LEVEL_ANSICHT
                    self.ansichten[self.aktuelle_ansicht].initialisiere_spiel_elemente()
                # Level Gewonnen: Nächstes Level
                elif (self.aktuelle_ansicht == self.LEVEL_ANSICHT
                    and event.key == pygame.K_RETURN # Enter-Taste gedrückt
                ):
                    if self.ansichten[self.aktuelle_ansicht].level_gewonnen():
                        start_ansicht = self.ansichten[self.START_ANSICHT]
                        level_ansicht = self.ansichten[self.LEVEL_ANSICHT]
                        level_ansicht.raumschiff = start_ansicht.raumschiffe[start_ansicht.ausgewaehltes_raumschiff]
                        if level_ansicht.aktuelles_level < len(level_ansicht.level) - 1:
                            self.aktuelle_ansicht = self.LEVEL_ANSICHT
                            level_ansicht.aktuelles_level += 1
                        else:
                            self.aktuelle_ansicht = self.START_ANSICHT
                            level_ansicht.aktuelles_level = 0
                        self.ansichten[self.aktuelle_ansicht].initialisiere_spiel_elemente()
                
            if self.ansichten[self.aktuelle_ansicht]:
                self.ansichten[self.aktuelle_ansicht].behandle_eingabe_ereignis(event, zeitschritt)
        
        # Eingabebehandlung Ansicht
        if self.ansichten[self.aktuelle_ansicht]:
            self.ansichten[self.aktuelle_ansicht].behandle_eingaben(zeitschritt)
    
    def _behandle_spiele_logik(self, zeitschritt):  # Private Mitglied Funktion für Spielelogik
        if self.ansichten[self.aktuelle_ansicht]:
            self.ansichten[self.aktuelle_ansicht].behandle_spiele_logik(zeitschritt)
    
    def _zeichne_spiele_elemente(self, zeitschritt): # Private Mitglied Funktion für das Zeichnen
        if self.ansichten[self.aktuelle_ansicht]:
            self.ansichten[self.aktuelle_ansicht].zeichne_spiele_elemente(zeitschritt)
        
        pygame.display.flip()           # Doppelpuffer: Zeichne in einem Nichtsichtbaren Speicher, während der andere Speicher dargestellt wird
    
    def _lade_highscore(self):
        # Prüfe Pfade
        if not os.path.exists(self.DIMORPHOS_APPDATA_PATH):
            return
        pfad_highscore = os.path.join(self.DIMORPHOS_APPDATA_PATH, "highscore.txt")
        if not os.path.isfile(pfad_highscore):
            return
        # Lade
        self.highscore.clear()
        with open(pfad_highscore, encoding='utf8', mode='r') as datei_highscore:
            for zeile in datei_highscore:
                (punkte, name) = zeile.split()
                self.highscore[int(punkte)] = name
        # Standardwerte
        if not self.highscore:
            self.highscore = {
                1000000 : "Martin",
                100000 : "Martin",
                10000 : "Martin",
                1000 : "Martin",
                100 : "Martin",
                10 : "Martin",
                1 : "Martin"
            }
    
    def _schreibe_highscore(self):
        # Prüfe Pfade
        if not os.path.exists(self.DIMORPHOS_APPDATA_PATH):
            os.makedirs(self.DIMORPHOS_APPDATA_PATH)
        pfad_highscore = os.path.join(self.DIMORPHOS_APPDATA_PATH, "highscore.txt")
        # Schreibe
        with open(pfad_highscore, encoding='utf8', mode='w') as datei_highscore:
            for punkte, name in self.highscore.items():
                datei_highscore.write(str(punkte) + ' ' + str(name) + '\n')
