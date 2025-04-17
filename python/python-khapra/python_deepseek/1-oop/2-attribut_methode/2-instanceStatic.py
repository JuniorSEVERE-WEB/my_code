"""
Attributs et Méthodes (différence entre self, méthodes d'instance vs statiques).
"""

class Etudiant:
  def __init__(self, nom, note):
    self.nom = nom
    self.note = note 

  def resultat(self):
    print(f"Bonjour {self.nom} ta note est {self.note}")  

  @staticmethod
  def is_valid(note):
    return 0 <= note <= 20

etudiant1 = Etudiant("Junior", 10)
etudiant2 = Etudiant("Obed", 26)

etudiant1.resultat()
# etudiant2.resultat()