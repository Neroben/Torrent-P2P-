from src.node import Node


def main():
    start = Node(8764, 1024, 'C:\\Users\\admin\\Desktop\\Seti\\Kursach Work\\Torrent\\Directory')
    print(start.get_list_file_on_node(('localhost', 8765)))
    print(start.get_list_addr_on_node(('localhost', 8765)))
    start.get_file_on_node(('localhost', 8765), 'image.jpg',  8763)

main()
