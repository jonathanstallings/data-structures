# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
from double_link_list import DoubleLinkList

#  (Input, expected) for well constructed instantiation arguments,
#  and one subsequent pop
valid_constructor_args = [
    ([1, 2, 3], 1),
    ([[1, 2, 3], "string"], [1, 2, 3]),
    ("string", 's')
]

# Invalid instantiation arguments
invalid_constructor_args = [
    (None),
    (1),
    (4.5235)
]

#  (Input, remove, expected) for well constructed instantiation arguments,
#  remove arg, and expected repr
remove_val_args = [
    ([1, 2, 3, 4, 5, 6, 7], 6)
]


@pytest.mark.parametrize("input, pop_val", valid_constructor_args)
def test_valid_contructor(input, pop_val):
    """Test valid constructor using by dequeuing after instantiation"""
    assert DoubleLinkList(input).pop() == pop_val


def test_empty_constructor():
    """Test valid empty constructor via dequeuing after instantiation"""
    with pytest.raises(IndexError):
        DoubleLinkList(()).pop()


@pytest.mark.parametrize("input", invalid_constructor_args)
def test_invalid_constructor(input):
    """Test invalid constuctor arguments"""
    with pytest.raises(TypeError):
        DoubleLinkList(input)


def test_insert_via_len():
    """Tests insert function for doublelinked list; using len"""
    adding_to = DoubleLinkList(())
    for i in xrange(40):
        adding_to.insert(i)

    assert len(adding_to) == 40
    assert adding_to.pop() == 39


def test_insert_via_pop():
    """Tests insert function for doublelinked list; using pop"""
    adding_to = DoubleLinkList(())
    for i in xrange(40):
        adding_to.insert(i)

    assert adding_to.pop() == 39


def test_insert_via_shift():
    """Tests insert function for doublelinked list; using shift"""
    adding_to = DoubleLinkList(())
    for i in xrange(40):
        adding_to.insert(i)

    assert adding_to.shift() == 0


def test_append_via_len():
    """Tests append method for doublelinked list; using len"""
    adding_to = DoubleLinkList(())
    for i in xrange(40):
        adding_to.append(i)

    assert len(adding_to) == 40


def test_append_via_pop():
    """Tests append method for doublelinked list; using len"""
    adding_to = DoubleLinkList(())
    for i in xrange(40):
        adding_to.append(i)

    assert adding_to.pop() == 0


def test_append_via_shift():
    """Tests append method for doublelinked list; using len"""
    adding_to = DoubleLinkList(())
    for i in xrange(40):
        adding_to.append(i)

    assert adding_to.shift() == 39


def test_pop_1():
    """Fill a DoubleLinkList with (1,2,3), check first pop"""
    adding_to = DoubleLinkList(())
    for i in xrange(3):
        adding_to.insert(i)
    assert adding_to.pop() == 2


def test_pop_2():
    """Fill a DoubleLinkList with (1,2,3), check second pop"""
    adding_to = DoubleLinkList(())
    for i in xrange(3):
        adding_to.insert(i)

    adding_to.pop()  # First action covered by test_pop_1
    assert adding_to.pop() == 1


def test_pop_3():
    """Fill a DoubleLinkList with (1,2,3), check third pop"""
    adding_to = DoubleLinkList(())
    for i in xrange(3):
        adding_to.insert(i)

    adding_to.pop()  # First action covered by test_pop_1
    adding_to.pop()  # Second action covered by test_pop_2
    assert adding_to.pop() == 0


def test_pop_4():
    """Fill a DoubleLinkList with (1,2,3), check fourth pop"""
    adding_to = DoubleLinkList(())
    for i in xrange(3):
        adding_to.insert(i)

    adding_to.pop()  # First action covered by test_pop_1
    adding_to.pop()  # Second action covered by test_pop_2
    adding_to.pop()
    with pytest.raises(IndexError):
        adding_to.pop()


def test_shift_1():
    """Fill a DoubleLinkList with (1,2,3), check first pop"""
    adding_to = DoubleLinkList(())
    for i in xrange(3):
        adding_to.insert(i)
    assert adding_to.shift() == 0


def test_shift_2():
    """Fill a DoubleLinkList with (1,2,3), check second pop"""
    adding_to = DoubleLinkList(())
    for i in xrange(3):
        adding_to.insert(i)

    adding_to.shift()  # First action covered by test_pop_1
    assert adding_to.shift() == 1


