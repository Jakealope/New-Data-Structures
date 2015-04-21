from bin_heap import BinaryHeap
import pytest


def test_is_empty():
    bin_list = BinaryHeap()
    assert bin_list.heaplist == [0]


def test_one_push_pop():
    bin_list = BinaryHeap()
    bin_list.push(10)
    assert bin_list.pop() == 10
