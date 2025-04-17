"""
Exercice 1 : Classe "Compte Bancaire" 
(Encapsulation Avancée)
Problème :
Crée une classe CompteBancaire avec :

Attributs privés : __numero_compte (chaîne)
 et __solde (nombre).

Constructeur qui initialise ces attributs.

Méthode deposer(montant) qui ajoute un 
montant au solde.

Méthode retirer(montant) qui retire un 
montant si le solde le permet.

Méthode publique afficher_solde() qui 
retourne le solde.

Règles :

Le __solde ne doit jamais être négatif.

Le __numero_compte ne doit pas être 
modifiable après la création.
"""
class CompteBancaire:
  def __init__(self, numero_compte, solde_initial):
    self.__numero_compte = numero_compte
    self.__solde_initial = max(solde_initial, 0)
     
  def deposer(self, montant):
    self.__solde_initial += montant
    print(f"{self.__solde_initial}Euros Ajoutees")

  def retirer(self, montant):
    if self.__solde_initial > 0 and self.__solde_initial > montant:
      self.__solde_initial -= montant 
      print(f"{self.__solde_initial} Euros restes sur ton compte")
    else:
      print("Pas assez d'argent sur ton compte")

  def afficher_solde(self):
    return self.__solde_initial

c1 = CompteBancaire("HAS123434", 1000)
c1.deposer(100)
c1.retirer(500)            

    

