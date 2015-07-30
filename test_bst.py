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
        root.insert(val, balanced=False)
    return root


@pytest.fixture()
def fixed_setup():
    root = Node(25)
    setup = [15, 30, 9, 17, 21, 39, 12, 24, 40, 14]
    for item in setup:
        root.insert(item, balanced=False)
    return root


@pytest.fixture()
def traversal_setup():
    root = Node()
    setup = ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
    for char in setup:
        root.insert(char, balanced=False)
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
    root.insert(expected, balanced=False)
    actual = root.val
    assert expected == actual


def test_insert_lesser_in_filled_root():
    root = Node(10)
    expected = 5
    root.insert(expected, balanced=False)
    actual = root.left.val
    assert expected == actual
    assert root.right is None


def test_insert_greater_in_filled_root():
    root = Node(10)
    expected = 15
    root.insert(expected, balanced=False)
    actual = root.right.val
    assert expected == actual
    assert root.left is None


def test_insert_lesser_in_filled_tree1():
    root = Node(10)
    root.left, root.right = Node(5), Node(15)
    root.insert(1, balanced=False)
    assert root.left.left.val == 1
    assert root.left.right is None


def test_insert_lesser_in_filled_tree2():
    root = Node(10)
    root.left, root.right = Node(5), Node(15)
    root.insert(7, balanced=False)
    assert root.left.right.val == 7
    assert root.left.left is None


def test_insert_greater_in_filled_tree1():
    root = Node(10)
    root.left, root.right = Node(5), Node(15)
    root.insert(17, balanced=False)
    assert root.right.right.val == 17
    assert root.right.left is None


def test_insert_greater_in_filled_tree2():
    root = Node(10)
    root.left, root.right = Node(5), Node(15)
    root.insert(12, balanced=False)
    assert root.right.left.val == 12
    assert root.right.right is None


def test_insert_duplicates():
    root = Node(10)
    root.left, root.right = Node(5), Node(15)
    root.insert(5, balanced=False)
    assert root.size() == 3
    root.insert(15, balanced=False)
    assert root.size() == 3


def test_insert(rand_setup):
    pre_size = rand_setup.size()
    new = 200
    rand_setup.insert(new, balanced=False)
    assert rand_setup.insert(new, balanced=False) is None
    rand_setup.insert(new, balanced=False)
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
    rand_setup.insert(rand, balanced=False)
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
    rand_setup.insert(new, balanced=False)
    rand_setup.insert(new, balanced=False)
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
    fixed_setup.insert(13, balanced=False)
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
    root = Node._sorted_list_to_bst(nodes, 0, 99)
    assert isinstance(root, Node)
    assert root.size() == 100 and root.balance() == 0


def test_create_best_case():
    root = Node.create_best_case(100)
    assert isinstance(root, Node)
    assert root.size() == 100 and root.balance() == 0


def test_create_worst_case():
    root = Node.create_worst_case(100)
    assert isinstance(root, Node)
    assert root.size() == 100 and root.balance() == -99


def test_lookup(traversal_setup):
    root = traversal_setup
    expected = root.left
    actual = root._lookup('B')
    assert expected is actual


def test_is_left_no_parent():
    root = Node(10)
    root.left, root.right = Node(5, root.left), Node(15)
    assert root._is_left() is None


def test_is_left_left_node():
    root = Node(10)
    root.left, root.right = Node(5, root.left), Node(15)
    node = root.left
    result = node._is_left()
    assert result is None


def test_is_left_right_node():
    root = Node(10)
    root.left, root.right = Node(5, root.left), Node(15)
    node = root.right
    assert not node._is_left()


def test_delete_root_only():
    root = Node('A')
    root.delete('A', balanced=False)
    assert root.val is None
    assert root.left is None and root.right is None


def test_delete_node_without_children(traversal_setup):
    root = traversal_setup
    root.delete('A', balanced=False)
    parent = root.left
    assert parent.left is None


def test_delete_node_with_one_child(traversal_setup):
    root = traversal_setup
    root.delete('G', balanced=False)
    parent = root
    assert parent.right.val == 'I'


