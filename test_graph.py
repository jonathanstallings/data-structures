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
