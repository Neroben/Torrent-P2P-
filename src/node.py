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
        connect_net(addr)
        self.networkInfo.new_node(addr)

    # получение списка доступных файлов
    def get_list_file_on_node(self, addr):
        return get_list_file_on_node(addr)

    # получение списка адресов узла
    def get_list_addr_on_node(self, addr):
        return get_list_addr_on_node(addr)

    def get_file_on_node(self, addr, filename, free_port):
        get_file_on_node(addr, filename, self.data_node.directory, free_port)