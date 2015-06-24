import pytest
import linked_list as ll


LLIST = ll.LinkedList([1, 2, 3])


class TestConstructor():
    def test_construct_none():
        with pytest.raises(TypeError):
            ll.LinkedList(None)

    def test_construct_single_integer():
        with pytest.raises(TypeError):
            ll.LinkedList(2)

    def test_construct_valid():
        _input = [1, 2, 3]
        expected_output = "(1, 2, 3)"
        assert ll.LinkedList(_input).display() == expected_output

    def test_construct_valid2():
        _input = ([1, 2, 3], 'string')
        expected_output = "([1, 2, 3], 'string')"
        assert ll.LinkedList([_input]) == expected_output

    def test_construct_valid3():
        _input = "string"
        expected_output = "('s', 't', 'r', 'i', 'n', 'g')"
        assert ll.LinkedList([_input]) == expected_output


class TestInsertVal():
    def test_single_value():
        LLIST.insert(4)
        assert LLIST == "(4, 1, 2, 3)"


class TestPop():
    def test_pop():
        LLIST.pop()
        assert LLIST == "(2, 3)"


def test_size():
    pass


def test_search_val():
    pass


def test_remove_node():
    new_list.remove(1)
    assert ne


def test_display():
    pass
