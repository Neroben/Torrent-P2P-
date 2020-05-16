import socket
import pickle


class Client(object):
    sock: socket = socket.socket()

    # подключение к узлу (обмен адресами)
    def connect_net(self, addr) -> bool:
        self.sock.connect(addr)
        self.sock.send('Hi!'.encode())

        data = self.sock.recv(1024).decode()
        if data == 'Hi!':
            return True
        return False

    # запрос доступных файлов узла
    def get_list_file_on_node(self, addr):
        self.sock.connect(addr)
        self.sock.send('List files'.encode())

        list_file = list()
        while True:
            data = self.sock.recv(1024).decode()
            if not data:
                break
            list_file.append(data)
        return list_file
