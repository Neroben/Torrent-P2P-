from src.node import Node


def main():
    start = Node(8764, 1024, 'C:\\Users\\admin\\Desktop\\Seti\\Kursach Work\\Torrent\\Directory')
    start.get_file_on_node(('localhost', 8765), 'image.jfif',  8763)


main()
