from __future__ import unicode_literals

from linked_list import LinkedList, Node


class Queue():

    def __init__(self, iterable=()):
        self.other = LinkedList()
        self.other.header = None
        self.other.tail = None
        self.other.length = 0
        for val in (iterable):
            self.enqueue(val)

    def __repr__(self):
        return repr(self.other)

    def __len__(self):
        return self.other.length

    def enqueue(self, value):
        """Add a value to the tail of a queue.

        args:
            value: The value to add to the queue
        """
        new_node = Node(value)  # Need to fix this logic
        if self.other.tail is None:
            self.other.header = self.other.tail = new_node
        else:
            self.other.tail.next = new_node
            self.other.tail = new_node
        self.other.length += 1

    def dequeue(self):
        """Remove and return a value from the head of the queue."""
        return self.other.pop()

    def size(self):
        return len(self)
