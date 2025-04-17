from abc import ABC, abstractmethod 

class Animal(ABC): #(herite de ABC)
  @abstractmethod
  def parler(self):#Methode abstraite (sans code)
    pass #On ne met rien ici!

  