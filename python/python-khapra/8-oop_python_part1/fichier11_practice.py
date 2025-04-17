"""
create student class that takes name & mark of 3 subjects as arguments in constructor
Then create a method to print the average
"""

class student:
  def __init__(self, name, mark1, mark2, mark3):
    self.name = name 
    self.mark1 = int(mark1)
    self.mark2 = int(mark2)
    self.mark3 = int(mark3)

  def moyenne(self):
     
    print(f"La moyenne de {self.name} est {(self.mark1 + self.mark2 + self.mark3) / 2}")

s1 = student("Junior", 60, 60, 60)    
s1.moyenne()