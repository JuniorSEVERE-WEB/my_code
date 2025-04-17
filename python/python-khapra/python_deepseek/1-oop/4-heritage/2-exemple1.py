class Vehicule:
  def __init__(self, marque):
    self.marque = marque 

  def demarrer(self):
    print(f"Le {self.marque} demarre!")

class Voiture(Vehicule):
  def __init__(self, marque, portes):
    super().__init__(marque)
    self.portes = portes 

  def klaxonner(self):
    print("Tut tut")

ma_voiture = Voiture("Peugeot", 5)
ma_voiture.demarrer()
ma_voiture.klaxonner()
