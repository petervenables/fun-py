"""Tests for finding non-duplicate numbers in a sorted list."""

import pytest
from src.non_dupes.find_non_duplicates import FindNonDuplicates


@pytest.mark.parametrize(
    "arr, result",
    [
        ([1, 1, 2], [1, 2, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]),
        ([2, 3, 3, 3, 6, 9, 9], [2, 3, 6, 9, 6, 9, 9]),
        ([1], [1])
    ],
)
def test_non_dupes(arr, result):
    """Test finding non-duplicate numbers in a sorted list."""
    fnd = FindNonDuplicates()
    output = fnd.moveElements(arr)
    assert output == result
