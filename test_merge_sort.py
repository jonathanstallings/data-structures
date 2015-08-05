from random import shuffle
import pytest

from merge_sort import merge_srt


def test_merge_sort():
    expected = range(20)
    actual = expected[:]
    shuffle(actual)
    merge_srt(actual)
    assert expected == actual


def test_merge_sort_with_duplicates():
    expected = [1, 3, 3, 6, 7, 8, 8, 8]
    actual = expected[:]
    shuffle(actual)
    merge_srt(actual)
    assert expected == actual


def test_merge_sort_wrong_type():
    with pytest.raises(TypeError):
        merge_srt(15)

