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
        taille_x , taille_y = pyautogui.size()
        self.fullscreen = True
        self.clock = pygame.time.Clock()
        self.acces = ["principale"]
        self.taille_x = taille_x-20
        self.taille_y = taille_y-100
        self.moitie_x = self.taille_x/2
        self.moitie_y = self.taille_y/2
        self.tier_x = self.taille_x/3
        self.deux_tiers_x = self.tier_x*2
        self.ecran = pygame.display.set_mode((self.taille_x,self.taille_y),pygame.FULLSCREEN)
        pygame.display.set_caption("jeu de rôle")
fenetre = fenetre()

class image:
    def __init__(self):
        class parametre:
            def __init__(self):
                jouer = pygame.image.load("assets/boutton du menu principal/boutton play.png")
                self.jouer = pygame.transform.scale(jouer,(100,100))
                parametre = pygame.image.load("assets/boutton du menu principal/paramètres.png")
                self.parametre = pygame.transform.scale(parametre,(75,75))
                retour = pygame.image.load("assets/boutton du menu principal/retour.png")
                self.retour = pygame.transform.scale(retour,(75,75))
                barre = pygame.image.load("assets/boutton du menu principal/para/barre.png")
                self.barre = pygame.transform.scale(barre,(500,100))
                rond = pygame.image.load("assets/boutton du menu principal/para/rond.png")
                self.rond = pygame.transform.scale(rond,(70, 70))
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
        self.perso1 = perso1()
        self.parametre = parametre()
image = image()

class boutons:
    def __init__(self,fenetre):
        class parametre:
            def __init__(self,fenetre):
                self.parametre = pygame.Rect((fenetre.tier_x-37,fenetre.moitie_x-37),(75,75))
                self.jouer = pygame.Rect((fenetre.moitie_x-50,fenetre.moitie_y-50),(100,100))
        self.parametre = parametre(fenetre)
boutons = boutons(fenetre)


#=========================================
#fonctions
#=========================================
def parametre():
    pass


#=========================================
#boucle principale
#=========================================
boucle_principale = True
while boucle_principale:
    fenetre.ecran.blit(image.parametre.jouer,(fenetre.moitie_x-50,fenetre.moitie_y-50))
    fenetre.ecran.blit(image.parametre.parametre,(fenetre.tier_x-37,fenetre.moitie_y-37))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_F11):
            if fenetre.fullscreen == True:
                fenetre.fullscreen = False
                fenetre.ecran = pygame.display.set_mode((fenetre.taille_x, fenetre.taille_y))
            else:
                fenetre.fullscreen = True
                fenetre.ecran = pygame.display.set_mode((fenetre.taille_x, fenetre.taille_y),pygame.FULLSCREEN)
        if event.type == pygame.QUIT:
            boucle_principale = False


#=========================================
#fermeture du jeux
#=========================================
#il faudra ajouter la sauvegard des données
pygame.quit()