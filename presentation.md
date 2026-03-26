# Plantree

## Présentation globale

Dans le cadre du thème de cette année, « Nature et Informatique », nous avons pensé à créer un jeu centré sur la flore. Le scénario final est le suivant : 
Dans le futur, à la suite d’une catastrophe naturelle, l’écosystème est menacé. L’environnement est presque détruit. Heureusement, des scientifiques ont trouvé une planète qui semble vivable non loin de la Terre. Cependant, la flore y est réduite. On y envoie alors un scientifique pour régler le problème mais lorsqu’il atterrit, il découvre avoir perdu les graines qu’il devait planter !

La problématique initiale consistait à déterminer quel type de jeu nous souhaitions créer, tout en mettant en place un système permettant au joueur de progresser et de gagner des graines de manière cohérente.

Notre choix s’est porté sur un ensemble de 3 mini-jeux à la suite des cours de NSI et au stage d’informatique (à EPITECH) que nous avions tous deux entrepris en seconde : un mastermind, une bataille navale ainsi qu’un breakout.
Nous avons également pensé à 3 biomes à remettre en état : une forêt, une prairie et enfin une plage.
Pour cela nous avons réalisé un système de score que le joueur doit augmenter en plaçant les plantes, qu’il aura préalablement remporté grâce aux mini-jeux, dans le bon biome. Le jeu comprend un système d’inventaire et de rareté de plantes.

## Présentation de l'équipe

CHEN Elsa : scénariste et codeuse, a mené les recherches sur les différentes plantes pour chaque biome pour, par la suite, s’occuper de leurs illustrations dans l’inventaire et a codé le mastermind et la bataille navale en python 

OULHI Sami : codeur, a réalisé le break out ainsi que l’interface du jeu, a généré le visuel et a adapté et intégré les codes Python dans le jeu.

Le temps passé est d’environ 35-40 heures chacun.

## Étapes du projet

1. Projet initial

A l’origine, nous étions partis sur un jeu avec un scénario un peu différent du scénario final : 
La flore de la Terre est détruite, mais des plantes ont survécus. Retrouvez-les et cultivez-les pour les replacer dans le bon biome pour sauver la Terre.
 Le jeu fonctionnerait donc avec un élément caché à trouver sur l’image de chaque biome et qui changerait de position. Une fois l’élément trouvé, le joueur gagnerait une plante et grâce à un système de cultivation, il augmenterait la quantité des plantes trouvées. 
Cependant nous avons découvert une incohérence dans le scénario : le joueur savait où replacer les plantes !

2. Changement de projet

Nous avons donc pris la décision de changer de projet en créant des mini-jeux et en modifiant le scénario.

3. Recherches

Pour chaque biome, nous avons réalisé des recherches pour sélectionner les plantes afin que cela soit le plus réaliste.

4. Codage des mini-jeux

Nous avons codé le mastermind grâce au cours sur les listes et la bataille navale à partir des tableaux à 2 dimensions.
Le breakout provient d’un code d’un jeu de pong individuel réalisé durant notre stage de seconde qui a été modifié pour devenir un breakout.

5. Génération des illustrations (visuel et plantes)

Nous avons cherché des illustrations libres de droit qui correspondait au visuel qu’on souhaitait. Après avoir enfin trouvé une image qui correspondait à nos attentes et libre de droit, nous avons découvert qu’elle avait été générée grâce à l’IA. 
Nous avons donc pris la décision de générer nous même des illustrations avec l’IA pour qu’elles correspondent complètement à notre projet.

Pour l’inventaire, chaque plante a été détourée puis mise en noir et blanc.
Ainsi, tant que les plantes n’ont pas été découvertes par le joueur, celles-ci seront en noir et blanc, et lorsque le joueur gagnera une plante, elle sera en couleur dans l’inventaire.

Chaque plante a un niveau de rareté (commune, rare…). Cela influence la fréquence à laquelle on peut les obtenir dans les mini-jeux et le nombre de points qu’elles rapportent (en effet, +5 pts pour les rares, +3 pour les peu communes et +2 pour les communes). Cela rend le jeu plus intéressant et ajoute un peu de hasard.

6. Codage de l’interface et adaptation des codes Python

