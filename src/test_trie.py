"""Test for our trie tree."""
import trie
import pytest


PARAMS_TABLE_INSERT = [
    ('fir', ['f', 'i', 'r']),
    ('fox', ['f', 'o', 'x']),
    ('fae', ['f', 'a', 'e'])
]


@pytest.mark.parametrize("data, results", PARAMS_TABLE_INSERT)
def test_insert_single_word(data, results):
    """Test if insertion works correctly for a single word."""
    test_tree = trie.TrieTree()
    test_tree.insert(data)
    assert test_tree.root.next_list[0].value == results[0]
    assert test_tree.root.next_list[0].end is False
    assert test_tree.root.next_list[0].next_list[0].value == results[1]
    assert test_tree.root.next_list[0].next_list[0].end is False
    assert test_tree.root.next_list[0].next_list[0].next_list[0].value == results[2]
    assert test_tree.root.next_list[0].next_list[0].next_list[0].end is True


def test_insert_duplicate():
    """Test if insertion works correctly for duplicate words."""
    test_tree = trie.TrieTree()
    test_tree.insert('twin')
    test_tree.insert('twin')
    assert len(test_tree.root.next_list) == 1


def test_insert_branching():
    """Test if insertion works correctly when branching."""
    test_tree = trie.TrieTree()
    test_tree.insert('fir')
    test_tree.insert('fae')
    assert len(test_tree.root.next_list) == 1
    assert len(test_tree.root.next_list[0].next_list) == 2


def test_insert_invalid():
    """Test if insertion works correctly when invalid."""
    test_tree = trie.TrieTree()
    with pytest.raises(TypeError):
        test_tree.remove(2)


def test_insert_empty_string():
    """Test if insertion works correctly with empty string."""
    test_tree = trie.TrieTree()
    with pytest.raises(IndexError):
        test_tree.remove('')


def test_contains_is_in_tree():
    """Test if contains work correctly for string in tree."""
    test_tree = trie.TrieTree()
    test_tree.insert('fir')
    test_tree.insert('fae')
    test_tree.insert('fox')
    assert test_tree.contains('fox')


def test_contains_not_in_tree():
    """Test if contains work correctly for string not in tree."""
    test_tree = trie.TrieTree()
    test_tree.insert('fir')
    test_tree.insert('fae')
    test_tree.insert('fox')
    assert test_tree.contains('forest') is False


def test_remove_in_tree():
    """Test if contains work correctly for removing string in tree."""
    test_tree = trie.TrieTree()
    test_tree.insert('fir')
    test_tree.insert('fae')
    test_tree.insert('fox')
    assert test_tree.contains('fox') is True
    test_tree.remove('fox')
    assert test_tree.contains('fox') is False


def test_remove_only_removes_endpoint_when_letters_have_children():
    """Test remove only removes endpoint when letters have children."""
    test_tree = trie.TrieTree()
    test_tree.insert('fir')
    test_tree.insert('fae')
    test_tree.insert('faerie')
    test_tree.insert('fox')
    assert test_tree.contains('fae') is True
    test_tree.remove('fae')
    assert test_tree.contains('fae') is False
    assert test_tree.contains('faerie')


def test_remove_not_in_tree():
    """Test remove works correctly when word is not in tree."""
    test_tree = trie.TrieTree()
    test_tree.insert('fir')
    test_tree.insert('faerie')
    test_tree.insert('fox')
    with pytest.raises(IndexError):
        test_tree.remove('fae')
    with pytest.raises(IndexError):
        test_tree.remove('forest')


def test_size():
    """Test if size works correctly."""
    test_tree = trie.TrieTree()
    assert test_tree.size() == 0
    test_tree.insert('fir')
    test_tree.insert('faerie')
    test_tree.insert('fox')
    assert test_tree.size() == 3
    test_tree.remove('fox')
    assert test_tree.size() == 2


def test_traversal_from_single_letter():
    """Test if traversal of a single letters works correctly."""
    test_tree = trie.TrieTree()
    test_list = ['fae', 'fir', 'faerie', 'fox', 'forest']
    for i in test_list:
        test_tree.insert(i)
    traversal_list = [i for i in test_tree.traversal('f')]
    for i in test_list:
        assert i in traversal_list
    assert len(test_list) == len(traversal_list)


def test_traversal_from_multiple_letters():
    """Test if traversal of multiple letters works correctly."""
    test_tree = trie.TrieTree()
    test_list = ['fae', 'fir', 'faerie', 'fox', 'forest']
    for i in test_list:
        test_tree.insert(i)
    traversal_list = [i for i in test_tree.traversal('fae')]
    test_list = ['fae', 'faerie']
    for i in test_list:
        assert i in traversal_list
    assert len(test_list) == len(traversal_list)


def test_trie_with_huge_database():
    """Import a gigantic dictionary and asserts that it works properly in trie tree."""
    test_tree = trie.TrieTree()
    with open('/usr/share/dict/words') as dictionary:
        data = dictionary.read()
        data = data.split('\n')
    if len(data) > 100000:
        data = data[:100000]
    for i in range(len(data)):
        test_tree.insert(data[i])
    assert test_tree.contains('dinosaur')
    test_tree.remove('dinosaur')
    assert test_tree.contains('dinosaurs')
    assert test_tree.contains('dinosaur') is False
