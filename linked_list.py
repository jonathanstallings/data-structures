from __future__ import unicode_literals


class Node(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Print representation of node."""
        return "{val}".format(val=self.val)


class LinkedList(object):
    """Class for a singly-linked list."""
    def __init__(self, iterable=()):
        self.header = None
        self.length = 0
        for val in reversed(iterable):
            self.insert(val)

    def __repr__(self):
        """Print representation of LinkedList."""
        node = self.header
        output = ""
        while node is not None:
            output += "{!r}, ".format(node.val)
            node = node.next
        return "({})".format(output.rstrip(' ,'))

    def insert(self, val):
        """Insert value at head of LinkedList.

        args:
            val: the value to add
        """
        self.header = Node(val, self.header)
        self.length += 1
        return None

    def pop(self):
        """Pop the first val off the head and return it."""
        if self.header is None:
            raise IndexError
        else:
            to_return = self.header
            self.header = to_return.next
            self.length -= 1
            return to_return

    def size(self):
        """Return current length of LinkedList."""
        return self.length

    def search(self, val):
        """Return the node containing val if present, else None.

        args:
            val: the value to add
        """
        node, _ = self._find(val)
        return node

    def remove(self, node):
        """Remove given node from list, return None.

        args:
            node: the node to be removed
        """
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
        Return a node and previous by matching against value or node.

        args:
            val: the value to find
            node: optionally, node to match identity against
        """
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
            #  Keeping track of node to left; incrementing node
            elif node_inspected.next is not None:
                left_node, node_inspected = node_inspected, node_inspected.next
            else:
                return None

        return node_inspected, left_node
