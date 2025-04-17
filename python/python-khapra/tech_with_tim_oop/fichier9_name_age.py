class Dog:

  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def get_name(self):
    return self.name  
  
  def get_age(self):
    return self.age 

d = Dog("Tim", 24)
print(d.get_name())
print(d.get_age())
d = Dog("Junior", 30)
print(d.get_name())
print(d.get_age())


"""
Cette expression, <class '__main__.Dog'>, est une représentation de la classe Dog en Python
"""