def test_shift_3():
    """Fill a DoubleLinkList with (1,2,3), check third pop"""
    adding_to = DoubleLinkList(())
    for i in xrange(3):
        adding_to.insert(i)

    adding_to.shift()  # First action covered by test_pop_1
    adding_to.shift()  # Second action covered by test_pop_2
    assert adding_to.shift() == 2


# def test_pop_4():
#     """Fill a DoubleLinkList with (1,2,3), check fourth pop"""
#     adding_to = DoubleLinkList(())
#     for i in xrange(3):
#         adding_to.insert(i)

#     adding_to.pop()  # First action covered by test_pop_1
#     adding_to.pop()  # Second action covered by test_pop_2
#     adding_to.pop()
#     with pytest.raises(IndexError):
#         adding_to.pop()



def test_shift():
    """Fill a DoubleLinkList with values, check pop off each one, then
    test that one more pop raises IndexError"""
    adding_to = DoubleLinkList(())
    for i in xrange(40):
        adding_to.insert(i)
    #  now pop'ing off each value successively
    for i in xrange(40):
        assert adding_to.shift() == i
    with pytest.raises(IndexError):
        adding_to.shift()


# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# import pytest

# from queue import Queue

# #  (Input, expected) for well constructed instantiation arguments,
# #  and one subsequent dequeue
# valid_constructor_args_dequeue = [
#     ([1, 2, 3], 1),
#     ([[1, 2, 3], "string"], [1, 2, 3]),
#     ("string", 's')
# ]

# # Invalid instantiation arguments
# invalid_constructor_args = [
#     (None),
#     (1),
#     (4.5235)
# ]


# @pytest.mark.parametrize("input,deque", valid_constructor_args_dequeue)
# def test_valid_contructor(input, deque):
#     """Test valid constructor using by dequeuing after instantiation"""
#     assert Queue(input).dequeue() == deque


# def test_empty_constructor():
#     """Test valid empty constructor via dequeuing after instantiation"""
#     with pytest.raises(IndexError):
#         Queue(()).dequeue()


# @pytest.mark.parametrize("input", invalid_constructor_args)
# def test_invalid_constructor(input):
#     """Test invalid constuctor arguments"""
#     with pytest.raises(TypeError):
#         Queue(input)


# def test_enqueue():
#     """Fill an empty contructor argument and assert len, deque)"""
#     filling_this = Queue(())
#     for i in xrange(40):
#         filling_this.enqueue(i)
#     assert len(filling_this) == 40
#     assert filling_this.dequeue() == 0


# def test_dequeue():
#     q = Queue([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#     for x in range(5):
#         q.dequeue()
#     assert q.dequeue() == 6
#     assert q.other.header.val == 7
#     assert q.other.tail.val == 10
#     assert len(q) == 4
#     while len(q):
#         q.dequeue()
#     assert q.other.header is None
#     assert q.other.tail is None




# ********
# @pytest.fixture
# def base_llist():
#     return ll.LinkedList([1, 2, 3])


# def test_construct_from_iterable_valid(base_llist):
#     expected_output = "(1, 2, 3)"
#     assert base_llist.display() == expected_output


# def test_construct_from_nested_iterable_valid():
#     arg = ([1, 2, 3], 'string')
#     expected_output = "([1, 2, 3], u'string')"
#     assert ll.LinkedList(arg).__repr__() == expected_output


# def test_construct_from_string_valid():
#     arg = "string"
#     expected_output = "(u's', u't', u'r', u'i', u'n', u'g')"
#     assert ll.LinkedList(arg).__repr__() == expected_output


# def test_construct_empty_valid():
#     expected_output = "()"
#     assert ll.LinkedList().__repr__() == expected_output


# def test_construct_from_none_fails():
#     with pytest.raises(TypeError):
#         ll.LinkedList(None)


# def test_construct_from_single_integer_fails():
#     with pytest.raises(TypeError):
#         ll.LinkedList(2)


# def test_insert_single_value(base_llist):
#     base_llist.insert(4)
#     assert base_llist.__repr__() == "(4, 1, 2, 3)"


# def test_pop(base_llist):
#     assert base_llist.pop() == 1
#     assert base_llist.__repr__() == "(2, 3)"


# def test_size(base_llist):
#     assert base_llist.size() == 3


# def test_search_val(base_llist):
#     searched_node = base_llist.search(2)
#     assert isinstance(searched_node, ll.Node)
#     assert searched_node.val == 2


# def test_remove_node(base_llist):
#     base_llist.remove(base_llist.search(2))
#     assert base_llist.__repr__() == "(1, 3)"


# def test_display(base_llist):
#     assert base_llist.display() == "(1, 2, 3)"
