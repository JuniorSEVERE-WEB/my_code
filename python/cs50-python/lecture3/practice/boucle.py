while True:
  try:
    x = int(input("aantre yon antye: "))
    break
  except ValueError:
    print("x is not an integer")
print(f"x is {x}")    