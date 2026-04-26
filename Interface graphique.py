import pygame ; from soufflecendre import * ; import os

os.chdir(os.path.dirname(os.path.abspath(__file__))) # Permet de définir ce fichier comme fichier de base pour les importations

pygame.init() # Démarre pygame
ecran_largeur = 1200 ; ecran_hauteur = 800 # Taille écran → possible récup taille écran pour afficher en plein écran

screen = pygame.display.set_mode((ecran_largeur, ecran_hauteur)) # Définit écran
clock = pygame.time.Clock() ; FPS = 60 # Gestion FPS dans la boucle tout en bas, met une limite max de FPS

def image(nom: str):
    img = pygame.image.load("images//epreuves//plateau//" + nom + ".png").convert_alpha()
    return img

icone = image("icone")

pygame.display.set_caption("Soufflecendre") # Change le nom de la fenêtre du jeu
pygame.display.set_icon(icone) # Change la petite icone en haut à gauche, c'est juste esthétique

cases = {
    "case_vide" : image("case_vide"),
    "colonne" : image("colonne"),
    "joueur" : image("joueur"),
}

cartes = {
    "corruption" : image("corruption"),
    "cultiste" : image("cultiste"),
    "eclatee" : image("eclatee"),
}

plateau = Plateau("case_vide") # Création d'un vieux plateau random
plateau[Case.F] = "colonne"

joueur = Joueur(Case.M) # Joueur qui va démarrer case M allez


def afficher_cases(plateau: Plateau[str]):
    for case in plateau.cases:
            screen.blit(cases[plateau[case]], (case.x*100 + ecran_largeur//2-200, case.y*100 +100))

def afficher_cartes(joueur):
    x = 100
    for type_de_carte in joueur.cartes:
        for carte in type_de_carte:
            screen.blit(cartes[carte.nom], (x, ecran_hauteur-250))
            x += 100
            if x == 500:
                x += 200

def afficher_joueur(joueur):
    screen.blit(cases["joueur"], (joueur.position.x*100 + ecran_largeur//2-200, joueur.position.y*100 +100))

class Souris():
    def __init__(self):
        self.position = (0, 0)
        self.clique_etat = False # Pour éviter que ça clique 54646848 fois par seconde

    def clique(self):
        self.position = pygame.mouse.get_pos()
        self.clique_etat = True
        print(f"clic ! {self.position}")

    def clique_relache(self):
        self.clique_etat = False

souris = Souris() # La souris !

while True:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    afficher_cases(plateau)
    afficher_cartes(joueur)
    afficher_joueur(joueur)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not souris.clique_etat: # On appuie si on a pas déjà appuyé
            souris.clique()
        elif event.type == pygame.MOUSEBUTTONUP: # On relache la souris
            souris.clique_relache()
    

    pygame.display.update()