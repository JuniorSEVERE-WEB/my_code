class Pet():
  def __init__(self, name, age):
    self.name = name 
    self.age = age 

  def show(self):
    print(f"I am {self.name} and i am {self.age} years old")  

class Cat(Pet):
  def speak(self):
    print("Meow")

class Dog(Pet):
  def speak(self):
    print("Bark")

p = Pet("Junior", 30)
p.show()
c = Cat("SEVERE", 23)
c.show()    
d = Dog("Tim", 20)
d.show()



  #inacheve  

