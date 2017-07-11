"""Test suite for sorting algorithms."""
import pytest
import random
import bubblesort

PARAMS_TABLE_INVALID = [
    ('string'),
    (1),
    (False),
    ([3, 'c', 2, 'a']),
    ([3, 2, [1], 4, 5]),
    (['1', 2, 3, 4, 5])
]


def test_bubblesort_already_sorted():
    """Test if bubblesort returns the same list if it is already sorted."""
    assert bubblesort.bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_bubblesort_large_sample():
    """Test if bubblesort works with large list of random numbers."""
    data = random.sample(range(100), 100)
    assert bubblesort.bubble_sort(data) == sorted(data)


def test_bubblesort_small_sample():
    """Test if bubblesort works with small list of random numbers."""
    data = random.sample(range(100), 5)
    assert bubblesort.bubble_sort(data) == sorted(data)


def test_bubblesort_empty_array():
    """Test if bubblesort works when an empty array is passed in."""
    assert bubblesort.bubble_sort([]) == []


def test_bubblesort_duplicate_numbers():
    """Test if bubblesort works when duplicate numbers are passed in."""
    assert bubblesort.bubble_sort([4, 3, 2, 1, 5, 3]) == [1, 2, 3, 3, 4, 5]


@pytest.mark.parametrize("data", PARAMS_TABLE_INVALID)
def test_bubblesort_raises_type_error_with_invalid_input(data):
    """Test if bubblesort works when an invalid input is passed in."""
    with pytest.raises(TypeError):
        bubblesort.bubble_sort(data)
