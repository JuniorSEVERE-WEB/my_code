class Utilisateur:
  def __init__(self, email, mdp):    
    self._email = email 
    self.__mdp = mdp

  def changer_mdp(self, ancien_mdp, nouveau_mdp):
    if ancien_mdp == self.__mdp:
      self.__mdp = nouveau_mdp   
      print("Mot de passe change!")
    else:
      print("Ancien mot de passe incorrect !")

u1 = Utilisateur("severejunior2017@gmail.com", 2011)
u1.changer_mdp(2011, 1994)
u1.changer_mdp(2000, 1994)
  