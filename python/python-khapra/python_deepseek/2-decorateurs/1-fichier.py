def decorateur(fonction):
  def fonction_modifie():
    print("Avant")
    resultat = fonction()
    print("Apres")
    return resultat
  return fonction_modifie

@decorateur
def hello():
  print("nan mitan")
hello()  