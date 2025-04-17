"""
Résumé du fonctionnement
On importe les modules nécessaires (random, string).

On définit une fonction generate_password() qui prend des paramètres.

On prépare les caractères possibles (lettres, chiffres, symboles).

On initialise le mot de passe et les vérifications.

On génère le mot de passe caractère par caractère.

On vérifie si les critères sont respectés.

On retourne le mot de passe final.

On demande à l'utilisateur ses préférences et on affiche le résultat.
"""
#1
import random #permet de générer des choses de manière aléatoire 
import string #module contient des listes prédéfinies de caractères (lettres, chiffres, symboles).
#Ces modules sont nécessaires pour créer un mot de passe aléatoire.

 #2-Cette fonction prend des paramètres pour personnaliser le mot de passe
def generate_password(min_length, numbers=True, special_characters=True):#On crée une fonction qui génère un mot de passe. 
    letters = string.ascii_letters # Contient toutes les lettres (majuscules et minuscules).
    digits = string.digits # Contient tous les chiffres (0-9).
    special = string.punctuation # Contient les symboles (!@#$%^&*, etc.).
    
    #3-Caractères autorisés possibles
    #characters : Une chaîne qui accumule tous les caractères possibles pour le mot de passe.
    characters = letters ## On commence avec les lettres
    if numbers:
        characters += digits # # On ajoute les chiffres si demandé
    if special_characters:   
        characters += special # On ajoute les symboles si demandé
        
    #4-On initialise tout avant de générer le mot de passe.
        
    pwd = "" #Variable qui stockera le mot de passe final.Le mot de passe commence vide
    meets_criteria = False # Est-ce que le mot de passe respecte les règles ?
    has_number = False  # Contient un chiffre ?
    has_special = False # Contient un symbole ?
    
    
    #5- Cette boucle construit le mot de passe caractère par caractère
    while not meets_criteria or len(pwd) < min_length:
        # Tant que le mot de passe n'est pas valide OU trop court, on continue.
        new_char = random.choice(characters)# Choisit un caractère aléatoire parmi ceux autorisés.
        pwd += new_char #Ajoute ce caractère au mot de passe.
        
        
        #6-On met à jour les booléens pour savoir si le mot de passe contient des chiffres/symboles.
        if new_char in digits:
            has_number = True # On a trouvé un chiffre
        elif new_char in special:
            has_special = True #On a trouvé un symbole
            
            
        #7- Cette partie vérifie si le mot de passe respecte toutes les règles demandées.    
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special    
            
    return pwd             #On renvoie le mot de passe final    


#C'est ici qu'on utilise la fonction pour créer un vrai mot de passe.        
min_length = int(input("Enter the miimum length: "))
has_number = input("Do you want to have numbers(y/n) ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"  
pwd = generate_password(min_length, has_number, has_special)   
print(f"The generated password is : {pwd}")

    