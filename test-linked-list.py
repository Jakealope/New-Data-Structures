import pytest

# This will be the tests for a linked list


def test_node_data():
    new = Node("Bob")
    assert new.data == "Bob"


def test_node_add():
    bob = Node("Bob")
    new = LinkedList()
    new.insert(bob)
    assert new.firstNode.data == "Bob"
