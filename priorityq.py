from __future__ import unicode_literals
from functools import total_ordering

from binary_heap import BinaryHeap


@total_ordering  # Will build out the remaining comparison methods
class QueueNode(object):
    """A class for a queue node."""
    def __init__(self, val, priority):
        super(QueueNode, self).__init__()
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
        pass

    def insert(item):
        """Insert an item into the queue."""
        pass

    def pop():
        """Remove the most importan item from the queue."""
        pass

    def peek():
        """Returns the most important item from queue without removal."""
