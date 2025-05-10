import pygame
import pytmx
import pyscroll
import pyautogui
##                 import json
import time


class Jeuettoutenfaite:
    def __init__(self):
        pygame.init()

        # Taille de la fenêtre
        self.taille_x, self.taille_y = pyautogui.size()
        self.taille_x -= 20
        self.taille_y -= 100
        self.TAILLE_X_MOITIE = self.taille_x / 2
        self.TAILLE_Y_MOITIE = self.taille_y / 2

        # Variable pour savoir si on est en plein écran
        self.en_plein_ecran = True

        # Création de la fenêtre (initialement en plein écran) puis de l'écran de chargement
        self.ecran = pygame.display.set_mode((self.taille_x, self.taille_y), pygame.FULLSCREEN)
        pygame.display.set_caption("Jeu de rôle : chargement")
        self.fontducharger = pygame.font.SysFont("Comfortaa", 36)
        self.etapecharger = 1

        self.ecran_charge()                                                                                                    # demarer l'écran de chargement

        # Limite de fps
        self.clock = pygame.time.Clock()

        # Chargement de la carte et des calques
        self.tmx_data = pytmx.util_pygame.load_pygame("assets/carte/carte2tmx.tmx")
        self.map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.carte_renderer = pyscroll.orthographic.BufferedRenderer(self.map_data, (self.taille_x, self.taille_y), clamp_camera=True)
        self.carte_renderer.zoom = 1.0
        self.groupe_de_calques = pyscroll.PyscrollGroup(map_layer=self.carte_renderer, default_layer=1)

        self.ecran_charge()                                                                                                    # actualiser l'écran de chargement

        # Chargement et redimensionnement des boutons du menu principal
        self.boutton_jouer_img = pygame.image.load("assets/boutton du menu principal/boutton play.png")
        self.boutton_jouer_img = pygame.transform.scale(self.boutton_jouer_img, (100, 100))
        self.position_boutton_jouer = self.boutton_jouer_img.get_rect(center=(self.TAILLE_X_MOITIE, self.TAILLE_Y_MOITIE))

        self.ecran_charge()                                                                                                    # actualiser l'écran de chargement

        self.boutton_parametre_img = pygame.image.load("assets/boutton du menu principal/paramètres.png")
        self.boutton_parametre_img = pygame.transform.scale(self.boutton_parametre_img, (75, 75))
        self.position_boutton_parametre = self.boutton_parametre_img.get_rect(center=(self.taille_x / 4, self.TAILLE_Y_MOITIE))

        self.ecran_charge()                                                                                                    # actualiser l'écran de chargement

        self.boutton_retour_img = pygame.image.load("assets/boutton du menu principal/retour.png")
        self.boutton_retour_img = pygame.transform.scale(self.boutton_retour_img, (75, 75))
        self.position_boutton_retour_fullscreen = self.boutton_retour_img.get_rect(bottomright=(self.taille_x - 50, self.taille_y - 50))
        self.position_boutton_retour_windowed = self.boutton_retour_img.get_rect(bottomright=(self.taille_x - 50, self.taille_y - 150))

        self.ecran_charge()                                                                                                    # actualiser l'écran de chargement

        # Chargement des éléments des paramètres
        self.barre_img = pygame.image.load("assets/boutton du menu principal/para/barre.png")
        self.barre_img = pygame.transform.scale(self.barre_img, (500, 100))
        self.rond_img = pygame.image.load("assets/boutton du menu principal/para/rond.png")
        self.rond_img = pygame.transform.scale(self.rond_img, (70, 70))

        self.ecran_charge()                                                                                                    # actualiser l'écran de chargement

        # Chargement de l'image du joueur
        self.img_joueur = pygame.image.load("assets/joueurs/spritesheet.png")

        self.ecran_charge()                                                                                                    # actualiser l'écran de chargement

        # Variables de jeu
        self.position_x_joueur = 0
        self.position_y_joueur = 0
        self.zoom = 1.0

        self.etapecharger = 4
        self.ecran_charge()                                                                                                    # finir l'écran de chargement

        # États du jeu
        self.etat = "menu_on"

    def ecran_charge(self):
        if self.etapecharger == 1:
            texte = self.fontducharger.render("Chargement ...", True, (197, 15, 31))
            texte_rect = texte.get_rect(center=(self.TAILLE_X_MOITIE, self.TAILLE_Y_MOITIE))
            self.ecran.fill((121, 125, 127))
            self.ecran.blit(texte, texte_rect)
            pygame.display.flip()
            self.etapecharger += 1
            time.sleep(0.2)

        if self.etapecharger == 2:
            texte = self.fontducharger.render("Chargement .", True, (197, 15, 31))
            texte_rect = texte.get_rect(center=(self.TAILLE_X_MOITIE, self.TAILLE_Y_MOITIE))
            self.ecran.fill((121, 125, 127))
            self.ecran.blit(texte, texte_rect)
            pygame.display.flip()
            self.etapecharger += 1
            time.sleep(0.2)

        if self.etapecharger == 3:
            texte = self.fontducharger.render("Chargement ..", True, (197, 15, 31))
            texte_rect = texte.get_rect(center=(self.TAILLE_X_MOITIE, self.TAILLE_Y_MOITIE))
            self.ecran.fill((121, 125, 127))
            self.ecran.blit(texte, texte_rect)
            pygame.display.flip()
            self.etapecharger = 1
            time.sleep(0.2)

        if self.etapecharger == 4:
            texte = self.fontducharger.render("C'est fait !", True, (197, 15, 31))
            texte_rect = texte.get_rect(center=(self.TAILLE_X_MOITIE, self.TAILLE_Y_MOITIE))
            self.ecran.fill((121, 125, 127))
            self.ecran.blit(texte, texte_rect)
            pygame.display.flip()
            self.etapecharger = 1
            time.sleep(0.5)


Jeuettoutenfaite()
