name = input("Tape nom w: ")

with open("jjj.txt", "a") as f:
  f.write(f"{name}\n")