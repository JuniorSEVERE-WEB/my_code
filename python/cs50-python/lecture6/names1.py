name = input("What's your name?: ")

file = open("names.text", "w")
file.write(f"{name}\n")
file.close()