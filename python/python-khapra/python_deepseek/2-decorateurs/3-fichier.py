def logger(fonction):
  def fonction_modifie(*args, **kwargs):
    print(f"Appel de {fonction.__name__} avec args={args}, kwargs={kwargs}")
    resultat = fonction(*args, **kwargs)
    print(f"Resultat: {resultat}") 
    return resultat
  return fonction_modifie 

@logger
def addition(a, b):
  return a + b
addition(3, 5) 

