from __future__ import unicode_literals


class BinaryHeap(object):
    """A class for a binary heap."""
    def __init__(self, iterable=(), heaptype='minheap'):
        self.tree = []
        self.heaptype = heaptype
        for val in iterable:
            self.push(val)

    def __repr__(self):
        return repr(self.tree)

    def __len__(self):
        return len(self.tree)

    def __iter__(self):
        return iter(self.tree)

    def pop(self):
        """Pop the head from the heap and return."""
        if len(self.tree) <= 1:
            to_return = self.tree.pop()
        else:
            endpos = len(self.tree) - 1
            self._swap(0, endpos)
            to_return = self.tree.pop()
            self._bubbledown(0)
        return to_return

    def push(self, value):
        """Push a value onto a stack.

        args:
            value: the value to add
        """
        self.tree.append(value)  # Add protecion for different types case
        if len(self.tree) > 1:
            endpos = len(self.tree) - 1
            self._bubbleup(endpos)

    def _bubbleup(self, pos):
        """Perform one step of heap sort up the tree.

        args:
            pos: the index position to inspect
        """
        parent = self._find_parent(pos)
        if pos == 0:  # find_parent will return -1 at end of list
            return
        elif self.tree[pos] < self.tree[parent]:
            self._swap(pos, parent)
            self._bubbleup(parent)

    def _bubbledown(self, pos):
        """Perform one step of heap sort down the tree.

        args:
            pos: the index position to inspect
        """
        lchild, rchild = self._find_children(pos)
        try:  # Evaluating whether lchild exists; may refactor
            lval = self.tree[lchild]
            try:
                rval = self.tree[rchild]
            except IndexError:  # Case of left_child only
                if lval < self.tree[pos]:
                    self._swap(lchild, pos)
            else:  # Case of left_child and right_child
                if lval < rval:
                    target = lchild
                else:
                    target = rchild
                if self.tree[target] < self.tree[pos]:
                    self._swap(target, pos)
                    self._bubbledown(target)

        except IndexError:  # Case of no lchild
            return

    def _find_parent(self, pos):
        """Returns the parent index of given position.

        args:
            pos: the index position to inspect

        Returns: index of the parent
        """
        parent = (pos - 1) // 2
        return parent

    def _find_children(self, pos):
        """Returns the indexes of children from given position.

        args:
            pos: the index position to inspect

        Returns: index of left child and right child
        """
        lchild = (pos * 2) + 1
        rchild = lchild + 1
        return lchild, rchild

    def _is_unsorted(self, val1, val2):
        """Compare two values according to heaptype.

        For a minheap, checks if first value is less than second value.
        For a maxheap, checks if first value is greater than second value.

        args:
            val1: first value
            val2: second value

        Returns: True if heaptype comparison matches, else False
        """
        if self.heaptype == 'minheap':
            return val1 < val2
        elif self.heaptype == 'maxheap':
            return val1 > val2
        else:
            raise AttributeError('heaptype not assigned')

    def _swap(self, pos1, pos2):
        """Swap the values at to index positions.

        args:
            pos1: the index of the first item
            pos2: the index of the second item'
        """
        self.tree[pos1], self.tree[pos2] = self.tree[pos2], self.tree[pos1]
