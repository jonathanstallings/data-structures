from random import shuffle
import pytest

from quick_sort import quick_srt


def test_quick_srt():
    expected = range(20)
    actual = expected[:]
    shuffle(actual)
    quick_srt(actual)
    assert expected == actual


def test_quick_srt_with_duplicates():
    expected = [1, 3, 3, 6, 7, 8, 8, 8]
    actual = expected[:]
    shuffle(actual)
    quick_srt(actual)
    assert expected == actual


def test_quick_srt_with_zero_items():
    expected = []
    actual = []
    quick_srt(actual)
    assert expected == actual


def test_quick_srt_with_one_item():
    expected = [1]
    actual = [1]
    quick_srt(actual)
    assert expected == actual


def test_quick_sort_wrong_type():
    with pytest.raises(TypeError):
        quick_srt(15)

