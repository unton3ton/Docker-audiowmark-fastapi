# cd /home/thony/Документы/AUDIOWATERMARK && source AUDIOFASTAPI2/bin/activate && python audio-fastapi-server.py

# pip install fastapi[all] uvicorn

import uvicorn
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
import shutil
import os


app = FastAPI()

# Папка для сохранения загруженных файлов
DIRECTORY = "data"

# Создаем папку, если она не существует
if not os.path.exists(DIRECTORY):
    os.makedirs(DIRECTORY)


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), message: str = Form(...)):
    file_location = os.path.join(DIRECTORY, file.filename)
    
    # Сохраняем файл
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    password = "maandag" 
    received_text = message  # Получаем текстовое сообщение

    # command = f"docker run -v /home/thony/Документы/AUDIOWATERMARK/data:/data audiowmark add {file.filename} {file.filename[:-4]}wm.wav {received_text}"
    command64 = f"docker run -v /home/thony/Документы/AUDIOWATERMARK/data:/data audiowmark1 add {file.filename} {file.filename[:-4]}wm64.wav {received_text}"
    
    # Выполняем команды
    # os.system(f'echo {password} | sudo -S {command}')
    os.system(f'echo {password} | sudo -S {command64}')
    
    return {"filename": file.filename, "location": file_location}


@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = os.path.join(DIRECTORY, filename)
    
    # Проверяем, существует ли файл
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        return {"error": "File not found"}


@app.post("/uploadwm/")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(DIRECTORY, file.filename)
    
    # Сохраняем файл
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    password = "maandag" 

    # command = f"docker run -v /home/thony/Документы/AUDIOWATERMARK/data:/data audiowmark get {file.filename} > wm.txt"
    command64 = f"docker run -v /home/thony/Документы/AUDIOWATERMARK/data:/data audiowmark1 get {file.filename} > wm64.txt"
    
    # Выполняем команды
    # os.system(f'echo {password} | sudo -S {command}')
    os.system(f'echo {password} | sudo -S {command64}')

    if os.path.isfile('wm.txt'):
        with open('wm.txt', 'r') as file:
            content = file.read()

    with open('wm64.txt', 'r') as file:
        content64 = file.read()
    
    # return {"wm": content, "wm64": content64}
    return {"wm64": content64}


@app.post("/rmdir/")
async def remove_dir():
    dir_path = f'/home/thony/Документы/AUDIOWATERMARK/{DIRECTORY}'
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
        os.makedirs(DIRECTORY)
        return {"remove a directory": DIRECTORY}
    else:
        return {"error": "Directory not found"}

if __name__ == "__main__":
    uvicorn.run("audio-fastapi-server:app", host="0.0.0.0", port=6000, reload=True)

# sudo docker save audiowmark1:latest > ./audiowmark1-256bit-64symbols-app.tar
# sudo docker load -i ./audiowmark1-256bit-64symbols-app.tar
# wget http://192.168.1.43:8000/audiowmark1-256bit-64symbols-app.tar

# INFO:     192.168.1.121:63473 - "POST /upload/ HTTP/1.1" 200 OK
# INFO:     192.168.1.121:63474 - "GET /download/berlinwm.wav HTTP/1.1" 200 OK
# INFO:     192.168.1.121:63475 - "GET /download/berlinwm64.wav HTTP/1.1" 200 OK
# INFO:     192.168.1.121:63476 - "POST /rmdir/ HTTP/1.1" 200 OK
# Input:        2.mp3
# Output:       2wm.wav
# Message:      01010101010101010101010101010101
# Strength:     10

# Time:         2:39
# Sample Rate:  44100
# Channels:     2
# Data Blocks:  3
# Input:        2.mp3
# Output:       2wm64.wav
# Message:      0101010101010101010101010101010101010101010101010101010101010101
# Strength:     10

# Time:         2:39
# Sample Rate:  44100
# Channels:     2
# Data Blocks:  1
# INFO:     192.168.1.121:63479 - "POST /upload/ HTTP/1.1" 200 OK
# INFO:     192.168.1.121:63480 - "GET /download/2wm.wav HTTP/1.1" 200 OK
# INFO:     192.168.1.121:63481 - "GET /download/2wm64.wav HTTP/1.1" 200 OK
# INFO:     192.168.1.121:63482 - "POST /rmdir/ HTTP/1.1" 200 OK
# Input:        berlin.mp3
# Output:       berlinwm.wav
# Message:      10101010101010101010101010101010
# Strength:     10

# Time:         3:59
# Sample Rate:  44100
# Channels:     2
# Data Blocks:  4
# Input:        berlin.mp3
# Output:       berlinwm64.wav
# Message:      1010101010101010101010101010101010101010101010101010101010101010
# Strength:     10

# Time:         3:59
# Sample Rate:  44100
# Channels:     2
# Data Blocks:  2
# INFO:     192.168.1.121:63483 - "POST /upload/ HTTP/1.1" 200 OK
# INFO:     192.168.1.121:63484 - "GET /download/berlinwm.wav HTTP/1.1" 200 OK
# INFO:     192.168.1.121:63485 - "GET /download/berlinwm64.wav HTTP/1.1" 200 OK
# INFO:     192.168.1.121:63724 - "POST /uploadwm/ HTTP/1.1" 200 OK
# INFO:     192.168.1.121:63486 - "POST /rmdir/ HTTP/1.1" 200 OK
