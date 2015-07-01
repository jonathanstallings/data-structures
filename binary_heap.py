from __future__ import unicode_literals


class BinaryHeap(object):
    """A class for a binary heap."""
    def __init__(self, iterable=()):
        self.tree = []
        for val in iterable:
            self.push(val)

    def __repr__(self):
        repr(self.tree)

    def pop(self):
        """Pop the head from the heap and return."""
        pass

    def push(self, value):
        """Push a value onto a stack.

        args:
            value: the value to add
        """
        self.tree.append(value)  # Add protecion for different types case
        self.bubbleup()

    def bubbleup(self):
        """Perform a heap sort from end of tree upwards."""
        pass

    def bubbledown(self):
        """Perform a heap sort from end of tree downwards."""
        pass

    def find_parent(self, index):
        """Returns the index of the parent on the tree.

        args:
            index: the index to inspect from

        Returns: index of the parent
        """
        parent_index = (index - 1) // 2
        return parent_index

    def find_left_child(self, index):
        """Returns the index of the left child.

        args:
            index: the index to inspect from

        Returns: index of the left child
        """
        left_child_index = (index * 2) + 1
        return left_child_index

    def compare_values(self, child_index, parent_index, minheap=True):
        """Compares the values of child and parent according to heap type.

        For a minheap, checks if child value is greater than parent value.
        For a maxheap, checks if child value is less than parent value.

        args:
            child_index: the index of the child
            parent_index: the index of the parent
            min: heap type comparison, defaults to minheap

        Returns: True if heap type comparison matches
        """
        child_value = self.tree[child_index].val
        parent_value = self.tree[parent_index].val
        if minheap is True:
            return child_value > parent_value
        else:
            return child_value < parent_value

    def swap_values(self, ind1, ind2):
        """Swaps the values of the two indexed positions."""
        self.tree[ind1], self.tree[ind2] = (self.tree[ind2], self.tree[ind1])
