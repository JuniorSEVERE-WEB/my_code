#creation d'une classe
class Livre:
  #creation d'un constructeur, une methode
  #speciale: creation d'un objet
  def __init__(self, titre, auteur, pages):
    self.titre = titre 
    self.auteur = auteur 
    self.pages = pages 

  #self: objet lui meme
  #methode pour assembler les informations
  def info(self):
    print(f"Le titre de ce livre est: {self.titre} l'auteur s'appelle {self.auteur}, ce livre contient {self.pages} pages")
 
 # creation de deux livres
livre1 = Livre("La cigale et la fourmi", "Fontaine", 74)
livre2 = Livre("Le corbeau et le renard", "Montesquieu", 100)

#appeler un attribut
print(livre1.auteur)

#appeler la methode de l'info
livre1.info()
livre2.info()
