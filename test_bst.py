from __future__ import unicode_literals
from random import randint
import types

import pytest

from bst import Node


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

    return root


@pytest.fixture()
def traversal_setup():
    root = Node()
    setup = ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
    for char in setup:
        root.insert(char)
    return root


def test_init_empty():
    root = Node()
    assert root.val is None
    assert root.left is None and root.right is None


def test_init_with_val():
    root = Node(10)
    assert root.val == 10
    assert root.left is None and root.right is None


def test_insert_in_empty_root():
    root = Node()
    expected = 10
    root.insert(expected)
    actual = root.val
    assert expected == actual


def test_insert_lesser_in_filled_root():
    root = Node(10)
    expected = 5
    root.insert(expected)
    actual = root.left.val
    assert expected == actual
    assert root.right is None


def test_insert_greater_in_filled_root():
    root = Node(10)
    expected = 15
    root.insert(expected)
    actual = root.right.val
    assert expected == actual
    assert root.left is None


def test_insert_lesser_in_filled_tree1():
    root = Node(10)
    root.left, root.right = Node(5), Node(15)
    root.insert(1)
    assert root.left.left.val == 1
    assert root.left.right is None


def test_insert_lesser_in_filled_tree2():
    root = Node(10)
    root.left, root.right = Node(5), Node(15)
    root.insert(7)
    assert root.left.right.val == 7
    assert root.left.left is None


def test_insert_greater_in_filled_tree1():
    root = Node(10)
    root.left, root.right = Node(5), Node(15)
    root.insert(17)
    assert root.right.right.val == 17
    assert root.right.left is None


def test_insert_greater_in_filled_tree2():
    root = Node(10)
    root.left, root.right = Node(5), Node(15)
    root.insert(12)
    assert root.right.left.val == 12
    assert root.right.right is None


def test_insert_duplicates():
    root = Node(10)
    root.left, root.right = Node(5), Node(15)
    root.insert(5)
    assert root.size() == 3
    root.insert(15)
    assert root.size() == 3


def test_insert(rand_setup):
    pre_size = rand_setup.size()
    new = 200
    rand_setup.insert(new)
    assert rand_setup.insert(new) is None
    rand_setup.insert(new)
    post_size = rand_setup.size()
    assert post_size > pre_size
    assert post_size == pre_size + 1


def test_contains_val():
    root = Node(10)
    root.left, root.right = Node(5), Node(15)
    assert root.contains(15) and not root.contains(27)
    root.left.left = Node(2)
    assert root.contains(2)


def test_contains(rand_setup):
    rand = randint(1, 100)
    rand_setup.insert(rand)
    assert rand_setup.contains(rand) is True


def test_size_with_filling():
    root = Node()
    assert root.size() == 0
    root.val = 10
    assert root.size() == 1
    root.left, root.right = Node(5), Node(15)
    assert root.size() == 3


def test_size(rand_setup):
    pre_size = rand_setup.size()
    new = 200
    rand_setup.insert(new)
    rand_setup.insert(new)
    post_size = rand_setup.size()
    assert post_size > pre_size
    assert post_size == pre_size + 1


def test_depth_1():
    root = Node()
    assert root.depth() == 1
    root.val = 10
    assert root.depth() == 1


def test_depth_2():
    root = Node(10)
    root.left = Node(5)
    assert root.depth() == 2
    root.right = Node(15)
    assert root.depth() == 2


def test_depth_3():
    root = Node(10)
    root.left, root.right = Node(5), Node(15)
    root.left.left, root.left.right = Node(3), Node(7)
    assert root.depth() == 3
    root.right.left, root.right.right = Node(12), Node(17)
    assert root.depth() == 3


def test_depth_n():
    rand = randint(1, 100)
    root = Node(0)
    curr = root
    for i in range(rand):
        curr.right = Node(i)
        curr = curr.right
    assert root.depth() == rand + 1


def test_depth(fixed_setup):
    assert fixed_setup.left.depth() == 4
    assert fixed_setup.right.depth() == 3
    fixed_setup.insert(13)
    assert fixed_setup.left.depth() == 5


def test_balance_equal():
    root = Node(10)
    assert root.balance() == 0
    root.left, root.right = Node(5), Node(15)
    assert root.balance() == 0
    root.left.left, root.left.right = Node(3), Node(7)
    root.right.right = Node(17)
    assert root.balance() == 0


def test_balance_positive():
    root = Node(10)
    root.left = Node(5)
    assert root.balance() == 1
    root.left.left, root.left.right = Node(3), Node(7)
    assert root.balance() == 2
    root.right = Node(15)
    assert root.balance() == 1


def test_balance_negative():
    root = Node(10)
    root.right = Node(5)
    assert root.balance() == -1
    root.right.left, root.right.right = Node(3), Node(7)
    assert root.balance() == -2
    root.left = Node(15)
    assert root.balance() == -1


def test_balance(rand_setup):
    left = rand_setup.left.depth() if rand_setup.left is not None else 0
    right = rand_setup.right.depth() if rand_setup.right is not None else 0
    if left > right:
        assert rand_setup.balance() > 0
    elif right > left:
        assert rand_setup.balance() < 0
    else:
        assert rand_setup.balance() == 0


def test_in_order(traversal_setup):
    root = traversal_setup
    expected = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    generator = root.in_order()
    assert isinstance(generator, types.GeneratorType)
    actual = list(generator)
    assert expected == actual


def test_pre_order(traversal_setup):
    root = traversal_setup
    expected = ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
    generator = root.pre_order()
    assert isinstance(generator, types.GeneratorType)
    actual = list(generator)
    assert expected == actual


def test_post_order(traversal_setup):
    root = traversal_setup
    expected = ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F']
    generator = root.post_order()
    assert isinstance(generator, types.GeneratorType)
    actual = list(generator)
    assert expected == actual


def test_breadth_first(traversal_setup):
    root = traversal_setup
    expected = ['F', 'B', 'G', 'A', 'D', 'I', 'C', 'E', 'H']
    generator = root.breadth_first()
    assert isinstance(generator, types.GeneratorType)
    actual = list(generator)
    assert expected == actual


def test_sorted_list_to_bst():
    nodes = range(100)
    root = Node._sorted_list_to_BST(nodes, 0, 99)
    assert isinstance(root, Node)
    assert root.size() == 100 and root.balance() == 0


def test_create_best_case():
    root = Node.create_best_case(100)
    assert isinstance(root, Node)
    assert root.size() == 100 and root.balance() == 0

