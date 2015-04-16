# This is a python Linked List


class Node(object):
    def __init__(self, val, _next=None):
        self.val = val
        self._next = _next


class LinkedList(object):
    def __init__(self, first=None):
        self.first = first

    def insert(self, new):
        # insert new at beginning of list
        if not self.first:
            self.first = new
        else:
            new._next = self.first
            self.first = new

    def pop(self):
        # pops first item from list and returns it
        if self.size() == 0:
            return "THE LIST! IT'S EMPTY!!"
        else:
            chopped = self.first
            self.first = self.first._next
            return chopped.val

    def size(self):
        # returns length of list
        current = self.first
        size = 0
        while current is not None:
            size += 1
            current = current._next
        return size

    def search(self, val):
        # return node containing 'val' in list, if present (else None)
        current = self.first
        while current.val != val:
            if current._next is None:
                return None
            else:
                current = current._next
        return current
