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
        """insert a node with val into the BST.

        If val is already present, it will be ignored.
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
        """return True if val is in the BST, False if not"""
        # import pdb; pdb.set_trace()
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
        """return the integer size of the BST.

        (equal to the total number of values stored in the tree),
        0 if the tree is empty.
        """
        left_size = self.left.size() if self.left is not None else 0
        right_size = self.right.size() if self.right is not None else 0
        return left_size + right_size + 1

    def depth(self):
        """return an integer representing the total number of levels in the tree.

        If there is one value, the depth should be 1, if two values it'll be 2,
        if three values it may be 2 or three, depending, etc.
        """
        left_depth = self.left.depth() if self.left is not None else 0
        right_depth = self.right.depth() if self.right is not None else 0
        return max(left_depth, right_depth) + 1

    def balance(self):
        """return an integer, positive or negative represents how balanced the tree is.

        Trees which are higher on the left than the right should return a positive value,
        trees which are higher on the right than the left should return a negative value.
        An ideallyl-balanced tree should return 0.
        """
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        if left_depth > right_depth:
            return 1
        elif left_depth < right_depth:
            return -1
        else:
            return 0
