class Pet():
  def __init__(self, name, age):
    self.name = name 
    self.age = age 

  def show(self):
    print(f"I am {self.name} and i am {self.age} years old")  

  def speak(self):
    print(f"I don't know what i say")  

class Cat(Pet):
  def __init__(self, name, age, color):
    super().__init__(name, age)
    self.color = color
  # no no i  cal super()

  def speak(self):
    print("Meow")

  def show(self):
    print(f"I am {self.name} and i am {self.age} years old and i am {self.color}")   

    

class Dog(Pet):
  def speak(self):
    print("Bark")



p = Pet("Junior", 30)
p.speak()
c = Cat("SEVERE", 23, "Brown")
c.show()    
d = Dog("Tim", 20)
d.speak()




  #inacheve  

