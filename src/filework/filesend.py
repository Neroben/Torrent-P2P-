import math
import os
from socket import socket
from threading import Thread


class FileSend(Thread):
    # Полный путь к файлу
    directory: str
    # Соккет передачи файла
    sock: socket
    # количество частей
    count_part: int
    # размер части
    size_part: int

    def __init__(self, directory, sock, size_part):
        Thread.__init__(self)
        self.directory = directory
        self.sock = sock
        self.size_part = size_part
        self.count_part = math.ceil(os.path.getsize(self.directory) / self.size_part)

    def run(self):
        # отправляем информацию о файле
        self.sock.send(('info' + ':' + str(self.count_part) + ':' + str(self.size_part)).encode())
        # ждём запросы на файл
        while self.sock:
            request = self.sock.recv(50).decode()
            self.sock.send(self.get_part(request.split(':')[1]))

    # получение части файла
    def get_part(self, part):
        f = open(self.directory, 'rb')
        if 0 >= part > self.count_part:
            return False
        f.seek(self.size_part * part)
        return f.read(self.size_part)
