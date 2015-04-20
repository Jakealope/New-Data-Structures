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
        new = ListItem(val, next=self.first)
        if self.first is None:
            self.first = self.last = new
        else:
            self.first = self.first.previous = new

    def append(self, val):
        # adds val to end of list
        new = ListItem(val, previous=self.last)
        if not self.last:
            self.first = self.last = new
        else:
            self.last = self.last.next = new

    def pop(self):
        # pops first value from list and returns it
        obsolete = self.first
        if self.first is None:
            raise ValueError("No items in list!")
        elif self.last is obsolete:
            self.first = self.last = None
        else:
            obsolete.next.previous = None
            self.first = self.first.next
        return obsolete.val

    def shift(self):
        # pops last value from list and returns it
        obsolete = self.last
        if self.last is None:
            raise ValueError("No items in list!")
        elif self.first is obsolete:
            self.first = self.last = None
        else:
            obsolete.prev.next = None
            self.last = self.last.previous
        return obsolete.val
