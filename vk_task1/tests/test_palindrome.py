import pytest
from functions.main import *


# Список различных тестов
@pytest.mark.parametrize('s, answer', [
    ('12344321', True),
    ('hello', False),
    ('Tooot', True)
])
# Тест-функция на проверку палиндрома
def test_is_palindrome(s: str, answer: bool):
    assert is_palindrome(s) == answer


# Список параметров для проверки типа данных
@pytest.mark.parametrize('s', [
    123, True, 2.54
])
# Тест-функция на тип введенных данных
def test_is_palindrome_typeError(s):
    with pytest.raises(TypeError):
        is_palindrome(s)
