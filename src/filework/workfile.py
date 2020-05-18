import os
import math
from src.datanode import DataNode


class WorkFile(DataNode):
    count_part: int
    size_file: int
    size_part: int
    fullname: str

    def __init__(self, fullname, size_part):
        self.fullname = fullname
        self.size_part = size_part
        self.size_file = os.path.getsize(self.directory)
        self.count_part = math.ceil(self.size_file / self.size_part)

