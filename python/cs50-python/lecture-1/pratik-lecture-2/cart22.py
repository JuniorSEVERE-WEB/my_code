def main():
  n = int(input("nombres lignes ou colonnes: "))
  dessinerTriangle(n)

def dessinerTriangle(nombre):
  for i in range(1, nombre + 1):
    for j in range(i):
      print("#", end="")
    print()

main()    