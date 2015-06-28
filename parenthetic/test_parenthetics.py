from __future__ import unicode_literals
import pytest
from parenthetics import parenthetical


#  Case that should return -1
broken_case = [
    "))sdf)as((43215("
    ")tqw()3",
    "345a)))",
    "eq()()q()hq()(hqre[][][]{()))",
    ")dfh",
    "ehu{()()())()()()()",
    "({})()()()()))asdg(())asgwq)()321t5(((()12fds"]

#  Case that should return 1
open_case = [
    "!@#^$#&(324643)(",
    "()asdgw()(@!#&^$#&)(",
    "13246((()asd()oigo",
    "$@*-=()()(",
    "(qy1235)()(qwet)((",
    "()()((3461(()25()153()145"
]

#  Case that should return 0
okay_case = [
    "(1266)()32164()!$#^%@&()|||",
    "((qwet)qwet)",
    "(52135(()1231())()q143265123()())"
]

#  Types that should fail with TypeError
bad_types = [
    0,
    None,
    5.32324,
    {1: 123123, "a": 45243},
    [1, 2, 3, 4, 5]
]


def test_broken_case_via_assert(broken_case=broken_case):
    """
    Testing a set of arguments that should return -1
    """
    for case in broken_case:
        assert parenthetical(case) == -1


def test_open_case_via_assert(open_case=open_case):
    """
    Testing a set of arguments that should return 1
    """
    for case in open_case:
        assert parenthetical(case) == 1


def test_okay_case_via_assert(okay_case=okay_case):
    """
    Testing a set of arguments that should return 1
    """
    for case in okay_case:
        assert parenthetical(case) == 0


def test_bad_types(bad_types=bad_types):
    """
    Testing types that are not currently supported by parenthetical;
    these will raise TypeError
    """
    for bad_type in bad_types:
        with pytest.raises(TypeError):
            parenthetical(bad_type)
