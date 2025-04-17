"""
Exercice 1 : Gestion d'Étudiants et Pro-
fesseurs
Problème :
Crée une classe Personne avec nom et âge.

Une classe Étudiant qui hérite de Personne
 et ajoute classe.

Une classe Professeur qui hérite de Personne
 et ajoute matière.
"""
class Personne:
  def __init__(self, nom, age):
    self.nom = nom
    self.age = age 

  def nameAge(self):
    print(f"{self.nom} a {self.age} ans.")  

class Etudiant(Personne):
  def __init__(self, nom, age, classe):
    super().__init__(nom, age)
    self.classe = classe 

  def nameAgeClasse(self):
    print(f"{self.nom} a {self.age} ans, il est en {self.classe}") 

class Professeur(Personne):
  def __init__(self, nom, age, matiere):
    super().__init__(nom, age)
    self.matiere = matiere 

  def nameAgeMatiere(self):
    print(f"{self.nom} a {self.age}, il est prof de {self.matiere}")  

c1 = Etudiant("Junior", 30, "NS4")
c1.nameAgeClasse()
c2 = Professeur("Junior", 30, "ETAP")
c2.nameAgeMatiere()

