import json
import os

def load_transactions(file_path):
    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        return []

    # Пытаемся открыть и загрузить данные из файла
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # Проверяем, является ли загруженные данные списком
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, IOError):
        return []

# Пример использования
if __name__ == "__main__":
    transactions = load_transactions('data/operations.json')
    print(transactions)