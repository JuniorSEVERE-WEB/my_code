class Pet():
  def __init__(self, name, age):
    self.name = name 
    self.age = age 

  def show(self):
    print(f"I am {self.name} and i am {self.age} years old")  

  def speak(self):
    print(f"I don't know what i say")  

class Cat(Pet):
  def speak(self):
    print("Meow")

class Dog(Pet):
  def speak(self):
    print("Bark")

class Fish(Pet):
  pass     

p = Pet("Junior", 30)
p.speak()
c = Cat("SEVERE", 23)
c.speak()    
d = Dog("Tim", 20)
d.speak()
f = Fish("Bubbles", 10)
f.speak()



  #inacheve  

