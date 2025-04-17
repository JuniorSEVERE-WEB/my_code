def main():
  n = int(input("Nomb liy pou triang ekilateral lan: "))
  desineTriyangEkilateral(n)

def desineTriyangEkilateral(p):
  largeurMax = 2 * p 

  for i in range(1, p + 1):
    if i == 1:
      hashtags = 1
    else:
      hashtags = 2 * i

    print(("#" * hashtags).center(largeurMax))    


main()
