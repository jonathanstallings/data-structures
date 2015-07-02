from __future__ import unicode_literals


class BinaryHeap(object):
    """A class for a binary heap."""
    def __init__(self, iterable=()):
        self.tree = []
        for val in iterable:
            import pdb; pdb.set_trace()
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
            self.swap_values(0, len(self.tree) - 1) # Swap values at end of tree with start
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

    def bubbleup(self, index):
        """Perform a heap sort from end of tree upwards."""
        parent_index = self.find_parent(index)
        try:
            parent_value = self.tree[parent_index]
        except IndexError:
            return
        child = self.tree[index]
        if child < parent_value:
            self.swap_values(parent_index, index)
            self.bubbleup(parent_index)

    def bubbledown(self, index=0):
        """Perform a heap sort from end of tree downwards."""
        parent_value = self.tree[index]
        left_child_index = self.find_left_child(index)
        right_child_index = left_child_index + 1
        try:
            left_child = self.tree[left_child_index]
            try:
                right_child = self.tree[right_child_index]
            except IndexError: #  Case of left_child only
                if left_child < parent_value:
                    self.swap_values(index, left_child_index)
                    self.bubbledown(index=left_child_index)
            else:  #  Case of left_child and right_child
                if left_child < right_child:
                    target_child = left_child
                    target_child_index = left_child_index
                else:
                    target_child = right_child
                    target_child_index = right_child_index
                if target_child < parent_value:
                    self.swap_values(index, target_child_index)
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
