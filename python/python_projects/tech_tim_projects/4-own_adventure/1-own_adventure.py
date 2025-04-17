name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Wchich way would you like to go?").lower().strip()

if answer == "left":
  answer = input("You come to a river, you can walk around it or swim accross?Type walk to walk around and swim to swim sccross(swim/walk): ")

  if answer == "swim":
    print("You swim accross and were eaten by an alligator.")

  elif answer == "walk":
    print("You walk for many miles, ran out water and you lost the game")

  else:
    print("Not a valid option, you lose.")    

elif answer == "right":
  answer = input("You come to a bridge , it looks wobbly, do you do want to cross it or head back?(cross/back)?")
  
  if answer == "back":
    print("You go back and lose")

  elif answer == "cross":
    answer = input("You cross the bridge and meet a stranger. Do you talk to them(yes/no)").lower().strip()
    if answer == "yes":
      print("You talk to the stranger and they give you gold. You win!")

    elif answer == "no":
      print("You ignore the stranger")

    else:
      print("Not a valid option. You lose")  

  else:
    print("Not a valid option, you lose.")


else:
  print("Not a valid option. You lose.")

print(f"Thank you for trying {name} ")  

