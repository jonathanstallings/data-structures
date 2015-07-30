"""Contains a Node class which implements an AVL binary search tree.

Each node can be considered a binary search tree and has the usual
methods to insert, delete, and check membership of nodes. By default,
the insert and delete methods will perform self-balancing consistent
with an AVL tree. This behavior can be suppressed by passing the optional
'balanced=False' keyword argument to the insert or delete methods.

The class also supports four traversal methods which return generators:

- in_order
- pre_order
- post_order
- breadth_first.

Additionally, methods are included to help visualize the tree structure.
get_dot returns DOT source code, suitable for use with programs such as
Graphviz (http://graphviz.readthedocs.org/en/stable/index.html), and
save_render saves a rendering of the tree structure to the file system.
Passing the optional 'render=True' keyword argument to the insert and
delete methods will automatically save a render to disk upon execution.

Finally, the helper methods 'create_best_case' and 'create_worst_case'
facilitates creation of tree composeds of _n_ integers.

This module was completed with reference to the following:

'Binary Search Tree libary in Python'
(http://www.laurentluce.com/posts/binary-search-tree-library-in-python/)
by Laurent Luce.

'How to Balance your Binary Search Trees - AVL Trees'
(https://triangleinequality.wordpress.com/2014/07/15/how-to-balance-your-binary-search-trees-avl-trees/)

'The AVL Tree Rotations Tutorial'
(http://pages.cs.wisc.edu/~paton/readings/liblitVersion/AVL-Tree-Rotations.pdf)
by John Hargrove

"""
from __future__ import print_function
from __future__ import unicode_literals
import random

from queue import Queue


