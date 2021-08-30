from marge_sort.marge_sort import merge_sort
import pytest


@pytest.mark.parametrize(
    "input,expected_value",
    [
        ([8, 4, 23, 42, 16, 15], [4, 8, 15, 16, 23, 42]),
        ([20, 18, 12, 8, 5, -2], [-2, 5, 8, 12, 18, 20]),
        ([5, 12, 7, 5, 5, 7], [5, 5, 5, 7, 7, 12]),
        ([2, 3, 5, 7, 13, 11], [2, 3, 5, 7, 11, 13]),
    ],
)
def test_sort(input, expected_value):
    temp = input
    merge_sort(temp)
    assert temp == expected_value
