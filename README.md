# OC Projet 3 - Aidez Mac Gyver à s'échapper!

## Notice d'installation et de lancement:

* sur linux:
   * Clonez le repo github: `git clone https://github.com/remace/OC-P3-MacGyver.git`
   * Se placer dans le dossier du projet: `cd OC-P3-MacGyver`
   * Créez un environnement virtuel python: `virtualenv env`
   * Activez cet environnement: `source env/bin/activate`
   * Installez pygame dans cet environnement: `python -m pip install -r requirements.txt`
   * Exécutez le fichier laucher.py: `python launcher.py`
   
* sur windows:
   * Cloner le repo github `git clone https://github.com/remace/OC-P3-MacGyver.git`
   * Se placer dans le dossier du projet: `cd %CD%\OC-P3-MacGyver`
   * Créer un environnement virtuel python `virtualenv env`
   * Activer cet environnement `%CD%/env/scripts/activate.ps1`
   * Installer les dépendances dans cet environnement`python -m pip install -r requirements.txt`
   * Exécuter le fichier launcher.py `python launcher.py`

## Notice d'utilisation:

Vous contrôlez le personnage qui commence en haut à gauche du labyrinthe. Votre but est de s'en échapper en neutralisant le garde, qui est immobile, situé en bas à droite de l'écran.
Pour ce faire, vous pouvez:

* Vous déplacer avec les flèches du pavé directionnel, ou les touches 'z','q','s','d'.
* Ramasser un objet (représenté par un coffre) situé sous vos pieds grâce aux touches 'espace' et 'e'
* Défier le garde (personnage vert en bas à droite), en se plaçant sur la même case que lui:
    * Si vous avez ramassé les 3 objets nécessaires, vous gagnez
    * Sinon vous perdez
    
## Démarche de conception

* Conception des structures de données du jeu, et de leur représentation
    * Le labyrinthe est représenté par une liste de liste de lieux
    * Les personnages sont chacun l'instance d'une classe qui leur correspond
* Création du jeu textuel qui s'exécute dans le terminal, notamment:
    * Les mécaniques de déplacement
    * Les mécaniques liées aux objets
    * Savoir à la fin de la partie si le joueur a gagné et l'afficher
* Ajout au-travers de cette logique, de l'interface graphique, grâce à la librairie pygame, notamment:
    * Retravailler les images fournies pour le projet
    * Evenements clavier
    * Boucle d'affichage avec le labyrinthe, les objets et personnages, ainsi qu'un inventaire et des indications sur la case de départ
    * Quelques sons pour donner des informations au joueur
    * Supprimer tous les messages inutiles qui s'affichent dans la console (ceux qui ne mettent pas en avant un comportement du jeu)
* Retravailler le labyrinthe pour qu'il y ressemble vraiment, plutôt qu'à une pièce avec seulement 2 personnages et 3 coffres à l'intérieur.

## Difficultés rencontrées

RAS
