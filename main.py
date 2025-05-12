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
        self.zoom_para = 1.0

        # Chargement de la carte et des calques
        self.tmx_data = pytmx.util_pygame.load_pygame("assets/carte/carte_v2.tmx")
        self.map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.position_du_spawn = self.tmx_data.get_object_by_name("spawn")  # Récupération de l'objet spawn
        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, (self.taille_x, self.taille_y), clamp_camera=True)
        self.map_layer.zoom = self.zoom_para + 2
        self.groupe_de_calques = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=5)

        self.ecran_charge()                                                                                                        # actualiser l'écran de chargement

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
        self.rect_rond_zoom = 920 + (self.zoom_para * 400)

        # Chargement de l'image du joueur
        self.position_x_joueur = self.position_du_spawn.x
        self.position_y_joueur = self.position_du_spawn.y
        self.img_joueur = pygame.image.load("assets/joueurs/sprites/1_leo/1face2.png")
        self.img_joueur.set_colorkey([255, 255, 255])


        self.etapecharger = 4
        self.ecran_charge()                                                                                                    # finir l'écran de chargement

        # États du jeu
        self.etat = "euu"
        self.menu_principal()

    def ecran_charge(self):
        texte2 = self.fontducharger.render("Note : Redemarer le jeu pour que les paramètres soits pris en compte",True,(197, 15, 31))
        texte_rect2 = texte2.get_rect(center=(self.TAILLE_X_MOITIE, (self.TAILLE_Y_MOITIE / 2) * 3))
        if self.etapecharger == 1:
            texte = self.fontducharger.render("Chargement ...", True, (197, 15, 31))
            texte_rect = texte.get_rect(center=(self.TAILLE_X_MOITIE, self.TAILLE_Y_MOITIE))
            self.ecran.fill((121, 125, 127))
            self.ecran.blit(texte, texte_rect)
            self.ecran.blit(texte2, texte_rect2)
            self.etapecharger = 2
            pygame.display.flip()
            time.sleep(0.2)

        if self.etapecharger == 2:
            texte = self.fontducharger.render("Chargement .", True, (197, 15, 31))
            texte_rect = texte.get_rect(center=(self.TAILLE_X_MOITIE, self.TAILLE_Y_MOITIE))
            self.ecran.fill((121, 125, 127))
            self.ecran.blit(texte, texte_rect)
            self.ecran.blit(texte2, texte_rect2)
            self.etapecharger = 3
            pygame.display.flip()
            time.sleep(0.2)

        if self.etapecharger == 3:
            texte = self.fontducharger.render("Chargement ..", True, (197, 15, 31))
            texte_rect = texte.get_rect(center=(self.TAILLE_X_MOITIE, self.TAILLE_Y_MOITIE))
            self.ecran.fill((121, 125, 127))
            self.ecran.blit(texte, texte_rect)
            self.ecran.blit(texte2, texte_rect2)
            self.etapecharger = 1
            pygame.display.flip()
            time.sleep(0.2)

        if self.etapecharger == 4:
            texte = self.fontducharger.render("C'est fait !", True, (197, 15, 31))
            texte_rect = texte.get_rect(center=(self.TAILLE_X_MOITIE, self.TAILLE_Y_MOITIE))
            self.ecran.fill((121, 125, 127))
            self.ecran.blit(texte, texte_rect)
            self.ecran.blit(texte2, texte_rect2)
            self.etapecharger = 1
            pygame.display.flip()
            time.sleep(0.5)

    def quitter(self):
        pygame.quit()

    def parametres(self):
        en_parametres = True
        zoom_drag = False  # Pour savoir si on déplace le bouton de zoom_para

        # Limites du slider
        pos_barre_x = 700
        largeur_barre = 500
        min_x = pos_barre_x + 20
        max_x = pos_barre_x + largeur_barre - 90  # Le rond fait ~70px

        # Valeurs de zoom_para modifiables
        zoom_min = 1.0
        zoom_max = 1.5

        # Position initiale du rond basée sur le zoom_para
        self.rect_rond_zoom = min_x + ((self.zoom_para - zoom_min) / (zoom_max - zoom_min)) * (max_x - min_x)

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

                    # Calcul du zoom_para en fonction de la position du rond
                    percent = (self.rect_rond_zoom - min_x) / (max_x - min_x)
                    self.zoom_para = round(zoom_min + percent * (zoom_max - zoom_min), 2)
                    self.map_layer.zoom = self.zoom_para + 2

            # Affichage
            self.ecran.fill((255, 255, 255))
            self.ecran.blit(self.boutton_retour_img, self.rect_boutton_retour)
            self.ecran.blit(self.barre_img, (pos_barre_x, 500))
            self.ecran.blit(self.rond_img, (self.rect_rond_zoom, 515))

            font = pygame.font.SysFont("monospace", 50)
            texte_zoom = font.render(f"Fov : {round(self.zoom_para, 2)}x", True, (0, 150, 200))
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
                        menu_principal = False
                        self.parametres()
                        return

                    if self.rect_boutton_jouer.collidepoint(souris_pos):
                        menu_principal = False
                        self.en_jeu()
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

    def en_jeu(self):
        self.etat = "en_jeu"
        en_jeu = True

        self.sprite_joueur = pygame.sprite.Sprite()
        self.sprite_joueur.image = self.img_joueur
        self.sprite_joueur.rect = self.img_joueur.get_rect()
        self.sprite_joueur.rect.topleft = (self.position_x_joueur, self.position_y_joueur)
        self.groupe_de_calques.add(self.sprite_joueur)

        while en_jeu:
            souris_pos = pygame.mouse.get_pos()
            self.controledujoueur()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_principal = False
                    self.quitter()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pass

                if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    if self.en_plein_ecran:
                        self.en_plein_ecran = False
                        self.ecran = pygame.display.set_mode((self.taille_x, self.taille_y))
                    elif not self.en_plein_ecran:
                        self.en_plein_ecran = True
                        self.ecran = pygame.display.set_mode((self.taille_x, self.taille_y), pygame.FULLSCREEN)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    en_jeu = False
                    self.menu_principal()
                    return
            self.sprite_joueur.rect.topleft = (self.position_x_joueur, self.position_y_joueur)
            self.groupe_de_calques.center(self.sprite_joueur.rect.center)  # Pour centrer la map sur le joueur

            self.groupe_de_calques.draw(self.ecran)
            pygame.display.flip()

    def controledujoueur(self):
        touche_appuyees = pygame.key.get_pressed()
        vitesse = 0.2  # vitesse du joueur en pixels

        if touche_appuyees[pygame.K_z]:
            self.position_y_joueur -= vitesse
        if touche_appuyees[pygame.K_s]:
            self.position_y_joueur += vitesse
        if touche_appuyees[pygame.K_q]:
            self.position_x_joueur -= vitesse
        if touche_appuyees[pygame.K_d]:
            self.position_x_joueur += vitesse


Jeuettoutenfaite()


# test