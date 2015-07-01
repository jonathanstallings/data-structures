from __future__ import unicode_literals


class BinaryHeap(object):
    """A class for a binary heap."""
    def __init__(self, arg):
        pass

    def __repr__():
        pass

    def pop():
        """Pop the head from the heap and return."""
        pass

    def push(value):
        """Push a value onto a stack.

        args:
            value: the value to add
        """
        pass

    def bubbleup():
        """Perform a heap sort from end of tree upwards."""
        pass

    def bubbledown():
        """Perform a heap sort from end of tree downwards."""
        pass

    def find_parent(index):
        """Returns the index of the parent on the tree.

        args:
            index: the index to inspect from

        Returns: index of the parent
        """
        pass

    def find_left_child(index):
        """Returns the index of the left child.

        args:
            index: the index to inspect from

        Returns: index of the left child
        """
        pass

    def compare_values(child_index, parent_index, min=True):
        """Compares the values of child and parent according to heap type.

        For a minheap, checks if child value is greater than parent value.
        For a maxheap, checks if child value is less than parent value.

        args:
            child_index: the index of the child
            parent_index: the index of the parent
            min: heap type comparison, defaults to minheap

        Returns: True if heap type comparison matches
        """
        pass

    def swap_values(index1, index2):
        """Swaps the values of the two indexed positions."""
        pass
