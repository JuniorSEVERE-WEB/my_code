from abc import ABC, abstractmethod

class Appareil(ABC):
  def allumer():
    pass
  def eteindre():
    pass 

class Tele(Appareil):
  def allumer(self):
    print("Allumer la tele")
  def eteindre(self):
    print("La tele s'est eteinte")

class Radio(Appareil):
  def allumer(self):
    print("Allumer la radio")
  def eteindre(self):
    print("La radio s'est eteinte")

c = Radio()
c.allumer()              