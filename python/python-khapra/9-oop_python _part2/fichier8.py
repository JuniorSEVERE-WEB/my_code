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
    self.brand = brand
    self.type = type

car1 = ToyotaCar("prius", "electric")
print(car1.type) # li mache