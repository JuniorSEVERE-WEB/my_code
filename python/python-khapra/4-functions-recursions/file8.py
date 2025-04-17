cities = ["Leogane", "Port-au-prince", "Carbaret"]
heroes = ["Dessalines", "Toussaint", "Mannigat", "President Peligre"]

def print_len(list):
  print(len(list))

def print_list(list):
  for item in list:
    print(item, end=" ")

print_list(heroes)    
print_list(cities)  