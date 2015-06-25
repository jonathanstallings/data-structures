import pytest
import linked_list as ll


@pytest.fixture
def base_llist():
    return ll.linked_list([1, 2, 3])


class TestConstructor():
    def test_construct_from_iterable_valid(base_llist):
        expected_output = "(1, 2, 3)"
        assert base_llist.display() == expected_output

    def test_construct_from_nested_iterable_valid():
        arg = ([1, 2, 3], 'string')
        expected_output = "([1, 2, 3], 'string')"
        assert ll.LinkedList([arg]) == expected_output

    def test_construct_from_string_valid():
        arg = "string"
        expected_output = "('s', 't', 'r', 'i', 'n', 'g')"
        assert ll.LinkedList([arg]) == expected_output

    def test_construct_from_none_fails():
        with pytest.raises(TypeError):
            ll.LinkedList(None)

    def test_construct_from_single_integer_fails():
        with pytest.raises(TypeError):
            ll.LinkedList(2)


class TestInsertVal():
    def test_single_value(base_llist):
        base_llist.insert(4)
        assert base_llist == "(4, 1, 2, 3)"


class TestPop():
    def test_pop(base_llist):
        base_llist.pop()
        assert base_llist == "(2, 3)"


class TestSize():
    def test_size(base_llist):
        assert base_llist.size() == 3


class TestSearchVal():
    def test_search_val(base_llist):
        searched_node = base_llist.seach(2)
        assert isinstance(searched_node, ll.Node)
        assert searched_node.val == 2


class TestRemoveNode():
    def test_remove_node(base_llist):
        base_llist.remove(2)
        assert base_llist == "(1, 3)"


class TestDisplay():
    def test_display(base_llist):
        assert base_llist.display == "(1, 2, 3)"
