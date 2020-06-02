import socket
from threading import Thread

from src.datanode import DataNode
from src.filework.filesend import FileSend
from src.networkInfo import NetworkInfo
import pickle


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
        self.data_node = data_node
        Thread.__init__(self)

    def run(self):
        self.sock = socket.socket()
        self.sock.bind(('', int(self.port)))
        # разрешить подключение к соккету
        self.sock.listen(1)
        while True:
            try:
                conn, addr = self.sock.accept()
                while True:
                    data = conn.recv(self.size_acceptance).decode()
                    if not data:
                        break
                    self.processing_data(conn, addr, data)
            except socket.error:
                print('Ошибка соединения, связь разована. Сервер ожидает другие соединения')

    def processing_data(self, conn, addr, data):

        if data.split(':')[0] == 'Hi!':
            self.info_net.new_node((addr[0], data.split(':')[1]))
            conn.send('Hi!'.encode())
            return
        if data == 'List files':
            conn.send(pickle.dumps(self.data_node.list_files()) + b'000')
            return
        if data == 'List addr':
            conn.send(pickle.dumps(self.info_net.node_addr) + b'000')
        if data.split(':')[0] == 'get':
            FileSend(self.data_node.directory + '\\' + data.split(':')[1], 1024, (addr[0], data.split(':')[2])).start()
