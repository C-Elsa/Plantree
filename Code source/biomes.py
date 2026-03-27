#Projet : Plantree
#Auteurs : Elsa CHEN, Sami OULHI

import pygame
import sys
import inventaire
from retour import dessiner_bouton_retour

def lancer_biomes(screen, score_biomes):

    pygame.display.set_caption("Biomes - Plantree")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)
    font_small = pygame.font.SysFont(None, 24)

    # Rareté des plantes
    rarete = {}
    communes = ["pissenlit", "ortie dioïque", "fougère mâle", "trèfle blanc",
                "pâquerette", "bouton d'or", "jonc épars", "roseau commun",
                "algue verte", "algue brune", "oyat", "roquette de mer"]
    peu_communes = ["doronic d'autriche", "ail des ours", "anémone des bois",
                    "iris des marais", "soucis d'eau", "menthe aquatique",
                    "panicaut maritime", "immortelle des dunes", "lavande de mer"]
    rares = ["orchis mâle", "lys martagon", "nénuphar blanc", "reine-des-prés",
             "posidonie", "algue rouge"]

    for nom in communes:     rarete[nom] = ("Commune", 2)
    for nom in peu_communes: rarete[nom] = ("Peu commune", 3)
    for nom in rares:        rarete[nom] = ("Rare", 5)

    # Biomes des plantes
    biomes_plantes = {
        "algue brune": "Mer", "algue rouge": "Mer", "algue verte": "Mer",
        "posidonie": "Mer", "lavande de mer": "Mer", "roquette de mer": "Mer",
        "panicaut maritime": "Mer", "oyat": "Mer", "immortelle des dunes": "Mer",
        "ail des ours": "Forêt", "anémone des bois": "Forêt", "doronic d'autriche": "Forêt",
        "fougère mâle": "Forêt", "lys martagon": "Forêt", "orchis mâle": "Forêt",
        "ortie dioïque": "Forêt", "pissenlit": "Forêt", "trèfle blanc": "Forêt",
        "bouton d'or": "Prairie", "iris des marais": "Prairie", "menthe aquatique": "Prairie",
        "nénuphar blanc": "Prairie", "reine-des-prés": "Prairie", "roseau commun": "Prairie",
        "soucis d'eau": "Prairie", "pâquerette": "Prairie", "jonc épars": "Prairie"
    }
    
    # Couleurs
    VERT_FONCE = (34, 85, 34)
    VERT_CLAIR = (120, 170, 120)
    BEIGE = (245, 240, 220)
    BRUN = (120, 90, 60)
    ROUGE_DOUX = (170, 80, 80)
    VERT_VALID = (60, 140, 80)
    NOIR_DOUX = (40, 40, 40)
    
    # Images biomes
    img_foret   = pygame.transform.scale(pygame.image.load("imageBiomeForêt.png"),   (200, 150))
    img_prairie = pygame.transform.scale(pygame.image.load("imageBiomePrairie.png"), (200, 150))
    img_mer     = pygame.transform.scale(pygame.image.load("imageBiomeMer.png"),     (200, 150))

    bg_minijeu = pygame.image.load("arrierePlanMiniJeu.png").convert()
    bg_minijeu = pygame.transform.scale(bg_minijeu, screen.get_size())
    
    biomes = {
        "Forêt":   {"image": img_foret,   "rect": pygame.Rect(680, 80,  200, 150), "score": score_biomes["Forêt"]},
        "Prairie": {"image": img_prairie, "rect": pygame.Rect(680, 260, 200, 150), "score": score_biomes["Prairie"]},
        "Mer":     {"image": img_mer,     "rect": pygame.Rect(680, 440, 200, 150), "score": score_biomes["Mer"]},
    }

    mission_finie = False
    etat_mission = ""
    
    def get_plantes_disponibles():
        return {nom: qte for nom, qte in inventaire.graines_compteur.items() if qte > 0}
    
    def score_planete():
        total = sum(data["score"] for data in biomes.values())
        return round(total / 3)

    plante_selectionnee = None
    message = ""
    message_timer = 0
    bouton_retour = None
    
    running = True
    while running:
        clock.tick(60)
        plantes_disponibles = get_plantes_disponibles()
        
        score = score_planete()
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if bouton_retour and bouton_retour.collidepoint(event.pos):
                    return score_biomes

                if not mission_finie:
                    
                    
                    for i, nom in enumerate(plantes_disponibles):
                        rect_plante = pygame.Rect(30, 100 + i * 60, 45, 45)
                        if rect_plante.collidepoint(event.pos):
                            plante_selectionnee = nom


                    if plante_selectionnee:
                        for nom_biome, data in biomes.items():
                            if data["rect"].collidepoint(event.pos):
                                
                                bon_biome = biomes_plantes.get(plante_selectionnee)
                                pts = rarete.get(plante_selectionnee, ("Commune", 2))[1]

                                if nom_biome == bon_biome:
                                    data["score"] = min(100, data["score"] + pts)
                                    score_biomes[nom_biome] = data["score"]                       
                                    message = f"BRAVO ! +{pts} pts"
                                else:
                                    data["score"] = max(0, data["score"] - pts)
                                    score_biomes[nom_biome] = data["score"]
                                    message = f"NON ! -{pts} pts"

                                inventaire.planter(plante_selectionnee)
                                plante_selectionnee = None
                                message_timer = 90

                                if score_planete() >= 80 or score_planete() <= 10:
                                    mission_finie = True
                                
                                break

        
        
        screen.blit(bg_minijeu, (0, 0))


        screen.blit(font.render("Biomes", True, VERT_FONCE), (440, 10))
        screen.blit(font.render(f"Score planète : {score_planete()}/100", True, BRUN), (350, 45))


        if not plantes_disponibles:
            txt = font_small.render("Aucune plante disponible — gagne des mini-jeux !", True, BRUN)
            screen.blit(txt, (150, 70))
        else:
            txt = font_small.render("Sélectionne une plante puis clique sur son biome", True, NOIR_DOUX)
            screen.blit(txt, (200, 70))

        # Imags des plantes à gauche
        for i, (nom, qte) in enumerate(plantes_disponibles.items()):
            
            rect_plante = pygame.Rect(30, 100 + i * 60, 45, 45)
            img = pygame.transform.scale(inventaire.img_couleur[nom], (45, 45))
            
            screen.blit(img, rect_plante)
            nom_txt = font_small.render(nom, True, NOIR_DOUX)
            
            screen.blit(nom_txt, (rect_plante.right + 5, rect_plante.y + 5))
            qte_txt = font_small.render(f"x{qte}", True, BRUN)
            screen.blit(qte_txt, (rect_plante.right + 5 + nom_txt.get_width() + 10, rect_plante.y + 5))
            
            if nom == plante_selectionnee:
                pygame.draw.rect(screen, VERT_CLAIR, rect_plante, 3)
            r_nom, r_pts = rarete.get(nom, ("Commune", 2))
            
            couleur_rarete = (
            (120, 120, 120) if r_nom == "Commune"
            else (70, 130, 180) if r_nom == "Peu commune"
            else (200, 140, 50)
        )
            screen.blit(font_small.render(r_nom, True, couleur_rarete),
                        (rect_plante.right + 5, rect_plante.y + 22))
        
        
        # Images à droite (biom)
        for nom_biome, data in biomes.items():
            screen.blit(data["image"], data["rect"])
            screen.blit(font_small.render(nom_biome, True, VERT_FONCE),
                       (data["rect"].x, data["rect"].y - 35))
            screen.blit(font_small.render(f"Score : {data['score']}/100", True, BRUN),
                       (data["rect"].x, data["rect"].y - 18))

        
        if message_timer > 0:
            couleur = VERT_VALID if "BRAVO" in message else ROUGE_DOUX
            screen.blit(font.render(message, True, couleur), (300, 280))
            message_timer -= 1

        bouton_retour = dessiner_bouton_retour(screen)
        
        if mission_finie:
            return score_biomes
            
        pygame.display.update()

    return score_biomes
