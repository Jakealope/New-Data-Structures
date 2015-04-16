# This is a python Linked List


class Node(object):
    def __init__(self, val, next_node=None):
        self.val = val
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

    def pop(self):
        # pops first item from list and returns it
        chopped = self.firstNode
        self.firstNode = self.firstNode.nextNode
        return chopped.val
