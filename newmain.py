import pygame
import pytmx
import pyscroll
import pyautogui
import time
#import json
pygame.init()

#=========================================
#initialisation des données
#=========================================
class fenetre:
    def __init__(self):
        taille_x , taille_y = 1000,500#pyautogui.size()
        if taille_x > taille_y*(16/9):
            taille_x = int(taille_y*(16/9))
        else:
            taille_y = int(taille_x*(9/16))

        self.fullscreen = False
        self.clock = pygame.time.Clock()
        self.acces = ["principale"]

        self.taille_x = taille_x-20
        self.taille_y = taille_y-100
        self.moitie_x = self.taille_x/2
        self.moitie_y = self.taille_y/2
        self.tier_x = self.taille_x/3
        self.deux_tiers_x = self.tier_x*2
        self.tier_y = self.taille_y/3
        self.deux_tiers_y = self.tier_y*2

        self.ecran = pygame.display.set_mode((self.taille_x,self.taille_y),)
        pygame.display.set_caption("jeu de rôle")

        self.boucle_principale = True
        self.boucle_parametre = True

        self.ratio = self.taille_x/1280
        self.demi_ratio = self.ratio/2
fenetre = fenetre()

class image:
    def __init__(self,fenetre):
        class parametre:
            def __init__(self,fenetre):
                jouer = pygame.image.load("assets/boutton du menu principal/boutton play.png")
                self.jouer = pygame.transform.scale(jouer,(200*fenetre.ratio,200*fenetre.ratio))
                parametre = pygame.image.load("assets/boutton du menu principal/paramètres.png")
                self.parametre = pygame.transform.scale(parametre,(175*fenetre.ratio,175*fenetre.ratio))
                retour = pygame.image.load("assets/boutton du menu principal/retour.png")
                self.retour = pygame.transform.scale(retour,(75*fenetre.ratio,75*fenetre.ratio))
                barre = pygame.image.load("assets/boutton du menu principal/para/barre.png")
                self.barre = pygame.transform.scale(barre,(500*fenetre.ratio,100*fenetre.ratio))
                rond = pygame.image.load("assets/boutton du menu principal/para/rond.png")
                self.rond = pygame.transform.scale(rond,(70*fenetre.ratio,70*fenetre.ratio))
        class perso1:
            def __init__(self):
                self.face1 = pygame.image.load("assets/joueurs/sprites/player_1/face1.png")
                self.face2 = pygame.image.load("assets/joueurs/sprites/player_1/face2.png")
                self.face3 = pygame.image.load("assets/joueurs/sprites/player_1/face3.png")
                self.gauche1 = pygame.image.load("assets/joueurs/sprites/player_1/gauche1.png")
                self.gauche2 = pygame.image.load("assets/joueurs/sprites/player_1/gauche2.png")
                self.gauche3 = pygame.image.load("assets/joueurs/sprites/player_1/gauche3.png")
                self.droite1 = pygame.image.load("assets/joueurs/sprites/player_1/droite1.png")
                self.droite2 = pygame.image.load("assets/joueurs/sprites/player_1/droite2.png")
                self.droite3 = pygame.image.load("assets/joueurs/sprites/player_1/droite3.png")
                self.dos1 = pygame.image.load("assets/joueurs/sprites/player_1/dos1.png")
                self.dos2 = pygame.image.load("assets/joueurs/sprites/player_1/dos2.png")
                self.dos3 = pygame.image.load("assets/joueurs/sprites/player_1/dos3.png")
        class carte:
            def __init__(self):
                self.perso1 = perso1()
                self.parametre = parametre(fenetre)
                image = image(fenetre)

class boutons:
    def __init__(self,fenetre,image):
        class parametre:
            def __init__(self,fenetre,image):
                self.parametre = image.parametre.parametre.get_rect(center=(fenetre.tier_x-(fenetre.ratio*100),fenetre.moitie_y))
                self.jouer = image.parametre.jouer.get_rect(center=(fenetre.moitie_x,fenetre.moitie_y))
                self.retour = image.parametre.retour.get_rect(topleft=(fenetre.taille_x-(100*fenetre.ratio),fenetre.taille_y-(100*fenetre.ratio)))
                self.rond_fps = image.parametre.rond.get_rect(topleft=((21*fenetre.ratio)+fenetre.moitie_x+(195*fenetre.ratio),fenetre.tier_y))
                self.barre_fps = image.parametre.barre.get_rect(topleft=(fenetre.moitie_x, fenetre.tier_y))
                self.rond_zoom = image.parametre.rond.get_rect(topleft=((21*fenetre.ratio)+fenetre.moitie_x+(195*fenetre.ratio),fenetre.deux_tiers_y))
                self.barre_zoom = image.parametre.barre.get_rect(topleft=(fenetre.moitie_x, fenetre.deux_tiers_y))
        self.parametre = parametre(fenetre,image)
boutons = boutons(fenetre,image)

class parametre:
    def __init__(self,fenetre):
        self.zoom = 1
        self.fps = 60
        self.langue = "francais"

        self.pos_barre_fps = 195*fenetre.ratio
        self.pos_barre_zoom = 195*fenetre.ratio
        self.max_barre = 390*fenetre.ratio
parametre = parametre(fenetre)