def test_delete_node_with_two_children(traversal_setup):
    root = traversal_setup
    root.delete('B', balanced=False)
    parent = root
    assert parent.left.val == 'C'
    successor = parent.left
    assert successor.left.val == 'A' and successor.right.val == 'D'


def test_delete_root_with_one_child():
    root = Node('F')
    root.left = Node('B')
    root.left.left, root.left.right = Node('A'), Node('D')
    root.delete('F', balanced=False)
    assert root.val == 'B'
    assert root.left.val == 'A' and root.right.val == 'D'


def test_delete_root_with_two_children(traversal_setup):
    root = traversal_setup
    root.delete('F', balanced=False)
    assert root.val == 'G'
    assert root.left.val == 'B' and root.right.val == 'I'


# Tests for AVL Balanced Behavior Follow
def test_avl_insert_in_empty_root():
    root = Node()
    expected = 10
    root.insert(expected)
    actual = root.val
    assert expected == actual


def test_avl_insert_lesser_in_filled_root():
    root = Node(10)
    expected = 5
    root.insert(expected)
    actual = root.left.val
    assert expected == actual
    assert root.right is None


def test_avl_insert_greater_in_filled_root():
    root = Node(10)
    expected = 15
    root.insert(expected)
    actual = root.right.val
    assert expected == actual
    assert root.left is None


def test_avl_insert_lesser_in_filled_tree1():
    root = Node(10)
    root.left, root.right = Node(5), Node(15)
    root.left.left = Node(2, root.left)
    root.insert(1)
    assert root.left.val == 2
    assert root.left.left.val == 1 and root.left.right.val == 5


def test_avl_insert_lesser_in_filled_tree2():
    root = Node(10)
    root.left, root.right = Node(5, root.left), Node(15)
    root.left.left = Node(2, root.left)
    root.insert(3)
    assert root.left.val == 3
    assert root.left.left.val == 2 and root.left.right.val == 5


def test_avl_insert_greater_in_filled_tree1():
    root = Node(10)
    root.left, root.right = Node(5), Node(15)
    root.right.right = Node(20, root.right)
    root.insert(17)
    assert root.right.val == 17
    assert root.right.left.val == 15 and root.right.right.val == 20


def test_avl_insert_greater_in_filled_tree2():
    root = Node(10)
    root.left, root.right = Node(5), Node(15, root.right)
    root.right.right = Node(20, root.right)
    root.insert(25)
    assert root.right.val == 20
    assert root.right.left.val == 15 and root.right.right.val == 25


def test_avl_delete_root_only():
    root = Node(0)
    root.delete(0)
    assert root.val is None
    assert root.left is None and root.right is None


def test_avl_delete_root_with_one_child():
    root = Node(10)
    root.left = Node(5, root)
    root.delete(10)
    assert root.val == 5
    assert root.left is None and root.right is None


def test_avl_delete_root_with_two_children():
    root = Node(10)
    root.left, root.right = Node(5, root), Node(15, root)
    root.delete(10)
    assert root.val == 15
    assert root.left.val == 5 and root.right is None


def test_avl_delete_node_without_children():
    root = Node(10)
    root.left, root.right = Node(5, root), Node(15, root)
    root.right.right = Node(20, root.right)
    root.delete(5)
    assert root.val == 15
    assert root.left.val == 10 and root.right.val == 20


def test_avl_delete_node_with_one_child():
    root = Node(10)
    root.left, root.right = Node(5, root), Node(15, root)
    root.right.left = Node(12, root.right)
    root.right.right = Node(20, root.right)
    root.right.left.right = Node(13, root.right.left)
    root.left.right = Node(8, root.left)
    root.delete(5)
    assert root.val == 12
    assert root.left.val == 10 and root.right.val == 15


def test_avl_delete_node_with_two_children():
    root = Node(10)
    root.left, root.right = Node(5, root), Node(15, root)
    root.right.left = Node(12, root.right)
    root.right.right = Node(20, root.right)
    root.right.left.right = Node(13, root.right.left)
    root.left.right = Node(8, root.left)
    root.delete(15)
    assert root.right.val == 13
    assert root.right.left.val == 12 and root.right.right.val == 20

