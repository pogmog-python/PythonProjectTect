import pandas as pd
import logging

# Настройка логирования для модуля data_reader
logger = logging.getLogger('data_reader')
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler('data_reader.log', mode='a', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# Создание форматировщика для логов
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def read_transactions_from_csv(file_path: str) -> list:
    """Функция для считывания финансовых операций из CSV файла."""
    try:
        logger.info(f'Чтение транзакций из CSV файла: {file_path}')
        df = pd.read_csv(file_path)
        transactions = df.to_dict(orient='records')
        logger.info(f'Успешно считано {len(transactions)} транзакций из CSV файла.')
        return transactions
    except Exception as e:
        logger.error(f'Ошибка при чтении CSV файла: {e}')
        return []


def read_transactions_from_excel(file_path: str) -> list:
    """Функция для считывания финансовых операций из Excel файла."""
    try:
        logger.info(f'Чтение транзакций из Excel файла: {file_path}')
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient='records')
        logger.info(f'Успешно считано {len(transactions)} транзакций из Excel файла.')
        return transactions
    except Exception as e:
        logger.error(f'Ошибка при чтении Excel файла: {e}')
        return []


# Пример использования.
if __name__ == "__main__":
    csv_file_path = 'data/transactions.csv'  # Путь к CSV файлу
    excel_file_path = 'data/transactions_excel.xlsx'  # Путь к Excel файлу

    csv_transactions = read_transactions_from_csv(csv_file_path)
    excel_transactions = read_transactions_from_excel(excel_file_path)

    print(csv_transactions)
    print(excel_transactions)
