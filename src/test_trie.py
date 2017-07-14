import trie
import pytest



PARAMS_TABLE_INSERT = [
    ('fir', ['f', 'i', 'r']),
    ('fox', ['f', 'o', 'x']),
    ('fae', ['f', 'a', 'e'])
]





@pytest.mark.parametrize("data, results", PARAMS_TABLE_INSERT)
def test_insert_single_word(data, results):
    """Test if insertion works correctly."""
    test_tree = trie.TrieTree()
    test_tree.insert(data)
    assert test_tree.root.next_list[0].value == results[0]
    assert test_tree.root.next_list[0].end is False
    assert test_tree.root.next_list[0].next_list[0].value == results[1]
    assert test_tree.root.next_list[0].next_list[0].end is False
    assert test_tree.root.next_list[0].next_list[0].next_list[0].value == results[2]
    assert test_tree.root.next_list[0].next_list[0].next_list[0].end is True

def test_insert_duplicate():
    """Test if insertion works correctly."""
    test_tree = trie.TrieTree()
    test_tree.insert('twin')
    test_tree.insert('twin')
    assert len(test_tree.root.next_list) == 1

def test_insert_branching():
    """Test if insertion works correctly."""
    test_tree = trie.TrieTree()
    test_tree.insert('fir')
    test_tree.insert('fae')
    assert len(test_tree.root.next_list) == 1
    assert len(test_tree.root.next_list[0].next_list) == 2

