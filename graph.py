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
        return [node for node in self]

    def edges(self):
        """Return a list of all edges in the graph."""
        edge_list = []
        for node in self:
            for edge in self[node]:
                edge_list.append([node, edge])
        return edge_list

    def add_node(self, n):
        """Add a new node to the graph."""
        self.graph.setdefault(n, set())  # Good! But should warn on 2nd add?

    def add_edge(self, n1, n2):
        """Add a new edge connecting n1 to n2."""
        self[n1].add(n2)

    def del_node(self, n):
        """Delete a node from the graph."""
        del self[n]
        for edgeset in self.graph.values():
            edgeset.discard(n)

    def del_edge(self, n1, n2):
        """Delete the edge connecting two nodes from graph."""
        self[n1].remove(n2)

    def has_node(self, n):
        """Check if a given node is in the graph."""
        return n in self

    def neighbors(self, n):
        """Return a list of all nodes connected to 'n' by edges."""
        neighbors = []
        for node in self:
            if n in self[node]:
                neighbors.append(node)
        return neighbors

    def adjacent(self, n1, n2):
        """Check if there is an edge connecting 'n1' and 'n2'."""
        return n2 in self[n1] or n1 in self[n2]


#  helper start conditions for testing
def helper():
    g = Graph()
    g.add_node(5)
    g.add_node(10)
    g.add_node(20)
    g.add_edge(10, 5)
    g.add_edge(10, 20)
    g.add_edge(5, 10)
    return g

