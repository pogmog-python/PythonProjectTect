import pytest
from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator


@pytest.fixture
def transactions_data():
    return [
        {'id': 1, 'description': 'Перевод организации', 'operationAmount': {'amount': '1000', 'currency': {'code': 'USD'}}},
        {'id': 2, 'description': 'Перевод со счета на счет', 'operationAmount': {'amount': '1500', 'currency': {'code': 'EUR'}}},
        {'id': 3, 'description': 'Перевод со счета на счет', 'operationAmount': {'amount': '2000', 'currency': {'code': 'USD'}}},
        {'id': 4, 'description': 'Перевод с карты на карту', 'operationAmount': {'amount': '300', 'currency': {'code': 'RUB'}}},
        {'id': 5, 'description': 'Перевод организации', 'operationAmount': {'amount': '500', 'currency': {'code': 'USD'}}},
    ]


def test_filter_usd(transactions_data):
    usd_transactions = list(filter_by_currency(transactions_data, "USD"))
    assert len(usd_transactions) == 3  # Мы ожидаем 3 транзакции в USD
    # Вы также можете проверить, что ID этих транзакций ожидаемы
    assert usd_transactions[0]['id'] == 1
    assert usd_transactions[1]['id'] == 3
    assert usd_transactions[2]['id'] == 5


def test_filter_no_usd(transactions_data):
    no_usd_transactions = list(filter_by_currency(transactions_data, "GBP"))
    assert len(no_usd_transactions) == 0


def test_empty_list():
    empty_transactions = list(filter_by_currency([], "USD"))
    assert len(empty_transactions) == 0


def test_no_matching_currency():
    transactions_data = [
        {
            "id": 1,
            "operationAmount": {
                "currency": {"code": "EUR"}
            }
        }
    ]
    filtered_transactions = list(filter_by_currency(transactions_data, "USD"))
    assert len(filtered_transactions) == 0


@pytest.fixture
def transactions_data2():
    return [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод со счета на счет"},
        {"id": 3, "description": "Перевод со счета на счет"},
        {"id": 4, "description": "Перевод с карты на карту"},
        {"id": 5, "description": "Перевод организации"},
    ]


def test_transaction_descriptions(transactions_data2):
    descriptions = transaction_descriptions(transactions_data2)
    results = list(descriptions)
    assert results == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]


def test_empty_transactions():
    empty_descriptions = transaction_descriptions([])
    assert list(empty_descriptions) == []


def test_missing_description():
    transactions_with_missing_description = [
        {"id": 1},
        {"id": 2, "description": "Перевод организации"},
    ]
    descriptions = transaction_descriptions(transactions_with_missing_description)
    assert list(descriptions) == [
        "Описание отсутствует",
        "Перевод организации"
    ]


@pytest.mark.parametrize("start, end, expected", [
    (1, 5, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]),
    (10, 12, [
        "0000 0000 0000 0010",
        "0000 0000 0000 0011",
        "0000 0000 0000 0012"
    ]),
    (9999, 10001, [
        "0000 0000 0000 9999",
        "0000 0000 0001 0000",
        "0000 0000 0001 0001"
    ])
])
def test_card_number_generator(start, end, expected):
    assert list(card_number_generator(start, end)) == expected


def test_card_number_generator_edge_cases():
    # Проверка на крайние значения
    assert list(card_number_generator(1, 1)) == ["0000 0000 0000 0001"]
    assert list(card_number_generator(9999, 9999)) == ["0000 0000 0000 9999"]
    assert list(card_number_generator(0, 0)) == ["0000 0000 0000 0000"]
