class person:
  __name__ = "anonymous"

  def __hello(self):
    print("hello person!")

  def welcome(self):
    self.__hello()

p1 = person()

print(p1.welcome())

"""
class person:
    def __hello(self):
        return "hello person!"  # Retourne la chaîne au lieu d'afficher

    def welcome(self):
        return self.__hello()  # Retourne la valeur de __hello()

p1 = person()
print(p1.welcome())  # Affiche "hello person!"
"""