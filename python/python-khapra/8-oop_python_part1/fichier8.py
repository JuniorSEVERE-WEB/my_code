"""
Methods are functions that belong to objects
"""

class student:
  def __init__(self, fullname):
    self.name = fullname

  def hello(self):
    print("hello", self.name)

s1 = student("Junior")
s1.hello()      