# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from queue import Queue

#  (Input, expected) for well constructed instantiation arguments,
#  and one subsequent dequeue
valid_constructor_args_dequeue = [
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


@pytest.mark.parametrize("input,deque", valid_constructor_args_dequeue)
def test_valid_contructor(input, deque):
    """Test valid constructor using by dequeuing after instantiation"""
    assert Queue(input).dequeue() == deque


def test_empty_constructor():
    """Test valid empty constructor via dequeuing after instantiation"""
    with pytest.raises(IndexError):
        Queue(()).dequeue()


@pytest.mark.parametrize("input", invalid_constructor_args)
def test_invalid_constructor(input):
    """Test invalid constuctor arguments"""
    with pytest.raises(TypeError):
        Queue(input)


def test_enqueue():
    """Fill an empty contructor argument and assert len, deque)"""
    filling_this = Queue(())
    for i in xrange(40):
        filling_this.enqueue(i)
    assert len(filling_this) == 40
    assert filling_this.dequeue() == 0


def test_dequeue():
    q = Queue([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    for x in range(5):
        q.dequeue()
    assert q.dequeue() == 6
    assert q.other.head.val == 7
    assert q.other.tail.val == 10
    assert len(q) == 4
    while len(q):
        q.dequeue()
    assert q.other.head is None
    assert q.other.tail is None
