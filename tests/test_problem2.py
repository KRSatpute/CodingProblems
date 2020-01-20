"""
test case for problem 2
"""
# pylint: skip-file


import pytest

from problem2_numeronym import match_pattern


def test_pattern_matching():

    input = "technology"

    assert match_pattern(input_str=input, input_pattern="t8y")
    assert match_pattern(input_str=input, input_pattern="t9")
    assert match_pattern(input_str=input, input_pattern="9y")
    assert match_pattern(input_str=input, input_pattern="tech2logy")
    assert match_pattern(input_str=input, input_pattern="8g1")
    assert match_pattern(input_str=input, input_pattern="te2n4y")

    assert not match_pattern(input_str=input, input_pattern="t9y")

    assert match_pattern(input_str="accessibility", input_pattern="a11y")

    assert match_pattern(input_str="internationalization",
                         input_pattern="i18n")
