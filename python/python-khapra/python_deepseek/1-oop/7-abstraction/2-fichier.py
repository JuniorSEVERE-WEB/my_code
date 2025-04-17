from abc import ABC, abstractmethod

class Animal(ABC):
  @abstractmethod
  def parler(self):
    pass 

class Chien(Animal):
  def parler(self):
    print("Woof! woof!")

class Chat(Animal):
  def parler(self):
    print("Miaou!")    

chien = Chien()
chien.parler()    