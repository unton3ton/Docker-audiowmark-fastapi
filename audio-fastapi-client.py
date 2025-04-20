# pip install requests_toolbelt requests

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

# Отправка строки-сообщения и файла
def upload_file_with_message(file_path: str, message: str):
    m = MultipartEncoder(
        fields={
            'file': (file_path, open(file_path, 'rb'), 'audio/wav'),  # или 'audio/mpeg' для mp3
            'message': message  # Передаем текстовое сообщение
        }
    )
    response = requests.post('http://192.168.1.43:6000/upload/', data=m, headers={'Content-Type': m.content_type})
    print(response.json())

# Функция для скачивания файла с сервера
def download_file(filename: str):
    url = f'http://192.168.1.43:6000/download/{filename}'
    # Отправляем GET-запрос для скачивания файла
    response = requests.get(url, stream=True)  # Используем stream=True для загрузки файла по частям
    print(f"Запрос на скачивание: {url}, статус: {response.status_code}")  # Выводим статус ответа
    if response.status_code == 200:
        # Сохраняем файл на диск
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):  # Читаем файл по частям
                f.write(chunk)
        print(f"Файл {filename} успешно скачан.")
    else:
        print(f"Ошибка при скачивании файла: {response.status_code}, {response.json()}")

# Отправка строки-сообщения и файла
def upload_filewm(file_path: str):
    m = MultipartEncoder(
        fields={
            'file': (file_path, open(file_path, 'rb'), 'audio/wav'),  # или 'audio/mpeg' для mp3
        }
    )
    response = requests.post('http://192.168.1.43:6000/uploadwm/', data=m, headers={'Content-Type': m.content_type})
    print(response.json())

def rmdir():
    response = requests.post('http://192.168.1.43:6000/rmdir/')
    print(response.json())

# Пример использования
if __name__ == "__main__":
    # Пример использования
    upload_file_with_message('2.mp3', "01010101010101010101010101010101")  # Отправляем файл и сообщение
    # download_file('2wm.wav')  # Запрос на скачивание: http://192.168.1.43:6000/download/2wm.wav, статус: 200
    download_file('2wm64.wav')
    rmdir()                   # {'remove a directory': 'data'}

    upload_file_with_message('berlin.mp3', "10101010101010101010101010101010")  # Отправляем файл и сообщение
    # download_file('berlinwm.wav')  # Запрос на скачивание: http://192.168.1.43:6000/download/2wm.wav, статус: 200
    download_file('berlinwm64.wav')

    upload_filewm('berlinwm64-1.wav')

    rmdir()

# {'filename': '2.mp3', 'location': 'data/2.mp3'}
# Запрос на скачивание: http://192.168.1.43:6000/download/2wm64.wav, статус: 200
# Файл 2wm64.wav успешно скачан.
# {'remove a directory': 'data'}
# {'filename': 'berlin.mp3', 'location': 'data/berlin.mp3'}
# Запрос на скачивание: http://192.168.1.43:6000/download/berlinwm64.wav, статус: 200
# Файл berlinwm64.wav успешно скачан.
# {'wm64': 'pattern  0:00 1010101010101010101010101010101010101010101010101010101010101010 
    # 1.403 0.321 CLIP-B\npattern  0:05 1010101010101010101010101010101010101010101010101010101010101010 
    # 1.440 0.113 A\npattern  1:33 1010101010101010101010101010101010101010101010101010101010101010 
    # 1.403 0.120 B\npattern  1:33 1010101010101010101010101010101010101010101010101010101010101010 
    # 1.422 0.116 AB\npattern  2:32 1010101010101010101010101010101010101010101010101010101010101010 
    # 1.382 0.214 CLIP-B\npattern   all 1010101010101010101010101010101010101010101010101010101010101010 1.422 0.116\n'}
# {'remove a directory': 'data'}