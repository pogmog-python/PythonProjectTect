import unittest
from unittest.mock import patch
from src.external_api import get_transaction_amount_in_rub

class TestTransactionAmount(unittest.TestCase):
    @patch('external_api.get_exchange_rate')
    def test_get_transaction_amount_in_rub_rub(self, mock_get_exchange_rate):
        transaction = {'currency': 'RUB', 'amount': 100}
        result = get_transaction_amount_in_rub(transaction)
        self.assertEqual(result, 100.0)

    @patch('external_api.get_exchange_rate')
    def test_get_transaction_amount_in_rub_usd(self, mock_get_exchange_rate):
        mock_get_exchange_rate.return_value = 75.0  # 1 USD = 75 RUB
        transaction = {'currency': 'USD', 'amount': 10}
        result = get_transaction_amount_in_rub(transaction)
        self.assertEqual(result, 750.0)

    @patch('external_api.get_exchange_rate')
    def test_get_transaction_amount_in_rub_eur(self, mock_get_exchange_rate):
        mock_get_exchange_rate.return_value = 80.0  # 1 EUR = 80 RUB
        transaction = {'currency': 'EUR', 'amount': 5}
        result = get_transaction_amount_in_rub(transaction)
        self.assertEqual(result, 400.0)

    def test_get_transaction_amount_in_rub_unsupported_currency(self):
        transaction = {'currency': 'ABC', 'amount': 100}
        with self.assertRaises(ValueError):
            get_transaction_amount_in_rub(transaction)

if __name__ == '__main__':
    unittest.main()