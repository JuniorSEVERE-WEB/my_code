class CompteBancaire:
  def __init__(self, titulaire, solde):
    self.titulaire = titulaire 
    self.solde = solde 

class CompteEpargne(CompteBancaire):
  def __init__(self, titulaire, solde, taux_interet):
    super().__init__(titulaire, solde)
    self.taux_interet = taux_interet

  def ajouter_interets(self):
    interets = self.solde * self.taux_interet
    self.solde += interets 
    print(f"+ {interets}Euros d'interets !")

c1 = CompteEpargne("Junior", 1000, 0.05)
c1.ajouter_interets()
