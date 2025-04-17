class Forme:
 def aire():
  return 0
 
class Carre(Forme):
 def __init__(self, cote):
  self.cote = cote 

 def aire(self):
  return self.cote ** 2
 
class Cercle(Forme):
 def __init__(self, rayon):
  self.rayon = rayon

 def aire(self):
  return (22/7) * self.rayon ** 2
 
carre = Carre(5)
cercle = Cercle(4)

print(carre.aire())
print(cercle.aire())




 