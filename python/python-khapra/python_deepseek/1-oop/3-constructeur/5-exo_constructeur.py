class Calculatrice:
  def __init__(self, marque):
    self.marque = marque 
    self.resultat = 0

  def additioner(self,nombre):
    self.resultat += nombre 
    print(f"le resultat, c'est {self.resultat}")
c1 = Calculatrice("ABM")
c1.additioner(4)    
c1.additioner(10)