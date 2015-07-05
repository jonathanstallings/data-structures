from __future__ import unicode_literals
from functools import total_ordering

from binary_heap import BinaryHeap


@total_ordering  # Will build out the remaining comparison methods
class QNode(object):
    """A class for a queue node."""
    def __init__(self, val, priority=None):
        """Initialize a QNode with a value and an optional priority.

        Priority must be an integer, most important being 0.
        """
        self.val = val
        self.priority = priority

    def __repr__(self):
        """Print representation of node."""
        return "{val}".format(val=self.val)

    def __str__(self):
        """Pretty print node value and priority."""
        return "{val}, Priority:{p}".format(val=self.val, p=self.priority)

    def __eq__(self, other):
        """Overloads equality comparison to check priority, then value."""
        if self.priority == other.priority:
            return self.val == other.val
        elif self.priority is None or other.priority is None:
            return False
        else:
            return self.priority == other.priority

    def __lt__(self, other):
        """Overloads lesser than comparison to check priority, then value."""
        if self.priority == other.priority:
            return self.val < other.val
        elif self.priority is None:
            return False
        elif other.priority is None:
            return True
        else:
            return self.priority < other.priority


class PriorityQ(object):
    """A class for a priority queue."""
    def __init__(self, iterable=()):
        """Initialize a priority queue, optionally with items from iterable.

        The items in the priority queue are stored in a binary minheap. Items
        first sorted by priority, then value. Priority is expressed as an
        integer with 0 being the most important.

        args:
            iterable: an optional iterable to add to the priority queue. Items
                      added this way will be given a priority of None.
        """
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
        """Insert an item into the priority queue.

        If the item is a QNode object, it will be added as is.
        If not, a new QNode object is created to hold the item with optional
        priority assigned.

        args:
            item: the item to add (QNode or other value)
            priority: the optional integer priority (0 is most important)
        """
        if isinstance(item, QNode):
            self.heap.push(item)
        else:
            self.heap.push(QNode(item, priority))

    def pop(self):
        """Remove and return the most important item from the queue."""
        return self.heap.pop()

    def peek(self):
        """Return the most important item from queue without removal."""
        return self.heap[0]
