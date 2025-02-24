import os
import requests
from dotenv import load_dotenv

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"


def operation_transaction(transaction: dict) -> float:
    """Конвертируем валюту через API_KEY и возвращаем его"""

    amount = transaction.get("operationAmount", {}).get("amount")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if amount is None or currency is None:
        raise ValueError("Недостаточно данных для конвертации")

    if currency == "RUB":
        return float(amount)

    elif currency in ["USD", "EUR"]:
        try:
            response = requests.get(
                API_URL.format(to="RUB", from_=currency, amount=amount),
                headers={"apikey": API_KEY}
            )
            if response.status_code == 200:
                data = response.json()
                return float(data["result"])
            else:
                raise Exception(f"Ошибка при конвертации валюты: {response.status_code}")

        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Ошибка при конвертации валюты: {e}")

    else:
        raise ValueError("Недопустимая валюта")


def get_transaction_amount_in_rub(transaction):
    currency = transaction['currency']
    amount = transaction['amount']

    if currency == 'RUB':
        return float(amount)
    elif currency in ('USD', 'EUR'):
        exchange_rate = operation_transaction(currency)
        return float(amount) * exchange_rate
    else:
        raise ValueError("Unsupported currency")


print(API_KEY)
