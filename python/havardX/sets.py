# Create an empty set
s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

print(s)

s.remove(3)
print(s)

# calculate how many element contain s = len(s)
print(f"The set has {len(s)} elements") 