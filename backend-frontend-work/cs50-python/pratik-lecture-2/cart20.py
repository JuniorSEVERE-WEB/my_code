def main():
  number = getNumber()
  mama(number)

def getNumber():
  n = int(input("Tape nomb liy # ou vle paret kolon lan: "))
  while n < 0:
    n = int(input("Tape yon nomb pozitif pito: "))
  return n

def mama(number):
  print("#\n" * number)  

main()