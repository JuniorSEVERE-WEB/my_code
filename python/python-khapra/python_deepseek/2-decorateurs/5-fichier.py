def decorateur(fonction):
  def mache():
    print("Avant")
    fonction()
    
    print("Apres")
  return mache

@decorateur
def junior():
  print("Junior")
junior()    