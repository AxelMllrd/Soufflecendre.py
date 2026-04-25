from soufflecendre import *

epreuve: Epreuve = Epreuve(Case.B)
epreuve.distance_joueur._valeurs.pop(Case.F)
epreuve.actu_distance_joueur()

plateau: Plateau[int] = epreuve.distance_joueur
# print plateau
x_min: int = 0
x_max: int = 0
y_min: int = 0
y_max: int = 0
for c in plateau.cases:
    if c.x > x_max:
        x_max = c.x
    if c.x < x_min:
        x_min = c.x
    if c.y > y_max:
        y_max = c.y
    if c.y < y_min:
        y_min = c.y


for y in range(y_min, y_max + 1):
    for x in range(x_min, x_max + 1):
        c: Case = Case(x, y)
        if plateau.existe(c):
            print(f"[{plateau[c]}]", end = "")
        else:
            print("[X]", end = "")
    print(end = "\n")