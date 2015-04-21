import bin_heap as bh


class Priority(object):
    """docstring for priority"""
    def __init__(self):
        self.bin_heap = bh()

    def insert(self, item, rank):
        bh.push(item, rank)
