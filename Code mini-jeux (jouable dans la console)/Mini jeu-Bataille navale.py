#Projet : Plantree
#Auteurs : Elsa CHEN, Sami OULHI

from random import randint, choice
#bataille navale revisitée
#l'ocean est un jardin
#les bateaux sont des parterres de fleurs

jardinJoueur=[["0" for i in range(6)] for j in range(6)] # vision du joueur
jardinSecret=[["0" for i in range(6)] for j in range(6)] # jardin à trouver

parterresDeFleurs=[2,2,2,3,3,4] #bateaux : 3 parterres de fleurs de 2, 2 parterres de fleurs de 3 et 1 parterre de fleurs de 4

typesRestants={2:3, 3:2, 4:1} # ce qu'il reste à toucher, clé: type du parterre; valeur: nb qu'il reste

typeParterre={} #va associer le numero du parterre à sa taille

def placementParterre(jardin):
    numeroDuParterre= 1
    for taille in parterresDeFleurs :
        typeParterre[str(numeroDuParterre)] = taille
        placé = False
        while placé == False :
            direction=choice(["i","j"])#i:horizontale et j:verticale
        
            if direction == "i":   # placement horizontal
                i = randint(0,5)   # ligne aléatoire
                j = randint(0,6-taille)   # colonne aléatoire
                caseLibre = True   #suppose que la case est libre

                for k in range(taille): #vérifie chaque case du parterre
                    if jardin[i][j+k] != "0":
                        caseLibre = False   #la case est occupée
                        
                if caseLibre==True :
                    for k in range(taille):
                        jardin[i][j+k] = str(numeroDuParterre)  # on place le parterre 
                    placé = True
                    
            else : #placement vertical
                i = randint(0,6-taille)   
                j = randint(0,5)
                caseLibre = True

                for k in range(taille):
                    if jardin[i+k][j] != "0":
                        caseLibre = False

                if caseLibre == True :
                    for k in range(taille):
                        jardin[i+k][j] = str(numeroDuParterre)
                    placé = True
        numeroDuParterre = numeroDuParterre + 1   # on passe au parterre d'après
      
def parterreArrosé(numeroDuParterre): #vérifie si un parterre est completement arrosé
    for ligne in jardinSecret:   
        if numeroDuParterre in ligne:    # si une partie du parterre existe encore
            return False         
    return True

nbArrosage = 25

parterresRestants = len(parterresDeFleurs)

def arrosage(i,j):
    global parterresRestants
    caseChoisie = jardinSecret[i][j]
    if caseChoisie != "0": # 0 c'est la terre
        jardinJoueur[i][j] = "X" # X ça veut dire que y'avait un parterre
        jardinSecret[i][j] = "X"
        print("Arrosé !")
        
        if parterreArrosé(caseChoisie) == True :
            print(" Le parterre a été complètement arrosé !")
            taille = typeParterre[caseChoisie]
            typesRestants[taille] =  typesRestants[taille]  -1
            parterresRestants = parterresRestants - 1
                
    else :
        jardinJoueur[i][j] ="~" # ~ c'était juste de la terre         
        print("Raté !")
        
def affiche(jardin):
    lettres = ["A","B","C","D","E","F"] #lignes
    print("  1 2 3 4 5 6") # colonnes
    for i in range(6):          
        print(lettres[i], end=" ")  

        for j in range(6):      
            print(jardin[i][j], end=" ")
        print("")
            
def jeu():
    global nbArrosage
    placementParterre(jardinSecret)
    lettres = ["A","B","C","D","E","F"]
    chiffres = ["1","2","3","4","5","6"]

    while nbArrosage > 0 and parterresRestants > 0:
        print("Nombre de parterres à arroser : ")
            
        for Type in typesRestants :
            print(typesRestants[Type],"parterres de", Type,"cases")
        print("\nArrosage restants :", nbArrosage)
        print("")

        affiche(jardinJoueur)

        ligne = input("Ligne (A-F) : ").upper() #demande au joueur une lettre

        while ligne not in lettres:
            print("Erreur")
            ligne = input("Ligne (A-F) : ").upper()
        i = lettres.index(ligne)  #transforme la lettre en numéro de ligne

        colonne = input("Colonne (1-6) : ")

        while colonne not in chiffres :
            print("Erreur")
            colonne = input("Colonne (1-6) : ")
        j = chiffres.index(colonne)
        if 0 <= j < 6:
            print("")
            if jardinJoueur[i][j] != "0": #verifie si cette case n'avait pas été deja choisie avant
                print("Case déjà arrosé !")
            else :
                arrosage(i,j)
                nbArrosage = nbArrosage - 1

    if parterresRestants == 0:
        print("Bravo !")
        print("Tout les parterres ont été arrosé !")

    else:
        print("Perdu !")
        print("Vous ne pouvez plus arroser...")
        affiche(jardinSecret)
