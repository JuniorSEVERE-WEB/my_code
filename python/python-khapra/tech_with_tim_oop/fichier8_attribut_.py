class Dog:

  def __init__(self, name,):
    self.name = name
    
  def get_name(self):
    return self.name  

d = Dog("Tim")
print(d.get_name())
d = Dog("Junior")
print(d.get_name())


"""
Cette expression, <class '__main__.Dog'>, est une représentation de la classe Dog en Python
"""