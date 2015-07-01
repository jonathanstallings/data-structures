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


def test_remove_0():
    """Fill a DoubleLinkList with (1,2,3), check removal of 0"""
    adding_to = DoubleLinkList(())
    for i in xrange(3):
        adding_to.insert(i)

    adding_to.remove(0)
    assert adding_to.pop() == 2
    assert adding_to.shift() == 1


def test_remove_1():
    """Fill a DoubleLinkList with (1,2,3), check removal of 1"""
    adding_to = DoubleLinkList(())
    for i in xrange(3):
        adding_to.insert(i)

    adding_to.remove(1)
    assert adding_to.pop() == 2
    assert adding_to.shift() == 0


def test_remove_2():
    """Fill a DoubleLinkList with (1,2,3), check removal of 3"""
    adding_to = DoubleLinkList(())
    for i in xrange(3):
        adding_to.insert(i)

    adding_to.remove(2)
    assert adding_to.pop() == 1
    assert adding_to.shift() == 0


def test_remove_5():
    """Fill a DoubleLinkList with (1,2,3), check removal of 5;
    should result in ValueError"""
    adding_to = DoubleLinkList(())
    for i in xrange(3):
        adding_to.insert(i)
    with pytest.raises(ValueError):
        adding_to.remove(5)
