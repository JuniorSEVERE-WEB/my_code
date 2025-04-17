class Dog:

  def __init__(self):
    pass 

  def add_one(self, x):
    return x + 1
   
  def bark(self):
    print("bank")
 #method = fonction inside the class

d = Dog()

d.bark()


print(type(d))
print(d.add_one(5))
"""
Cette expression, <class '__main__.Dog'>, est une représentation de la classe Dog en Python
"""