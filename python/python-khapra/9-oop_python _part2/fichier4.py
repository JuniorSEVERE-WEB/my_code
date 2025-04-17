"""
when one class (child/derived) derives the
properties & method of another class(parent/base)
"""

class Car:
  @staticmethod
  def start():
    print("car started..")

  @staticmethod
  def stop():
    print("car stopped")

class ToyotaCar(Car):
  def __init__(self, name):
    self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)

"""

Type	Paramètre requis ?	Accès aux attributs ?	Exemple
Méthode "Normale"	Oui (self)	Oui (self.name)	def drive(self): ...
Méthode Statique	Non	Non	@staticmethod def start(): ...
"""