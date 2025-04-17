try:
  x = int(input("What's is x?: "))
  print(f"x is {x}")
  # if i type cat, it's an valueError
except ValueError:
  print("x is not an integer") 

