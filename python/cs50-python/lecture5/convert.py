def main():
  while True:
    au = input("Au: ")
    try:
      au = float(au)
      break
    except ValueError:
      continue

  print(f"{au} AU is {convert(au)} m")


def convert(au):
  if not isinstance(au, (int, float)):
    raise TypeError("au must be an int or float")
  return au * 149597870700

