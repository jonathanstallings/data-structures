from __future__ import unicode_literals


class Node(object):
    """A class for a binary search tree node."""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        """insert a node with val into the BST.

        If val is already present, it will be ignored.
        """
        if self.contains(val):
            return
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
        pass

    def size(self):
        """return the integer size of the BST.

        (equal to the total number of values stored in the tree),
        0 if the tree is empty.
        """
        pass

    def depth(self):
        """return an integer representing the total number of levels in the tree.

        If there is one value, the depth should be 1, if two values it'll be 2,
        if three values it may be 2 or three, depending, etc.
        """
        pass

    def balance(self):
        """return an integer, positive or negative represents how balanced the tree is.

        Trees which are higher on the left than the right should return a positive value,
        trees which are higher on the right than the left should return a negative value.
        An ideallyl-balanced tree should return 0.
        """
        pass
