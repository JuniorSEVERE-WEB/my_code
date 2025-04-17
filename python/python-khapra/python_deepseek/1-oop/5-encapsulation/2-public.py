class Personne:
  def __init__(self, nom):
    self.nom = nom #attribut public

  def parler(self):
    print(f"{self.nom} parle ")

personne = Personne("Junior")
personne.parler()#Junior parle
print(personne.nom)# Junior
personne.nom = "CS50P"
personne.parler()    