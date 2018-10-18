from __future__ import unicode_literals

from linked_list import LinkedList


class Stack():

    def __init__(self, iterable=()):
        self.other = LinkedList()
        self.other.__init__(iterable)

    def __repr__(self):
        return repr(self.other)

    def push(self, value):
        """Add a value to the head of the stack.

        args:
            value: The value to add to the stack
        """
        self.other.insert(value)

    def pop(self):
        """Remove a value from head of stack and return."""
        return self.other.pop()
