# This is a doubly linked list


class ListItem(object):
    def __init__(self, val, previous=None, next=None):
        self.val = val
        self.next = next
        self.previous = previous


class DLinked(object):
    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last

    def insert(self, val):
        # adds val to beginning of list
        new_item = ListItem(val, next=self.first)
        if self.first is None:
            self.first = self.last = new_item
        else:
            self.first = self.first.previous = new_item
