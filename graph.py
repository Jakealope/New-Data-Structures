# a simple graph that will allow us to impliment a graph data structure

import heapq


class SimpleGraph(object):

    def __init__(self, edges=None):
        self.dict_graph = {}

    def nodes(self):
        '''return a iterator through of all nodes in the graph'''
        return self.dict_graph.iterkeys()
