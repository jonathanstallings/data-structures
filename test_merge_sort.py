from random import shuffle
import pytest

from merge_sort import merge_srt


def test_merge_sort():
    expected = range(20)
    unsorted = expected[:]
    shuffle(unsorted)
    merge_srt(unsorted)
    actual = unsorted
    assert expected == actual


def test_insertion_sort_with_duplicates():
    expected = [1, 3, 3, 6, 7, 8, 8, 8]
    unsorted = expected[:]
    shuffle(unsorted)
    merge_srt(unsorted)
    actual = unsorted
    assert expected == actual


def test_merge_sort_wrong_type():
    with pytest.raises(TypeError):
        merge_srt(15)

