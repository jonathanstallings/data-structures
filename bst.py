from __future__ import unicode_literals
from queue import Queue


class Node(object):
    """A class for a binary search tree node."""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return '{}'.format(self.val)

    def __len__(self):
        return self.size()

    def __iter__(self):
        return self.in_order()

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
        return left_depth - right_depth

    def in_order(self):
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.val
                node = node.right

    def pre_order(self):
        stack = []
        node = self
        while stack or node:
            if node:
                yield node.val
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right

    def post_order(self):
        stack = []
        node = self
        last = None
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek = stack[-1]
                if peek.right is not None and last != peek.right:
                    node = peek.right
                else:
                    yield peek.val
                    last = stack.pop()
                    node = None

    def breadth_first(self):
        q = Queue()
        q.enqueue(self)
        while q.size() > 0:
            node = q.dequeue()
            yield node.val
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)


if __name__ == '__main__':
    from timeit import Timer

    """Document the best and worst cases for searching for a value in the tree.
        The worst case consists of a tree with one long linear branch.
        The best case is a perfectly balanced tree.
    """
    worst = Node(1)
    for val in range(2, 32):
        worst.insert(val)

    best = Node(16)
    best_values = [
        8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30, 1, 3, 5,
        7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31
    ]
    for val in best_values:
        best.insert(val)

    worst_case = Timer(
        'worst.contains(31)', 'from __main__ import worst').timeit(1000)
    best_case = Timer(
        'best.contains(31)', 'from __main__ import best').timeit(1000)

    print "The worst case took {}.".format(worst_case)
    print "The best case took {}.".format(best_case)
