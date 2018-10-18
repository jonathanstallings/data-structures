from __future__ import unicode_literals


class BinaryHeap(object):
    """A class for a binary heap."""
    def __init__(self, iterable=(), minheap=True):
        """Initializes a binary heap, optionally with items from an iterable.

        By default, the binary will sort as a minheap, with smallest values
        at the head. If minheap is set to false, the binary heap will sort
        as a maxheap, with largest values at the head.
        """
        self.tree = []
        self.minheap = minheap
        for val in iterable:
            self.push(val)

    def __repr__(self):
        return repr(self.tree)

    def __len__(self):
        return len(self.tree)

    def __iter__(self):
        return iter(self.tree)

    def __getitem__(self, index):
        return self.tree[index]

    def __setitem__(self, index, value):
        self.tree[index] = value

    def pop(self):
        """Pop the head from the heap and return."""
        if len(self) <= 1:
            to_return = self.tree.pop()
        else:
            endpos = len(self) - 1
            self._swap(0, endpos)
            to_return = self.tree.pop()
            self._bubbledown(0)
        return to_return

    def push(self, value):
        """Push a value onto a stack.

        args:
            value: the value to add
        """
        self.tree.append(value)  # Add protection for different types case
        if len(self) > 1:
            endpos = len(self) - 1
            self._bubbleup(endpos)

    def _bubbleup(self, pos):
        """Perform one step of heap sort up the tree.

        args:
            pos: the index position to inspect
        """
        parent = self._find_parent(pos)
        if pos == 0:  # find_parent will return -1 at end of list
            return
        elif self._is_unsorted(self[pos], self[parent]):
            self._swap(pos, parent)
            self._bubbleup(parent)

    def _bubbledown(self, pos):
        """Perform one step of heap sort down the tree.

        args:
            pos: the index position to inspect
        """
        lchild, rchild = self._find_children(pos)
        try:  # Evaluating whether lchild exists; may refactor
            lval = self[lchild]
            try:
                rval = self[rchild]
            except IndexError:  # Case of left_child only
                if self._is_unsorted(lval, self[pos]):
                    self._swap(lchild, pos)
            else:  # Case of left_child and right_child
                if self._is_unsorted(lval, rval):
                    target = lchild
                else:
                    target = rchild
                if self._is_unsorted(self[target], self[pos]):
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
        """Returns the indices of children from given position.

        args:
            pos: the index position to inspect

        Returns: index of left child and right child
        """
        lchild = (pos * 2) + 1
        rchild = lchild + 1
        return lchild, rchild

    def _is_unsorted(self, item1, item2):
        """Compare two items according to heaptype.

        For a minheap, checks if first item is less than second item.
        For a maxheap, checks if first item is greater than second item.

        args:
            item1: first item
            item2: second item

        Returns: True if heaptype comparison matches, else False
        """
        if self.minheap is True:
            return item1 < item2
        elif self.minheap is False:
            return item1 > item2
        else:
            raise AttributeError('heaptype not assigned')

    def _swap(self, pos1, pos2):
        """Swap the values at given index positions.

        args:
            pos1: the index of the first item
            pos2: the index of the second item
        """
        self[pos1], self[pos2] = self[pos2], self[pos1]
