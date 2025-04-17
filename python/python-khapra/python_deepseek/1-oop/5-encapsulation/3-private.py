class CompteBancaire:
  def __init__(self, nom):
    self.__nom = nom

  def afficher_solde(self):
    print(f"Solde: {self.__nom}")  

compte = CompteBancaire("Junior")
compte.afficher_solde()    
print(compte._CompteBancaire__nom)  # ⚠️ Accès technique (name mangling)