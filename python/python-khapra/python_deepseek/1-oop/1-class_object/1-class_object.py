# definition de la classe chien
class Chien:
  #Constructeur( methode speciale pour 
  #initialiser l'objet:  Méthode appelée à la
  #  création d'un objet.)
  def __init__(self, nom, age): #Méthode appelée:création d'un objet
    self.nom = nom  # Attribut "nom"
    self.age = age  # Attribut "age"
    #self : Représente l'objet lui-même(like"je" ou "moi").

  #methode pour aboyer
  def aboyer(self):
    print(f"{self.nom} dit: woof! woof!")

# Créer des Objets (Instances)    
#Un objet est une réalisation concrète de la classe.

#Creation de deux chiens differents
chien_1 = Chien("Junior", 3) #Chien_1 est une instance de Chien
chien_2 = Chien("Djefte", 13) 

#Acceder aux attributs 
print(chien_1.nom)
print(chien_2.age)

chien_1.aboyer()

