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
        """Implement this and following method with logic to compare
        priority and value appropiately.
        """
        if self.priority is None and other.priority is None:
            self.value == other.value
        elif self.priority is None or other.priority is None:
            return False
        else:
            self.priority == other.priority

    def __lt__(self, other):
        """Implement in tandem with __eq__."""
        if self.priority is None and other.priority is None:
            self.value < other.value
        elif self.priority is None or other.priority is None:
            self.priority > other.priority  # Since None is less than anything
        else:
            self.priority < other.priority


class PriorityQ(object):
    """A class for a priority queue. Compose this from BinaryHeap."""
    def __init__(self, iterable=()):
        """We can iteratively use insert here."""
        self.heap = BinaryHeap(iterable=())
        for item in iterable:
            self.insert(item)

    def insert(self, item, priority=None):  # Want to extend spec to add priority as 2nd optional arg
        """Insert an item into the queue. Would be nice to examine item as follows:
        If item is node:
            add to PriorityQ
        else:
            init QNode with item as val and priority as None
            add to PriorityQ
        """
        if isinstance(item, QNode):
            self.heap.push(item)
        else:
            self.heap.push(QNode(item, priority))

    def pop():
        """Remove the most important item from the queue."""
        pass

    def peek():
        """Returns the most important item from queue without removal."""
