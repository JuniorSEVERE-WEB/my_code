import inflect 

p = inflect.engine()

names = []

while True:
  try:
    name = input("Name: ")
    names.append(name)


  except EOFError:
    print()
    break

output = p.join(names)
print("Audieu, audieu, to " + output)
print(output)  

# install pip inflect