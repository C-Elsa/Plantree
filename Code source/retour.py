#Projet : Plantree
#Auteurs : Elsa CHEN, Sami OULHI

import pygame
import math

def dessiner_bouton_retour(screen):
    cx, cy, r = 50, 50, 25  

    pygame.draw.circle(screen, (50, 50, 50), (cx, cy), r)

    # ←
    pygame.draw.line(screen, (255, 255, 255), (cx - 10, cy), (cx + 8, cy), 3)
    pygame.draw.line(screen, (255, 255, 255), (cx - 10, cy), (cx - 3, cy - 7), 3)
    pygame.draw.line(screen, (255, 255, 255), (cx - 10, cy), (cx - 3, cy + 7), 3)

    return pygame.Rect(cx - r, cy - r, r * 2, r * 2)  # pour détecter le clic
