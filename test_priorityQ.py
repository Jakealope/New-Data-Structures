import _priorityQ as pq
import sys
import pytest


class QueueTest():

    def test_init(self):
        queue = pq.Priority()
        assert type(queue) == pq.Priority
