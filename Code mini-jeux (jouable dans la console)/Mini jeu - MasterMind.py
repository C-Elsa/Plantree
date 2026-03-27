#Projet : Plantree
#Auteurs : Elsa CHEN, Sami OULHI

from random import randint
import pygame, sys


couleurs=['rouge','vert','bleu','jaune','noir'] # couleurs disponibles dans ce jeu.

def tirage(couleurs):
    resultat = []
    indiceMax = len(couleurs) - 1
    for i in range (0, 4) :
        resultat.append(couleurs[randint(0,indiceMax)])
    return resultat                             


def nbCouleursBienPlacees(tirage,essai):
    BP = 0
    for i in range (0, 4) :
        if tirage[i]==essai[i] :
            BP = BP + 1
    return BP
       
    # Renvoie le nombre de pions colorés ayant la même position dans les listes essai et tirage.
    # essai: liste de 4 couleurs: 4 pions colorés ordonnés choisis par le joueur.
    # tirage: liste de 4 couleurs: 4 pions colorés ordonnés que le joueur doit deviner.
    # couleurs possibles: 'rouge','vert','bleu','jaune','noir'
    
def nbCouleursMalPlacees(tirage,essai):
    MP = 0
    tirage1 = []
    essai1 = []

    for i in range(len(tirage)):
        if tirage[i] != essai[i]:
            tirage1.append(tirage[i])
            essai1.append(essai[i])

    for couleur in essai1:
        if couleur in tirage1:
            MP += 1
            
    return MP


    # Renvoie le nombre de pions colorés communs aux listes essai et tirage mais qui n'ont pas la même position.
    # essai: liste de 4 couleurs: 4 pions colorés ordonnés choisis par le joueur.
    # tirage: liste de 4 couleurs: 4 pions colorés ordonnés que le joueur doit deviner.
    
    
def demandeEssai():
    joueur = input("Entrez votre proposition de 4 couleurs : ")
    essai = []
    if len(joueur) == 4 :
        for i in range (0, 4) :
            if joueur[i] == "v" :
                essai.append("vert")
            if joueur[i] == "b" :
                essai.append("bleu")
            if joueur[i] == "r" :
                essai.append("rouge")
            if joueur[i] == "n" :
                essai.append("noir")
            if joueur[i] == "j" :
                essai.append("jaune")
    else :
        return False
    return essai
                    
               
    # Demande au joueur de rentrer sa proposition de 4 couleurs ordonnées (utiliser input(...))
    # Le joueur rentre sa liste de 4 couleurs à l'aide d'une suite de 4 lettres:
    # r pour rouge, v pour vert, b pour bleu, j pour jaune, n pour noir.
    # exemple: vbbj pour vert, bleu, bleu, jaune
    # Renvoie la liste des 4 couleurs proposées par le joueur: 
    #   c'est une liste de couleurs parmi 'rouge','vert','bleu','jaune','noir'
    # Renvoie False si la proposition du joueur ne contient pas 4 lettres correspondant à des couleurs
    
   
def jouerUnTour(code):
    essai = demandeEssai()
    if not essai:  
        print("Erreur : entrez 4 lettres correspondant aux couleurs !")
        return False
    
    BP = nbCouleursBienPlacees(code, essai)
    MP = nbCouleursMalPlacees(code, essai)
    
    print(f"Bien placées : {BP}, Mal placées : {MP}")
    
    if BP == 4:
        print("Bravo ! Vous avez trouvé le code !")
        return True
    else:
        return False

    # Procède à un nouveau tour de jeu: nouvel essai du joueur.
    # Affiche le nombre de pions bien placés et mal placés.
    # Renvoie True si le joueur a découvert les 4 couleurs, False sinon
    # tirage: liste de 4 couleurs: les 4 pions colorés ordonnés à deviner.
    
    
def masterMind():
    code = tirage(couleurs)  
    for i in range(8):
        gagne = jouerUnTour(code)
        if gagne == True:
            break
    else:
        print("Perdu ! Le code était :", code)

    #Joue au masterMind !
    