class Node(object):
    """A class for a binary search tree node."""
    def __init__(self, val=None, parent=None):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        return '<BST: ({})>'.format(self.val)

    def __str__(self):
        return '{}'.format(self.val)

    def __len__(self):
        return self.size()

    def __iter__(self):
        return self.in_order()

    def insert(self, val, balanced=True, render=False):
        """Insert a node with a value into the tree.

        If val is already present, it will be ignored.

        args:
            val: the value to insert
            balanced: performs AVL self-balancing if set to True
            render: automatically saves a render to disk if set to True
        """
        if self.val is not None:
            if val == self.val:
                return None
            if val < self.val:
                if self.left is None:
                    self.left = Node(val, self)
                    if balanced:
                        self.left._self_balance()
                else:
                    self.left.insert(val, balanced, render)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val, self)
                    if balanced:
                        self.right._self_balance()
                else:
                    self.right.insert(val, balanced, render)
        else:
            self.val = val
        if render and self.parent is None:
            self.save_render()

    def delete(self, val, balanced=True, render=False):
        """Delete a node matching value and reorganize tree as needed.

        If the matched node is the only node in the tree, only its value
        will be deleted.

        args:
            val: the value of the node to delete
            balanced: performs AVL self-balancing if set to True
            render: automatically saves a render to disk if set to True
        """
        node = self.lookup(val)
        parent = node.parent
        if node is not None:
            children_count = node._children_count()
            if children_count == 0:
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                    if balanced:
                        parent._self_balance()
                else:
                    self.val = None
            elif children_count == 1:
                if node.left:
                    child = node.left
                else:
                    child = node.right
                if parent:
                    if parent.left is node:
                        parent.left = child
                    else:
                        parent.right = child
                    child.parent = parent
                    if balanced:
                        child._self_balance()
                else:
                    self.left = child.left
                    self.right = child.right
                    try:
                        self.right.parent = self
                        self.left.parent = self
                    except AttributeError:
                        pass
                    self.val = child.val
                    if balanced:
                        self._self_balance()
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.val = successor.val
                if parent.left == successor:
                    parent.left = successor.right
                    try:
                        parent.left.parent = parent
                    except AttributeError:
                        pass
                    parent._self_balance()
                else:
                    parent.right = successor.right
                    try:
                        parent.right.parent = parent
                    except AttributeError:
                        pass
                    if balanced:
                        parent._self_balance()
        if render and self.parent is None:
            self.save_render()

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

    def lookup(self, val):
        """Find a node by value and return that node and its parent.

        args:
            val: the value to search by
            parent: the parent of the node (for recursion)

        returns: a tuple with node and its parent
        """
        if val < self.val:
            if self.left is None:
                return None, None
            return self.left.lookup(val)
        elif val > self.val:
            if self.right is None:
                return None, None
            return self.right.lookup(val)
        else:
            return self

    def size(self):
        """Return the total number of nodes in the tree.

        returns: integer of total node; 0 if empty
        """
        if self.val is None:
            return 0
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

    def _is_left(self):
        """Check nodes relationship to parent.

        returns:
            - True if node is left child of parent
            - False if node is right childe of parent
            - None if node has no parent
        """
        if self.parent is None:
            return None
        else:
            return self is self.parent.left

    def _rotate_right(self):
        """Perform a single right tree rotation."""
        pivot = self.left
        if pivot is None:
            return
        self.val, pivot.val = pivot.val, self.val
        self.left = pivot.left
        if self.left is not None:
            self.left.parent = self
        pivot.left = pivot.right
        if pivot.left is not None:
            pivot.left.parent = pivot
        pivot.right = self.right
        if pivot.right is not None:
            pivot.right.parent = pivot
        self.right, pivot.parent = pivot, self

    def _rotate_left(self):
        """Perform a single left tree rotation."""
        pivot = self.right
        if pivot is None:
            return
        self.val, pivot.val = pivot.val, self.val
        self.right = pivot.right
        if self.right is not None:
            self.right.parent = self
        pivot.right = pivot.left
        if pivot.right is not None:
            pivot.right.parent = pivot
        pivot.left = self.left
        if pivot.left is not None:
            pivot.left.parent = pivot
        self.left, pivot.parent = pivot, self

    def _self_balance(self):
        """Balance the subtree from given node."""
        balance = self.balance()
        # Tree is left heavy
        if balance == 2:
            if self.left.balance() <= -1:
                # Double Right
                self.left._rotate_left()
            # Single Right
            self._rotate_right()
            if self.parent is not None:
                self.parent._self_balance()

        # Tree is right heavy
        elif balance == -2:
            if self.right.balance() >= 1:
                # Double Left
                self.right._rotate_right()
            # Single Left
            self._rotate_left()
            if self.parent is not None:
                self.parent._self_balance()
        else:
            if self.parent is not None:
                self.parent._self_balance()

    def in_order(self):
        """Return a generator with tree values from in-order traversal"""
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
        """Return a generator with tree values from pre-order traversal"""
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
        """Return a generator with tree values from post-order traversal"""
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
        """Return a generator with tree values from breadth first traversal"""
        q = Queue()
        q.enqueue(self)
        while q.size() > 0:
            node = q.dequeue()
            yield node.val
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

    def _children_count(self):
        """Return a node's number of children."""
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def get_dot(self):
        """Return the tree with root as a dot graph for visualization."""
        return "digraph G{\n%s}" % ("" if self.val is None else (
            "\t%s;\n%s\n" % (
                self.val,
                "\n".join(self._get_dot())
            )
        ))

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.val, self.left.val)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.val, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.val, self.right.val)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.val, r)

    def save_render(self, savefile="tree.gv"):
        """Render and save a represntation of the tree.

        args:
            savefile: the optional filename
        """
        from graphviz import Source
        src = Source(self.get_dot())
        path = 'graphviz/{}'.format(savefile)
        src.render(path)

    @classmethod
    def _sorted_list_to_bst(cls, items=[], start=None, end=None, parent=None):
        """Create a balanced binary search tree from sorted list.

        args:
            items: the sorted list of items to insert into tree
            start: the start of the list
            end: the end of the list

        returns: a balanced binary search tree (node)
        """
        if start > end:
            return None
        mid = start + (end - start) // 2
        node = Node(items[mid], parent)
        node.left = cls._sorted_list_to_bst(items, start, mid - 1, node)
        node.right = cls._sorted_list_to_bst(items, mid + 1, end, node)
        return node

    @classmethod
    def create_best_case(cls, n):
        """Create a balanced binary search tree from a given range.

        args:
            n: the range of integers to insert into the tree

        returns: a balanced binary search tree (node)
        """
        return cls._sorted_list_to_bst(range(n), 0, n - 1)

    @classmethod
    def create_worst_case(cls, n):
        """Create an unbalanced binary search tree from a given range.

        The tree will be one long linear branch to the right.

        args:
            n: the range of integers to add to the tree

        returns: a (very) unbalanced binary search tree (node)
        """
        node = Node(0)
        parent = node
        for i in range(1, n):
            parent.right = Node(i, parent)
            parent = parent.right
        return node

if __name__ == '__main__':
    from timeit import Timer

    """Document the best and worst cases for searching for a value in the tree.
        The worst case consists of a tree with one long linear branch.
        The best case is a perfectly balanced tree.
    """

    SIZE = 900
    LOOKUP = 900

    worst = Node.create_worst_case(SIZE)
    best = Node.create_best_case(SIZE)

    worst_case = Timer(
        'worst.contains({})'.format(LOOKUP, SIZE), 'from __main__ import worst'
    ).timeit(1000)

    best_case = Timer(
        'best.contains({})'.format(LOOKUP), 'from __main__ import best'
    ).timeit(1000)

    print(
        "\nLookup Time Comparison: Best and Worst Case\n"
        "\nGiven a tree of {n} items, find a node with value of {l}.\n"
        .format(n=SIZE, l=LOOKUP)
    )

    print(
        "Worst case, with tree balanced at {b}.\n"
        "Time: {t}\n"
        .format(b=worst.balance(), t=worst_case)
    )
    print(
        "Best case,  with tree balanced at {b}.\n"
        "Time: {t}\n"
        .format(b=best.balance(), t=best_case)
    )
