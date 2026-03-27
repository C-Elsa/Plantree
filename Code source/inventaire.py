import pygame

pygame.font.init()
font_inventaire = pygame.font.SysFont(None, 24)

ordre_acquisition = []

plantes = {
    "ail des ours": False, "algue brune": False, "algue rouge": False,
    "algue verte": False, "anémone des bois": False, "bouton d'or": False,
    "doronic d'autriche": False, "fougère mâle": False, "immortelle des dunes": False,
    "iris des marais": False, "jonc épars": False, "lavande de mer": False,
    "lys martagon": False, "menthe aquatique": False, "nénuphar blanc": False,
    "orchis mâle": False, "ortie dioïque": False, "oyat": False,
    "panicaut maritime": False, "pâquerette": False, "pissenlit": False,
    "posidonie": False, "reine-des-prés": False, "roquette de mer": False,
    "roseau commun": False, "soucis d'eau": False, "trèfle blanc": False,
}

graines_compteur = {nom: 0 for nom in plantes}

img_couleur = {
    "ail des ours": pygame.image.load("ail des ours couleur.png"),
    "algue brune": pygame.image.load("algue brune couleur.png"),
    "algue rouge": pygame.image.load("algue rouge couleur.png"),
    "algue verte": pygame.image.load("algue verte couleur.png"),
    "anémone des bois": pygame.image.load("anemone des bois couleur.png"),
    "bouton d'or": pygame.image.load("bouton d'or couleur.png"),
    "doronic d'autriche": pygame.image.load("doronic d'autriche couleur.png"),
    "fougère mâle": pygame.image.load("fougere male couleur.png"),
    "immortelle des dunes": pygame.image.load("immortelle des dunes couleur.png"),
    "iris des marais": pygame.image.load("iris des marais couleur.png"),
    "jonc épars": pygame.image.load("jonc epars couleur.png"),
    "lavande de mer": pygame.image.load("lavande de mer couleur.png"),
    "lys martagon": pygame.image.load("lys martagon couleur.png"),
    "menthe aquatique": pygame.image.load("menthe aquatique couleur.png"),
    "nénuphar blanc": pygame.image.load("nenuphar blanc couleur.png"),
    "orchis mâle": pygame.image.load("orchis male couleur.png"),
    "ortie dioïque": pygame.image.load("ortie dioique couleur.png"),
    "oyat": pygame.image.load("oyat couleur.png"),
    "panicaut maritime": pygame.image.load("panicaut maritime couleur.png"),
    "pâquerette": pygame.image.load("paquerette couleur.png"),
    "pissenlit": pygame.image.load("pissenlit couleur.png"),
    "posidonie": pygame.image.load("posidonie couleur.png"),
    "reine-des-prés": pygame.image.load("reine des pres couleur.png"),
    "roquette de mer": pygame.image.load("roquette de mer couleur.png"),
    "roseau commun": pygame.image.load("roseau commun couleur.png"),
    "soucis d'eau": pygame.image.load("soucis d'eau couleur.png"),
    "trèfle blanc": pygame.image.load("trefle blanc couleur.png"),
}

img_nb = {
    "ail des ours": pygame.image.load("ail des ours nb.png"),
    "algue brune": pygame.image.load("algue brune nb.png"),
    "algue rouge": pygame.image.load("algue rouge nb.png"),
    "algue verte": pygame.image.load("algue verte nb.png"),
    "anémone des bois": pygame.image.load("anemone des bois nb.png"),
    "bouton d'or": pygame.image.load("bouton d'or nb.png"),
    "doronic d'autriche": pygame.image.load("doronic d'autriche nb.png"),
    "fougère mâle": pygame.image.load("fougere male nb.png"),
    "immortelle des dunes": pygame.image.load("immortelle des dunes nb.png"),
    "iris des marais": pygame.image.load("iris des marais nb.png"),
    "jonc épars": pygame.image.load("jonc epars nb.png"),
    "lavande de mer": pygame.image.load("lavande de mer nb.png"),
    "lys martagon": pygame.image.load("lys martagon nb.png"),
    "menthe aquatique": pygame.image.load("menthe aquatique nb.png"),
    "nénuphar blanc": pygame.image.load("nenuphar blanc nb.png"),
    "orchis mâle": pygame.image.load("orchis male nb.png"),
    "ortie dioïque": pygame.image.load("ortie dioique nb.png"),
    "oyat": pygame.image.load("oyat nb.png"),
    "panicaut maritime": pygame.image.load("panicaut maritime nb.png"),
    "pâquerette": pygame.image.load("paquerette nb.png"),
    "pissenlit": pygame.image.load("pissenlit nb.png"),
    "posidonie": pygame.image.load("posidonie nb.png"),
    "reine-des-prés": pygame.image.load("reine des pres nb.png"),
    "roquette de mer": pygame.image.load("roquette de mer nb.png"),
    "roseau commun": pygame.image.load("roseau commun nb.png"),
    "soucis d'eau": pygame.image.load("soucis d'eau nb.png"),
    "trèfle blanc": pygame.image.load("trefle blanc nb.png"),
}

for dico in (img_couleur, img_nb):
    for plante in dico:
        dico[plante] = pygame.transform.scale(dico[plante], (100, 100))

def peut_planter(nom):
    return graines_compteur[nom] > 0

def planter(nom):
    if graines_compteur[nom] > 0:
        graines_compteur[nom] -= 1


def ajouter_graine(nom):
     if nom in plantes:
        graines_compteur[nom] = 3  # directement 3 graines d'un coup
        if not plantes[nom]:
            plantes[nom] = True
            ordre_acquisition.append(nom)
        print(f"Plante débloquée : {nom}")
        

def hauteur_totale():
    ESPACE = 140
    nb_lignes = (len(plantes) + 4) // 5
    return nb_lignes * ESPACE


def afficher(screen, scroll_y=0):
    TAILLE = 100
    ESPACE = 140
    MARGE_X = 150
    MARGE_Y = 80
    HEIGHT = 600

    x = MARGE_X
    y = MARGE_Y - scroll_y

    for plante in plantes:
        if -TAILLE < y < HEIGHT:
            image = img_couleur[plante] if plantes[plante] else img_nb[plante]
            screen.blit(image, (x, y))
            nom = font_inventaire.render(plante, True, (255, 255, 255))
            nom_x = x + (TAILLE - nom.get_width()) // 2
            screen.blit(nom, (nom_x, y + TAILLE + 5))

        x += ESPACE
        if x > 800:
            x = MARGE_X
            y += ESPACE
