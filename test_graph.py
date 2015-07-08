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


def test_nodes_empty(graph_empty):
    out = graph_empty.nodes()
    assert str(out) == "[]"
    assert len(out) == 0


def test_nodes_filled(graph_filled):
    out = graph_filled.nodes()
    expected_nodes = set([5, 10, 15, 20, 25, 30])
    assert set(out) == expected_nodes
    assert len(out) == 6


def test_edges_empty(graph_empty):
    out = graph_empty.edges()
    assert str(out) == "[]"
    assert len(out) == 0


def test_edges_filled(graph_filled):
    out = graph_filled.edges()
    expected_edges = set([(5, 10), (10, 5), (10, 20), (10, 15), (20, 5)])
    assert set(out) == expected_edges
    assert len(out) == 5


def test_host_node_empty(graph_empty):
    unexpected_nodes = set([0, 2, 7, 13, 27, 33])
    for node in unexpected_nodes:
        assert graph_empty.has_node(node) == False


def test_has_node_filled(graph_filled):
    expected_nodes = set([5, 10, 15, 20, 25, 30])
    unexpected_nodes = set([0, 2, 7, 13, 27, 33])
    for node in expected_nodes:
        assert graph_filled.has_node(node) == True
    for node in unexpected_nodes:
        assert graph_filled.has_node(node) == False


def test_neighbors_empty(graph_empty):
    with pytest.raises(KeyError):
        graph_empty.neighbors(3)


def test_neighbors_filled_not_present(graph_filled):
    with pytest.raises(KeyError):
        graph_filled.neighbors(3)


#  input, expected output for neighbors in graph_filled
neighbor_params = [
    (5, set([10])),
    (10, set([5, 20, 15])),
    (20, set([5])),
    (25, set()),
    (30, set())
]


@pytest.mark.parametrize("input, out", neighbor_params)
def test_neighbors_filled_present(input, out, graph_filled):
    assert graph_filled.neighbors(input) == out 


def test_adjacent_empty(graph_empty):
    with pytest.raises(KeyError):
        graph_empty.adjacent(4, 2)


def test_adjacent_filled_existing(graph_filled):
    expected_edges = set([(5, 10), (10, 5), (10, 20), (10, 15), (20, 5)])
    for a, b in expected_edges:
        assert graph_filled.adjacent(a, b) == True


def test_adjacent_filled_existing_node_unexisting_edge(graph_filled):
    bad_edges = set([(5, 15), (20, 10), (5, 20)])
    for a, b in bad_edges:
        assert graph_filled.adjacent(a, b) == False


def test_adjacent_filled_missing_node(graph_filled):
    with pytest.raises(KeyError):
        graph_filled.adjacent(7, 3)
