from __future__ import unicode_literals


class LinkedList(object):
    """Class for a singly-linked list."""
    def __init__(self, iterable):
        self.length = len(iterable)  # Will resize for pop, insert, remove
        self.header = None
        stored_for_next = None  # Seed value

        for index, val in zip(range(self.length, 0, -1), reversed(iterable)):
            if index == self.length:
                # Case: right-most item in linked list; implicit None for next
                created = Node(val)
            elif index == 1:
                # Case of needing to store list header
                self.header = Node(val, stored_for_next)
            else:
                # All other linked nodes
                created = Node(val, stored_for_next)

            stored_for_next = created  # Store for next iteration

    def __repr__(self):
        """Print LinkedList as Tuple literal."""
        end_flag = False
        vals = []
        current_node = self.header

        while not end_flag:
            vals.append(current_node.val)

            if current_node.next:
                current_node = current_node.next

            else:
                end_flag = True
                break

        vals = tuple(vals)
        return str(vals)

    def insert(self, val):
        """Insert val at head of LinkedList."""
        self.header = Node(val, self.header)
        self.length += 1
        return None

    def pop(self):
        """Pop the first val off the head and return it."""
        to_return = self.header
        self.header = to_return.next
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

    def _find(self, val):
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
                left_node = node_inspected
                node_inspected = node_inspected.next

        return node_inspected, left_node


class Node(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        #  Just display value
        return "{val}".format(val=self.val)
