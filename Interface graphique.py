import pygame ; import main ; import os ; import time

os.chdir(os.path.dirname(os.path.abspath(__file__))) # Permet de définir ce fichier comme fichier de base pour les importations

pygame.init()
ecran_largeur = 1000 ; ecran_hauteur = 600

screen = pygame.display.set_mode((ecran_largeur, ecran_hauteur))
clock = pygame.time.Clock() ; FPS = 60

while True:
    clock.tick(FPS)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()

pygame.quit()