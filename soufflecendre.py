from __future__ import annotations
from typing import TypeVar, Generic

from queue import Queue

T = TypeVar('T')

class Case:
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.x: int = x
        self.y: int = y

    def __add__(self, other: Case) -> Case:
        return Case(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Case) -> Case:
        return Case(self.x - other.x, self.y - other.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Case):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    A: Case
    B: Case
    C: Case
    D: Case
    E: Case
    F: Case
    G: Case
    H: Case
    I: Case
    J: Case
    K: Case
    L: Case
    M: Case
    N: Case
    O: Case
    P: Case

    liste: list[Case]

    HAUT: Case
    BAS: Case
    GAUCHE: Case
    DROITE: Case

Case.A = Case(0, 0)
Case.B = Case(1, 0)
Case.C = Case(2, 0)
Case.D = Case(3, 0)
Case.E = Case(0, 1)
Case.F = Case(1, 1)
Case.G = Case(2, 1)
Case.H = Case(3, 1)
Case.I = Case(0, 2)
Case.J = Case(1, 2)
Case.K = Case(2, 2)
Case.L = Case(3, 2)
Case.M = Case(0, 3)
Case.N = Case(1, 3)
Case.O = Case(2, 3)
Case.P = Case(3, 3)

Case.liste = [Case.A, Case.B, Case.C, Case.D, Case.E, Case.F, Case.G, Case.H, Case.I, Case.J, Case.K, Case.L, Case.M, Case.N, Case.O, Case.P]

Case.HAUT = Case(0, -1)
Case.BAS = Case(0, 1)
Case.GAUCHE = Case(-1, 0)
Case.DROITE = Case(1, 0)

# ---------------------------------------------------- #

class Noeud:
    def __init__(self, parent: Noeud | None, case: Case):
        self.parent: Noeud | None = parent
        self.case: Case = case
        self.suivants: list[Noeud | None] = []

    def parent_existe(self, parent: Case | Noeud) -> bool:
        n: Noeud = self
        case: Case
        if isinstance(parent, Noeud):
            case = parent.case
        else:
            case = parent

        while n.parent is not None:
            if n.parent.case == case:
                return True
            n = n.parent
        return False

# ---------------------------------------------------- #

class Entite:
    def __init__(self, case: Case):
        self.nom: str
        self.description: str
        self.position: Case = case
        self.blocage: int = 0

# ---------------------------------------------------- #

class Carte:
    INUTILISEE = 0
    DEFAUSSEE = 1
    ECLATEE = 2

    def __init__(self):
        self.nom: str
        self.etat = Carte.INUTILISEE

class Cultiste(Carte):
    def __init__(self):
        super().__init__()
        self.nom = "Cultiste"

class Corruption(Carte):
    def __init__(self):
        super().__init__()
        self.nom = "Corruption"

class Joueur(Entite):
    def __init__(self, case: Case):
        super().__init__(case)
        self.nom = "Joueur"
        self.cartes: list[list[Carte]] = [[Corruption() for _ in range(4)], [Cultiste() for _ in range(4)]]

# ---------------------------------------------------- # 

class Ennemi(Entite):
    def __init__(self, case: Case):
        super().__init__(case)
        self.nom = self.__qualname__
        self.blocage = 1
        self.degats = 1
        self.vitesse = 1
        self.portee = 1
    
    def mouv_qcq(self, epreuve: Epreuve, noeud: Noeud, dist: int) -> Noeud:
        for dep in [Case.HAUT, Case.BAS, Case.GAUCHE, Case.DROITE]:
            if not noeud.parent_existe(noeud.case + dep) and self.blocage < epreuve.blocage[self.position + dep]:
                if dist > 1:
                    noeud.suivants.append(self.mouv_qcq(epreuve, Noeud(noeud, noeud.case + dep), dist - 1))
                else:
                    noeud.suivants.append(Noeud(noeud, noeud.case + dep))
        return noeud
    
    def mouv_ligne(self, epreuve: Epreuve, noeud: Noeud, dist: int) -> Noeud:
        # Cas 1 : premier case de deplacement (initie le mouv)
        if noeud.parent is None:
           noeud.suivants.append(self.mouv_ligne(epreuve, Noeud(noeud, noeud.case + Case.HAUT), dist - 1))
           noeud.suivants.append(self.mouv_ligne(epreuve, Noeud(noeud, noeud.case + Case.BAS), dist - 1))
           noeud.suivants.append(self.mouv_ligne(epreuve, Noeud(noeud, noeud.case + Case.GAUCHE), dist - 1))
           noeud.suivants.append(self.mouv_ligne(epreuve, Noeud(noeud, noeud.case + Case.DROITE), dist - 1))
           return noeud
        
        # Cas 2 : le deplacement doit être le même que le précédent
        dep: Case = noeud.parent.case - noeud.case
        if self.blocage < epreuve.blocage[self.position + dep]:
            if dist > 1:
                noeud.suivants.append(self.mouv_ligne(epreuve, Noeud(noeud, noeud.case + dep), dist - 1))
            else:
                noeud.suivants.append(Noeud(noeud, noeud.case + dep))
        return noeud

    deplacement = mouv_qcq

    def attaque(self) -> int:
        return self.degats

class Objet(Entite):
    def __init__(self, case: Case):
        super().__init__(case)
        self.nom = self.__qualname__ 

    def actif(self) -> bool:
        return False

    def effet(self) -> None:
        pass

class Plateau(Generic[T]):
    def __init__(self, valeur_init: T):
        self._cases: list[T] = [valeur_init] * 16

    def __getitem__(self, key: int | Case) -> T:
        if isinstance(key, int):
            return self._cases[key]
        return self._cases[key.x + 4 * key.y]
    
    def __setitem__(self, key: int | Case, valeur: T) -> None:
        if isinstance(key, int):
            self._cases[key] = valeur
        else:
            self._cases[key.x + 4 * key.y] = valeur

class Epreuve:
    def __init__(self, joueur: Case):
        self.entites: Plateau[list[Entite]] = Plateau([])
        self.blocage: Plateau[int] = Plateau(0)
        self.distance_joueur: Plateau[int] = Plateau(0)
        self.joueur: Joueur = Joueur(joueur)
        self.ennemis: list[Ennemi] = []
        self.objets: list[Objet] = []

    def actu_blocage(self) -> None:
        for case in range(16):
            max: int = 0
            for entite in self.entites[case]:
                if not isinstance(entite, Ennemi) and entite.blocage > max:
                    max = entite.blocage
            self.blocage[case] = max
            
    def actu_distance_joueur(self) -> None:
        q: Queue[Case] = Queue()
        q.put(self.joueur.position)
        while not q.empty():
            c: Case = q.get()
            if self.distance_joueur[c]:
                pass

    def tour_joueur(self) -> None:
        pass

    def tour_ennemi(self) -> None:
        pass

    def fin(self) -> int: # 0 : RAS, >0 : victoire, <0 : defaite
        return 0

    def jouer(self) -> None:
        pass