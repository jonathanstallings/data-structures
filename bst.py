from __future__ import unicode_literals


class Node(object):
    """A class for a binary search tree node."""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return '{}'.format(self.val)

    def insert(self, val):
        """Insert a node with a value into the tree.

        If val is already present, it will be ignored.

        args:
            val: the value to insert
        """
        if val == self.val:
            return None
        if val < self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)

    def contains(self, val):
        """Check tree for node with given value.

        args:
            val: the value to check for

        returns: True if val is in the tree, False if not.
        """
        if val == self.val:
            return True
        elif val < self.val:
            if self.left is None:
                return False
            return self.left.contains(val)
        elif val > self.val:
            if self.right is None:
                return False
            return self.right.contains(val)

    def size(self):
        """Return the total number of nodes in the tree.

        returns: integer of total node; 0 if empty
        """
        left_size = self.left.size() if self.left is not None else 0
        right_size = self.right.size() if self.right is not None else 0
        return left_size + right_size + 1

    def depth(self):
        """Return an the total number of levels in the tree.

        If there is one value, the depth should be 1, if two values it'll be 2,
        if three values it may be 2 or three, depending, etc.

        returns: integer of level number
        """
        left_depth = self.left.depth() if self.left is not None else 0
        right_depth = self.right.depth() if self.right is not None else 0
        return max(left_depth, right_depth) + 1

    def balance(self):
        """Return a positive or negative number representing tree balance.

        Trees higher on the left than the right should return a positive value,
        trees higher on the right than the left should return a negative value.
        An ideally-balanced tree should return 0.

        returns: integer
        """
        left_depth = self.left.depth() if self.left is not None else 0
        right_depth = self.right.depth() if self.right is not None else 0
        if left_depth > right_depth:
            return 1
        elif left_depth < right_depth:
            return -1
        else:
            return 0

