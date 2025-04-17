reponse = input("Greeting:")

newReponse = reponse.lower().strip()

if 'hello' in newReponse:
  print("$0")
elif 'h' == newReponse[0]:
  print("$20")  
else:
  print("$100")  