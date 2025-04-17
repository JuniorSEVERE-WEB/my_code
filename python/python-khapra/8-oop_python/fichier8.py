"""
Methods are functions that belong to objects
"""
#creating class
class student:
  def __init__(self, fullname):
    self.name = fullname

  def hello(self):
    print("hello", self.name)


#creating object
s1 = student("Junior")

#methods (m panse)
s1.hello()      