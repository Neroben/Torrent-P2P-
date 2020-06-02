from src.datanode import DataNode
from src.networkInfo import NetworkInfo
from src.server import Server
from src.client import *


class Node(object):
    server: Server
    networkInfo: NetworkInfo = NetworkInfo()
    data_node: DataNode

    def __init__(self, port, size_acceptance, directory):
        self.networkInfo = NetworkInfo()
        self.data_node = DataNode(directory)
        # запуск серверва
        self.server = Server(port, self.networkInfo, self.data_node, size_acceptance)
        self.server.start()

    # подключение к сети
    def connect_network(self, addr):
        if connect_net(addr):
            self.networkInfo.new_node(addr)

    # получение списка доступных файлов
    def get_list_file_on_node(self, addr):
        return get_list_file_on_node(addr)

    # получение списка адресов узла
    def get_list_addr_on_node(self, addr):
        return get_list_addr_on_node(addr)

    # получить файл filename по адресу addr, порт приема free_port
    def get_file_on_node(self, addr, filename, free_port):
        get_file_on_node(addr, filename, self.data_node.directory, free_port)

    # список подключенных узлов
    def get_list_connect_addr(self):
        self.check_connect_addr()
        return self.networkInfo.node_addr

    # проверка подключенных узлов
    def check_connect_addr(self):
        for addr in self.networkInfo.node_addr:
            if not connect_net(addr):
                self.networkInfo.node_addr.discard(addr)
