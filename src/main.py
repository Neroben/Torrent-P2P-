from src.node import Node


def main():
    port1 = input('Введите порт приема сервера: ')
    start1 = Node(port1, 1024, 'C:\\Users\\admin\\Desktop\\Seti\\Kursach Work\\Teamviewer-Python-master')

    for str in start1.get_list_file_on_node(('localhost', 8765)):
        print(str)

main()
