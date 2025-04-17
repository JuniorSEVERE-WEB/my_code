class student:
  college_name = "ABC College"
  name = "anonymous" #class attr

  def __init__(self, name, marks):
    self.name = name #obj attr > class attr
    self.marks = marks

    print("Junior, redwi tan rezo sosyo ou yo")

s1 = student("Junior", 30)
print(s1.name, s1.marks)

print(student.college_name)
print(student.name) #no make sense


"""
class & instance attributes

class.attr
obj.attr
"""