#Projet : Plantree
#Auteurs : Elsa CHEN, Sami OULHI

import pygame
import sys
import random
import inventaire
from retour import dessiner_bouton_retour

def bataille_navale(screen):

    WIDTH, HEIGHT = 1000, 600
    pygame.display.set_caption("Jardin Naval 🌸")

    # Couleurs
    WHITE  = (255, 255, 255)
    BLACK  = (0, 0, 0)
    BLUE   = (173, 216, 230)
    GREEN  = (144, 238, 144)
    RED    = (255, 99, 71)
    YELLOW = (255, 255, 0)

    # Grille
    GRID_SIZE = 6
    CELL_SIZE = 70
    OFFSET_X  = 100
    OFFSET_Y  = 120

    font  = pygame.font.SysFont(None, 28)
    clock = pygame.time.Clock()

    
    parterresDeFleurs = [2, 2, 2, 3, 3, 4]
    typeParterre      = {}
    
    fleur_img = pygame.image.load("fleur.png")
    fleur_img = pygame.transform.scale(fleur_img, (CELL_SIZE - 10, CELL_SIZE - 10))

    terre_img = pygame.image.load("terre-bn.png")
    terre_img = pygame.transform.scale(terre_img, (CELL_SIZE - 10, CELL_SIZE - 10))
    
    bg_minijeu = pygame.image.load("arrierePlanMiniJeu.png").convert()
    bg_minijeu = pygame.transform.scale(bg_minijeu, (WIDTH, HEIGHT))
    
    
    def reset():
        jardinJoueur = [["0"] * GRID_SIZE for _ in range(GRID_SIZE)] 
        jardinSecret = [["0"] * GRID_SIZE for _ in range(GRID_SIZE)]
        typesRestants = {2: 3, 3: 2, 4: 1}
        typeParterre.clear()
        placementParterre(jardinSecret)
        return jardinJoueur, jardinSecret, typesRestants, len(parterresDeFleurs), 28, False, False, None, ""

    def placementParterre(jardin):
        numeroDuParterre = 1
        for taille in parterresDeFleurs:
            typeParterre[str(numeroDuParterre)] = taille
            place = False
            while not place:
                direction = random.choice(["i", "j"])
                if direction == "i":
                    i = random.randint(0, 5)
                    j = random.randint(0, GRID_SIZE - taille)
                    if all(jardin[i][j+k] == "0" for k in range(taille)):
                        for k in range(taille):
                            jardin[i][j+k] = str(numeroDuParterre)
                        place = True
                else:
                    i = random.randint(0, GRID_SIZE - taille)
                    j = random.randint(0, 5)
                    if all(jardin[i+k][j] == "0" for k in range(taille)):
                        for k in range(taille):
                            jardin[i+k][j] = str(numeroDuParterre)
                        place = True
            numeroDuParterre += 1

    def parterreArrose(numeroDuParterre, jardinSecret):
        for ligne in jardinSecret:
            if numeroDuParterre in ligne:
                return False
        return True

    def arrosage(i, j, jardinJoueur, jardinSecret, typesRestants, parterresRestants):
        caseChoisie = jardinSecret[i][j]
        msg = ""
        if caseChoisie != "0":
            jardinJoueur[i][j] = "X"
            jardinSecret[i][j] = "X"
            msg = "Arrosé ! "
            if parterreArrose(caseChoisie, jardinSecret):
                taille = typeParterre[caseChoisie]
                typesRestants[taille] -= 1
                parterresRestants -= 1
                msg = "Parterre entièrement arrosé ! "
        else:
            jardinJoueur[i][j] = "~"
            msg = "Raté... "
        return parterresRestants, msg

    def dessiner_grille(jardinJoueur, jardinSecret, perdu):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                x = OFFSET_X + j * CELL_SIZE
                y = OFFSET_Y + i * CELL_SIZE
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

                pygame.draw.rect(screen, BLUE, rect)

                val = jardinJoueur[i][j]

                if val == "X":
                    pygame.draw.rect(screen, GREEN, rect)
                    screen.blit(fleur_img, (x + 5, y + 5))

                elif val == "~":
                    screen.blit(terre_img, (x + 5, y + 5))
                    
                elif perdu and jardinSecret[i][j] not in ("0", "X"):
                    s = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
                    s.fill((100, 200, 100, 150))
                    screen.blit(s, (x, y))

                pygame.draw.rect(screen, BLACK, rect, 1)

    # on initialise
    jardinJoueur, jardinSecret, typesRestants, parterresRestants, nbArrosage, gagne, perdu, graine, message = reset()
    bouton_retour = None
    bouton_rejouer = None

    running = True
    while running:
        clock.tick(60)
        screen.blit(bg_minijeu, (0, 0))
        # on vérifie
        if not gagne and parterresRestants == 0:
            gagne = True
            non_obtenues = [p for p in inventaire.plantes if not inventaire.plantes[p]]

            if non_obtenues:
                graine = random.choice(non_obtenues)
            else:
                graine = random.choice(list(inventaire.plantes.keys()))
            
            inventaire.ajouter_graine(graine)
            

        if not perdu and nbArrosage <= 0 and parterresRestants > 0:
            perdu = True

        
        dessiner_grille(jardinJoueur, jardinSecret, perdu)


        screen.blit(font.render(f"Arrosages restants : {nbArrosage}", True, BLACK), (550, 120))
        screen.blit(font.render("Parterres restants :", True, BLACK), (550, 150))
        y_info = 175
        for taille, nb in typesRestants.items():
            screen.blit(font.render(f"  {nb} parterre(s) de {taille} cases", True, BLACK), (550, y_info))
            y_info += 25

    
        screen.blit(font.render(message, True, BLACK), (550, 90))


        if gagne:
            screen.blit(font.render("Bravo ! Jardin arrosé !", True, GREEN), (550, 300))
            screen.blit(font.render(f"Plante : {graine}", True, GREEN), (550, 330))
            bouton_rejouer = pygame.Rect(580, 370, 150, 40)
            pygame.draw.rect(screen, (0, 200, 0), bouton_rejouer, border_radius=8)
            screen.blit(font.render("Rejouer", True, WHITE), (615, 382))


        elif perdu:
            screen.blit(font.render("Perdu... ", True, RED), (600, 300))
            bouton_rejouer = pygame.Rect(580, 340, 150, 40)
            pygame.draw.rect(screen, (0, 200, 0), bouton_rejouer, border_radius=8)
            screen.blit(font.render("Rejouer", True, WHITE), (615, 352))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_retour and bouton_retour.collidepoint(event.pos):
                    return

                if (gagne or perdu) and bouton_rejouer and bouton_rejouer.collidepoint(event.pos):
                    jardinJoueur, jardinSecret, typesRestants, parterresRestants, nbArrosage, gagne, perdu, graine, message = reset()

                if not gagne and not perdu:
                    mx, my = event.pos
                    j = (mx - OFFSET_X) // CELL_SIZE
                    i = (my - OFFSET_Y) // CELL_SIZE
                    if 0 <= i < GRID_SIZE and 0 <= j < GRID_SIZE:
                        if jardinJoueur[i][j] == "0":
                            parterresRestants, message = arrosage(i, j, jardinJoueur, jardinSecret, typesRestants, parterresRestants)
                            nbArrosage -= 1

        bouton_retour = dessiner_bouton_retour(screen)
        pygame.display.flip()
