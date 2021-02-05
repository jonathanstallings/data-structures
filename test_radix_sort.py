from random import shuffle
import pytest

from radix_sort import radix_srt


def test_radix_srt():
    expected = range(20)
    actual = expected[:]
    shuffle(actual)
    radix_srt(actual)
    assert expected == actual


def test_radix_srt_with_duplicates():
    expected = [1, 3, 3, 6, 7, 8, 8, 8]
    actual = expected[:]
    shuffle(actual)
    radix_srt(actual)
    assert expected == actual


def test_radix_srt_with_zero_items():
    expected = []
    actual = []
    radix_srt(actual)
    assert expected == actual


def test_radix_srt_with_one_item():
    expected = [1]
    actual = [1]
    radix_srt(actual)
    assert expected == actual


def test_radix_sort_wrong_type():
    with pytest.raises(TypeError):
        radix_srt(15)

