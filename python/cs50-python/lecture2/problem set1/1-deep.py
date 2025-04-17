reponse = input("What is the answer to the Great Question of Life, the Universe and Everything?: ")
if reponse.strip() == "42":
  print("Yes")
elif reponse.lower().strip() == "forty-two":
  print("Yes")
elif reponse.lower().strip() == "forty two":
  print("Yes")  
else:
  print("No")  
