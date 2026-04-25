import pygame ; from soufflecendre import * ; import os

os.chdir(os.path.dirname(os.path.abspath(__file__))) # Permet de définir ce fichier comme fichier de base pour les importations

pygame.init() # Démarre pygame
ecran_largeur = 1000 ; ecran_hauteur = 600 # Taille écran → possible récup taille écran pour afficher en plein écran

screen = pygame.display.set_mode((ecran_largeur, ecran_hauteur)) # Définit écran
clock = pygame.time.Clock() ; FPS = 60 # Gestion FPS dans la boucle tout en bas, met une limite max de FPS

def image(nom):
    img = pygame.image.load("images//epreuves//plateau//" + nom + ".png").convert_alpha()
    return img

pygame.display.set_caption("Soufflecendre") # Change le nom de la fenêtre du jeu

cases = {
    "case_vide" : image("case_vide"),
    "colonne" : image("colonne"),
}

plateau = Plateau("case_vide")
plateau[Case.F] = "colonne"

def afficher_cases(plateau):
    for case in plateau.cases:
            screen.blit(cases[plateau[case]], (case.x*100 + ecran_largeur//2-200, case.y*100))


while True:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    afficher_cases(plateau)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()