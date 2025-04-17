#creation d'une classe de voiture
class Voiture:
  #creation d'un constructeur speciale
  #appelle : creation d'objet
  def __init__(self, marque, anne, pays):
    self.marque = marque #attribut
    self.anne = anne #attribut
    self.pays = pays #attribut
    #self: objet lui meme ()

  #methode pour decrire la voiture
  def description(self):
    print(f"machin sa , mak li se {self.marque} anne li se {self.anne} e pays machinn sa fet se {self.pays}")

  # ceation de deux voitures differents 
machine1 = Voiture("Tesla", 2020, "USA")  
machine2 = Voiture("Mercedes", 2018, "Japon")

#acceder a un attribut 
print(machine1.marque)

#acceder a un methode 
machine1.description()
machine2.description()



