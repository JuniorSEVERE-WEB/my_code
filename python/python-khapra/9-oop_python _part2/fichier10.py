"""
class method

a class method is bound to the 
class & receives the class as an implicit first argument

note -staic method can't acces or modify class & generally
for utility
"""

class Student:
  @classmethod #decorator 
  def college(cls):
    pass