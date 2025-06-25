import subprocess


# Тест-функция для запуска приложения
def test_start_vkteams(get_file_path):
    try:
        id_process = None
        file_path = get_file_path  # Путь к приложению
        process = subprocess.Popen(file_path)  # Запуск приложения
        id_process = process.pid  # ID процесса
        process.kill()
    # Отлов ошибки на наличие файла
    except FileNotFoundError:
        print('Файл не найден')
    finally:
        assert id_process is not None
