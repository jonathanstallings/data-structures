from __future__ import unicode_literals
import pytest

from priorityq import PriorityQ, QNode


def test_QNode_init_no_priority():
    r = QNode(10)
    assert r.val == 10
    assert r.priority is None


def test_QNode_init_with_priority():
    p = QNode('string', 0)
    assert p.val == 'string'
    assert p.priority is 0
    assert p.val, p.priority == ('string', 0)


def test_QNode_val_comparison():
    p = QNode(10)
    r = QNode(5)
    assert p > r


def test_QNode_priority_comparison():
    p = QNode(10, 0)
    r = QNode(10)
    assert p < r


def test_QNode_equal_priority_comparison():
    p = QNode(10, 1)
    r = QNode(5, 1)
    assert p > r


def test_QNode_equality_comparison():
    p = QNode(10, 10)
    r = QNode(10, 10)
    assert p == r