#=========================================
#fonctions
#=========================================
def parametres(fenetre,image,boutons,parametre):
    fenetre.boucle_parametre = True
    slide = False
    slide2 = False
    while fenetre.boucle_parametre:
        parametre.zoom = round(0.5+(parametre.pos_barre_zoom/parametre.max_barre),2)
        parametre.fps = int(30+(parametre.pos_barre_fps/parametre.max_barre*60))
        #affichage
        fenetre.ecran.fill((0,0,0))

        font = pygame.font.SysFont("monospace", int(50*fenetre.ratio))
        texte = font.render(f"zoom:{parametre.zoom}",True,(0,150,200))
        fenetre.ecran.blit(texte,(50*fenetre.ratio,fenetre.deux_tiers_y+(25*fenetre.ratio)))
        texte = font.render(f"fps:{parametre.fps}",True,(0,150,200))
        fenetre.ecran.blit(texte,(50*fenetre.ratio,fenetre.tier_y+(25*fenetre.ratio)))

        fenetre.ecran.blit(image.parametre.barre, (fenetre.moitie_x, fenetre.tier_y))
        fenetre.ecran.blit(image.parametre.rond,((21*fenetre.ratio)+fenetre.moitie_x+parametre.pos_barre_fps, fenetre.tier_y+(15*fenetre.ratio)))
        fenetre.ecran.blit(image.parametre.barre,(fenetre.moitie_x,fenetre.deux_tiers_y))
        fenetre.ecran.blit(image.parametre.rond, ((21*fenetre.ratio) + fenetre.moitie_x + parametre.pos_barre_zoom, fenetre.deux_tiers_y + (15*fenetre.ratio)))
        fenetre.ecran.blit(image.parametre.retour,(fenetre.taille_x-(100*fenetre.ratio),fenetre.taille_y-(100*fenetre.ratio)))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #retour
                if boutons.parametre.retour.collidepoint(event.pos):
                    fenetre.boucle_parametre = False
                #non_slide fps
                elif boutons.parametre.barre_fps.collidepoint(event.pos):
                    slide = True
                # non_slide zoom
                elif boutons.parametre.barre_zoom.collidepoint(event.pos):
                    slide2 = True
            #sliding fps
            elif slide == True:
                if pygame.mouse.get_pos()[0] - fenetre.moitie_x - 37 < 0:
                    parametre.pos_barre_fps = 0
                elif pygame.mouse.get_pos()[0] - fenetre.moitie_x - 37 > parametre.max_barre:
                    parametre.pos_barre_fps = parametre.max_barre
                else:
                    parametre.pos_barre_fps = pygame.mouse.get_pos()[0] - fenetre.moitie_x - 37
                if event.type == pygame.MOUSEBUTTONUP:
                    slide = False
                    boutons.parametre.rond_fps = image.parametre.rond.get_rect(topleft=(21 + fenetre.moitie_x + parametre.pos_barre_fps, fenetre.tier_y))
            # sliding zoom
            elif slide2 == True:
                if pygame.mouse.get_pos()[0] - fenetre.moitie_x - 37 < 0:
                    parametre.pos_barre_zoom = 0
                elif pygame.mouse.get_pos()[0] - fenetre.moitie_x - 37 > parametre.max_barre:
                    parametre.pos_barre_zoom = parametre.max_barre
                else:
                    parametre.pos_barre_zoom = pygame.mouse.get_pos()[0] - fenetre.moitie_x - 37
                if event.type == pygame.MOUSEBUTTONUP:
                    slide2 = False
                    boutons.parametre.rond_zoom = image.parametre.rond.get_rect(topleft=(21 + fenetre.moitie_x + parametre.pos_barre_zoom, fenetre.deux_tiers_y))

            #gestion de la fenetre
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_F11):
                if fenetre.fullscreen == True:
                    fenetre.fullscreen = False
                    fenetre.ecran = pygame.display.set_mode((fenetre.taille_x, fenetre.taille_y))
                else:
                    fenetre.fullscreen = True
                    fenetre.ecran = pygame.display.set_mode((fenetre.taille_x, fenetre.taille_y), pygame.FULLSCREEN)
            if event.type == pygame.QUIT:
                fenetre.boucle_parametre = False
                fenetre.boucle_principale = False

    fenetre.ecran.fill((0,0,0))

#=========================================
#carte
#=========================================
def carte(fenetre,image,boutons,parametre):
    fenetre.ecran.fill((0,0,0))


#=========================================
#boucle principale
#=========================================
while fenetre.boucle_principale:
    fenetre.ecran.blit(image.parametre.jouer,(fenetre.moitie_x-(100*fenetre.ratio),fenetre.moitie_y-(100*fenetre.ratio)))
    fenetre.ecran.blit(image.parametre.parametre,(fenetre.tier_x-(175*fenetre.ratio)-(fenetre.ratio*100),fenetre.moitie_y-(87*fenetre.ratio)))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if boutons.parametre.parametre.collidepoint(event.pos):
                parametres(fenetre,image,boutons,parametre)
            elif boutons.parametre.jouer.collidepoint(event.pos):
                carte(fenetre,image,boutons,parametre)
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_F11):
            if fenetre.fullscreen == True:
                fenetre.fullscreen = False
                fenetre.ecran = pygame.display.set_mode((fenetre.taille_x, fenetre.taille_y))
            else:
                fenetre.fullscreen = True
                fenetre.ecran = pygame.display.set_mode((fenetre.taille_x, fenetre.taille_y),pygame.FULLSCREEN)
        if event.type == pygame.QUIT:
            fenetre.boucle_principale = False


#=========================================
#fermeture du jeu
#=========================================
#il faudra ajouter la sauvegarde des données
pygame.quit()
