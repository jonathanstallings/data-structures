from __future__ import unicode_literals
import pytest

from graph import Graph


@pytest.fixture()
def graph_empty():
    g = Graph()
    return g


@pytest.fixture()
def graph_filled():
    g = Graph()
    g.graph = {
        5: set([10]),
        10: set([5, 20, 15]),
        15: set(),
        20: set([5]),
        25: set(),
        30: set()
    }
    return g


def test_valid_constructor():
    g = Graph()
    assert isinstance(g, Graph)
    assert isinstance(g.graph, dict)
    assert len(g.graph) == 0 and len(g) == 0


def test_invalid_constructor():
    with pytest.raises(TypeError):
        Graph(10)


def test_add_node_to_empty(graph_empty):
    graph_empty.add_node(40)
    assert 40 in graph_empty
    assert isinstance(graph_empty[40], set) and len(graph_empty[40]) == 0


def test_add_node_to_filled(graph_filled):
    graph_filled.add_node(40)
    assert 40 in graph_filled
    assert isinstance(graph_filled[40], set)
    assert len(graph_filled[40]) == 0


def test_add_node_to_filled_existing_node(graph_filled):
    with pytest.raises(KeyError):
        graph_filled.add_node(5)


def test_add_node_wrong_type(graph_empty):
    with pytest.raises(TypeError):
        graph_empty.add_node([1, 2, 3])

