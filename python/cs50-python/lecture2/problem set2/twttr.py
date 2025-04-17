reponse = input("Input: ")
print("Outpout: ", end="")
for letter in reponse:
  if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(letter, end="")

print()    