class Calculatrice:
  @staticmethod
  def add(a, b):
    return a + b
  
  @staticmethod
  def mult(a, b):
    return a * b 
  
c1 = Calculatrice.add(3, 4)
print(c1)
c2 = Calculatrice.mult(3, 4)
print(c2)