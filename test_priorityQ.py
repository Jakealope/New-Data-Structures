import priorityQ as pq
import sys
import pytest


class QueueTest():

    def test_init(self):
        queue = pq.Priority()
        assert type(queue) == pq.Priority

    def test_insert(self):
        self.assertEqual(self.append.item)
