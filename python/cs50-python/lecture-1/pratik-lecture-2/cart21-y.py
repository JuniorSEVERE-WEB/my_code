def main():
  lignes = int(input("Combien de lignes que tu veux?: "))
  colonnes = int(input("Combien de colonnes veux-tu?: "))
  dessinerRectangle(lignes, colonnes)

def dessinerRectangle(nbLignes, nbColonnes):
  for i in range(nbLignes):
      for j in range(nbColonnes):
         print("#", end="")
      print()   
main()