Nous avons choisi la bibliothèque Pygame pour coder l’interface et adapté les codes Python graphiquement. 
Le fonctionnement du jeu repose sur une boucle principale qui gère les évènements utilisateurs (clics de souris, interactions clavier, …) ainsi que l’actualisation de l’affichage. Le jeu est organisé en plusieurs états (mini-jeux, biome, inventaire …), ce qui permet de gérer très facilement les différentes phases de jeu et les transitions entre elles. 


## Validation de l’opérationnalité et du fonctionnement 

1. Etat d’avancement du projet au moment du dépôt

Le projet est totalement fonctionnel.

2. Approches mises en œuvre pour vérifier l’absence de bugs

Nous avons testé chaque partie du programme séparément, puis l’ensemble du jeu une fois tout assemblé. Nous avons aussi vérifié que l’interface fonctionnait correctement. Ensuite, nous avons joué au jeu en essayant différentes actions pour repérer d’éventuels problèmes.
Nous avons notamment testé des cas particuliers, comme les doublons dans le Mastermind ou les placements limites dans la bataille navale. Cela nous a permis de détecter et corriger plusieurs bugs.

3. Difficultés rencontrées et solutions apportées :

Lors du codage du Mastermind, si la composition secrète comprenait plusieurs fois la même couleur, les informations de ‘mal placés’ s’avéraient incorrectes. Pour cela nous avons donc modifié notre algorithme en deux étapes : nous comptabilisons d’abord les « bien placés », puis nous travaillons sur des copies des deux combinaisons en retirant ces éléments. Ensuite nous comparons les couleurs restantes en tenant compte de leur nombre d’occurrences, ce qui permet d’éviter tout double comptage et d’obtenir un résultat correct. 

Lors du codage de la bataille navale, nous avons rencontré des difficultés par rapport au placement aléatoire des parterres (les bateaux). 
Les bateaux ne devaient pas se superposer ou dépasser de la grille.
Pour cela, nous avons créé une variable caseLibre et réalisé que les placements possibles pour un bateau était la longueur de la ligne ou de la colonne moins la taille du bateau. 
Ex : [0,0,0,0,0,0] si ceci est une ligne de 6 cases la grille
Nous voulons placer un bateau de 3 cases soit 1,1,1.
Les cas possibles sont [1,1,1,0,0,0], [0,1,1,1,0,0],[0,0,1,1,1,0] ou [0,0,0,1,1,1]
Soit le premier 1 est dans les positions 0, 1, 2, 3 donc (0,3)   or 3 = 6 (longueur ligne) – 3 (longueur bateau)
D’où randint(0,6-taille) qui devient randint(0, GRID_SIZE-taille)

Une difficulté importante a également été d’intégrer les différents mini-jeux et systèmes (interface, inventaire, score) dans un programme unique et cohérent, ce qui nous a demandé de bien organiser notre code et la structure du projet.
L’utilisation de commentaires nous a aidés à mieux structurer et comprendre le code, facilitant ainsi l’intégration des différents éléments. 
## Ouverture 

1. Idées d’améliorations du projet :

Nous aurions aimé réaliser nous même les illustrations mais nous n’avions pas pu par faute de temps.

Nous avons également pensé à améliorer le visuel des mini-jeux, à ajouter un système pour pouvoir jouer à la bataille navale contre une IA et à développer l’inventaire pour avoir des fiches informatives pour chaque plante, enfin, la modification de l’arrière plan en fonction du score aurait été intéressante. 


2. Conclusion :

Le jeu est assez complet, avec différents types de mini-jeux, ce qui le rend varié et plus intéressant à jouer. Il permet également d’apprendre le nom de certaines plantes ainsi que leur habitat, ce qui donne une petite dimension éducative au projet. 
Sa réalisation nous a fait prendre conscience de la complexité du développement d’un jeu vidéo : derrière un fonctionnement qui nous paraît un peu simple, il y a en réalité de nombreux aspects à gérer, comme la logique algorithmique, les interactions ou encore la correction des erreurs (qui ont été nombreuses !). 
Ce projet nous a donc permis de développer notre rigueur, notre capacité à résoudre des problèmes, mais aussi à organiser un programme plus complexe en combinant plusieurs fonctionnalités.

