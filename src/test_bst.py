"""Test definitions for bst."""

import pytest
import bst

PARAMS_TABLE_INSERT = [
    ([5, 6, 3, 4], [5, 6, 3, 4])
]

PARAMS_TABLE_SEARCH = [
    ([5, 6, 3, 4, 0], 5, 5),
    ([10, 5, 20, 35, 7], 20, 20),
]

PARAMS_TABLE_SEARCH_NONE = [
    ([10, 5, 20, 35, 7], 137, None)
]

PARAMS_TABLE_SIZE = [
    ([5, 6, 3], 3),
    ([10, 5, 20, 35, 7], 5),
    ([], 0)
]

PARAMS_TABLE_DEPTH = [
    ([5], 0),
    ([10, 5, 20, 35, 7], 2),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 8),
    ([5, 6, 3], 1),
    ([5, 1], 1)
]

PARAMS_TABLE_CONTAINS = [
    ([5], 5, True),
    ([10, 5, 20, 35, 7], 6, False),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 7, True)
]

PARAMS_TABLE_BALANCE = [
    ([5], 0),
    ([10, 5, 20, 35, 7], 0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 8),
    ([6, 2, 3, 4, 1, 5, 7, 8, 9], -1)
]

PARAMS_TABLE_BREADTH = [
    ([4, 2, 3, 1, 6, 5, 7], [4, 2, 3, 1, 6, 5, 7])
]
PARAMS_TABLE_PREORDER = [
    ([4, 2, 3, 1, 6, 5, 7], [4, 2, 1, 3, 6, 5, 7])
]
PARAMS_TABLE_POSTORDER = [
    ([4, 2, 3, 1, 6, 5, 7], [1, 3, 2, 5, 7, 6, 4])
]
PARAMS_TABLE_INORDER = [
    ([4, 2, 3, 1, 6, 5, 7], [1, 2, 3, 4, 5, 6, 7])
]
@pytest.mark.parametrize("data, results", PARAMS_TABLE_INSERT)
def test_insert(data, results):
    """Test if insertion works correctly."""
    test_tree = bst.Binary_Search_Tree()
    assert test_tree.root is None
    for i in data:
        test_tree.insert(i)
    assert test_tree.root.value == results[0]
    assert test_tree.root.right.value == results[1]
    assert test_tree.root.left.value == results[2]
    assert test_tree.root.left.right.value == results[3]


@pytest.mark.parametrize("data, search_for_me, result", PARAMS_TABLE_SEARCH)
def test_search(data, search_for_me, result):
    """Test if search works correctly."""
    test_tree = bst.Binary_Search_Tree()
    for i in data:
        test_tree.insert(i)
    assert test_tree.search(search_for_me).value == result


@pytest.mark.parametrize("data, search_for_me, result", PARAMS_TABLE_SEARCH_NONE)
def test_search(data, search_for_me, result):
    """Test if search works correctly."""
    test_tree = bst.Binary_Search_Tree()
    for i in data:
        test_tree.insert(i)
    assert test_tree.search(search_for_me) == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_SIZE)
def test_size(data, result):
    """Test if size works correctly."""
    test_tree = bst.Binary_Search_Tree()
    for i in data:
        test_tree.insert(i)
    assert test_tree.size() == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_DEPTH)
def test_depth(data, result):
    """Test if depth works correctly."""
    test_tree = bst.Binary_Search_Tree()
    for i in data:
        test_tree.insert(i)
    assert test_tree.depth() == result


@pytest.mark.parametrize("data, contains_me, result", PARAMS_TABLE_CONTAINS)
def test_contains(data, contains_me, result):
    """Test if contains works correctly."""
    test_tree = bst.Binary_Search_Tree()
    for i in data:
        test_tree.insert(i)
    assert test_tree.contains(contains_me) == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_BALANCE)
def test_balance(data, result):
    """Test if balance works correctly."""
    test_tree = bst.Binary_Search_Tree()
    for i in data:
        test_tree.insert(i)
    assert test_tree.balance() == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_BREADTH)
def test_breadth_first(data, result):
    """test breadth first"""
    test_tree = bst.Binary_Search_Tree(data)
    assert test_tree.breadth_first() == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_PREORDER)
def test_pre_order(data, result):
    """test breadth first"""
    test_tree = bst.Binary_Search_Tree(data)
    assert test_tree.pre_order() == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_POSTORDER)
def test_post_order(data, result):
    """test breadth first"""
    test_tree = bst.Binary_Search_Tree(data)
    assert test_tree.post_order() == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_INORDER)
def test_in_order(data, result):
    """test breadth first"""
    test_tree = bst.Binary_Search_Tree(data)
    assert test_tree.in_order() == result