import os
import shutil

from src.filework.workfile import WorkFile


class FileRecv(WorkFile):
    directory_part: str
    filename: str
    integrity = set()

    # создание папки для частей файла
    def generate_dir(self):
        path = os.path.dirname(self.fullname)
        self.directory_part = path + os.path.basename(self.fullname).split('.')[0] + 'part'
        os.mkdir(self.directory_part)

    # сохранение части файла
    def save_part(self, part: str, data: bytes):
        f = open(self.directory_part + part, 'wb')
        f.write(data)
        self.integrity.add(part)

    # проверка целостности файла
    def check_integrity_speed(self):
        listfile = list()
        for a in range(self.size_part):
            if a not in self.integrity:
                listfile.append(a)
        return listfile


    # проверка целостности файла
    def check_integrity(self):
        filenames = self.list_files()
        listfile = list()
        for a in range(self.size_part):
            if a not in filenames:
                listfile.append(a)
        return listfile


    def build_file(self):
        temp = self.check_integrity()
        if temp:
            return temp
        fin = open(os.path.dirname(self.fullname) + os.path.basename(self.fullname), 'wb')
        for a in range(self.size_part):
            fout = open(self.directory_part + str(a), 'rb')
            data = fout.read()
            fin.write(data)
        shutil.rmtree(self.directory_part)
