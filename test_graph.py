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
