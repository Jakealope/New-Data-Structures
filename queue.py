

class QueueItem(object):
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev


class Queue(object):
    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last

    def enqueue(self, val):
        # adds val to beginning of queue
        new = QueueItem(val, next=self.last)
        if not self.first:
            self.first = self.last = new
        else:
            self.last.prev = new
            self.last = new

    def dequeue(self):
        # pops last value from list and returns it
        obsolete = self.first
        if self.first is None:
            raise ValueError("No items in queue.")
        elif self.last is obsolete:
            self.first = self.last = None
        else:
            obsolete.prev.next = None
            self.first = self.first.prev
        return obsolete.val
