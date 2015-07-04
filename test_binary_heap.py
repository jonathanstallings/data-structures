from __future__ import unicode_literals
import pytest
from binary_heap import BinaryHeap

#  (in, expected) for constructors
valid_constructor_args = [
    ["qzdfwqefnsadnfoiaweod", "a"],
    [[6, 7, 9, 4, 2, 1, 56, 8, 0, 43523], 0],
    [[1243.12235, 13262.3, 26523.15, 98653.234], 1243.12235]
]

valid_constructor_args_max = [
    ["qzdfwqefnsadnfoiaweod", "z"],
    [[6, 7, 9, 4, 2, 1, 56, 8, 0, 43523], 43523],
    [[1243.12235, 13262.3, 26523.15, 98653.234], 98653.234]
]

pop_constructors = [
    [5, 8, 98, 43, 21, 1, 3, 7, 0, 3, 4, 7, 2345, 4, 64],
    [33, 5314, 124, 243, 234, 1324, 2, 342, 1243, 134],
    ]

invalid_constructors = [
    8,
    None,
    4.523423
    ]


def minheap_sorted(heap):
    for i in range(len(heap)):
        try:
            if heap[i] > heap[(2*i + 1)]:
                return False
            if heap[i] > heap[(2*i) + 2]:
                return False
        except IndexError:
            return True


def maxheap_sorted(heap):
    for i in range(len(heap)):
        try:
            if heap[i] < heap[(2*i + 1)]:
                return False
            if heap[i] < heap[(2*i) + 2]:
                return False
        except IndexError:
            return True


@pytest.mark.parametrize("input, output", valid_constructor_args)
def test_valid_instantiation_min(input, output):
    """Test instantiation by creating and doing one pop"""
    heap_under_test = BinaryHeap(input)
    assert minheap_sorted(heap_under_test)
    assert heap_under_test.pop() == output


@pytest.mark.parametrize("input, output", valid_constructor_args_max)
def test_valid_instantiation_max(input, output):
    """Test instantiation by creating and doing one pop"""
    heap_under_test = BinaryHeap(input, minheap=False)
    assert maxheap_sorted(heap_under_test)
    assert heap_under_test.pop() == output


@pytest.mark.parametrize("bad_input", invalid_constructors)
def test_invalid_instantiation(bad_input):
    """Test that bad by creating and doing one pop"""
    with pytest.raises(TypeError):
        BinaryHeap(bad_input)


def test_push1():
    """  First push single item from list of [9, 5, 2, 1, 0, 7] """
    heap_under_test = BinaryHeap()
    heap_under_test.push(9)
    assert heap_under_test.pop() == 9


def test_push2():
    """ First push two items from list of [9, 5, 2, 1, 0, 7]; current
        test for min heap """
    heap_under_test = BinaryHeap()
    heap_under_test.push(5)
    heap_under_test.push(9)
    assert heap_under_test.pop() == 5


def test_push3():
    """ First push three items from list of [9, 5, 2, 1, 0, 7]; current
        test for min heap """
    heap_under_test = BinaryHeap()
    heap_under_test.push(5)
    heap_under_test.push(9)
    heap_under_test.push(2)
    assert heap_under_test.pop() == 2


def test_push4():
    """ First push three items from list of [9, 5, 2, 1, 0, 7]; current
        test for min heap """
    heap_under_test = BinaryHeap()
    heap_under_test.push(5)
    heap_under_test.push(9)
    heap_under_test.push(2)
    heap_under_test.push(1)
    assert heap_under_test.pop() == 1


def test_push5():
    """ First push three items from list of [9, 5, 2, 1, 0, 7]; current
        test for min heap """
    heap_under_test = BinaryHeap()
    heap_under_test.push(5)
    heap_under_test.push(9)
    heap_under_test.push(2)
    heap_under_test.push(1)
    heap_under_test.push(0)
    assert heap_under_test.pop() == 0


def test_push6():
    """ First push three items from list of [9, 5, 2, 1, 0, 7]; current
        test for min heap """
    heap_under_test = BinaryHeap()
    heap_under_test.push(5)
    heap_under_test.push(9)
    heap_under_test.push(2)
    heap_under_test.push(1)
    heap_under_test.push(0)
    heap_under_test.push(7)
    assert heap_under_test.pop() == 0


def test_pop1():
    #  Will pass argumnents, instantiate, heap, check for expected pop
    pass


def test_pop2():
    # Pop off of an emptied heap
    pass


def test_pop3():
    pass


def test_pop4():
    pass

def test_push():
    #  Create range of numbers
    #  Shuffle that range
    #  Push each in a for loop
    #  Check that pop
    pass
