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
    graph_empty.add_node(10)
    assert 10 in graph_empty
    assert isinstance(graph_empty[10], set) and len(graph_empty[10]) == 0

