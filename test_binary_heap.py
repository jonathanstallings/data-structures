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


def is_minheap_sorted(heap):
    """Confirm that heap is minheap sorted.

    Original idea from:
    https://github.com/MigrantJ/data-structures/blob/binheap/binheap/binheap.py
    """
    for i in range(len(heap)):
        try:
            if heap[i] > heap[(2*i + 1)]:
                return False
            if heap[i] > heap[(2*i) + 2]:
                return False
        except IndexError:
            return True


def is_maxheap_sorted(heap):
    """Confirm that heap is maxheap sorted."""
    for i in range(len(heap)):
        try:
            if heap[i] < heap[(2*i + 1)]:
                return False
            if heap[i] < heap[(2*i) + 2]:
                return False
        except IndexError:
            return True


@pytest.fixture()
def minheap_empty():
    return BinaryHeap()


def test_find_parent():
    minheap = BinaryHeap([0, 1, 2, 3, 4, 5, 6])
    assert minheap._find_parent(2) == 0
    assert minheap._find_parent(6) == 2


def test_find_children():
    minheap = BinaryHeap([0, 1, 2, 3, 4, 5, 6])
    assert minheap._find_children(0) == (1, 2)
    assert minheap._find_children(2) == (5, 6)


def test_is_unsorted_minheap_comparison():
    minheap = BinaryHeap(minheap=True)
    assert minheap._is_unsorted(1, 2)


def test_is_unsorted_maxheap_comparison():
    minheap = BinaryHeap(minheap=False)
    assert minheap._is_unsorted(2, 1)


def test_swap():
    minheap = BinaryHeap([0, 1, 2, 3, 4, 5, 6])
    minheap._swap(0, 6)
    assert minheap.tree[0] == 6
    assert minheap.tree[6] == 0


def test_bubbledown_minheap():
    minheap = BinaryHeap([0, 1, 2, 3, 4, 5, 6])
    minheap[0] = 4000
    minheap._bubbledown(0)
    assert minheap[0] == 1
    assert is_minheap_sorted(minheap)


def test_bubbledown_maxheap():
    maxheap = BinaryHeap([6, 5, 4, 3, 2, 1, 0], minheap=False)
    maxheap[6] = 4000
    maxheap._bubbleup(6)
    assert maxheap[0] == 4000
    assert is_maxheap_sorted(maxheap)


@pytest.mark.parametrize("input, output", valid_constructor_args)
def test_valid_instantiation_min(input, output):
    """Test instantiation by creating and doing one pop"""
    heap_under_test = BinaryHeap(input)
    assert is_minheap_sorted(heap_under_test)
    assert heap_under_test.pop() == output


@pytest.mark.parametrize("input, output", valid_constructor_args_max)
def test_valid_instantiation_max(input, output):
    """Test instantiation by creating and doing one pop"""
    heap_under_test = BinaryHeap(input, minheap=False)
    assert is_maxheap_sorted(heap_under_test)
    assert heap_under_test.pop() == output


@pytest.mark.parametrize("bad_input", invalid_constructors)
def test_invalid_instantiation(bad_input):
    """Test that bad by creating and doing one pop"""
    with pytest.raises(TypeError):
        BinaryHeap(bad_input)


def test_push1(minheap_empty):
    """  First push single item from list of [9, 5, 2, 1, 0, 7] """
    minheap_empty.push(9)
    assert minheap_empty.pop() == 9


def test_push2(minheap_empty):
    """ First push two items from list of [9, 5, 2, 1, 0, 7]; current
        test for min heap """
    minheap_empty.push(5)
    minheap_empty.push(9)
    assert minheap_empty.pop() == 5


def test_push3(minheap_empty):
    """ First push three items from list of [9, 5, 2, 1, 0, 7]; current
        test for min heap """
    minheap_empty.push(5)
    minheap_empty.push(9)
    minheap_empty.push(2)
    assert minheap_empty.pop() == 2


def test_push4(minheap_empty):
    """ First push four items from list of [9, 5, 2, 1, 0, 7]; current
        test for min heap """
    minheap_empty.push(5)
    minheap_empty.push(9)
    minheap_empty.push(2)
    minheap_empty.push(1)
    assert minheap_empty.pop() == 1


def test_push5(minheap_empty):
    """ First push five items from list of [9, 5, 2, 1, 0, 7]; current
        test for min heap """
    minheap_empty.push(5)
    minheap_empty.push(9)
    minheap_empty.push(2)
    minheap_empty.push(1)
    minheap_empty.push(0)
    assert minheap_empty.pop() == 0


def test_push6(minheap_empty):
    """ First push six items from list of [9, 5, 2, 1, 0, 7]; current
        test for min heap """
    minheap_empty.push(5)
    minheap_empty.push(9)
    minheap_empty.push(2)
    minheap_empty.push(1)
    minheap_empty.push(0)
    minheap_empty.push(7)
    assert minheap_empty.pop() == 0


def test_pop_minheap():
    minheap = BinaryHeap([7, 9, 18, 1, 38, 5.4, 6])
    minheap.push(0)
    length = len(minheap)
    assert minheap.pop() == 0
    assert len(minheap) == length - 1


def test_pop_maxheap():
    maxheap = BinaryHeap([7, 9, 18, 1, 38, 5.4, 6], minheap=False)
    maxheap.push(400)
    length = len(maxheap)
    assert maxheap.pop() == 400
    assert len(maxheap) == length - 1


def test_multipop_minheap():
    minheap = BinaryHeap([7, 9, 18, 1, 38, 5.4, 6, 200])
    length = len(minheap)
    minheap.pop()
    minheap.pop()
    minheap.push(0)
    minheap.pop()
    minheap.pop()
    assert minheap.pop() == 7
    assert len(minheap) == length - 4


def test_multipop_maxheap():
    maxheap = BinaryHeap([7, 9, 18, 1, 38, 5.4, 6, 200], minheap=False)
    length = len(maxheap)
    maxheap.pop()
    maxheap.pop()
    maxheap.push(400)
    maxheap.pop()
    maxheap.pop()
    assert maxheap.pop() == 9
    assert len(maxheap) == length - 4
