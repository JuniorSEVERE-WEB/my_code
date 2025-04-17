#definition de la classe
class Rectangle:
  #cration d'un constructeur, methode speciale
  # appele creation d'objet
  def __init__(self, longueur, largeur):
    self.longueur = longueur #attribut
    self.largeur = largeur 
    #self: objet lui meme(je ou moi)

  #methode pour l'aire
  def aire(self):
    print(f"La surface est {self.largeur * self.largeur}")

  #methode pour le permetre
  def perimetre(self):
    print(f"Le perimetre est: {self.longueur + self.largeur}")
  
  #creation de deux rectangles
rectangle1 = Rectangle(3, 4)
rectangle2 = Rectangle(4, 4)

  #appeler l'atribut d'un longueur
print(rectangle1.longueur)  

#methode pour appeler surface et le perimetre
rectangle1.aire()
rectangle2.perimetre()
    
