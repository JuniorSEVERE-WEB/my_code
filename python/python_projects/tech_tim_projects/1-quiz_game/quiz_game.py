"""
Yon pwogram kote ou poze moun tan kesyon
kote ke nan fen pwogram lan, lap afiche kombyen
 kesyon ki te poze , konbyen
kesyon itilizate a reponn e kombyen li rate, 
lap afiche mwayen reyisit itilizate a tou
"""

print("nou pral jwe yon ti jwet, nap poze 4 kesyon")
score = 0
incorrect = 0
kesyon = 0

answer = input("Pa ki let nom Messi komanse: ").lower().strip()
if answer == "m":
  print("Correct")
  score += 1
else:
  print("Incorrect")  
  incorrect += 1
kesyon += 1  

answer = input("Pa ki let nom Neymar komanse: ").lower().strip()
if answer == "n":
  print("Correct")
  score += 1
else:
  print("Incorrect")  
  incorrect += 1
kesyon += 1  

answer = input("Banm siyati Junior: ").lower().strip()
if answer == "severe":
  print("Correct")
  score += 1
else:
  print("Incorrect")    
  incorrect += 1
kesyon += 1  

print(f" sou {kesyon} kesyon , ou reponn {score} kesyon korek, epi ou reponn {incorrect} kesyon enkorek")  
resultat = (score / 3) * 100
print(f"Ou fe {resultat:.2f} %")

print("Mesi deske w te jwe ak nou")  
