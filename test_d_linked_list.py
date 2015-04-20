# This file is for testing the Double Linked List

from d_linked_list import DLinked
import pytest


def test_insert_one():
    linked = DLinked()
    linked.insert("Bob")
    assert linked.first_item.val == "Bob"


def test_insert_multi():
    linked = DLinked()
    linked.insert("Fred")
    linked.insert("Bob")
    linked.insert("Joe")
    assert linked.first_item.val == "Joe"
