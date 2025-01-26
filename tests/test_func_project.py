import pytest
from typing import List, Dict

# Импортируем функции, которые будем тестировать
from src.masks import get_mask_card_number, get_mask_account
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card, get_date


#Пример фикстуры для тестов
@pytest.fixture
def sample_data():
    """

    :return:
    """
    return [
        {"state": "EXECUTED", "date": "2023-01-01", "amount": 100},
        {"state": "CANCELED", "date": "2023-01-02", "amount": 200},
        {"state": "EXECUTED", "date": "2023-01-03", "amount": 300},
    ]


# Тесты для функции filter_by_state
def test_filter_by_state(sample_data):
    result = filter_by_state(sample_data, "EXECUTED")
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_no_match(sample_data):
    result = filter_by_state(sample_data, "UNKNOWN")
    assert len(result) == 0


# Тесты для функции sort_by_date
def test_sort_by_date(sample_data):
    result = sort_by_date(sample_data, arg_for_sort=False)
    assert result[0]["date"] == "2023-01-01"
    assert result[1]["date"] == "2023-01-02"
    assert result[2]["date"] == "2023-01-03"


def test_sort_by_date_with_same_dates():
    data = [
        {"state": "EXECUTED", "date": "2023-01-01"},
        {"state": "EXECUTED", "date": "2023-01-01"},
    ]
    result = sort_by_date(data)
    assert result[0]["date"] == result[1]["date"]


# Тесты для функции get_mask_card_number
def test_get_mask_card_number():
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"
    assert get_mask_card_number("1234") == "1234 ** **** 1234"
    assert get_mask_card_number("") == "  ** ****  "


# Тесты для функции get_mask_account
def test_get_mask_account():
    assert get_mask_account("1234567890123456") == "**3456"
    assert get_mask_account("1234") == "**1234"
    assert get_mask_account("") == "**"


# Тесты для функции mask_account_card
def test_mask_account_card():
    assert mask_account_card("Card 1234567812345678") == "Card 1234 56** **** 5678"
    assert mask_account_card("Счет 1234567890123456") == "Счет **3456"
    assert mask_account_card("Invalid input") == "Invalid input"


# Тесты для функции get_date
def test_get_date():
    assert get_date("2023-01-01") == "01.01.2023"
    assert get_date("2023-12-31") == "31.12.2023"
    assert get_date("") == ".."

# Запуск тестов
#if __name__ == "__main__":
#pytest.main()
