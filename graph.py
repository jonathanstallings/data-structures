from __future__ import unicode_literals


class Graph(object):
    """A class for a simple graph data structure."""
    def __init__(self):
        self.graph = {}

    def __repr__(self):  # Consider how we want to repr this.
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
        for edgeset in self.graph.values():
            edgeset.discard(index)

    def add_node(self, n):
        """Add a new node to the graph. Will raise an error if node 
        already exists.

        Note that node name 'n' needs to be a hashable or immutable value"""
        if self.has_node(n):
            raise KeyError('Node already in graph.')
        self[n] = set()

    def add_edge(self, n1, n2):
        """Add a new edge connecting n1 to n2. Will implicitly create 
        n1 and n2 if either do not exist."""
        if not self.has_node(n2):
            self.add_node(n2)
        try:
            self[n1].add(n2)
        except KeyError:
            self.add_node(n1)
            self[n1].add(n2)

    def del_node(self, n):
        """Delete a node from the graph. Will cleanup all edges pointing
        towards the node being deleted"""
        del self[n]

    def del_edge(self, n1, n2):
        """Delete stated edge connecting node n1 to n2. Will raise a KeyError
        if the edge does not exist"""
        self[n1].remove(n2)

    def has_node(self, n):
        """Check if a given node is in the graph, return True if it exists,
        False otherwise"""
        return n in self

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return [node for node in self]

    def iter_edges(self):
        """Generate an iterator packed with all existing edges in
        (node, edge) format"""
        for node in self:
            for edge in self[node]:
                yield (node, edge)

    def edges(self):
        """Return a list of all edges in (node, edge_node) format,
        where node points to edge_node"""
        return list(self.iter_edges())

    def iter_neighbors(self, n):
        """Generate an iterator packed with all existing edges for node
        n"""
        for node in self:
            if n in self[node]:
                yield node

    def neighbors(self, n):
        """Return the set of edges that node n points towards"""
        return self[n]

    def adjacent(self, n1, n2):
        """Check if there is an edge pointing from node n1 to n2"""
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

