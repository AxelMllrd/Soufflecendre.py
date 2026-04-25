import pygame ; from soufflecendre import * ; import os

os.chdir(os.path.dirname(os.path.abspath(__file__))) # Permet de définir ce fichier comme fichier de base pour les importations

pygame.init()
ecran_largeur = 1000 ; ecran_hauteur = 600

screen = pygame.display.set_mode((ecran_largeur, ecran_hauteur))
clock = pygame.time.Clock() ; FPS = 60

pygame.display.set_caption("Soufflecendre")

image_case_vide = pygame.image.load("images//epreuves//plateau//case_vide.png")

plateau = Plateau("vide")
plateau[Case.F] = "Colonne"

def afficher_cases(plateau):
    for case in plateau.cases:
        if plateau[case] == "vide":
            screen.blit(image_case_vide, (case.x*100, case.y*100))


while True:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    afficher_cases(plateau)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()