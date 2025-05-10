import pygame
import pyautogui
import time


def chargement():
    pygame.init()
    taillex, tailley = pyautogui.size()
    taillex -= 20
    tailley -= 100

    pygame.display.set_caption("Test")
    ecran = pygame.display.set_mode((taillex, tailley))
    fontducharger = pygame.font.SysFont("Comfortaa", 36)

    for i in range(5):

        texte = fontducharger.render("Chargement ...", True, (197, 15, 31))
        texte_rect = texte.get_rect(center=(taillex // 2, tailley // 2))
        ecran.fill((121, 125, 127))
        ecran.blit(texte, texte_rect)
        pygame.display.flip()

        time.sleep(0.5)

        texte = fontducharger.render("Chargement .", True, (197, 15, 31))
        texte_rect = texte.get_rect(center=(taillex // 2, tailley // 2))
        ecran.fill((121, 125, 127))
        ecran.blit(texte, texte_rect)
        pygame.display.flip()

        time.sleep(0.5)

        texte = fontducharger.render("Chargement ..", True, (197, 15, 31))
        texte_rect = texte.get_rect(center=(taillex // 2, tailley // 2))
        ecran.fill((121, 125, 127))
        ecran.blit(texte, texte_rect)
        pygame.display.flip()

        time.sleep(0.5)

        texte = fontducharger.render("Chargement ...", True, (197, 15, 31))
        texte_rect = texte.get_rect(center=(taillex // 2, tailley // 2))
        ecran.fill((121, 125, 127))
        ecran.blit(texte, texte_rect)
        pygame.display.flip()


chargement()
pygame.quit()


#  font.render("Chargement ...", True, (197, 15, 31))
#
#
#
#
#