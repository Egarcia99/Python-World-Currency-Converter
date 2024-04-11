
# Currency Converter and Exchange Rate Tool

This Python script allows users to convert between different currencies and get exchange rates using the free.currconv.com API. Users can input commands to list available currencies, perform currency conversion, or retrieve exchange rates between two currencies.

## Features

- List Currencies: Users can view a list of available currencies along with their currency codes and symbols.
- Convert Currency: Users can input a base currency, amount, and target currency to convert between currencies.
- Get Exchange Rate: Users can input two currencies to retrieve the exchange rate between them.

## Setup

1. Clone or download the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Obtain an API key from [free.currconv.com](https://free.currconv.com/). Save the API key in a `.env` file in the same directory as the script using the format `API_KEY=your_api_key`.
4. Run the script using Python: `python currency_converter.py`.

## Usage

Upon running the script, users are prompted with a menu offering options to list currencies, convert currency, or get exchange rates. Users can input commands or enter `q` to quit.

### Commands

- List: Displays a list of available currencies.
- Convert: Allows users to convert between currencies by inputting a base currency, amount, and target currency.
- Rate: Retrieves the exchange rate between two currencies.

### Example Usage

1. List available currencies:
   ```
   Enter a command or q to quit: list
   ```

2. Convert currency:
   ```
   Enter a command or q to quit: convert
   Enter a base currency: USD
   Enter an amount in USD: 100
   Enter a currency to convert to: EUR
   ```

3. Get exchange rate:
   ```
   Enter a command or q to quit: rate
   Enter a base currency: USD
   Enter a currency to convert to: EUR
   ```

## Notes

- Ensure your API key is properly saved in the `.env` file and that the API key has access to the required endpoints.
- This script utilizes the free.currconv.com API, so be mindful of any rate limits or usage restrictions imposed by the API provider.

Feel free to modify and adapt the script according to your needs or integrate it into other projects. For any issues or feature requests, please open an issue on the GitHub repository.
