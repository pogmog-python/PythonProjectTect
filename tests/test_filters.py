from src.filters import filter_banking_transactions_by_description, filter_banking_description


def test_empty_list_description():
    """Проверяет, что функция возвращает 0 для всех категорий, если входной список пуст."""
    result = filter_banking_description([], ["groceries", "utilities"])
    assert result == {"groceries": 0, "utilities": 0}, "Тест не пройден: ожидается {'groceries': 0, 'utilities': 0}"


def test_no_matches_description():
    """Проверяет, что функция возвращает 0 для всех категорий, если нет совпадений."""
    banking_description = [
        {"description": "Payment for groceries"},
        {"description": "Transfer to savings"},
    ]
    result = filter_banking_description(banking_description, ["utilities", "rent"])
    assert result == {"utilities": 0, "rent": 0}, "Тест не пройден: ожидается {'utilities': 0, 'rent': 0}"


def test_single_match_description():
    """Проверяет, что функция возвращает правильное количество операций для каждой категории, если есть одно
    совпадение."""
    banking_description = [
        {"description": "Payment for groceries"},
        {"description": "Payment for utilities"},
    ]
    result = filter_banking_description(banking_description, ["groceries", "utilities"])
    assert result == {"groceries": 1, "utilities": 1}, "Тест не пройден: ожидается {'groceries': 1, 'utilities': 1}"


def test_multiple_matches_description():
    """Проверяет, что функция корректно считает количество совпадений для каждой категории."""
    banking_description = [
        {"description": "Payment for groceries"},
        {"description": "Payment for utilities"},
        {"description": "Transfer to groceries"},
    ]
    result = filter_banking_description(banking_description, ["groceries", "utilities"])
    assert result == {"groceries": 2, "utilities": 1}, "Тест не пройден: ожидается {'groceries': 2, 'utilities': 1}"


def test_case_insensitivity_description():
    """Проверяет, что функция не чувствительна к регистру символов в описании."""
    banking_description = [
        {"description": "Payment for Groceries"},
        {"description": "Transfer to Savings"},
    ]
    result = filter_banking_description(banking_description, ["groceries"])
    assert result == {"groceries": 1}, "Тест не пройден: ожидается {'groceries': 1}"


def test_empty_list_transactions():
    """Проверяет, что функция возвращает пустой список, если входной список пуст."""
    result = filter_banking_transactions_by_description([], "groceries")
    assert result == [], "Тест не пройден: ожидается []"


def test_no_matches_transactions():
    """Проверяет, что функция возвращает пустой список, если нет совпадений с поисковой строкой."""
    banking_description = [
        {"description": "Payment for groceries"},
        {"description": "Transfer to savings"},
    ]
    result = filter_banking_transactions_by_description(banking_description, "utilities")
    assert result == [], "Тест не пройден: ожидается []"


def test_single_match_transactions():
    """Проверяет, что функция возвращает правильный словарь, если есть одно совпадение."""
    banking_description = [
        {"description": "Payment for groceries"},
        {"description": "Payment for utilities"},
    ]
    result = filter_banking_transactions_by_description(banking_description, "groceries")
    assert result == ["{'description': 'Payment for groceries'}"], \
        "Тест не пройден: ожидается ['{\'description\': \'Payment for groceries\'}']"


def test_multiple_matches_transactions(_transactions):
    """Проверяет, что функция возвращает все совпадения, если их несколько."""
    banking_description = [
        {"description": "Payment for groceries"},
        {"description": "Payment for utilities"},
        {"description": "Transfer to groceries"},
    ]
    result = filter_banking_transactions_by_description(banking_description, "groceries")
    expected = [
        "{'description': 'Payment for groceries'}",
        "{'description': 'Transfer to groceries'}"
    ]
    assert result == expected, f"Тест не пройден: ожидается {expected}"


def test_case_insensitivity_transactions():
    """Проверяет, что функция корректно работает с учетом регистра символов."""
    banking_description = [
        {"description": "Payment for Groceries"},
        {"description": "Transfer to Savings"},
    ]
    result = filter_banking_transactions_by_description(banking_description, "groceries")
    assert result == ["{'description': 'Payment for Groceries'}"], \
        "Тест не пройден: ожидается ['{\'description\': \'Payment for Groceries\'}']"