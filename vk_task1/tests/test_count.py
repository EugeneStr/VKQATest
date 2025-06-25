import pytest
from functions.main import *


# Список различных тестов
@pytest.mark.parametrize('s, count', [
    ('hello мир', 3),
    ('hEllo МИр', 3),
    ('123456', 0)
])
# Тест-функция на подсчет гласных
def test_count_vowels(s: str, count: int):
    assert count_vowels(s) == count


# Список параметров для проверки типа данных
@pytest.mark.parametrize('s', [
    123, True, 2.54
])
# Тест-функция на тип введенных данных
def test_count_vowels_typeError(s):
    with pytest.raises(TypeError):
        count_vowels(s)
