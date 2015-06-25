from __future__ import unicode_literals
from linked_list import LinkedList


class Stack():

    def __init__(self, iterable=()):
        self.other = LinkedList()
        self.other.__init__(iterable)

    def __repr__(self):
        return self.other.__repr__()

    def push(self, value):
        """Will add a value to the stack"""
        self.other.insert(value)

    def pop(self):
        """Will remove val from stack and return"""
        val = self.other.pop()

        return val
