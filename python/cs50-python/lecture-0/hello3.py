def main():
  name = input("Enter your name") 
  hello(name)

def hello(to="world!"):
  print(f"hello, {to}")

main()
