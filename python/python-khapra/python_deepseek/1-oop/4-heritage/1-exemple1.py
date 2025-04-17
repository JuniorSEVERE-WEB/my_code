class Animal:
  def __init__(self, nom):
    self.nom = nom #attribut commun tous les animaux

  def manger(self):
    print(f"{self.nom} mange!") #methode commune

class Chien(Animal): #herite de Animal
  def aboyer(self):
    print(f"{self.nom} dit: Woof!") #methode specifique du chien


rex = Chien("Rex")
rex.manger() #Rex mange 
rex.aboyer()#Rex dit : woof