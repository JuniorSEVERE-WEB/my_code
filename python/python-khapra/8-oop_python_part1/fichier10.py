class student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def hello(self):
    print(f"Byenvini {self.name}")

  def goodbye(self):
    return f" pouw konen laj ou ke w gen {self.age}"

s1 = student("Junior", 30)
s1.hello()

print(s1.goodbye())

