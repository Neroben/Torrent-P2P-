from src.node import Node


def main():
    port1 = input('Введите порт приема сервера: ')
    start1 = Node(port1, 1024)

    # port2 = input('Введите порт приема сервера: ')
    # start2 = Node(port2, 1024)

    port2 = input('Введите порт подключения клиента: ')
    start1.connect_network(('localhost', int(port2)))




main()
