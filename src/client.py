import socket
import pickle

from src.filework.filerecv import FileRecv


# подключение к узлу (обмен адресами)
def connect_net(addr) -> bool:
    sock = socket.socket()
    sock.connect(addr)
    var_str = 'Hi!' + ':' + str(addr[1])
    sock.send(var_str.encode())

    data = sock.recv(15).decode()
    sock.close()
    if data == 'Hi!':
        return True
    return False


# запрос доступных файлов узла
def get_list_file_on_node(addr):
    sock = socket.socket()
    sock.connect(addr)
    sock.send('List files'.encode())

    full_data = b''
    while True:
        data: bytes = sock.recv(1024)
        full_data = full_data + data
        if b'000' in full_data:
            break
    sock.close()
    return pickle.loads(full_data)


# запрос работающих адресов узлов из узла по адресу
def get_list_addr_on_node(addr):
    sock = socket.socket()
    sock.connect(addr)
    sock.send('List addr'.encode())

    full_data = b''
    while True:
        data: bytes = sock.recv(1024)
        full_data = full_data + data
        if b'000' in full_data:
            break
    sock.close()
    return pickle.loads(full_data)


def get_file_on_node(addr, filename, directory):
    sock = socket.socket()
    sock.connect(addr)
    request = 'get' + ':' + str(filename)
    sock.send(request.encode())

    answer = sock.recv(100)
    if answer == 'Not file!':
        return False
    # file:кол-во частей:размер части
    temp = answer.split(':')
    a = FileRecv(sock, directory, filename, int(temp[1]), int(temp[2]))

    sock.close()
