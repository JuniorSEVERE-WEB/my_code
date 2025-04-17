

def main():
  number = getNumber()
  mama(number)

def getNumber():
  n = int(input("Tape nom de fwa ou vle messi paret: "))
  while n < 0:
    n = int(input("ou te tape yon nomb negatif: "))
    return n

def mama(n):
  print(f"Messi\n" * n)  

main()  


