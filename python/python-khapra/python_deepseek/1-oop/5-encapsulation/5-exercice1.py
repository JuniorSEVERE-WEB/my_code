"""
Exercice 1 : Classe "Thermostat"
Problème :
Crée une classe Thermostat avec :

Un attribut privé __temperature
(initialisé à 20).

Une méthode augmenter() qui ajoute
 1°C.

Une méthode afficher() qui retourne 
la température.

Bonus : La température ne peut pas 
dépasser 30°C.
"""
class Thermostat:
  def __init__(self, temperature):
    self.__temperature = temperature

  def augmenter(self):
    self.__temperature += 1
    print(f"La temperature passe a {self.__temperature}")


  def afficher(self):
    if self.__temperature <= 30:
      print(f"La temperature qui est inf a 30 est : {self.__temperature}")
    else:
      print("Temperature maximale atteinte")  
    
    
t1 = Thermostat(30) 
t1.augmenter()       
t1.afficher()