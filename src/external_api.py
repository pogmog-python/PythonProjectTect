import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data/latest"
API_KEY = os.getenv("API_ACCESS_KEY")

def get_exchange_rate(base_currency):
    response = requests.get(f"{API_URL}?base={base_currency}", headers={"apikey": API_KEY})
    if response.status_code != 200:
        raise Exception("Error fetching exchange rates")
    data = response.json()
    return data["rates"]["RUB"]


def get_transaction_amount_in_rub(transaction):
    currency = transaction['currency']
    amount = transaction['amount']

    if currency == 'RUB':
        return float(amount)
    elif currency in ('USD', 'EUR'):
        exchange_rate = get_exchange_rate(currency)
        return float(amount) * exchange_rate
    else:
        raise ValueError("Unsupported currency")