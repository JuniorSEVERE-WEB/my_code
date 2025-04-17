import time 

def decorateur(fonction):
  def complexe(*args, **kwargs):
    debut = time.time()
    regulat = fonction(*args, **kwargs)
    fin = time.time()
    print(f"ou dire {fin - debut:.2f} seondes")
    return regulat 
  return complexe

@decorateur 
def attendre(secondes):
  time.sleep(secondes)

attendre(2)  
