from bin_heap import BinaryHeap
import pytest


def test_is_empty():
    bin_list = BinaryHeap()
    assert bin_list.heaplist == [0]


def test_one_push_pop():
    bin_list = BinaryHeap()
    bin_list.push(10)
    assert bin_list.pop() == 10


def all_items(heap):
    items = []
    while True:
        try:
            items.append(heap.pop())
        except IndexError:
            return items
    return items


def test_reverse_range():
    heap = BinaryHeap()
    for i in range(5, 0, -1):
        heap.push(i)
    assert all_items(heap) == range(1, 6)
