import pytest
import os


# Фикстура с путем к приложению
@pytest.fixture()
def get_file_path():
    # Получение системного пути до appdata\Local
    localappdata_path = os.getenv("LOCALAPPDATA")
    file_path = localappdata_path + '\\Programs\\VK Teams\\vkteams.exe'
    return file_path
