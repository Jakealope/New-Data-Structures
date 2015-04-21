#!/usr/bin/env python


class BinaryHeap(object):
    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0

    def push(self, val):
        self.heaplist.append(val)
        self.currentsize += 1
        self.bubble_up(self.currentsize)

    def pop(self):
        return_val = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentsize]
        self.currentsize = self.currentsize - 1
        self.heaplist.pop()
        self.settle_down(1)
        return return_val
