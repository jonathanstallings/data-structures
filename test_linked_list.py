from __future__ import unicode_literals
import pytest
import linked_list as ll


@pytest.fixture
def base_llist():
    return ll.LinkedList([1, 2, 3])


def test_construct_from_iterable_valid(base_llist):
    expected_output = "(1, 2, 3)"
    assert base_llist.display() == expected_output


def test_construct_from_nested_iterable_valid():
    arg = ([1, 2, 3], 'string')
    expected_output = "([1, 2, 3], u'string')"
    assert ll.LinkedList(arg).__repr__() == expected_output


def test_construct_from_string_valid():
    arg = "string"
    expected_output = "(u's', u't', u'r', u'i', u'n', u'g')"
    assert ll.LinkedList(arg).__repr__() == expected_output


def test_construct_empty_valid():
    expected_output = "()"
    assert ll.LinkedList().__repr__() == expected_output


def test_construct_from_none_fails():
    with pytest.raises(TypeError):
        ll.LinkedList(None)


def test_construct_from_single_integer_fails():
    with pytest.raises(TypeError):
        ll.LinkedList(2)


def test_insert_single_value(base_llist):
    base_llist.insert(4)
    assert base_llist.__repr__() == "(4, 1, 2, 3)"


def test_pop(base_llist):
    assert base_llist.pop() == 1
    assert base_llist.__repr__() == "(2, 3)"


def test_size(base_llist):
    assert base_llist.size() == 3


def test_search_val(base_llist):
    searched_node = base_llist.search(2)
    assert isinstance(searched_node, ll.Node)
    assert searched_node.val == 2


def test_remove_node(base_llist):
    base_llist.remove(base_llist.search(2))
    assert base_llist.__repr__() == "(1, 3)"


def test_display(base_llist):
    assert base_llist.display() == "(1, 2, 3)"
