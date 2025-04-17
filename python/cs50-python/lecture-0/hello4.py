def main():
  x = int(input("What's X?: "))
  print(f"x squared is {square(x)}")

def square(i):
  return pow(i, 2) #or  i ** 2

main()  