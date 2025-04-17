class person:
  __name__ = "anonymous" # Attribut de classe
  
  #__nom_methode  self.__nom_methode()
  #Méthode "privée" __hello
  def __hello(self):
    print("hello person!")
  
  #Méthode publique welcome
  def welcome(self):
    self.__hello() ## Appel de la méthode privée

p1 = person()

print(p1.welcome())

"""
Particularité : __name__ est un attribut de classe (partagé par toutes les instances),
 pas une variable d'instance (comme avec __init__).

Attention : En Python, __name__ est normalement un attribut spécial qui stocke le nom d'une classe 
(ex: person.__name__ retourne "person"). Ici, il est redéfini comme "anonymous", ce qui est déconseillé
(cela peut causer des bugs).

def __hello(self):
    return "hello person!"  # Retourne la chaîne au lieu de l'afficher

def welcome(self):
    return self.__hello()   # Retourne la valeur de __hello()
"""