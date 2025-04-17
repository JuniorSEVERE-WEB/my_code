"""
5. Exercice pour Toi
Problème :
Crée une classe Email avec :

Une méthode statique valider_format(email
 qui vérifie si l'email contient @.

Une méthode d'instance envoyer() qui 
affiche "Email envoyé à [adresse]
"""
class Email:
  def __init__(self, adresse):
    self.adresse = adresse
    

  @staticmethod
  def valider_format(email):
    if "@" in email:
      return email
    
  def envoyer(self):
    print(f"email est envoye a {self.adresse}") 

if Email.valider_format("severejunior2017@gmail.com"):
  email1 = Email("seerejunior2017@gmail.com")
  email1.envoyer()