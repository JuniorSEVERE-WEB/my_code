class student:
  def __init__(self, name, age):
    self.name = name 
    self.age = age

  def hello(self):
    print(f"m rele {self.name} mwen gen {self.age} an")

s1 = student("Junior", 30)      
s1.hello()