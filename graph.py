from __future__ import unicode_literals

from queue import Queue
import priorityq as pq


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
        for edgeset in self.graph.values():
            edgeset.pop(index, None)

    def add_node(self, n):
        """Add a new node to the graph. Will raise an error if node
        already exists.

        Note that node name 'n' needs to be a hashable or immutable value
        """
        if self.has_node(n):
            raise KeyError('Node already in graph.')
        self[n] = dict()

    def add_edge(self, node1, node2, edge_weight):
        """Add a new edge connecting n1 to n2. Will implicitly create
        n1 and n2 if either do not exist.
        """
        if not self.has_node(node2):
            self.add_node(node2)
        try:
            self[node1].update({node2: edge_weight})
        except KeyError:
            self.add_node(node1)
            self[node1].update({node2: edge_weight})

    def del_node(self, n):
        """Delete a node from the graph. Will cleanup all edges pointing
        towards the node being deleted.
        """
        del self[n]

    def del_edge(self, n1, n2):
        """Delete stated edge connecting node n1 to n2. Will raise a KeyError
        if the edge does not exist.
        """
        self[n1].pop(n2)

    def has_node(self, n):
        """Check if a given node is in the graph, return True if it exists,
        False otherwise.
        """
        return n in self

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return [node for node in self]

    def iter_edges(self):
        """Generate an iterator packed with all existing edges in
        (node, edge) format.
        """
        for node in self:
            for edge in self[node]:
                yield (node, edge)

    def edges(self):
        """Return a list of all edges in (node, edge_node) format,
        where node points to edge_node.
        """
        return list(self.iter_edges())

    def iter_neighbors(self, n):
        """Generate an iterator packed with all existing edges for node."""
        for node in self:
            if n in self[node]:
                yield node

    def neighbors(self, n):
        """Return the set of edges that node n points towards."""
        return self[n]

    def adjacent(self, n1, n2):
        """Check if there is an edge pointing from node n1 to n2."""
        return n2 in self[n1]

    def depth_first_traversal(self, start):
        """Perform full depth-first traversal of graph from start.

        args:
            start: the node to start traversal

        returns: the list of nodes traversed
        """
        path = []
        visited = set()

        def step(node, path, visited):
            if node not in visited:
                path.append(node)
                visited.add(node)
                for child in iter(self[node]):
                    step(child, path, visited)
                return

        step(start, path, visited)
        return path

    def breadth_first_traversal(self, start):
        """Perform a full breadth first traversal of graph from start.

        args:
            start: the node to start traversal

        returns: a list of nodes traversed
        """
        path = []
        visited = set()
        temp = Queue([start])

        while temp:
            node = temp.dequeue()
            if node not in visited:
                path.append(node)
                visited.add(node)
                for child in self[node]:
                    if child not in visited:
                        temp.enqueue(child)
        return path

    def uniform_cost_search(self, start, goal):
        """Return the shortest path from start to goal node.

        args:
            start: the node to begin the path
            goal: the node to end the path
        """
        q = pq.PriorityQ()
        q.insert((0, start, []), priority=0)
        seen = {}

        while q:
            cost, point, path = q.pop()
            if point in seen and seen[point] < cost:
                continue
            path = path + [point]
            if point == goal:
                return path
            for child in self[point]:
                child_cost = self[point][child]
                if child not in seen:
                    tot_cost = child_cost + cost
                    q.insert((tot_cost, child, path), priority=tot_cost)
            seen[point] = cost
        return None

    def bellmanford(self, node1, node2):
        """Find the shortest path from node1 to node2

        It is possible to access a graph with negatives weights using this
        algorithm

        This implementation is adapted for Python from the pseudocode
        here:
        https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm#Algorithm

        This algorithm is currently generating useful, extra data that
        isn't being returned. May want to update the API to allow access
        to this info.
        """

        distance = {node: float("inf") if node != node1 else 0
                     for node in self}

        predecessor = {node: None for node in self}

        for _ in self:
            for node in self:
                # Point of this and inner loop is to grab each of the edges by
                # node times; expect O( node * edge ); note that edges are nested
                # under nodes dict ; hence two inner loops needed to grab these
                for edgen, weight in self[node].iteritems():
                    if distance[node] + weight < distance[edgen]:
                        distance[edgen] = distance[node] + weight
                        predecessor[edgen] = node
        for node in self:
                # Consistancy check per pseudo code; check for loops where
                # cost is negative per cycle
                for edgen, weight in self[node].iteritems():
                    if distance[node] + weight < distance[edgen]:
                        raise ZeroDivisionError
        # Now build a path from predecessor dict
        rpath = []
        pointer = node2
        while True:
            rpath.append(pointer)
            if pointer == node1:
                break
            pointer = predecessor[pointer]
        rpath.reverse()
        return rpath
