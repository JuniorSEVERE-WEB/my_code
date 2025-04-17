import random 
import string 

def generate_password(min_length, number = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits 
    special = string.punctuation 
    
    characters = letters 
    if number:
        characters += digits
    if special_characters:
        characters += special 
    
    pwd = ""    
    meets_criteria = False 
    has_number = False
    has_special = False 
    
    
    
    while not meets_criteria and len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            has_number = True 
        if new_char in special:
            has_special = True 
            
        meets_criteria = True
        if number: 
            meets_criteria = has_number 
        if special_characters:
            meets_criteria = meets_criteria and has_special  
            
    return pwd 



#C'est ici qu'on utilise la fonction pour créer un vrai mot de passe.        
min_length = int(input("Enter1 the miimum length: "))
has_number = input("Do1 you want to have numbers(y/n) ").lower() == "y"
has_special = input("Do1 you want to have special characters (y/n)? ").lower() == "y"  
pwd = generate_password(min_length, has_number, has_special)   
print(f"The generated password is : {pwd}")

    