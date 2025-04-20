![](https://raw.githubusercontent.com/unton3ton/Docker-audiowmark-fastapi/refs/heads/main/photo_2025-03-19_06-51-33.jpg)

```bash
sudo pacman -S docker
systemctl start docker
systemctl enable docker
docker --version
sudo docker build -t audiowmark .
```

Чтобы смонтировать файл в контейнер, при выполнении команды docker run нужно использовать опцию -v или --volume. Затем следует указать каталог хоста, содержащий файлы, и каталог контейнера, в котором нужно получить к ним доступ.  
 
Пример команды:

```bash
docker run -v /путь/к/хост-директории:/путь/в/контейнере имя_образа
```

![](https://raw.githubusercontent.com/unton3ton/Docker-audiowmark-fastapi/refs/heads/main/client.PNG)

```bash
sudo docker run -v /home/thony/Документы/AUDIOWATERMARK/data:/data audiowmark add 2.mp3 2wm.wav 01010101010101010101010101010101
sudo docker run -v /home/thony/Документы/AUDIOWATERMARK/data:/data audiowmark get 2wm.wav
```

![](https://raw.githubusercontent.com/unton3ton/Docker-audiowmark-fastapi/refs/heads/main/server.PNG)

# a note

### [audiowmark/src/wmcommon.cc](https://github.com/swesterfeld/audiowmark/blob/eced66fcf2145fe3e25bf08af47ac1a4d17ac0b0/src/wmcommon.cc#L38)  
 
### 38 строка: size_t Params::payload_size    = 256; // - 64 символа //128; //- 32 символа

# Sources

* [Docker для веб-разработки: Руководство для начинающих](https://appmaster.io/ru/blog/docker-dlia-veb-razrabotki)
* [Изучаем команду wget на 12 примерах](https://habr.com/ru/companies/ruvds/articles/346640/)
