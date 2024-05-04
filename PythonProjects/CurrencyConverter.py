# A program that shows the currency conversion rates

import requests

API_KEY = "fca_live_Pc1XEUY8Hw3QnYs83nUAb5bLJ8HBMUxlZdKXNRHC"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURRENCEIES = ["CAD", "USD", "EUR", "JPY", "CNY", "MXN", "RUB", "AUD"]

def currenciesExchangeRate(base):
  currencies = ",".join(CURRENCEIES)
  url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
  try:
    response = requests.get(url)
    data = response.json()
    return data["data"]

  except Exception as e:
    print("Invalid Currency")
    return None

while True:
  # amount = input("How much money would you like to convert? (press q to quit): ")
  base = input("Enter the Currency of the (press q to quit): ").upper()

  if base == "Q":
    print("Quitting Program")
    break

  data = currenciesExchangeRate(base)
  if not data:
    continue

  if base not in CURRENCEIES:
    print("Not a Currency in the data base")

  data = currenciesExchangeRate(base)
  del data[base]
  for ticker, value in data.items():
    print(f"{ticker}: {value}")