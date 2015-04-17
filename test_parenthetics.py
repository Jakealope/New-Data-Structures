from parenthetics import is_balanced
import pytest
# These are unit tests for the parenthetics.py file


def test_isone():
    assert is_balanced("(") == 1


def test_isneg():
    assert is_balanced(")") == -1


def test_iszero():
    assert is_balanced("( )") == 0
