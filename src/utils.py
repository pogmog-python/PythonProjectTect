import json
import os
import logging

# Настройка логирования для модуля masks
logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)  # Установим уровень логирования не ниже DEBUG

# Создание обработчиков
file_handler = logging.FileHandler('../logs/utils.log', mode='a', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)  # Записываем все сообщения от DEBUG и выше

# Создание форматировщика
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавление обработчиков к логгеру
logger.addHandler(file_handler)


def load_transactions(file_path):
    """Загружает транзакции из указанного файла."""
    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        logger.warning(f'Файл {file_path} не найден.')
        return []

    # Пытаемся открыть и загрузить данные из файла
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # Проверяем, является ли загруженные данные списком
            if isinstance(data, list):
                logger.info(f'Успешно загружено {len(data)} транзакций из {file_path}.')
                return data
            else:
                logger.error(f'Загруженные данные не являются списком: {file_path}.')
                return []
    except json.JSONDecodeError as e:
        logger.error(f'Ошибка декодирования JSON в файле {file_path}: {e}')
        return []
    except IOError as e:
        logger.error(f'Ошибка ввода-вывода при чтении файла {file_path}: {e}')
        return []


# Пример использования
if __name__ == "__main__":
    transactions = load_transactions('data/operations.json')
    print(transactions)
