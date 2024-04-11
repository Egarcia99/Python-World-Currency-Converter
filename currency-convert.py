from requests import get
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()
api_key = os.getenv("API_KEY")  # Retrieve the API key
BASE_URL = "https://free.currconv.com/"  # Define the base URL for the API

# List of popular currencies for user reference
popular_currencies = [
    ("USD", "United States Dollar"),
    ("EUR", "Euro"),
    ("JPY", "Japanese Yen"),
    ("GBP", "British Pound"),
    ("AUD", "Australian Dollar"),
    ("CAD", "Canadian Dollar"),
    ("CHF", "Swiss Franc"),
    ("CNY", "Chinese Yuan"),
    ("SEK", "Swedish Krona"),
    ("NZD", "New Zealand Dollar")
]

def get_currencies():
    # Fetches all available currencies and their symbols from the API
    endpoint = f"api/v7/currencies?apiKey={api_key}"
    url = BASE_URL + endpoint
    response = get(url).json()['results']
    # Map currency codes to their symbols, default to the code if no symbol exists
    currency_symbols = {code: details.get("currencySymbol", "") for code, details in response.items()}
    # Sort currencies alphabetically by their code
    sorted_currencies = sorted(response.items(), key=lambda x: x[0])
    return sorted_currencies, currency_symbols

def print_currencies(currencies):
    # Prints each currency's code, name, and symbol
    for code, details in currencies:
        symbol = details.get("currencySymbol", "No symbol")
        print(f"{code} // {details['currencyName']} // {symbol}")

def print_popular_currencies():
    # Displays a list of popular currencies for quick reference
    print("\nHere are some popular currencies for reference:\n")
    for code, name in popular_currencies:
        print(f"{code} - {name}")
    print()  # Add a newline for better readability

def exchange_rate(currency1, currency2, currency_symbols):
    # Fetches and displays the exchange rate between two currencies
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={api_key}"
    url = BASE_URL + endpoint
    response = get(url).json()
    if not response:
        print('Invalid currencies.')
        return None

    rate = next(iter(response.values()))
    # Display symbols or currency codes if symbols are not available
    symbol1 = currency_symbols.get(currency1, "")
    symbol2 = currency_symbols.get(currency2, "")
    print(f"{symbol1}1 = {symbol2}{rate}")
    return rate

def convert(currency1, currency2, amount, currency_symbols):
    # Converts an amount from one currency to another using the exchange rate
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return
    
    rate = exchange_rate(currency1, currency2, currency_symbols)
    if rate is None:
        return
    
    converted_amount = rate * amount
    symbol1 = currency_symbols.get(currency1, currency1)
    symbol2 = currency_symbols.get(currency2, currency2)
    # Format and display the conversion with appropriate currency symbols or codes
    print(f"{symbol1}{amount} is approximately equal to {symbol2}{converted_amount:.2f}")

def main():
    # Main program function
    currencies, currency_symbols = get_currencies()  # Retrieve currency data

    print("Hello! Welcome to the currency converter!\n")
    print("List - lists the different currencies around the world\n")
    print("Convert - convert from one currency to another\n")
    print("Rate - get the exchange rate between two currencies\n")

    while True:
        command = input("\nEnter a command or q to quit: ").lower()
        
        if command == "q":
            break  # Exit the loop to quit
        elif command == "list":
            print_currencies(currencies)  # List all currencies
        elif command == "convert":
            print_popular_currencies()  # Show popular currencies before conversion
            currency1 = input("Enter a base currency: ").upper()
            amount = input("Enter an amount in " + currency1 + ": ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount, currency_symbols)  # Perform conversion
        elif command == "rate":
            print_popular_currencies()  # Show popular currencies before getting rate
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2, currency_symbols)  # Get and display rate
        else:
            print("Unrecognized command!\n")  # Handle invalid commands

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
