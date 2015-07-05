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

    def __str__(self):
        """Pretty print node value and priority."""
        return "{val}, Priority:{p}".format(val=self.val, p=self.priority)

    def __eq__(self, other):
        """Implement this and following method with logic to compare
        priority and val appropiately.
        """
        if self.priority == other.priority:
            return self.val == other.val
        elif self.priority is None or other.priority is None:
            return False
        else:
            return self.priority == other.priority

    def __lt__(self, other):
        """Implement in tandem with __eq__."""
        if self.priority == other.priority:
            return self.val < other.val
        elif self.priority is None:
            return False
        elif other.priority is None:
            return True
        else:
            return self.priority < other.priority


class PriorityQ(object):
    """A class for a priority queue. Compose this from BinaryHeap."""
    def __init__(self, iterable=()):
        """We can iteratively use insert here."""
        self.heap = BinaryHeap(iterable=())
        for item in iterable:
            self.insert(item)

    def __repr__(self):
        return repr(self.heap)

    def __len__(self):
        return len(self.heap)

    def __iter__(self):
        return iter(self.heap)

    def __getitem__(self, index):
        return self.heap[index]

    def __setitem__(self, index, value):
        self.heap[index] = value

    def insert(self, item, priority=None):
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

    def pop(self):
        """Remove the most important item from the queue."""
        return self.heap.pop()

    def peek(self):
        """Returns the most important item from queue without removal."""
        return self.heap[0]
