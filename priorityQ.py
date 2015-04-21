import heapq as hq


class Priority(object):
    """docstring for priority"""
    def __init__(self):
        self.heapq = hq()

    def insert(self, item, rank):
        hq.push(item, rank)
