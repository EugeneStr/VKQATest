import os
import urllib.request
import subprocess


# Тест-функция для установки приложения по URL
def test_install_vkteams():
    try:
        url = "https://vkteams-www.hb.bizmrg.com/win/x64/vkteams.msi"
        installer_file = "vkteams.msi"
        # Скачивание установщика по URL-адресу
        urllib.request.urlretrieve(url, installer_file)
        # Установка приложения на ПК
        subprocess.run(['msiexec', '/i', installer_file, '/quiet'], check=True)
        os.remove(installer_file)
    # Отлов ошибки при установке
    except subprocess.CalledProcessError:
        print('При установке произошла ошибка')


# Тест-функция для поиска установленного приложения на ПК
def test_find_app(get_file_path):
    _is_exists = False
    file_path = get_file_path  # Путь к приложению
    if os.path.exists(file_path):
        _is_exists = True
    assert _is_exists is True
