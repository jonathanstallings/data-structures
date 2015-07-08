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
    g = graph_empty
    new = 40
    g.add_node(new)
    assert new in g
    assert isinstance(g[new], set) and len(g[new]) == 0


def test_add_node_to_filled(graph_filled):
    g = graph_filled
    new = 40
    g.add_node(new)
    assert new in g
    assert isinstance(g[new], set)
    assert len(g[new]) == 0


def test_add_node_to_filled_existing_node(graph_filled):
    with pytest.raises(KeyError):
        graph_filled.add_node(5)


def test_add_node_wrong_type(graph_empty):
    with pytest.raises(TypeError):
        graph_empty.add_node([1, 2, 3])


def test_add_edge_new_nodes(graph_empty):
    g = graph_empty
    n1, n2 = 30, 40
    g.add_edge(n1, n2)
    assert n1 in g and n2 in g
    assert n2 in g[n1]
    assert len(g[n2]) == 0


def test_add_edge_n2_new(graph_filled):
    g = graph_filled
    n1, n2 = 30, 40
    g.add_edge(n1, n2)
    assert n1 in g and n2 in g
    assert n2 in g[n1]
    assert len(g[n2]) == 0


def test_add_edge_n1_new(graph_filled):
    g = graph_filled
    n1, n2 = 1, 5
    g.add_edge(n1, n2)
    assert n1 in g and n2 in g
    assert n2 in g[n1]
    assert len(g[n2]) == 1


def test_add_edge_n1_n2_exist_with_edges(graph_filled):
    g = graph_filled
    n1, n2 = 20, 10
    g.add_edge(n1, n2)
    assert n1 in g and n2 in g
    assert n2 in g[n1]
    assert len(g[n1]) == 2 and len(g[n2]) == 3


def test_add_edge_n1_n2_exist_without_edges(graph_filled):
    g = graph_filled
    n1, n2 = 25, 30
    g.add_edge(n1, n2)
    assert n1 in g and n2 in g
    assert n2 in g[n1]
    assert len(g[n1]) == 1 and len(g[n2]) == 0


def test_del_node_exists(graph_filled):
    g = graph_filled
    g.del_node(5)
    assert 5 not in g
    assert 5 not in g.graph.values()


def test_del_node_empty_error(graph_empty):
    with pytest.raises(KeyError):
        graph_empty.del_node(10)


def test_del_edge_exists(graph_filled):
    g = graph_filled
    n1, n2 = 10, 5
    g.del_edge(n1, n2)
    assert n1 in g and n2 in g
    assert n2 not in g[n1]


def test_del_edge_not_exist(graph_filled):
    with pytest.raises(KeyError):
        graph_filled.del_edge(100, 200)

