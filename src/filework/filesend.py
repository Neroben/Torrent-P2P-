from src.filework.workfile import WorkFile


class FileSend(WorkFile):

    # получение части файла
    def get_part(self, part):
        f = open(self.directory, 'rb')
        if 0 >= part > self.count_part:
            return False
        f.seek(self.size_part * part)
        return f.read(self.size_part)
