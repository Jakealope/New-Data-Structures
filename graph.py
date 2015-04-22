# a simple graph that will allow us to impliment a graph data structure

import heapq


class SimpleGraph(object):

    def __init__(self, edges=None):
        self.dict_graph = {}

    def nodes(self):
        '''return a iterator through of all nodes in the graph'''
        return self.dict_graph.iterkeys()

    def edges(self):
        '''return a list of all edges in the graph'''
        edges = []
        for key, value in self.dict_graph.iteritems():
            for item in value:
                edges.append((key, item))
        return edges
