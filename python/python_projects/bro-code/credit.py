sum_odd_digit = 0 
sum_even_digit = 0 

cart_number = input("Antre nimewo kat ou: ")
cart_number = cart_number.replace("-", "")
cart_number = cart_number.replace(" ", "")
cart_number = cart_number[::-1]

for i in cart_number[::2]:
    sum_odd_digit += int(i)
    
for i in cart_number[1::2]:
    i = int(i) * 2
    if i >= 10:
        sum_even_digit += (1+(i % 10))
    else:
        sum_even_digit += i
        
total = sum_odd_digit + sum_even_digit
if total % 10 == 0:
    print("Cette carte est valide!")      
else:
    print("Cette carte est invalide! ")              


print(cart_number)