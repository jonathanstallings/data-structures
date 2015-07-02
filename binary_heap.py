from __future__ import unicode_literals


class BinaryHeap(object):
    """A class for a binary heap."""
    def __init__(self, iterable=()):
        self.tree = []
        for val in iterable:
            self.push(val)

    def __repr__(self):
        repr(self.tree)

    def __len__(self):
        len(self.tree)

    def __iter__():
        pass

    def pop(self):
        """Pop the head from the heap and return."""
        if len(self) == 1:
            to_return = self.tree.pop()
            self.bubbledown()
            return to_return
        else:
            self.swap_values(self.tree[0], self.tree[1])
            to_return = self.tree.pop()  # Should raise error on empty
            self.bubbledown()
            return to_return

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

    def bubbledown(self, index=0):
        """Perform a heap sort from end of tree downwards."""
        parent = self.tree[index]
        left_child_index = self.find_left_child(parent)
        right_child_index = left_child_index + 1
        try:
            left_child = self.tree[left_child_index]
            try:
                right_child = self.tree[right_child_index]
            except IndexError:
                if self.compare_values(parent_value=parent, child_value=left_child):
                    self.swap_values(parent, left_child)
            if left_child < right_child:
                target_child = left_child
                target_child_index = left_child_index
            else:
                target_child = right_child
                target_child_index = right_child_index
            self.compare_values(parent_value=parent, child_value=target_child)
            self.swap_values(parent, target_child)
            self.bubbledown(index=target_child_index)
        except IndexError:
            return

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

    def compare_values(self, parent_value=None, child_value=None, minheap=True):
        """Compares the values of child and parent according to heap type.

        For a minheap, checks if child value is greater than parent value.
        For a maxheap, checks if child value is less than parent value.

        args:
            child_index: the index of the child
            parent_index: the index of the parent
            min: heap type comparison, defaults to minheap

        Returns: True if heap type comparison matches
        """
        if minheap is True:
            return child_value > parent_value
        else:
            return child_value < parent_value

    def swap_values(self, ind1, ind2):
        """Swaps the values of the two indexed positions."""
        self.tree[ind1], self.tree[ind2] = (self.tree[ind2], self.tree[ind1])
