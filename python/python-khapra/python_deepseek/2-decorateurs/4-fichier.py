def decorateur(fonction):
  def fonction_age(age):
    if age < 18:
      raise ValueError("laj ou two piti")
    return fonction(age)
  return fonction_age

@decorateur 
def entrer_en_boite(age):
  return "Bienvenue au boite de nuit"

print(entrer_en_boite(20))
print(entrer_en_boite(30))