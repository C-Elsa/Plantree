#Projet : Plantree
#Auteurs : Elsa CHEN, Sami OULHI

import pygame
import sys
import random
import inventaire
from retour import dessiner_bouton_retour

def lancer_breakout(screen):

    WIDTH, HEIGHT = 1000, 600
    pygame.display.set_caption("Breakout - Plantree")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)
    font_small = pygame.font.SysFont(None, 24)

    BLANC = (255, 255, 255)
    NOIR = (0, 0, 0)
    VERT = (0, 200, 0)
    ROUGE = (200, 0, 0)
    BLEU = (50, 100, 200)
    FOND = (10, 20, 40)

    bg_minijeu = pygame.image.load("arrierePlanMiniJeu.png").convert()
    bg_minijeu = pygame.transform.scale(bg_minijeu, (WIDTH, HEIGHT))
    

    raquette = pygame.Rect(WIDTH//2 - 60, HEIGHT - 40, 120, 15)
    raquette_vitesse = 7


    balle_x, balle_y = WIDTH//2, HEIGHT//2
    balle_dx, balle_dy = 4, -4
    balle_r = 10


    try:
        graine_img = pygame.transform.scale(pygame.image.load("graine.png"), (balle_r*2, balle_r*2))
        use_graine_img = True
    except:
        use_graine_img = False

    # Briques (plantes)
    BRIQUE_COLS = 10
    BRIQUE_ROWS = 5
    BRIQUE_W = 80
    BRIQUE_H = 30
    BRIQUE_MARGE = 5
    OFFSET_X = (WIDTH - (BRIQUE_COLS * (BRIQUE_W + BRIQUE_MARGE))) // 2
    OFFSET_Y = 60

    couleurs_briques = [
        (180, 60, 60), (180, 120, 60), (160, 180, 60),
        (60, 180, 100), (60, 140, 180)
    ]


    noms_plantes = list(inventaire.img_couleur.keys())
    imgs_briques = []
    for nom in noms_plantes[:BRIQUE_ROWS]:
        img = pygame.transform.scale(inventaire.img_couleur[nom], (BRIQUE_W, BRIQUE_H))
        imgs_briques.append(img)

    def creer_briques():
        briques = []
        for row in range(BRIQUE_ROWS):
            for col in range(BRIQUE_COLS):
                x = OFFSET_X + col * (BRIQUE_W + BRIQUE_MARGE)
                y = OFFSET_Y + row * (BRIQUE_H + BRIQUE_MARGE)
                briques.append(pygame.Rect(x, y, BRIQUE_W, BRIQUE_H))
        return briques


    vies = 5
    score = 0
    briques = creer_briques()
    gagne = False
    perdu = False
    bouton_retour = None
    bouton_rejouer = None
    graine_obtenue = ""

    graines = list(inventaire.plantes.keys())

    running = True
    while running:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_retour and bouton_retour.collidepoint(event.pos):
                    return
                if (gagne or perdu) and bouton_rejouer and bouton_rejouer.collidepoint(event.pos):
                    return lancer_breakout(screen)

        # Déplacement avec la souris
        if not gagne and not perdu:
            mouse_x = pygame.mouse.get_pos()[0]
            raquette.centerx = mouse_x
            raquette.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

            # Déplacement balle
            balle_x += balle_dx
            balle_y += balle_dy


            if balle_x - balle_r <= 0 or balle_x + balle_r >= WIDTH:
                balle_dx = -balle_dx
            if balle_y - balle_r <= 0:
                balle_dy = -balle_dy


            if balle_y + balle_r >= HEIGHT:
                vies -= 1
                balle_x, balle_y = WIDTH//2, HEIGHT//2
                balle_dx = random.choice([-4, 4])
                balle_dy = -4
                if vies <= 0:
                    perdu = True


            balle_rect = pygame.Rect(balle_x - balle_r, balle_y - balle_r, balle_r*2, balle_r*2)
            if balle_rect.colliderect(raquette) and balle_dy > 0:
                balle_dy = -balle_dy
                # angle selon où la balle le touche !
                offset = (balle_x - raquette.centerx) / (raquette.width / 2)
                balle_dx = offset * 5


            for brique in briques[:]:
                if balle_rect.colliderect(brique):
                    briques.remove(brique)
                    balle_dy = -balle_dy
                    score += 10
                    break


            if len(briques) == 0:
                gagne = True
                non_obtenues = [p for p in inventaire.plantes if not inventaire.plantes[p]]
                
                if non_obtenues:
                    graine_obtenue = random.choice(non_obtenues)
                else:
                    graine_obtenue = random.choice(graines)
                inventaire.ajouter_graine(graine_obtenue)



        screen.blit(bg_minijeu, (0, 0))


        for i, brique in enumerate(briques):
            row = (brique.y - OFFSET_Y) // (BRIQUE_H + BRIQUE_MARGE)
            if row < len(imgs_briques):
                screen.blit(imgs_briques[row], brique)
            else:
                pygame.draw.rect(screen, couleurs_briques[row % len(couleurs_briques)], brique, border_radius=4)
            pygame.draw.rect(screen, NOIR, brique, 1, border_radius=4)


        pygame.draw.rect(screen, VERT, raquette, border_radius=8)

        pygame.draw.circle(screen, VERT, (int(balle_x), int(balle_y)), balle_r)

        txt_vies = font.render(f"Vies : {vies}", True, NOIR)
        txt_score = font.render(f"Score : {score}", True, NOIR)
        screen.blit(txt_vies, (200, 20))
        screen.blit(txt_score, (WIDTH - 150, 20))


        if gagne:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 160))
            screen.blit(overlay, (0, 0))
            screen.blit(font.render("Bravo ! Plante remportée !", True, VERT), (320, 250))
            screen.blit(font_small.render(f"Graine obtenue : {graine_obtenue}", True, VERT), (380, 300))
            bouton_rejouer = pygame.Rect(420, 350, 150, 45)
            pygame.draw.rect(screen, VERT, bouton_rejouer, border_radius=8)
            screen.blit(font.render("Rejouer", True, BLANC), (455, 362))


        if perdu:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 160))
            screen.blit(overlay, (0, 0))
            screen.blit(font.render("Perdu... Plus de vies !", True, ROUGE), (350, 250))
            bouton_rejouer = pygame.Rect(420, 320, 150, 45)
            pygame.draw.rect(screen, VERT, bouton_rejouer, border_radius=8)
            screen.blit(font.render("Rejouer", True, BLANC), (455, 332))

        bouton_retour = dessiner_bouton_retour(screen)
        pygame.display.update()
