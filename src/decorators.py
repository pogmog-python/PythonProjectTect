from functools import wraps


def log(filename=None):
    """
    Декоратор для логирования работы функции.

    filename: Имя файла для логирования. Если None, логирование происходит в консоль.
    """

    # Определяем функцию записи в файл или в консоль
    def log_message(message):
        """ функция для записи сообщений, которая проверяет, должен ли вывод идти в файл или в консоль."""
        if filename:
            with open(filename, 'a') as f:
                f.write(message + '\n')
        else:
            print(message)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """внутренняя функция, которая обрабатывает вызов оборачиваемой функции, логирует начало выполнения,
             результат и обрабатывает возможные исключения. """
            try:
                log_message(f'Starting {func.__name__} with args: {args}, kwargs: {kwargs}')
                result = func(*args, **kwargs)
                log_message(f'{func.__name__} ok; result: {result}')
                return result
            except Exception as e:
                log_message(f'{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}')
                raise  # Генерируем ошибку дальше после логирования

        return wrapper

    return decorator

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)