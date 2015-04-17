from parenthetics import isBalanced
import pytest
# These are unit tests for the parenthetics.py file


def test_isone():
    assert isBalanced("(") == 1


def test_isneg():
    assert isBalanced(")") == -1


def test_iszero():
    assert isBalanced("( )") == 0
