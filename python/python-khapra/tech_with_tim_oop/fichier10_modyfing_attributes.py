class Dog:

  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def get_name(self):
    return self.name  
  
  def get_age(self):
    return self.age 
  
  def set_age(self, age):
    self.age = age 

d = Dog("Tim", 24)
d.set_age(23)
print(d.get_name())
print(d.get_age())
d = Dog("Junior", 30)
print(d.get_name())
print(d.get_age())


"""
Cette expression, <class '__main__.Dog'>, est une représentation de la classe Dog en Python
"""