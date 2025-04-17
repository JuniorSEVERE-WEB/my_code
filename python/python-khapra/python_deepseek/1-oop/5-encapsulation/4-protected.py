class Personne: 
  def __init__(self, nom):
    self._nom = nom 

  def parler(self):
    print(f" {self._nom} parle")

personne = Personne("Junior")
personne.parler()
print(personne._nom)#pas trop jolie
personne._nom = "CS50" #pas trop jolie
  