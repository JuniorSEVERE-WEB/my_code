
def main():
  n = int(input("Tape yon nombre, nap kalkile faktoryel li pou ou: "))
  fact = 1
  for i in range(1, n+1):
   fact = fact * i
  print(f"faktoryel {n} se {fact}") 

main()   
