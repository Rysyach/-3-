import pytest
import sys
from lib import get_min, get_max, get_sum, get_multiply, prepare_lines


@pytest.mark.parametrize("test_data, expected", [
    ([1, 2, 3], 1),
    ([-1, -2, -3], -3),
    ([1], 1),
    ([], None)
])
def test_get_min(test_data, expected):
    assert get_min(test_data) == expected


@pytest.mark.parametrize("test_data, expected", [
    ([1, 2, 3], 3),
    ([-1, -2, -3], -1),
    ([1], 1),
    ([], None)
])
def test_get_max(test_data, expected):
    assert get_max(test_data) == expected


@pytest.mark.parametrize("test_data, expected", [
    ([1, 2, 3], 6),
    ([-1, -2, -3], -6),
    ([], 0)
])
def test_get_sum(test_data, expected):
    assert get_sum(test_data) == expected


@pytest.mark.parametrize("test_data, expected", [
    ([1, 2, 3], 6),
    ([-1, -2, -3], -6),
    ([], 0)
])
def test_get_multiply(test_data, expected):
    assert get_multiply(test_data) == expected


@pytest.mark.parametrize("test_data, expected", [
    (["1", "2 3", "4"], [1, 2, 3, 4]),
    (["a1", "2", "3"], [2, 3]),
    ([], [])
])
def test_prepare_lines(test_data, expected):
    assert prepare_lines(test_data) == expected
