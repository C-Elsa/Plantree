import pygame, sys
import mastermind
import inventaire
import biomes
import batailleNavale
import breakout
from retour import dessiner_bouton_retour
# 
pygame.init()
pygame.mixer.init()

etat = "menu"
etat_fin = None

# Fenêtre
WIDTH, HEIGHT = 1000, 600 # Dimensions de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Fenêtre
pygame.display.set_caption("Plantree") # Titre

clock = pygame.time.Clock()  

background = pygame.image.load("arrierePlanPlantree2.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

background1 = pygame.image.load("arrierePlanPlantreeIntro.png").convert()
background1 = pygame.transform.scale(background1, (WIDTH, HEIGHT))

bg_levels = [
    pygame.transform.scale(pygame.image.load("imagePrincipalNiv0.png").convert(), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load("imagePrincipalNiv1.png").convert(), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load("imagePrincipalNiv2.png").convert(), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load("imagePrincipalNiv3.png").convert(), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load("imagePrincipalNiv4.png").convert(), (WIDTH, HEIGHT)),
]


# Couleurs
GREEN = (138, 198, 165) 
LIGHT = (236, 244, 239) 
TITLE  = (120, 255, 210)
WHITE  = (210, 255, 240)
DARK   = (40, 110, 100)
BUTTON = (10, 40, 35)

VERT_FONCE = (40, 90, 60)
VERT_DOUX = (120, 170, 130)
VERT_CLAIR = (180, 220, 190)

BEIGE_FONCE = (120, 100, 70)
BEIGE = (200, 180, 140)

ROUGE_DOUX = (180, 80, 80)
VERT_SUCCES = (70, 150, 90)

NOIR_DOUX = (50, 50, 50)

# Polices
title_font = pygame.font.Font("Orbitron-Bold.ttf", 80)
btn_font = pygame.font.Font("Orbitron-Regular.ttf", 26) 

# Boutons
start_btn = pygame.Rect(WIDTH//2 - 170, 400, 340, 70)
quit_btn  = pygame.Rect(WIDTH//2 - 170, 500, 340, 70)
 
minijeux_btn = pygame.Rect(80, 420, 220, 70)
biome_btn = pygame.Rect(390, 420, 220, 70)
inventaire_btn = pygame.Rect(700, 420, 220, 70)

mastermind_btn = pygame.Rect(80, 300, 220, 70)
batnav_btn = pygame.Rect(390, 300, 220, 70)
breakout_btn = pygame.Rect(700, 300, 220, 70)

bouton_retour = pygame.Rect(0, 0, 0, 0)

quit_fin_btn = pygame.Rect(WIDTH//2 - 100, 360, 200, 60)
continuer_btn = pygame.Rect(WIDTH//2 - 100, 440, 200, 60)


# Texte
intro_textes = [
    "Des scientifiques ont découvert une nouvelle planète.",
    "Mais la flore y est réduite : l'un d'eux y est envoyé pour la développer.",
    "Catastrophe ! À l'atterrissage, il perd les sachets de graines à planter ...",
    "Aidez-le à retrouver les graines en jouant à des mini-jeux !",
    "À vous de rendre cette planète vivable !",
]

font = pygame.font.SysFont("Playfair Display", 38)

# Autres variables : 
alpha_intro = 0
alpha_principal = 0
score_global = 20
scroll_y = 0
niveau = 1

score_biomes = {
    "Forêt": 20,
    "Prairie": 20,
    "Mer": 20
}

score_global = 20

# Temps
temps_intro = 0  # en secondes

def biomes_niveau(score):
    if score < 30:
        return 0
    elif score < 45:
        return 1
    elif score < 60:
        return 2
    elif score < 80:
        return 3
    else:
        return 4   

running = True
while running: 
    
    dt = clock.tick(60) / 1000

    mouse = pygame.mouse.get_pos() 
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and etat == "menu":
            if start_btn.collidepoint(mouse):
                etat = "intro"
                temps_intro = 0
                pygame.mixer.music.load("artemis---30-seconds-of-epic-music-space-soundtrack.mp3")
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play()
            if quit_btn.collidepoint(mouse):
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and etat == "principal":
            if minijeux_btn.collidepoint(mouse):
                etat = "minijeux"
            elif biome_btn.collidepoint(mouse):
                etat = "biomes"
            elif inventaire_btn.collidepoint(mouse):
                etat = "inventaire"

        if event.type == pygame.MOUSEBUTTONDOWN and etat == "minijeux":
            if bouton_retour and bouton_retour.collidepoint(event.pos):
                etat = "principal"
            elif mastermind_btn.collidepoint(mouse):
                etat = "mastermind"
            elif batnav_btn.collidepoint(mouse):
                etat = "bataille navale"
            elif breakout_btn.collidepoint(mouse):
                etat = "breakout"

        if event.type == pygame.MOUSEBUTTONDOWN and etat == "inventaire":
            if bouton_retour and bouton_retour.collidepoint(event.pos):
                etat = "principal"

        if event.type == pygame.MOUSEWHEEL and etat == "inventaire":
            scroll_y -= event.y * 30
            scroll_y = max(0, scroll_y)
        
        if event.type == pygame.MOUSEBUTTONDOWN and etat == "fin":
            
            if quit_fin_btn.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

            if etat_fin == "victoire" and continuer_btn.collidepoint(event.pos):
                etat = "principal"
            
# fin des évènements  ---------------------------------------------------------------------


    if etat == "menu" :
        screen.blit(background, (0, 0)) # Le fond a un arriere plan défini au début


        title = title_font.render("Plantree", True, TITLE)
        screen.blit(title, title.get_rect(center=(WIDTH//2, 160)))


        for btn, text in [(start_btn, "START"), (quit_btn, "QUIT")]:
    
            color = DARK if btn.collidepoint(mouse) else WHITE
    
            pygame.draw.rect(screen, color, btn, border_radius=18)

            label = btn_font.render(text, True, BUTTON)
            screen.blit(label, label.get_rect(center=btn.center))
        
            
    if etat == "intro" :
        temps_intro += dt
        if alpha_intro < 255:
            alpha_intro += 2
        
        background1.set_alpha(alpha_intro)
        screen.blit(background1, (0, 0))

        # Texte 1 
        if temps_intro > 5 :
            t1 = font.render(intro_textes[0], True, (255, 255, 255))
            screen.blit(t1, t1.get_rect(center=(WIDTH//2, 220)))

        # Texte 2 
        if temps_intro > 11 :
            t2 = font.render(intro_textes[1], True, (255, 255, 255))
            screen.blit(t2, t2.get_rect(center=(WIDTH//2, 270)))

        # Texte 3
        if temps_intro > 17 :
            t3 = font.render(intro_textes[2], True, (255, 255, 255))
            screen.blit(t3, t3.get_rect(center=(WIDTH//2, 320)))
            
        if temps_intro > 23 :    
            t4 = font.render(intro_textes[3], True, (255, 255, 255))
            screen.blit(t4, t4.get_rect(center=(WIDTH//2, 360)))
        
        if temps_intro > 26 :
            t5 = font.render(intro_textes[4], True, (255, 255, 255))
            screen.blit(t5, t5.get_rect(center=(WIDTH//2, 400)))

        # Fin intro 
        if temps_intro > 32 :
            pygame.mixer.music.fadeout(2000)
            print("Intro terminée")
            etat = "principal"
            
    
    if etat == "principal" :
        if alpha_principal < 255:
            alpha_principal += 2
            
        niveau = biomes_niveau(score_global)

        bg = bg_levels[niveau]
        bg.set_alpha(alpha_principal)

        screen.blit(bg, (0, 0))

        score_text = font.render(f"Score planète : {score_global}/100", True, WHITE)
        screen.blit(score_text, (20, 20))


        for btn, text, color in [
            (minijeux_btn, "Mini-jeux", (242 ,227 , 204)),
            (biome_btn, "Biomes", (242 ,227 , 204)),
            (inventaire_btn, "Inventaire", (242 ,227 , 204))
        ]:
            
            if btn.collidepoint(mouse):
                pygame.draw.rect(screen, WHITE, btn, border_radius=12)
            else:
                pygame.draw.rect(screen, color, btn, border_radius=12)

            label = btn_font.render(text, True, DARK)
            screen.blit(label, label.get_rect(center=btn.center))
            
                    
    if etat == "minijeux":
        screen.fill((20,30,40))
        titre = title_font.render("Mini-jeux", True, WHITE)
        screen.blit(titre, (300,100))
        

        score_text = font.render(f"Score planète : {score_global}/100", True, WHITE)
        screen.blit(score_text, (20, 20))

        
        for btn, text, color in [
            (mastermind_btn, "MasterMind", (242 ,227 , 204)),
            (batnav_btn, "Bataille navale", (242 ,227 , 204)),
            (breakout_btn, "Breakout", (242 ,227 , 204))
        ]:
            
            if btn.collidepoint(mouse):
                pygame.draw.rect(screen, WHITE, btn, border_radius=12)
            else:
                pygame.draw.rect(screen, color, btn, border_radius=12)

            label = btn_font.render(text, True, DARK)
            screen.blit(label, label.get_rect(center=btn.center))
            
        bouton_retour = dessiner_bouton_retour(screen)
            
                   
    if etat == "mastermind":
        mastermind.lancer_mastermind(screen)
        bouton_retour = dessiner_bouton_retour(screen)
        etat = "principal"
    
    if etat == "bataille navale" :
        batailleNavale.bataille_navale(screen)
        bouton_retour = dessiner_bouton_retour(screen)
        etat = "principal"
    
    if etat == "breakout" :
        breakout.lancer_breakout(screen)
        bouton_retour = dessiner_bouton_retour(screen)
        etat = "principal"
                    
    if etat == "inventaire":
        screen.fill((30,40,30))
        inventaire.afficher(screen, scroll_y)
        bouton_retour = dessiner_bouton_retour(screen)
            
    if etat == "biomes":
        score_biomes = biomes.lancer_biomes(screen, score_biomes)
        score_global = (score_biomes["Forêt"] + score_biomes["Prairie"] + score_biomes["Mer"]) // 3

        if score_global >= 80:
            etat = "fin"
            etat_fin = "victoire"
        elif score_global <= 10:
            etat = "fin"
            etat_fin = "defaite"
        else:
            etat = "principal"
    
    if etat == "fin":
        bg = bg_levels[niveau]
        screen.blit(bg, (0, 0))
        
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 120)) 
        screen.blit(overlay, (0, 0))

        if etat_fin == "victoire":
            
            txt = font.render("MISSION ACCOMPLIE", True, VERT_VALID)
            screen.blit(txt, txt.get_rect(center=(WIDTH//2, 250)))


        elif etat_fin == "defaite":
            
            txt = font.render("MISSION ECHOUEE", True, ROUGE_DOUX)
            screen.blit(txt, txt.get_rect(center=(WIDTH//2, 250)))

        pygame.draw.rect(screen, BEIGE_FONCE, quit_fin_btn, border_radius=10)
        txt_quit = font.render("QUIT", True, BEIGE)
        screen.blit(txt_quit, txt_quit.get_rect(center=quit_fin_btn.center))


        if etat_fin == "victoire":
            
            pygame.draw.rect(screen, VERT_FONCE, continuer_btn, border_radius=10)
            txt_cont = font.render("CONTINUER", True, BEIGE)
            screen.blit(txt_cont, txt_cont.get_rect(center=continuer_btn.center))
            
    pygame.display.update()
