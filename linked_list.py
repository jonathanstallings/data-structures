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
        to_return = self.header  # Use tuple reassignment
        self.header = to_return.next
        # to_return, self.header = self.header, to_return.next
        to_return.next = None
        self.length -= 1
        return to_return

    def size(self):
        """Return current length of LinkedList."""
        return self.length

    def search(self, val):
        """Return the node containing val if present, else None"""
        node, left = self._find(val)
        return node

    def remove(self, val):  # Check Spec: Pass node vs val
        """Remove given node from list, return None"""
        node_to_remove, left_neighbor = self._find(val)

        if self.header == node_to_remove:
            self.pop()

        else:
            left_neighbor.next = node_to_remove.next
            node_to_remove.next = None

        return None

    def display(self):
        """Print LinkedList as Tuple literal"""
        return self.__repr__()

    def _find(self, val):  # Check with spec re: this.
        """Return a Node and left-neighboor by val."""
        val_present = False
        node_inspected = self.header
        left_node = None

        while not val_present:
            #  Interrogate each Node
            if node_inspected.val == val:
                val_present = True
                break
            else:
                #  Keeping track of node to left; incrementing node
                left_node, node_inspected = node_inspected, node_inspected.next

        return node_inspected, left_node
