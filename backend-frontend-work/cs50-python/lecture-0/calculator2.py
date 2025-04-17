a = float(input("Enter a float number: "))
b = float(input("Enter an another float number: "))

c = round(a / b, 2) 
print(c) #0.67 instead 0.666666
print(f"{c:.2f}")
