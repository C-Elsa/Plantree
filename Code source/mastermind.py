import pygame
import sys
import random
import inventaire
from retour import dessiner_bouton_retour

def lancer_mastermind(screen) :
        

    WIDTH, HEIGHT = 1000, 600
    pygame.display.set_caption("Mastermind - Plantree")

    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None, 36)
    
    bouton_retour = None
    bouton_rejouer = None

    gagne = False
    perdu = False

    # couleurs possibles
    couleurs = ['rouge','vert','bleu','jaune','noir']

    # fleurs (images)
    fleurs = {
        "rouge": pygame.image.load("fleur_rouge.png"),
        "vert": pygame.image.load("fleur_verte.png"),
        "bleu": pygame.image.load("fleur_bleue.png"),
        "jaune": pygame.image.load("fleur_jaune.png"),
        "noir": pygame.image.load("fleur_noire.png")
    }

    bg_minijeu = pygame.image.load("arrierePlanMiniJeu.png").convert()
    bg_minijeu = pygame.transform.scale(bg_minijeu, (WIDTH, HEIGHT))
    
    graines = ["ail des ours", "algue brune", "algue rouge", "algue verte", "anémone des bois", "bouton d'or", "doronic d'autriche", "fougère mâle",  "immortelle des dunes",  "iris des marais","jonc épars", "lavande de mer",  "lys martagon","menthe aquatique", "nénuphar blanc",  "orchis mâle",  "ortie dioïque",  "oyat",  "panicaut maritime",  "pâquerette",  "pissenlit",  "posidonie",  "reine-des-prés",  "roquette de mer", "roseau commun",  "soucis d'eau",  "trèfle blanc", ]   
    for f in fleurs:
        fleurs[f] = pygame.transform.scale(fleurs[f], (50,50))

    # tirage du code
    def tirage():
        resultat = []
        for i in range(4):
            resultat.append(random.choice(couleurs))
        return resultat

    def nbCouleursBienPlacees(tirage,essai):
        BP = 0
        for i in range(4):
            if tirage[i]==essai[i]:
                BP += 1
        return BP


    def nbCouleursMalPlacees(tirage,essai):
        tirage1 = []
        essai1 = []
        for i in range(4):
            if tirage[i] != essai[i]:
                tirage1.append(tirage[i])
                essai1.append(essai[i])
        MP = 0
        tirage1_copie = tirage1.copy()
        for couleur in essai1:
            if couleur in tirage1_copie:
                MP += 1
                tirage1_copie.remove(couleur)  
        return MP


    code_secret = tirage()

    # grille
    grille = [["" for _ in range(4)] for _ in range(7)]
    resultats = []

    ligne_actuelle = 0
    colonne_actuelle = 0

    # palette de fleurs
    palette = ["rouge","vert","bleu","jaune","noir"]

    palette_rects = []

    for i in range(5):

        rect = pygame.Rect(250 + i*90, 520, 60, 60)
        palette_rects.append(rect)

    running = True

    while running:

        clock.tick(60)

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_BACKSPACE and colonne_actuelle > 0:
                    colonne_actuelle -= 1
                    grille[ligne_actuelle][colonne_actuelle] = ""

            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_retour and bouton_retour.collidepoint(event.pos):
                    return
                
                if (gagne or perdu) and bouton_rejouer and bouton_rejouer.collidepoint(event.pos):
                    return lancer_mastermind(screen)
            
                
                for i,rect in enumerate(palette_rects):

                    if rect.collidepoint(event.pos):
                        
                        if ligne_actuelle >= 7:
                            continue
                        
                        couleur = palette[i]

                        if colonne_actuelle < 4:

                            grille[ligne_actuelle][colonne_actuelle] = couleur
                            colonne_actuelle += 1

                        if colonne_actuelle == 4:

                            essai = grille[ligne_actuelle]

                            BP = nbCouleursBienPlacees(code_secret, essai)
                            MP = nbCouleursMalPlacees(code_secret, essai)

                            resultats.append((BP,MP))

                            if BP == 4:
                                gagne = True          
                                graine = random.choice(graines)
                                inventaire.ajouter_graine(graine)
                            else:
                                ligne_actuelle += 1
                                colonne_actuelle = 0

                                if ligne_actuelle >= 7:
                                    perdu = True
                    
        screen.blit(bg_minijeu, (0, 0))

        # afficher la grille

        for ligne in range(7):
            for col in range(4):

                couleur = grille[ligne][col]
            
                x = 260 + col*70
                y = 100 + ligne*60

                pygame.draw.rect(screen,(180,180,180),(x,y,50,50),2)

                if couleur != "":
                    screen.blit(fleurs[couleur], (x,y))

        # afficher résultats

        for i,(bp,mp) in enumerate(resultats):

            txt = font.render(f"{bp} BP  {mp} MP", True, (0,0,0))
            screen.blit(txt,(600, 110 + i*60))

        # palette

        for i,rect in enumerate(palette_rects):

            couleur = palette[i]
            screen.blit(fleurs[couleur], rect)
        
        if gagne:

            txt = font.render("Bravo ! Code trouvé !", True, (0,150,0))
            screen.blit(txt, (650,40))

            txt2 = font.render(f"Nouvelle graine obtenue : {graine}", True, (0,200,0))
            x_txt2 = (1000 - txt2.get_width()) // 2  # pour les plantes trop longues ! 
            y_txt2 = 80  

            screen.blit(txt2, (x_txt2, y_txt2))
            
            bouton_rejouer = pygame.Rect(750, 170, 150, 50)
            pygame.draw.rect(screen, (0, 200, 0), bouton_rejouer, border_radius=8)
            txt_rejouer = font.render("Rejouer", True, (255, 255, 255))
            screen.blit(txt_rejouer, (785, 183))
            

        if perdu:

            txt = font.render("Perdu !", True, (200,0,0))
            screen.blit(txt, (750,40))

            # afficher le code secret
            for i,couleur in enumerate(code_secret):
                screen.blit(fleurs[couleur], (720 + i*55, 90))
            
            bouton_rejouer = pygame.Rect(750, 170, 150, 50)
            pygame.draw.rect(screen, (0, 200, 0), bouton_rejouer, border_radius=8)
            txt_rejouer = font.render("Rejouer", True, (255, 255, 255))
            screen.blit(txt_rejouer, (785, 183))
            
    
        txt_aide1 = font.render("Appuyer sur BACKSPACE pour modifier votre choix", True, (60,60,60))
        screen.blit(txt_aide1, (20, 10))

        txt_aide2 = font.render("BP = Bien placées   MP = Mal placées", True, (60,60,60))
        screen.blit(txt_aide2, (200, 40))
        
        bouton_retour = dessiner_bouton_retour(screen)


        pygame.display.update()
