import requests
import sys
import json

if len(sys.argv) != 2:  # Correction de la syntaxe : len(sys.argv) != 2
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])  # Correction de "lmit" → "limit"

o = response.json()
for result in o["results"]:
    print(result["trackName"])

# if i type in terminal python itunes.py weezer  : many line code will appear in terminal, these lines code exist already on internet

