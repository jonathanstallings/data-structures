from __future__ import unicode_literals


class BinaryHeap(object):
    """A class for a binary heap."""
    def __init__(self, iterable=()):
        self.tree = []
        for val in iterable:
            self.push(val)

    def __repr__(self):
        return repr(self.tree)

    def __len__(self):
        len(self.tree)

    def __iter__():
        pass

    def pop(self):
        """Pop the head from the heap and return."""
        if len(self.tree) == 1:
            to_return = self.tree.pop()
            return to_return
        else:
            self.swap_values(0, len(self.tree)-1) # Swap values at end of tree with start
            to_return = self.tree.pop()  # Should raise error on empty
            self.bubbledown()
            return to_return

    def push(self, value):
        """Push a value onto a stack.

        args:
            value: the value to add
        """
        self.tree.append(value)  # Add protecion for different types case
        if len(self.tree) > 1:
            self.bubbleup(len(self.tree)-1)

    def bubbleup(self, pos):
        """Perform a heap sort from end of tree upwards."""
        parent = self.find_parent(pos)
        if pos == 0:  #  find_parent will return -1 at end of list
            return
        elif self.tree[pos] < self.tree[parent]:
            self.tree[pos], self.tree[parent] = self.tree[parent], self.tree[pos]
            self.bubbleup(parent)


    def bubbledown(self, pos=0):
        """Perform a heap sort from end of tree downwards."""
        parent_value = self.tree[pos]
        lchild = self.find_lchild(pos)
        rchild = lchild + 1
        try:
            left_child = self.tree[lchild]
            try:
                right_child = self.tree[rchild]
            except IndexError: #  Case of left_child only
                if left_child < parent_value:
                    self.swap_values(pos, lchild)
                    self.bubbledown(pos=lchild)
            else:  #  Case of left_child and right_child
                if left_child < right_child:
                    target_child = left_child
                    target_child_pos = lchild
                else:
                    target_child = right_child
                    target_child_pos = rchild
                if target_child < parent_value:
                    self.swap_values(pos, target_child_pos)
                    self.bubbledown(pos=target_child_pos)

        except IndexError:
            return

    def find_parent(self, pos):
        """Returns the pos of the parent on the tree.

        args:
            pos: the pos to inspect from

        Returns: pos of the parent
        """
        parent = (pos - 1) // 2
        return parent

    def find_lchild(self, pos):
        """Returns the pos of the left child.

        args:
            pos: the pos to inspect from

        Returns: pos of the left child
        """
        lchild = (pos * 2) + 1
        return lchild


    def compare_values(self, parent_value=None, child_value=None, minheap=True):
        """Compares the values of child and parent according to heap type.

        For a minheap, checks if child value is greater than parent value.
        For a maxheap, checks if child value is less than parent value.

        args:
            child_pos: the pos of the child
            parent: the pos of the parent
            min: heap type comparison, defaults to minheap

        Returns: True if heap type comparison matches
        """
        if minheap is True:
            return child_value > parent_value
        else:
            return child_value < parent_value
