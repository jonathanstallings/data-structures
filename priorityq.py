from __future__ import unicode_literals
from functools import total_ordering

from binary_heap import BinaryHeap


@total_ordering  # Will build out the remaining comparison methods
class QNode(object):
    """A class for a queue node."""
    def __init__(self, val, priority=None):
        self.val = val
        self.priority = priority

    def __repr__(self):
        """Print representation of node."""
        return "{val}".format(val=self.val)

    def __eq__(self, other):
        """Implement this and following two methods with logic to compare
        priority and value appropiately.
        """
        pass

    def __lt__(self, other):
        """Implement in tandem with __eq__."""
        pass


class PriorityQ(object):
    """A class for a priority queue. Compose this from BinaryHeap."""
    def __init__(self, iterable=()):
        """We can iteratively use insert here."""
        pass

    def insert(item):  # Wamt to extend spec to include priority as 2nd arg
        """Insert an item into the queue. Would be nice to examine item as follows:
        If item is node:
            add to PriorityQ
        else:
            init QNode with item as val and priority as None
        """
        pass

    def pop():
        """Remove the most important item from the queue."""
        pass

    def peek():
        """Returns the most important item from queue without removal."""
