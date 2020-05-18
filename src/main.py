from src.node import Node


def main():
    port1 = input('Введите порт приема сервера: ')
    start1 = Node(port1, 1024, 'C:\\Users\\admin\\Desktop\\Seti\\Kursach Work\\Teamviewer-Python-master')

    start1.connect_network(('localhost', 8765))
    a = start1.get_list_addr_on_node(('localhost', 8765))

    for str in a:
        print(str)

main()
