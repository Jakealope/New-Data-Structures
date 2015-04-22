# This file is for testing the Double Linked List

from d_linked_list import DLinked
import pytest


def test_insert_one():
    linked = DLinked()
    linked.insert("Bob")
    assert linked.first.val == "Bob"


def test_insert_multi():
    linked = DLinked()
    linked.insert("Fred")
    linked.insert("Bob")
    linked.insert("Joe")
    assert linked.first.val == "Joe"


def test_append_one():
    linked = DLinked()
    linked.append("Bob")
    assert linked.last.val == "Bob"


def test_append_multi():
    linked = DLinked()
    linked.append("Fred")
    linked.append("Bob")
    linked.append("Joe")
    assert linked.last.val == "Joe"


def test_pop_one():
    linked = DLinked()
    linked.insert("Bob")
    assert linked.pop() == "Bob"


def test_pop_empty():
    linked = DLinked()
    with pytest.raises(ValueError):
        linked.pop()


def test_shift_one():
    linked = DLinked()
    linked.insert("Bob")
    assert linked.shift() == "Bob"


def test_shift_empty():
    linked = DLinked()
    with pytest.raises(ValueError):
        linked.shift()


def test_remove_empty():
    linked = DLinked()
    with pytest.raises(AttributeError):
        linked.remove("Bob")


def test_remove_one():
    linked = DLinked()
    linked.insert("Bob")
    linked.remove("Bob")
    with pytest.raises(AttributeError):
        linked.remove("Bob")


def test_remove_wrong():
    linked = DLinked()
    linked.insert("Fred")
    linked.insert("Bob")
    linked.insert("Joe")
    with pytest.raises(ValueError):
        linked.remove("Sue")


def test_multi():
    linked = DLinked()
    linked.insert("Fred")
    linked.insert("Bob")
    linked.insert("Joe")
    assert linked.first.val == "Joe"
