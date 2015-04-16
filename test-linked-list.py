from linked_list import Node, LinkedList
import pytest

# This will be the tests for a linked list


def test_node_val():
    new = Node("Bob")
    assert new.val == "Bob"


def test_node_add():
    bob = Node("Bob")
    new = LinkedList()
    new.insert(bob)
    assert new.first.val == "Bob"


def test_next_node_none():
    bob = Node("Bob")
    new = LinkedList()
    new.insert(bob)
    assert new.first._next is None


def test_add_second_node():
    joe = Node("Joe")
    bob = Node("Bob")
    new = LinkedList()
    new.insert(bob)
    new.insert(joe)
    assert new.first._next.val == "Bob"


def test_pop():
    joe = Node("Joe")
    bob = Node("Bob")
    new = LinkedList()
    new.insert(bob)
    new.insert(joe)
    assert new.pop() == "Joe"


def test_pop_size():
    joe = Node("Joe")
    bob = Node("Bob")
    new = LinkedList()
    new.insert(bob)
    new.insert(joe)
    new.pop()
    assert new.size() == 1


def test_size():
    joe = Node("Joe")
    bob = Node("Bob")
    new = LinkedList()
    new.insert(bob)
    new.insert(joe)
    assert new.size() == 2


def test_search_fail():
    joe = Node("Joe")
    bob = Node("Bob")
    new = LinkedList()
    new.insert(bob)
    new.insert(joe)
    assert new.search("Fred") is None


def test_search_success():
    joe = Node("Joe")
    bob = Node("Bob")
    new = LinkedList()
    new.insert(bob)
    new.insert(joe)
    assert new.search("Bob") == bob


def test_remove():
    joe = Node("Joe")
    bob = Node("Bob")
    new = LinkedList()
    new.insert(bob)
    new.insert(joe)
    new.remove(bob)
    assert new.search("Bob") is None


def test_remove_empty():
    new = LinkedList()
    assert new.remove("Bob") == "THE LIST! IT'S EMPTY!!"


def test_pop_empty():
    new = LinkedList()
    assert new.pop() == "THE LIST! IT'S EMPTY!!"


def test_remove_fail():
    joe = Node("Joe")
    bob = Node("Bob")
    new = LinkedList()
    new.insert(bob)
    new.insert(joe)
    with pytest.raises(ValueError):
        new.remove("Fred")
