# tests for a simple graph

from graph import SimpleGraph
import pytest


def test_add_nodes():
    """nodes are added"""
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    assert 'a' in g.nodes()
    assert 'b' in g.nodes()
    assert 'c' in g.nodes()


def test_del_nodes():
    """nodes are deleted"""
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    g.del_node('a')
    assert 'a' not in g.nodes()
    assert g.has_node('a') is False


def test_del_error():
    """error raised when non-existant value deleted"""
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    with pytest.raises(KeyError):
        g.del_node('p')


def test_del_edge():
    """other edges preserved when one deleted"""
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    g.del_edge('a', 'c')
    assert g.neighbors('a') == {'b': 0}


def test_add_edge():
    """edge added, new node added"""
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    g.add_edge('q', 'a')
    assert g.has_node('q')
    assert g.neighbors('q') == {'a': 0}


def test_edge_error():
    """delete non-existant edge"""
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    with pytest.raises(KeyError):
        g.del_edge('a', 'z')


def test_has_node():
    """edge added, new node added"""
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    assert g.has_node('b')


def test_adjacent():
    """adjacent correctly identify edges, new edge add node"""
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'd')
    g.add_edge('a', 'f')
    assert 'f' in g.nodes()
    assert g.adjacent('a', 'd')
    assert not g.adjacent('a', 'b')


def test_adjacent_error():
    """error raised when nodes non-existant"""
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    with pytest.raises(KeyError):
        g.adjacent('l', 'm')


def test_edges():
    """edges prints correct edges as tuples"""
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    assert ('a', 'c') in g.edges()
    assert ('a', 'b') in g.edges()


def test_breadth():
    g = SimpleGraph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'c')
    g.add_edge('b', 'd')
    g.add_edge('b', 'e')
    g.add_edge('e', 'f')
    g.add_edge('f', 'g')
    assert g.breadth_first_traversal('a') == ['a', 'c', 'b', 'e', 'd', 'f', 'g']
