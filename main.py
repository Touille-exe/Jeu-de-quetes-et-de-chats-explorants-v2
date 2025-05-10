import pygame
import pytmx
import pyscroll
import pyautogui
##     import json
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

        # Variables de jeu
        self.position_x_joueur = 0
        self.position_y_joueur = 0
        self.zoom = 1.0

        # Chargement de la carte et des calques
        self.tmx_data = pytmx.util_pygame.load_pygame("assets/carte/carte2tmx.tmx")
        self.map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.carte_renderer = pyscroll.orthographic.BufferedRenderer(self.map_data, (self.taille_x, self.taille_y), clamp_camera=True)
        self.carte_renderer.zoom = 1.0
        self.groupe_de_calques = pyscroll.PyscrollGroup(map_layer=self.carte_renderer, default_layer=1)

        self.ecran_charge()                                                                                       # actualiser l'écran de chargement

        # Couleurs
        self.rouge_de_lecriture = (197, 15, 31)
        self.vert_de_lecriture = (21, 171, 12)
        self.gris_du_fond = (121, 125, 127)
        self.blanc = (255, 255, 255)
        self.noir = (0, 0, 0)
        self.rouge = (255, 0, 0)

        # Chargement et redimensionnement des boutons du menu principal
        self.boutton_jouer_img = pygame.image.load("assets/boutton du menu principal/boutton play.png")
        self.boutton_jouer_img = pygame.transform.scale(self.boutton_jouer_img, (100, 100))
        self.rect_boutton_jouer = self.boutton_jouer_img.get_rect(center=(self.TAILLE_X_MOITIE, self.TAILLE_Y_MOITIE))

        self.boutton_parametre_img = pygame.image.load("assets/boutton du menu principal/paramètres.png")
        self.boutton_parametre_img = pygame.transform.scale(self.boutton_parametre_img, (75, 75))
        self.rect_boutton_parametre = self.boutton_parametre_img.get_rect(center=(self.taille_x / 4, self.TAILLE_Y_MOITIE))

        self.boutton_retour_img = pygame.image.load("assets/boutton du menu principal/retour.png")
        self.boutton_retour_img = pygame.transform.scale(self.boutton_retour_img, (75, 75))
        self.rect_boutton_retour = self.boutton_retour_img.get_rect(bottomright=(self.taille_x - 50, self.taille_y - 50))


        self.ecran_charge()                                                                                                    # actualiser l'écran de chargement

        # Chargement des éléments des paramètres
        self.barre_img = pygame.image.load("assets/boutton du menu principal/para/barre.png")
        self.barre_img = pygame.transform.scale(self.barre_img, (500, 100))
        self.rond_img = pygame.image.load("assets/boutton du menu principal/para/rond.png")
        self.rond_img = pygame.transform.scale(self.rond_img, (70, 70))
        self.rect_rond_zoom = 920 + (self.zoom * 400)

        # Chargement de l'image du joueur
        self.img_joueur = pygame.image.load("assets/joueurs/spritesheet.png")

        self.etapecharger = 4
        self.ecran_charge()                                                                                                    # finir l'écran de chargement

        # États du jeu
        self.etat = "euu"
        self.menu_principal()

    def ecran_charge(self):
        if self.etapecharger == 1:
            texte = self.fontducharger.render("Chargement ...", True, (197, 15, 31))
            texte_rect = texte.get_rect(center=(self.TAILLE_X_MOITIE, self.TAILLE_Y_MOITIE))
            self.ecran.fill((121, 125, 127))
            self.ecran.blit(texte, texte_rect)
            self.etapecharger += 1
            time.sleep(0.2)

        if self.etapecharger == 2:
            texte = self.fontducharger.render("Chargement .", True, (197, 15, 31))
            texte_rect = texte.get_rect(center=(self.TAILLE_X_MOITIE, self.TAILLE_Y_MOITIE))
            self.ecran.fill((121, 125, 127))
            self.ecran.blit(texte, texte_rect)
            self.etapecharger += 1
            time.sleep(0.2)

        if self.etapecharger == 3:
            texte = self.fontducharger.render("Chargement ..", True, (197, 15, 31))
            texte_rect = texte.get_rect(center=(self.TAILLE_X_MOITIE, self.TAILLE_Y_MOITIE))
            self.ecran.fill((121, 125, 127))
            self.ecran.blit(texte, texte_rect)
            self.etapecharger = 1
            time.sleep(0.2)

        if self.etapecharger == 4:
            texte = self.fontducharger.render("C'est fait !", True, (197, 15, 31))
            texte_rect = texte.get_rect(center=(self.TAILLE_X_MOITIE, self.TAILLE_Y_MOITIE))
            self.ecran.fill((121, 125, 127))
            self.ecran.blit(texte, texte_rect)
            self.etapecharger = 1
            time.sleep(0.5)

        pygame.display.flip()

    def quitter(self):
        pygame.quit()

    def parametres(self):
        en_parametres = True
        zoom_drag = False  # Pour savoir si on déplace le bouton de zoom

        # Limites du slider
        pos_barre_x = 700
        largeur_barre = 500
        min_x = pos_barre_x + 20
        max_x = pos_barre_x + largeur_barre - 90  # Le rond fait ~70px

        # Position initiale du rond basée sur le zoom
        self.rect_rond_zoom = min_x + ((self.zoom - 0.5) / (1.5 - 0.5)) * (max_x - min_x)

        while en_parametres:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_parametres = False
                    self.quitter()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        en_parametres = False
                        self.menu_principal()
                        return

                    if event.key == pygame.K_F11:
                        self.en_plein_ecran = not self.en_plein_ecran
                        if self.en_plein_ecran:
                            self.ecran = pygame.display.set_mode((self.taille_x, self.taille_y), pygame.FULLSCREEN)
                        else:
                            self.ecran = pygame.display.set_mode((self.taille_x, self.taille_y - 90))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rect_boutton_retour.collidepoint(event.pos):
                        en_parametres = False
                        self.menu_principal()
                        return

                    # Détection du clic sur le rond
                    position_boutton_rond_zoom = self.rond_img.get_rect(topleft=(self.rect_rond_zoom, 515))
                    if position_boutton_rond_zoom.collidepoint(event.pos):
                        zoom_drag = True

                if event.type == pygame.MOUSEBUTTONUP:
                    zoom_drag = False

                if event.type == pygame.MOUSEMOTION and zoom_drag:
                    mouse_x = pygame.mouse.get_pos()[0]
                    self.rect_rond_zoom = max(min_x, min(mouse_x, max_x))

                    # Calcul du zoom en fonction de la position du rond
                    percent = (self.rect_rond_zoom - min_x) / (max_x - min_x)
                    self.zoom = round(0.5 + percent * (1.5 - 0.5), 2)
                    self.carte_renderer.zoom = self.zoom

            # Affichage
            self.ecran.fill((255, 255, 255))
            self.ecran.blit(self.boutton_retour_img, self.rect_boutton_retour)
            self.ecran.blit(self.barre_img, (pos_barre_x, 500))
            self.ecran.blit(self.rond_img, (self.rect_rond_zoom, 515))

            font = pygame.font.SysFont("monospace", 50)
            texte_zoom = font.render(f"Zoom: {round(self.zoom, 2)}x", True, (0, 150, 200))
            self.ecran.blit(texte_zoom, (50, 500))

            pygame.display.flip()
            self.clock.tick(60)

    def menu_principal(self):
        self.etat = "menu_principal"
        pygame.display.set_caption("Jeu de rôle : Main menu")
        menu_principal = True
        while menu_principal:
            souris_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_principal = False
                    self.quitter()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.rect_boutton_parametre.collidepoint(souris_pos):
                        self.parametres()
                        return

                if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    if self.en_plein_ecran:
                        self.en_plein_ecran = False
                        self.ecran = pygame.display.set_mode((self.taille_x, self.taille_y))
                    elif not self.en_plein_ecran:
                        self.en_plein_ecran = True
                        self.ecran = pygame.display.set_mode((self.taille_x, self.taille_y), pygame.FULLSCREEN)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    menu_principal = False
                    self.quitter()
                    return


            self.ecran.fill((0, 0, 0))
            self.ecran.blit(self.boutton_jouer_img, self.rect_boutton_jouer)
            self.ecran.blit(self.boutton_parametre_img, self.rect_boutton_parametre)

            pygame.display.flip()
            self.clock.tick(60)

Jeuettoutenfaite()


# test