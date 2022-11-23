import os
from requests import get
from pprint import PrettyPrinter

API_KEY = "e8e6bc3d7d677f497380"
BASE_URL = "https://free.currconv.com/"

printer = PrettyPrinter()

def get_currencies():
	endpoint = f"api/v7/currencies?apiKey={API_KEY}"
	url = BASE_URL + endpoint
	data = get(url).json()['results']

	data = list(data.items())
	data.sort()
	
	return data

def print_currencies(currencies):
	for name, currency in currencies:
		name = currency['currencyName']
		_id = currency['id']
		symbol = currency.get("currencySymbol", "")
		print(f"{_id} - {name} - {symbol}")

def exchange_rate(currency1, currency2):
	endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
	url = BASE_URL + endpoint
	response = get(url)

	data = response.json()

	if len(data) == 0:
		print("*INVALID CURRENCIES*")
		return

	rate = list(data.values())[0]
	print(f"{currency1} -> {currency2} = {rate}")

	return rate


def convert(currency1, currency2, amount):
	rate = exchange_rate(currency1, currency2)
	if rate is None:
		return

	try:
		amount = float(amount)
	except:
		print("*INVALID AMOUNT*")
		return

	converted_amount = rate * amount
	print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
	return converted_amount
	
def main():
	currencies = get_currencies()

	print("Welcome to Currency Converter!")
	print("List - lists the different currencies - Type: list")
	print("Convert - convert from one currency to another - Type: convert")
	print("Rate - get the exchange rate of two currencies - Type: rate")
	print()

	while True:
		command = input("Enter a command (q to quit): ")

		if command == "q":
			break
		elif command == "list":
			print_currencies(currencies)
		elif command == "convert":
			currency1 = input("Enter a base currency: ").upper()
			amount = input(f"Enter an amount in {currency1}: ").upper()
			currency2 = input("Enter a currency to convert to: ").upper()
			convert(currency1, currency2, amount)
		elif command == "rate":
			currency1 = input("Enter a base currency: ").upper()
			currency2 = input("Enter a currency to convert to: ").upper()
			exchange_rate(currency1, currency2)
		else:
			print("*UNRECOGNIZED COMMAND*")

main()
			
			
		

 