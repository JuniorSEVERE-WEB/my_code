montantDu = 50

while montantDu > 0:
  print(f"Amount Due: {montantDu} ")
  pieceDemonnaie = int(input("Insert Coin: "))

  #if pieceDemonnaie == 25 or pieceDemonnaie == 10 or pieceDemonnaie == 5:
  if pieceDemonnaie in [25, 10, 5]: 
    montantDu  -= pieceDemonnaie 

changementPropre = abs(montantDu)    

print(f"Change Owed: {changementPropre}")
