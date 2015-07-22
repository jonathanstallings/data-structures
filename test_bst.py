from __future__ import unicode_literals
from bst import Node
from random import randint
import pytest


@pytest.fixture()
def rand_setup():
    root = Node(randint(1, 100))
    for idx in range(20):
        val = randint(1, 100)
        root.insert(val)

    return root


@pytest.fixture()
def fixed_setup():
    root = Node(25)
    root.insert(15)
    root.insert(30)
    root.insert(9)
    root.insert(17)
    root.insert(21)
    root.insert(39)
    root.insert(12)
    root.insert(24)
    root.insert(40)
    root.insert(14)


def test_insert(rand_setup):
    pre_size = rand_setup.size()
    rand = randint(1, 100)
    rand_setup.insert(rand)
    assert rand_setup.insert(rand) is None
    rand_setup.insert(rand)
    post_size = rand_setup.size()
    assert post_size > pre_size
    assert post_size == pre_size + 1


def test_contains(rand_setup):
    rand = randint(1, 100)
    rand_setup.insert(rand)
    assert rand_setup.contains(rand) is True


def test_size(rand_setup):
    pre_size = rand_setup.size()
    rand = randint(1, 100)
    rand_setup.insert(rand)
    rand_setup.insert(rand)
    post_size = rand_setup.size()
    assert post_size > pre_size
    assert post_size == pre_size + 1


def test_depth(fixed_setup):
    assert fixed_setup.left.depth() == 5
    assert fixed_setup.right.depth() == 4
    fixed_setup.insert(13)
    assert fixed_setup.left.depth() == 6


def test_balance(rand_setup):
    left = rand_setup.left.depth()
    right = rand_setup.right.depth()
    if left > right:
        assert rand_setup.balance() == -int
    elif right > left:
        assert rand_setup.balance() == abs(int)
    else:
        assert rand_setup.balance() == 0
