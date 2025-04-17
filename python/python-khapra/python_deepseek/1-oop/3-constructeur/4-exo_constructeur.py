class Livre:
  def __init__(self, titre, auteur, pages):
    self.titre = titre 
    self.auteur = auteur 
    self.pages = pages 
    self.is_emprunte = False 

  def emprunter(self):
    self.is_emprunte = True 
    print(f"Ce livre est prete, il a {self.pages} pages, il est ecrit par {self.auteur}, le titre est: {self.titre}")


c1 = Livre("Junior", "Livre de programmation", 100)
c1.emprunter()