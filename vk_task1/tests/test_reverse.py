import pytest
from functions.main import *


# Список различных тестов
@pytest.mark.parametrize('s, s_res', [
    ('ДраКон', 'ноКарД'),
    ('DrAgon ', ' nogArD'),
    (' Д ра кОн', 'нОк ар Д '),
    ('   ', '   '),
    ('', ''),
    ('#_*', '*_#')
])
# Тест-функция на переворачивание строки
def test_reverse_string(s: str, s_res: str):
    assert reverse_string(s) == s_res


# Список параметров для проверки типа данных
@pytest.mark.parametrize('s', [
    123, True, 2.54
])
# Тест-функция на тип введенных данных
def test_reverse_string_typeError(s):
    with pytest.raises(TypeError):
        reverse_string(s)
