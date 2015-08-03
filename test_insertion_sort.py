from random import shuffle
import pytest

from insertion_sort import in_sort


def test_insertion_sort():
    expected = range(20)
    unsorted = expected[:]
    shuffle(unsorted)
    in_sort(unsorted)
    actual = unsorted
    assert expected == actual


def test_insertion_sort_with_duplicates():
    expected = [1, 3, 3, 6, 7, 8, 8, 8]
    unsorted = expected[:]
    shuffle(unsorted)
    in_sort(unsorted)
    actual = unsorted
    assert expected == actual


def test_insertion_sort_wrong_type():
    with pytest.raises(TypeError):
        in_sort('some string')

