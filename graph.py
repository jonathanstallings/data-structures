from __future__ import unicode_literals


class Graph(object):
    """A class for a simple graph data structure."""
    def __init__(self):
        self.graph = {}

    def __repr__(self):
        return repr(self.graph)

    def __len__(self):
        return len(self.graph)

    def __iter__(self):
        return iter(self.graph)

    def __getitem__(self, index):
        return self.graph[index]

    def __setitem__(self, index, value):
        self.graph[index] = value

    def __delitem__(self, index):
        del self.graph[index]

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return [node for node in self.graph]

    def edges(self):
        """Return a list of all edges in the graph."""
        return "edge list"

    def add_node(self, n):
        """Add a new node to the graph."""
        self.graph[n] = set()

    def add_edge(self, n1, n2):
        """Add a new edge connecting n1 to n2."""
        self.graph[n1].add(n2)

    def del_node(self, n):
        """Delete a node from the graph."""
        del self.graph[n]
        for edgeset in self.graph.values():
            edgeset.discard(n)

    def del_edge(self, n1, n2):
        """Delete the edge connecting two nodes from graph."""
        self.graph[n1].remove(n2)

    def has_node(self, n):
        """Check if a given node is in the graph."""
        return n in self.graph

    def neighbors(self, n):
        """Return a list of all nodes connected to 'n' by edges."""
        neighbors = []
        for node in self.graph:
            if n in self.node:
                neighbors.append(node)
        return neighbors
