https://github.com/swesterfeld/audiowmark


sudo pacman -S docker
systemctl start docker
systemctl enable docker
docker --version


sudo docker build -t audiowmark1 .

###########################################################################################################
Чтобы смонтировать файл в контейнер, при выполнении команды docker run нужно использовать опцию -v или --volume. Затем следует указать каталог хоста, содержащий файлы, и каталог контейнера, в котором нужно получить к ним доступ.  2

Пример команды:

docker run -v /путь/к/хост-директории:/путь/в/контейнере имя_образа
###########################################################################################################

sudo docker run -v /home/thony/Документы/audiowmark-master256bit-64symbols/data1:/data --rm -i audiowmark1 -h

sudo docker run -v /home/thony/Документы/audiowmark-master256bit-64symbols/data1:/data audiowmark1 add 1.mp3 1wm.wav 0123456789abcdef0011223344556677

sudo docker run -v /home/thony/Документы/audiowmark-master256bit-64symbols/data1:/data audiowmark1 get 1wm.wav 

sudo docker run -v /home/thony/Документы/audiowmark-master256bit-64symbols/data1:/data audiowmark1 add 2.mp3 2wm.wav 0101010101010101010101010101010101010101010101010101010101010101

sudo docker run -v /home/thony/Документы/audiowmark-master256bit-64symbols/data1:/data audiowmark1 get 2wm.wav
