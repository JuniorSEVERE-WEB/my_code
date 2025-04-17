def announce(f):
  def wrapper():
    print("Before....ok")
    f()
    print("Afeter...ok")
  return wrapper

@announce
def bonjour():
  print("Bonjour")  

bonjour()
