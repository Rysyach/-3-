import pytest
from lib import get_min, get_max, get_sum, get_multiply, prepare_lines
from main import run
import datetime
import numpy as np


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
    ([], None)
])
def test_get_sum(test_data, expected):
    assert get_sum(test_data) == expected


@pytest.mark.parametrize("test_data, expected", [
    ([1, 2, 3], 6),
    ([-1, -2, -3], -6),
    ([], None)
])
def test_get_multiply(test_data, expected):
    assert get_multiply(test_data) == expected


@pytest.mark.parametrize("test_data, expected", [
    (["1", "2 3", "4"], [1, 2, 3, 4]),
    (["a1", "2", "3"], [2, 3]),
    (["", "2", " 3", "10"], [2, 3, 10]),
    ([], [])
])
def test_prepare_lines(test_data, expected):
    assert prepare_lines(test_data) == expected


def test_performance():
    test_data = np.random.randint(1, 10, 5)
    start = datetime.datetime.now()
    get_sum(test_data)
    finish = datetime.datetime.now()
    result_1 = finish - start

    test_data = np.random.randint(1, 10, 5000)
    start = datetime.datetime.now()
    get_sum(test_data)
    finish = datetime.datetime.now()
    result_2 = finish - start
    assert result_2 > result_1
