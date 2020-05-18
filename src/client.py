import socket
import pickle


class Client(object):

    # подключение к узлу (обмен адресами)
    def connect_net(self, addr) -> bool:
        sock = socket.socket()
        sock.connect(addr)
        varstr = 'Hi!' + ':' + str(addr[1])
        sock.send(varstr.encode())

        data = sock.recv(15).decode()
        sock.close()
        if data == 'Hi!':
            return True
        return False

    # запрос доступных файлов узла
    def get_list_file_on_node(self, addr):
        sock = socket.socket()
        sock.connect(addr)
        sock.send('List files'.encode())

        list_file = list()
        fulldata = b''
        while True:
            data: bytes = sock.recv(1024)
            fulldata =fulldata + data
            if b'000' in fulldata:
                break
        sock.close()
        return pickle.loads(fulldata)

    # запрос работающих адресов узлов из узла по адресу
    def get_list_addr_on_node(self, addr):
        sock = socket.socket()
        sock.connect(addr)
        sock.send('List addr'.encode())

        fulldata = b''
        while True:
            data: bytes = sock.recv(1024)
            fulldata = fulldata + data
            if b'000' in fulldata:
                break
        sock.close()
        return pickle.loads(fulldata)


    def get_file_on_node(self, addr, filename):
        sock = socket.socket()
        sock.connect(addr)
        request = 'get' + ':' + str(filename)
        sock.send(request.encode())

        sock.close()
