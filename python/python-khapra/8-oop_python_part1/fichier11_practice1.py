"""
create student class that takes name & mark of 3 subjects as arguments in constructor
Then create a method to print the average
"""

class student:
  def __init__(self, name, marks):
    self.name = name 
    self.marks = (marks)


  def moyenne(self):
    sum = 0
    for val in self.marks:
      sum += val
    print(f"La moyenne de {self.name} est {(sum) / 3}")

s1 = student("Junior", [100, 100, 100])    
s1.moyenne()