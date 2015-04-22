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
