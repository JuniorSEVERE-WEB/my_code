"""
super method
super() method is used to acces methods 
of the parent class

"""


class Car:
    def __init__(self, type):
      self.type = type 


    @staticmethod
    def start():
      print("car started..")

    @staticmethod
    def stop():
      print("car stopped")

class ToyotaCar(Car):
  def __init__(self, brand, type):
    super().__init__(type)
    self.brand = brand
    super().start() #affiche car started
   

car1 = ToyotaCar("prius", "electric")
print(car1.type) 