from __future__ import unicode_literals


class Node(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        #  Just display value
        return "{val}".format(val=self.val)


class LinkedList(object):
    """Class for a singly-linked list."""
    def __init__(self, iterable=()):
        self.header = None
        self.length = 0
        for val in reversed(iterable):
            self.insert(val)

    def __repr__(self):
        """Print LinkedList as Tuple literal."""
        node = self.header
        output = ""
        while node is not None:
            output += "{!r}, ".format(node.val)
            node = node.next
        return "({})".format(output.rstrip(' ,'))

    def insert(self, val):
        """Insert val at head of LinkedList."""
        self.header = Node(val, self.header)
        self.length += 1
        return None

    def pop(self):
        """Pop the first val off the head and return it."""
        if self.header is None:
            raise IndexError
        else:
            to_return = self.header  # Use tuple reassignment
            self.header = to_return.next
            self.length -= 1
            return to_return

    def size(self):
        """Return current length of LinkedList."""
        return self.length

    def search(self, val):
        """Return the node containing val if present, else None"""
        node, left = self._find(val)
        return node

    def remove(self, node):  # Check Spec: Pass node vs val
        """Remove given node from list, return None"""
        node_to_remove, left_neighbor = self._find(node.val, node)

        if self.header == node_to_remove:
            self.pop()

        else:
            left_neighbor.next = node_to_remove.next

        return None

    def display(self):
        """Print LinkedList as Tuple literal"""
        return self.__repr__()

    def _find(self, val, node=None):
        """
        Return a node and previous by matching against value or node."""
        matched = False
        node_inspected = self.header
        left_node = None

        while not matched:
            #  Interrogate each Node
            if node_inspected.val == val:
                if node is not None:
                    if node_inspected is node:
                        matched = True
                        break
                else:
                    matched = True
                    break
            else:
                #  Keeping track of node to left; incrementing node
                left_node, node_inspected = node_inspected, node_inspected.next

        return node_inspected, left_node
