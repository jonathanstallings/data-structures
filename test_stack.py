from __future__ import unicode_literals
import pytest

from stack import Stack


@pytest.fixture
def base_stack():
    return Stack([1, 2, 3])


def test_construct_from_iterable_valid(base_stack):
    expected_output = "(1, 2, 3)"
    assert base_stack.__repr__() == expected_output


def test_construct_from_nested_iterable_valid():
    arg = ([1, 2, 3], 'string')
    expected_output = "([1, 2, 3], u'string')"
    assert Stack(arg).__repr__() == expected_output


def test_construct_from_string_valid():
    arg = "string"
    expected_output = "(u's', u't', u'r', u'i', u'n', u'g')"
    assert Stack(arg).__repr__() == expected_output


def test_construct_empty_valid():
    expected_output = "()"
    assert Stack().__repr__() == expected_output


def test_construct_from_none_fails():
    with pytest.raises(TypeError):
        Stack(None)


def test_construct_from_single_integer_fails():
    with pytest.raises(TypeError):
        Stack(2)


def test_push(base_stack):
    base_stack.push(4)
    assert base_stack.__repr__() == "(4, 1, 2, 3)"


def test_pop(base_stack):
    assert base_stack.pop() == 1
    assert base_stack.__repr__() == "(2, 3)"


def test_pop_after_multi_push(base_stack):
    for x in range(10):
        base_stack.push(x)
    assert base_stack.pop() == 9
