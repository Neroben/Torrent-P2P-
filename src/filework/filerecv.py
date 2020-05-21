import os
import shutil
import socket
from threading import Thread


class FileRecv(Thread):
    # директория куда сохранять файл
    directory: str
    # директория временных файлов
    directory_part: str
    # название файла
    filename: str
    # скачанные файлы
    integrity = set()
    # количество частей
    count_part: int
    # размер части
    size_part: int
    # сокет запроса частей
    sock: socket
    # свободный порт для приема данных
    free_port: int
    # хост из которого будут идти данные
    host: str

    def __init__(self, directory: str, filename: str, addr, free_port):
        Thread.__init__(self)
        self.sock = socket.socket()
        self.sock.connect(addr)
        self.free_port = int(free_port)
        request = 'get:' + str(filename) + ':' + str(self.free_port)
        self.sock.send(request.encode())
        self.sock.close()
        self.directory = directory
        self.filename = filename
        self.host = addr[0]
        self.generate_dir()

    def run(self):
        self.sock = socket.socket()
        self.sock.bind((self.host, self.free_port))
        self.sock.listen(1)
        conn, addr = self.sock.accept()
        self.sock = conn
        info = self.sock.recv(50).decode()
        self.count_part = int(info.split(':')[1])
        self.size_part = int(info.split(':')[2])
        while True:
            list_file = self.check_integrity_speed()
            if not list_file:
                self.build_file()
                shutil.rmtree(self.directory_part)
                break
            for file in list_file:
                self.sock.send(('get_part:' + str(file)).encode())
                self.save_part(str(file), self.sock.recv(self.size_part))
                self.integrity.add(file)
        self.sock.send('close'.encode())
        self.sock.close()

    # создание папки для частей файла
    def generate_dir(self):
        self.directory_part = self.directory + '\\' + self.filename.split('.')[0] + 'part'
        os.mkdir(self.directory_part)

    # сохранение части файла (часть, данные)
    def save_part(self, part: str, data: bytes):
        f = open(self.directory_part + '\\' + part, 'wb')
        f.write(data)
        self.integrity.add(part)

    # проверка целостности файла
    def check_integrity_speed(self):
        list_file = list()
        for a in range(self.count_part):
            if a not in self.integrity:
                list_file.append(a)
        return list_file

    # проверка целостности файла
    def check_integrity(self):
        filenames = self.list_files()
        list_file = list()
        for a in range(self.count_part):
            if str(a) not in filenames:
                list_file.append(a)
        return list_file

    # собрать файл
    def build_file(self):
        temp = self.check_integrity()
        if temp:
            return temp
        fin = open(self.directory + '\\' + self.filename, 'wb')
        for a in range(self.count_part):
            f_out = open(self.directory_part + '\\' + str(a), 'rb')
            data = f_out.read()
            fin.write(data)

        # получение списка доступных файлов
    def list_files(self):
        return os.listdir(self.directory_part)
