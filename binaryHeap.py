#!/usr/bin/env python


class BinaryHeap(object):
    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0

    def push(self, val):
        self.heaplist.append(val)
        self.currentsize += 1
        self.bubble_up(self.currentsize)
