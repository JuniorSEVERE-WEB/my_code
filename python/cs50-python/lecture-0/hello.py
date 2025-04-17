


#remove the whitespace from str
#name = name.strip()


#capitalize user's name
#name = name.capitalize()

#capitalize each begin word
# name = name.title()


#remove the whitespace from str and capitalize user's name
# name = name.strip().Capitalize()


# tips
# name = input("Enter your name: ").strip().Capitalize( )

name = input("What's your name?: ").strip().title()

#split user's name into first name and last name
first, middle,  last = name.split(" ")

#interactive mode = type "python " in terminal

#say hello to user


print(f"Hello, {first}")