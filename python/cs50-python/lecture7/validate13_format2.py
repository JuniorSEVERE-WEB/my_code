import re

name = input("What's your name: ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
  last, first = matches.groups()
  name = f"{first} {last}"
print(f"hello, {name}")  