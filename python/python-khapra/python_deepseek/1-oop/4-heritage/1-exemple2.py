class Animal:
  def __init__(self, nom):
    self.nom = nom #attribut commun tous les animaux

  def manger(self):
    print(f"{self.nom} mange!") #methode commune

class Chien(Animal): #herite de Animal
  def __init__(self, nom, race):
    super().__init__(nom) #appelle le constructeur de Animal avec "nom"
    self.race = race #attribut specifique a Chien

  def info(self):
    print(f"{self.nom} est un {self.race}")
    
medor = Chien("Medor", "Labrador")
medor.info()
medor.manger()    
"""
4. Utilisation de super() pour Personnaliser le Constructeur
Si la classe enfant a un constructeur (__init__), on utilise super() pour appeler celui du parent :


"""