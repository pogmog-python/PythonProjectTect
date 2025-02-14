import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
import os

# Импортируем функцию, которую будем тестировать
from src.utils import load_transactions

class TestLoadTransactions(unittest.TestCase):

    @patch('os.path.exists')
    def test_file_does_not_exist(self, mock_exists):
        mock_exists.return_value = False
        result = load_transactions('data/non_existent_file.json')
        self.assertEqual(result, [])

    @patch('builtins.open', new_callable=mock_open, read_data='')
    def test_file_is_empty(self, mock_file):
        with patch('os.path.exists', return_value=True):
            result = load_transactions('data/empty_file.json')
            self.assertEqual(result, [])

    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}')
    def test_file_contains_non_list_data(self, mock_file):
        with patch('os.path.exists', return_value=True):
            result = load_transactions('data/non_list_data.json')
            self.assertEqual(result, [])

    @patch('builtins.open', new_callable=mock_open, read_data='[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]')
    def test_file_contains_list_data(self, mock_file):
        with patch('os.path.exists', return_value=True):
            result = load_transactions('data/valid_data.json')
            expected = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
            self.assertEqual(result, expected)

    @patch('builtins.open', new_callable=mock_open)
    def test_json_decode_error(self, mock_file):
        mock_file.side_effect = json.JSONDecodeError("Expecting value", "", 0)
        with patch('os.path.exists', return_value=True):
            result = load_transactions('data/invalid_json.json')
            self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()