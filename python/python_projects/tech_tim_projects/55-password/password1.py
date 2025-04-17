from cryptography.fernet import Fernet

def write_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)

write_key()    

def view():
  with open("passwords.txt", "r") as f:
    for line in f.readlines():
      data = line.strip()
      user, passw = data.split("|")
      print(f"User: {user} Password: {passw}")


def add():
  name = input("Your name: ")
  password = input("Your password: ")

  with open("passwords.txt", "a") as f:
    f.write(f"{name}|{password}\n")

while True:
  mode = input("Type add or view to manage users or q to quit this program: ").lower().strip()
  if mode == "q":
    print("ou femen pwogram lan")
    break
  if mode == "add":
    add()
  elif mode == "view":
    view()
  else:
    print("Invalid mode")

