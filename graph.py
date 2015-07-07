from __future__ import unicode_literals


class Graph(object):
    """A class for a simple graph data structure."""
    def __init__(self):
        self.nodes = {}

    def __repr__(self):
        pass

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return [node for node in self.nodes]

    def edges(self):
        """Return a list of all edges in the graph."""
        return "edge list"

    def add_node(self, n):
        """Add a new node to the graph."""
        self.nodes[n] = set()

    def add_edge(self, n1, n2):
        """Add a new edge connecting n1 to n2."""
        self.nodes[n1].add(n2)

    def del_node(self, n):
        """Delete a node from the graph."""
        del self.nodes[n]
        for edgeset in self.nodes.values:
            edgeset.discard(n)

    def del_edge(self, n1, n2):
        """Delete the edge connecting two nodes from graph."""
        self.nodes[n1].remove(n2)

    def has_node(self, n):
        """Check if a given node is in the graph."""
        return n in self.nodes

    def neighbors(self, n):
        """Return a list of all nodes connected to 'n' by edges."""
        neighbors = []
        for node in self.nodes:
            if n in self.node:
                neighbors.append(node)
        return neighbors
