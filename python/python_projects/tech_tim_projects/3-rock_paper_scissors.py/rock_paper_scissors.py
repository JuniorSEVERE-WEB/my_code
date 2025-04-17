import random 
print("Nou pral jwe jwet Rock Paper Scissors lan")

genyen = 0 
pedi = 0
nul = 0 

options = ["rock", "paper", "scissors"]



while True:
  user = input("Chwazi youn nan jwet sa yo:\n Rock/Paper/Scissors\n tape q pou w kite jwet lan ").lower()
  if user == "q":
    print("Jwet la kanpe")
    break 
  random_number = random.randint(0, 2)

  computer_pick = options[random_number]

  if user not in options:
    continue

  if user == computer_pick:
    print("Match nil ant itilizate ak computer a")
    nul += 1
    continue
  elif user == "rock" and  computer_pick == "scissors":
    print("You won!")
    genyen += 1
    continue
  elif user == "paper" and computer_pick == "rock":
    print("You won!")
    genyen += 1
    continue
  elif user == "scissors" and computer_pick == "paper":
    print("You won!")
    genyen += 1
    continue
  else:
    print("You lost!")
    pedi += 1 

print(f"Ou genyen {genyen} fwa, ou pedi {pedi} fwa e computer an ak ou fe {nul} egalizasyon")    