try:
  x = int(input("What's is x?: "))
# if i type cat, it's an valueError
except ValueError:
  print("x is not an integer") 
else:
  print(f"x is {x}")
