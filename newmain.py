import pygame
import pytmx
import pyscroll
import pyautogui
import time
##     import json
pygame.init()

class fenetre:
    def __init__(self):
        taille_x , taille_y = pyautogui.size()
        self.taille_x = taille_x-20
        self.taille_y = taille_y-100
        self.moitie_x = self.taille_x/2
        self.moitie_y = self.taille_y/2
        self.tier_x = self.taille_x/3
        self.deux_tiers_x = self.tier_x*2