"""Test for our hash data structure."""
import pytest
import hash

PARAMS_TABLE = [
    ('donuts', 6),
    ('hashy', 'no'),
    ('firefly', 'canceled'),
    ('choochoo', [5, 6, 4, 3]),
    ("mylittlepony", {"isbrony": "ispony"})
]

PARAMS_TABLE_TYPE_ERRORS = [
    (5, ),
    ([], ),
    (True, ),
    ({}, ),
    ((), )
]


@pytest.mark.parametrize("key, value", PARAMS_TABLE)
def test_fnv_key_value(key, value):
    """Test if insertion works correctly."""
    test_table = hash.HashTable(1000)
    test_table.fnv_set(key, value)
    assert test_table.fnv_get(key) == value


@pytest.mark.parametrize("key, value", PARAMS_TABLE)
def test_additive_key_value(key, value):
    """Test if insertion works correctly."""
    test_table = hash.HashTable(100)
    test_table.additive_set(key, value)
    assert test_table.additive_get(key) == value


def test_additive_duplicate_value():
    """Test if insertion works correctly."""
    test_table = hash.HashTable(100)
    test_table.additive_set("key", "value")
    test_table.additive_set("key", "value2")
    assert test_table.additive_get("key") == "value"


def test_fnv_duplicate_value():
    """Test if insertion works correctly."""
    test_table = hash.HashTable(1000)
    test_table.fnv_set("key", "value")
    test_table.fnv_set("key", "value2")
    assert test_table.fnv_get("key") == "value"


@pytest.mark.parametrize("value", PARAMS_TABLE_TYPE_ERRORS)
def test_additive_set_type_error_without_string(value):
    test_table = hash.HashTable(100)
    with pytest.raises(TypeError):
        test_table.additive_set(value, "unicorns")


@pytest.mark.parametrize("value", PARAMS_TABLE_TYPE_ERRORS)
def test_fnv_set_type_error_without_string(value):
    test_table = hash.HashTable(1000)
    with pytest.raises(TypeError):
        test_table.fnv_set(value, "pony")






