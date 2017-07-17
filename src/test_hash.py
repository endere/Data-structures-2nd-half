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
    """Test if insertion works correctly with the fnv hash."""
    test_table = hash.HashTable(1000)
    test_table.set(key, value)
    assert test_table.get(key) == value


@pytest.mark.parametrize("key, value", PARAMS_TABLE)
def test_additive_key_value(key, value):
    """Test if insertion works correctly with the additive hash."""
    test_table = hash.HashTable(1000, 'add')
    test_table.set(key, value)
    assert test_table.get(key) == value


def test_additive_get_not__there():
    """Test if get returns none with additive hash."""
    test_table = hash.HashTable(1000, 'add')
    assert test_table.get('test') is None


def test_fnv_get_not__there():
    """Test if get returns none with fnv hash."""
    test_table = hash.HashTable(1000)
    assert test_table.get('test') is None


def test_additive_duplicate_value():
    """Test if values with duplicate keys are not stored with additive hash."""
    test_table = hash.HashTable(1000, 'add')
    test_table.set("key", "value")
    test_table.set("key", "value2")
    assert test_table.get("key") == "value"


def test_fnv_duplicate_value():
    """Test if values with duplicate keys are not stored with fnv hash."""
    test_table = hash.HashTable(1000)
    test_table.set("key", "value")
    test_table.set("key", "value2")
    assert test_table.get("key") == "value"


@pytest.mark.parametrize("value", PARAMS_TABLE_TYPE_ERRORS)
def test_additive_set_type_error_without_string(value):
    """Test function raises an error when a non-string is inserted in additive hash."""
    test_table = hash.HashTable(1000, 'add')
    with pytest.raises(TypeError):
        test_table.set(value, "unicorns")


@pytest.mark.parametrize("value", PARAMS_TABLE_TYPE_ERRORS)
def test_fnv_set_type_error_without_string(value):
    """Test function raises an error when a non-string is inserted in fnv hash."""
    test_table = hash.HashTable(1000)
    with pytest.raises(TypeError):
        test_table.set(value, "pony")


# def test_with_huge_database_fnv():
#     """Import a gigantic dictionary and asserts that it works properly in fnv hash."""
#     test_table = hash.HashTable(1000)
#     with open('/usr/share/dict/words') as dictionary:
#         data = dictionary.read()
#         data = data.split('\n')
#     if len(data) > 100000:
#         data = data[:100000]
#     for i in range(len(data)):
#         test_table.set(data[i], data[i])
#     assert test_table.get('dinosaur') == 'dinosaur'
#     assert test_table.get("qwertyuiop") is None


# def test_with_huge_database_additive():
#     """Import a gigantic dictionary and asserts that it works properly in additive hash."""
#     test_table = hash.HashTable(1000, 'add')
#     with open('/usr/share/dict/words') as dictionary:
#         data = dictionary.read()
#         data = data.split('\n')
#     if len(data) > 100000:
#         data = data[:100000]
#     for i in range(len(data)):
#         test_table.set(data[i], data[i])
#     assert test_table.get('dinosaur') == 'dinosaur'
#     assert test_table.get("qwertyuiop") is None
