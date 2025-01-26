

def filter_by_currency(transactions, currency_code):
    """
    Функция фильтрует список транзакций по заданной валюте.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """
    Генератор, который возвращает описание каждой транзакции по очереди.
    """
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start: int, end: int):
    """Генератор, который возвращает номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, end + 1):
        # Форматируем номер карты с ведущими нулями и группируем по 4 цифры
        yield (f"{number:0>16}"[:4] + " " + f"{number:0>16}"[4:8] + " " + f"{number:0>16}"[8:12] + " "
               + f"{number:0>16}"[12:16])
