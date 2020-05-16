import os


class DataNode(object):
    directory: str

    def __init__(self, directory: str):
        self.directory = directory

    # получение списка доступных файлов
    def get_list_file(self):
        return os.listdir(self.directory)

