# Функция, возвращающая перевернутую строку
def reverse_string(s: str):
    return s[::-1]


# Функция, возвращающая количество гласных
def count_vowels(s: str):
    vowels = 'aeiuoаеёиоуыэюя'  # Гласные русского и английского алфавита
    count = 0
    # Подсчет гласных с учетом регистра
    for c in s:
        if c.lower() in vowels:
            count += 1
    return count


# Функция, проверяющая строку на палиндром
def is_palindrome(s: str):
    # Проверка типа входных данных
    if type(s) is not str:
        raise TypeError('Ошибка типа переменной')
    # Проверка на палиндром с учетом регистра
    return s.lower() == s[::-1].lower()
