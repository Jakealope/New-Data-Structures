from linked_list.py import Node, LinkedList
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


def test_next_node_none():
    bob = Node("Bob")
    new = LinkedList()
    new.insert(bob)
    assert new.firstNode.nextNode is None


def test_add_second_node():
    joe = Node("Joe")
    bob = Node("Bob")
    new = LinkedList()
    new.insert(bob)
    new.insert(joe)
    assert new.firstNode.nextNode.data == "Bob"
