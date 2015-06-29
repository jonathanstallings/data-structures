# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pytest

from parenthetics import parenthetical


def test_open_parens():
    assert parenthetical('(') == 1
    assert parenthetical('( (()) ') == 1
    assert parenthetical('  ()() (') == 1
    assert parenthetical('(    other    )  characters  (')


def test_balanced_parens():
    assert parenthetical('((()))') == 0
    assert parenthetical('()()()') == 0
    assert parenthetical('(    other    )  characters  ()') == 0


def test_broken_parens():
    assert parenthetical(')') == -1
    assert parenthetical(') )(()))') == -1
    assert parenthetical(' ()()())') == -1
    assert parenthetical('(    other    )  characters  )') == -1


def test_special_unicode_character_input():
    assert parenthetical('  (パイソン) (') == 1
    assert parenthetical('  (パイソン)  ') == 0
    assert parenthetical(') (パイソン)  ') == -1


def test_bad_input():
    with pytest.raises(TypeError):
        parenthetical(123)
