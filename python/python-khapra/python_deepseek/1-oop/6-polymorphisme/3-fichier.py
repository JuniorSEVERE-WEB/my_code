class Employe:
  def calculer_salaire(self):
    return 1000
  
class Manager(Employe):
  def calculer_salaire(self):
    return super().calculer_salaire() + 500
  
class Developpeur(Employe):
  def calculer_salaire(self):
    return super().calculer_salaire() + 300

manager = Manager()    
dev = Developpeur()

print(manager.calculer_salaire())