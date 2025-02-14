import pytest
from src.decorators import log


# Пример функции для тестирования
@log()
def add(x, y):
    return x + y


@log()
def divide(x, y):
    return x / y


# Тест успешного выполнения функции
def test_add(capsys):
    add(1, 2)
    captured = capsys.readouterr()
    assert "Starting add with args: (1, 2), kwargs: {}" in captured.out
    assert "add ok; result: 3" in captured.out


# Тест обработки исключения
def test_divide_by_zero(capsys):
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    captured = capsys.readouterr()
    assert "Starting divide with args: (1, 0), kwargs: {}" in captured.out
    assert "divide error: division by zero. Inputs: (1, 0), {}" in captured.out


# Тест обработки некорректного типа
def test_add_with_string(capsys):
    with pytest.raises(TypeError):
        add(1, 'two')
    captured = capsys.readouterr()
    assert "Starting add with args: (1, 'two'), kwargs: {}" in captured.out
    assert "add error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, 'two'), {}" in captured.out
