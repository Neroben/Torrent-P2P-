import socket
from threading import Thread

from src.datanode import DataNode
from src.networkInfo import NetworkInfo


class Server(Thread):
    # порт ожидания сервера
    port: int
    # соккет
    sock: socket
    # размер передаваемых данных
    size_acceptance: int
    # информация о сети
    info_net: NetworkInfo
    # данные
    data_node: DataNode


    def __init__(self, port, info_net, data_node, size_acceptance):
        """Инициализация потока"""
        self.port = port
        self.size_acceptance = size_acceptance
        self.info_net = info_net
        Thread.__init__(self)

    def run(self):
        self.sock = socket.socket()
        self.sock.bind(('', int(self.port)))
        # разрешить подключение к соккету
        self.sock.listen(1)
        while True:
            conn, addr = self.sock.accept()
            while True:
                data = conn.recv(self.size_acceptance).decode()
                if not data:
                    break
                self.processing_data(conn, addr, data)

    def processing_data(self, conn, addr, data):
        if data == 'Hi!':
            self.info_net.new_node(addr)
            conn.send('Hi!'.encode())
            return
        if data == 'List files':
            for name in self.data_node.list_files:
                conn.send(name.encode())


