from __future__ import unicode_literals

from linked_list import LinkedList


class Queue():

    def __init__(self, iterable=()):
        self.other = LinkedList()
        self.other_init__(iterable)
        self.tail = None

    def __repr__(self):
        pass

    def __len__(self):
        pass

    def enqueue(self, value):
        """Add a value to the tail of a queue

        args:
            value: The value to add to the queue
        """
        pass

    def dequeue(self):
        """Remove a value from the head of the queue"""
        pass
