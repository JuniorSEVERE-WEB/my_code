import re

email = input("What's your email?: ").strip()


if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
  print("Valid")
else:
  print("Invalid")  


#when i type cs50 in the email #Invalid
#malan@cs50.havard.edu
