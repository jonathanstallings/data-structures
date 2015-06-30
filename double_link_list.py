from __future__ import unicode_literals


class Node(object):

    def __init__(self, val, prev=None, next_=None):
        self.val = val
        self.prev = prev
        self.next = next_

    def __repr__(self):
        """Print representation of node."""
        return "{val}".format(val=self.val)


class DoubleLinkList(object):
    """Class for a doubly-linked list."""
    def __init__(self, iterable=()):
        self._current = None
        self.head = None
        self.tail = None
        self.length = 0
        for val in reversed(iterable):
            self.insert(val)

    def __repr__(self):
        """Print representation of DoubleLinkList."""
        node = self.head
        output = ""
        for node in self:
            output += "{!r}, ".format(node.val)
        return "({})".format(output.rstrip(' ,'))

    def __len__(self):
        return self.length

    def __iter__(self):
        if self.head is not None:
            self._current = self.head
        return self

    def next(self):
        if self._current is None:
            raise StopIteration
        node = self._current
        self._current = self._current.next
        return node

    def insert(self, val):
        """Insert value at head of DoubleLinkList.

        args:
            val: the value to add
        """
        old_head = self.head
        self.head = Node(val, prev=None, next_=old_head)
        if old_head is None:
            self.tail = self.head
        else:
            old_head.prev = self.head
        self.length += 1
        return None

    def pop(self):
        """Pop the first val off the head and return it."""
        if self.head is None:  # Add tail management
            raise IndexError
        else:
            to_return = self.head
            self.head = to_return.next
            self.head.prev = None
            if len(self) == 0:
                self.tail = None
            self.length -= 1
            return to_return.val

    def size(self):
        """Return current length of DoubleLinkList."""
        return len(self)

    def search(self, search_val):
        """Return the node containing val if present, else None.

        args:
            search_val: the value to search by

        returns: a node object or None
        """
        for node in self:
            if node.val == search_val:
                return node
        else:
            return None

    def remove(self, search_node):
        """Remove given node from list, return None.

        args:
            search_node: the node to be removed
        """
        if search_node == self.head:
            self.header = search_node.next
            self.header.prev = None
        elif search_node == self.tail:
            self.tail = search_node.prev
            self.tail.next = None
        else:
            for node in self:
                if node == search_node:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    return None


    def append(self, val):
        """Append a node with value to end of list."""
        current_tail = self.tail  # update with head management
        self.tail = Node(val, prev=current_tail, next_=None)
        if current_tail is not None:
            current_tail.next = self.tail
        self.length += 1
        return None

    def shift(self):
        """Remove the last value from the tail and return."""
        if self.tail is None:  # Update with head management
            raise IndexError
        else:
            to_return = self.tail
            self.tail = to_return.prev
            self.tail.next = None
            self.length -= 1
            return to_return.val

    def display(self):
        """Shows representation of DoubleLinkList."""
        return repr(self)
