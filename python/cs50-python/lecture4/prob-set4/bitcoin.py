import sys
import requests


if len(sys.argv) == 2:
  try:
    value = float(sys.argv[1])
  except:
    print("Command-line argument is not a number")
    sys.exit(1)  

else:
  print("Missing command-line argument")
  sys.exit(1)

try:
  r = requests.get('https://api.coincap.io/v2/assets/bitcoin')
  response = r.json()
  bitcoin = response['bpi']['USD']['rate_float']
  total_amount = bitcoin * value
  print(f"${total_amount:,.4f}")

except requests.RequestException:
  print("RequestException")
  sys.exit(1)
