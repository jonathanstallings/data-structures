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


def test_has_edge_empty(graph_empty):
    assert graph_empty.has_edge() == False
