from __future__ import unicode_literals

from linked_list import LinkedList, Node


class Queue():

    def __init__(self, iterable=()):
        self.other = LinkedList()
        self.header = None
        self.tail = None
        self.length = 0
        for val in (iterable):
            self.enqueue(val)

    def __repr__(self):
        return repr(self.other)

    def __len__(self):
        return self.length

    def enqueue(self, value):
        """Add a value to the tail of a queue.

        args:
            value: The value to add to the queue
        """
        new_node = Node(value)  # Need to fix this logic
        if len(self) == 0:
            self.header = new_node
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def dequeue(self):
        """Remove and return a value from the head of the queue."""
        return self.other.pop()

    def size(self):
        return len(self)
