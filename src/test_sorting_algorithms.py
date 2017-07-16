"""Test suite for sorting algorithms."""
import pytest
import random
import bubblesort
import bogosort
import insertionsort

PARAMS_TABLE_INVALID = [
    ('string'),
    (1),
    (False),
    ([3, 'c', 2, 'a']),
    ([3, 2, [1], 4, 5]),
    (['1', 2, 3, 4, 5])
]

PARAMS_TABLE_FUNCTIONS = [
    (bubblesort.bubble_sort),
    (bogosort.bogo_sort),
    (insertionsort.insertion_sort)
]


@pytest.mark.parametrize("function", PARAMS_TABLE_FUNCTIONS)
def test_already_sorted(function):
    """Test if algorithm returns the same list if it is already sorted."""
    assert function([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize("function", PARAMS_TABLE_FUNCTIONS)
def test_large_sample(function):
    """Test if algorithm works with large list of random numbers."""
    data = random.sample(range(100), 100)
    if function is not bogosort.bogo_sort:
        assert function(data) == sorted(data)


@pytest.mark.parametrize("function", PARAMS_TABLE_FUNCTIONS)
def test_small_sample(function):
    """Test if algorithm works with small list of random numbers."""
    data = random.sample(range(100), 5)
    assert function(data) == sorted(data)


@pytest.mark.parametrize("function", PARAMS_TABLE_FUNCTIONS)
def test_empty_array(function):
    """Test if algorithm works when an empty array is passed in."""
    assert function([]) == []


@pytest.mark.parametrize("function", PARAMS_TABLE_FUNCTIONS)
def test_duplicate_numbers(function):
    """Test if algorithm works when duplicate numbers are passed in."""
    assert function([4, 3, 2, 1, 5, 3]) == [1, 2, 3, 3, 4, 5]


@pytest.mark.parametrize("function", PARAMS_TABLE_FUNCTIONS)
def test_raises_type_error_with_invalid_input(function):
    """Test if algorithm works when an invalid input is passed in."""
    for data in PARAMS_TABLE_INVALID:
        with pytest.raises(TypeError):
            function(data)
