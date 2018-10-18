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
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {},
        'D': {'A': 5},
        'E': {},
        'F': {}
    }
    return g


@pytest.fixture()
def graph_filled_for_traversal():
    g = Graph()
    g.graph = {
        'A': {'B': 10, 'C': 15},
        'B': {'D': 15, 'E': 5, 'C': 2},
        'C': {'F': 50, 'G': 25},
        'D': {},
        'E': {'C': 5},
        'F': {'E': 10},
        'G': {'F': 20}
    }
    return g


@pytest.fixture()
def graph_filled_for_traversal_neg_edges():
    g = Graph()
    g.graph = {
        'A': {'B': -5, 'C': 15},
        'B': {'D': 15, 'E': 5, 'C': 2},
        'C': {'F': 50, 'G': -20},
        'D': {},
        'E': {'C': 5},
        'F': {'E': 10},
        'G': {'F': 20}
    }
    return g


@pytest.fixture()
def graph_filled_for_traversal_neg_edges_loop():
    g = Graph()
    g.graph = {
        'A': {'B': -5, 'C': 15},
        'B': {'D': 15, 'E': 5, 'C': 2},
        'C': {'F': 50, 'G': -20},
        'D': {},
        'E': {'C': -50},
        'F': {'E': 10},
        'G': {'F': 20}
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
    new = 'A'
    g.add_node(new)
    assert new in g
    assert isinstance(g[new], dict) and len(g[new]) == 0


def test_add_node_to_filled(graph_filled):
    g = graph_filled
    new = 'G'
    g.add_node(new)
    assert new in g
    assert isinstance(g[new], dict)
    assert len(g[new]) == 0


def test_add_node_to_filled_existing_node(graph_filled):
    with pytest.raises(KeyError):
        graph_filled.add_node('B')


def test_add_node_wrong_type(graph_empty):
    with pytest.raises(TypeError):
        graph_empty.add_node([1, 2, 3])


def test_add_edge_new_nodes(graph_empty):
    g = graph_empty
    n1, n2 = 'A', 'B'
    g.add_edge(n1, n2, 10)
    assert n1 in g and n2 in g
    assert n2 in g[n1]
    assert g[n1][n2] == 10


def test_add_edge_n2_new(graph_filled):
    g = graph_filled
    n1, n2 = 'A', 'G'
    g.add_edge(n1, n2, 10)
    assert n1 in g and n2 in g
    assert n2 in g[n1]
    assert g[n1][n2] == 10


def test_add_edge_n1_new(graph_filled):
    g = graph_filled
    n1, n2 = 'G', 'A'
    g.add_edge(n1, n2, 10)
    assert n1 in g and n2 in g
    assert n2 in g[n1]
    assert g[n1][n2] == 10


def test_add_edge_n1_n2_exist_with_edges(graph_filled):
    g = graph_filled
    n1, n2 = 'D', 'A'
    g.add_edge(n1, n2, 10)
    assert n1 in g and n2 in g
    assert n2 in g[n1]
    assert g[n1][n2] == 10


def test_add_edge_n1_n2_exist_without_edges(graph_filled):
    g = graph_filled
    n1, n2 = 'E', 'F'
    g.add_edge(n1, n2, 10)
    assert n1 in g and n2 in g
    assert n2 in g[n1]
    assert g[n1][n2] == 10


def test_del_node_exists(graph_filled):
    g = graph_filled
    g.del_node('A')
    assert 'A' not in g
    assert 'A' not in g.graph.values()


def test_del_node_empty_error(graph_empty):
    with pytest.raises(KeyError):
        graph_empty.del_node('A')


def test_del_edge_exists(graph_filled):
    g = graph_filled
    n1, n2 = 'B', 'A'
    g.del_edge(n1, n2)
    assert n1 in g and n2 in g
    assert n2 not in g[n1]


def test_del_edge_not_exist(graph_filled):
    with pytest.raises(KeyError):
        graph_filled.del_edge('X', 'Y')


def test_nodes_empty(graph_empty):
    out = graph_empty.nodes()
    assert str(out) == "[]"
    assert len(out) == 0


def test_nodes_filled(graph_filled):
    out = graph_filled.nodes()
    expected_nodes = set(['A', 'B', 'C', 'D', 'E', 'F'])
    assert set(out) == expected_nodes
    assert len(out) == 6


def test_edges_empty(graph_empty):
    out = graph_empty.edges()
    assert str(out) == "[]"
    assert len(out) == 0


def test_edges_filled(graph_filled):
    out = graph_filled.edges()
    expected_edges = set([
        ('A', 'B'), ('B', 'A'), ('B', 'D'), ('B', 'C'), ('D', 'A')
    ])
    assert set(out) == expected_edges
    assert len(out) == 5


def test_host_node_empty(graph_empty):
    unexpected_nodes = set([0, 2, 7, 13, 27, 33])
    for node in unexpected_nodes:
        assert graph_empty.has_node(node) is False


def test_has_node_filled(graph_filled):
    expected_nodes = set(['A', 'B', 'C', 'D', 'E', 'F'])
    unexpected_nodes = set(['G', 'H', 'I', 'J', 'K', 10])
    for node in expected_nodes:
        assert graph_filled.has_node(node) is True
    for node in unexpected_nodes:
        assert graph_filled.has_node(node) is False


def test_neighbors_empty(graph_empty):
    with pytest.raises(KeyError):
        graph_empty.neighbors('G')


def test_neighbors_filled_not_present(graph_filled):
    with pytest.raises(KeyError):
        graph_filled.neighbors('G')


#  input, expected output for neighbors in graph_filled
neighbor_params = [
    ('A', {'B': 10}),
    ('B', {'A': 5, 'D': 15, 'C': 20}),
    ('C', {}),
    ('D', {'A': 5}),
    ('E', {}),
    ('F', {})
]


@pytest.mark.parametrize("input, out", neighbor_params)
def test_neighbors_filled_present(input, out, graph_filled):
    assert graph_filled.neighbors(input) == out


def test_adjacent_empty(graph_empty):
    with pytest.raises(KeyError):
        graph_empty.adjacent('A', 'B')


def test_adjacent_filled_existing(graph_filled):
    expected_edges = set([
        ('A', 'B'), ('B', 'A'), ('B', 'D'), ('B', 'C'), ('D', 'A')
    ])
    for a, b in expected_edges:
        assert graph_filled.adjacent(a, b) is True


def test_adjacent_filled_existing_node_unexisting_edge(graph_filled):
    bad_edges = set([('A', 'C'), ('D', 'B'), ('A', 'D')])
    for a, b in bad_edges:
        assert graph_filled.adjacent(a, b) is False


def test_adjacent_filled_missing_node(graph_filled):
    with pytest.raises(KeyError):
        graph_filled.adjacent('G', 'H')


def test_depth_first_traversal(graph_filled_for_traversal):
    level1 = set(['A'])
    level2 = set(['B', 'C'])
    level3 = set(['D', 'E', 'F', 'G'])
    output = graph_filled_for_traversal.depth_first_traversal('A')
    assert len(output) == 7
    assert output[0] in level1
    assert output[1] in level2
    assert output[2] in level3


def test_breadth_first_traversal(graph_filled_for_traversal):
    level1 = set(['A'])
    level2 = set(['B', 'C'])
    level3 = set(['D', 'E', 'F', 'G'])
    output = graph_filled_for_traversal.breadth_first_traversal('A')
    assert len(output) == 7
    assert output[0] in level1
    assert output[1] in level2
    assert output[2] in level2
    assert output[3] in level3


def test_depth_first_traversal_no_arg(graph_filled_for_traversal):
    with pytest.raises(TypeError):
        graph_filled_for_traversal.depth_first_traversal()


def test_breadth_first_traversal_no_arg(graph_filled_for_traversal):
    with pytest.raises(TypeError):
        graph_filled_for_traversal.breadth_first_traversal()


def test_graph_weighted_edges(graph_filled):
    assert graph_filled['A']['B'] == 10
    assert graph_filled['B']['A'] == 5
    assert graph_filled['B']['D'] == 15
    assert graph_filled['B']['C'] == 20
    assert graph_filled['D']['A'] == 5


def test_uniform_cost_search(graph_filled_for_traversal):
    g = graph_filled_for_traversal
    expected = ['A', 'B', 'C', 'G', 'F']
    actual = g.uniform_cost_search('A', 'F')
    assert expected == actual


def test_bellmanford(graph_filled_for_traversal):
    g = graph_filled_for_traversal
    expected = ['A', 'B', 'C', 'G', 'F']
    actual = g.bellmanford('A', 'F')
    assert expected == actual


def test_bellmanford_neg_edges(graph_filled_for_traversal_neg_edges):
    g = graph_filled_for_traversal_neg_edges
    expected = ['A', 'B', 'C', 'G', 'F']
    actual = g.bellmanford('A', 'F')
    assert expected == actual


def test_bellmanford_neg_edges_with_loop(
        graph_filled_for_traversal_neg_edges_loop):
    g = graph_filled_for_traversal_neg_edges_loop
    expected = ['A', 'B', 'C', 'G', 'F']
    with pytest.raises(ZeroDivisionError):
        g.bellmanford('A', 'F')