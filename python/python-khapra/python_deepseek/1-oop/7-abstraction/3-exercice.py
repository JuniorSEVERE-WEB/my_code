"""
Exercice 1 : Formes Géométriques
Problème :
Crée une classe abstraite Forme avec :
Méthode abstraite aire().
Méthode abstraite perimetre().
Ensuite, crée des classes Cercle et Rectangle qui implémentent ces méthodes.
"""
from abc import ABC, abstractmethod
import math

class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass

    @abstractmethod
    def perimetre(self):
        pass

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def perimetre(self):
        return 2 * math.pi * self.rayon

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)

# Test
cercle = Cercle(3)
print(cercle.aire())      # ~28.27
print(cercle.perimetre()) # ~18.84

rectangle = Rectangle(4, 5)
print(rectangle.aire())      # 20
print(rectangle.perimetre()) # 18