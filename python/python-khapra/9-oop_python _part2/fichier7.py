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
  def __init__(self, brand):
    self.brand = brand

car1 = ToyotaCar("prius")
print(car1.type) # li pa mache