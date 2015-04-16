# This is a python Linked List


class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, first=None):
        self.first = first

    def insert(self, new):
        # insert new at beginning of list
        if not self.first:
            self.first = new
        else:
            new.next_node = self.first
            self.first = new
