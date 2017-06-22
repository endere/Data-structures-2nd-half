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
    ([4, 2, 3, 1, 6, 5, 7], [4, 2, 6, 1, 3, 5, 7]),
    ([75, 97, 40, 7, 48, 65, 83, 27, 38, 1, 16, 86, 87, 100, 47, 53, 55, 54], [75, 40, 97, 7, 48, 83, 100, 1, 27, 47, 65, 86, 16, 38, 53, 87, 55, 54])
]
PARAMS_TABLE_PREORDER = [
    ([4, 2, 3, 1, 6, 5, 7], [4, 2, 1, 3, 6, 5, 7]),
    ([75, 97, 40, 7, 48, 65, 83, 27, 38, 1, 16, 86, 87, 100, 47, 53, 55, 54], [75, 40, 7, 1, 27, 16, 38, 48, 47, 65, 53, 55, 54, 97, 83, 86, 87, 100])
]
PARAMS_TABLE_POSTORDER = [
    ([4, 2, 3, 1, 6, 5, 7], [1, 3, 2, 5, 7, 6, 4]),
    ([75, 97, 40, 7, 48, 65, 83, 27, 38, 1, 16, 86, 87, 100, 47, 53, 55, 54], [1, 16, 38, 27, 7, 47, 54, 55, 53, 65, 48, 40, 87, 86, 83, 100, 97, 75])
]
PARAMS_TABLE_INORDER = [
    ([4, 2, 3, 1, 6, 5, 7], [1, 2, 3, 4, 5, 6, 7]),
    ([75, 97, 40, 7, 48, 65, 83, 27, 38, 1, 16, 86, 87, 100, 47, 53, 55, 54], [1, 7, 16, 27, 38, 40, 47, 48, 53, 54, 55, 65, 75, 83, 86, 87, 97, 100])
]
PARAMS_TABLE_DELETION = [
    ([4, 2, 3, 1, 6, 5, 7], 6, [4, 2, 6, 1, 3, 5, 7]),
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
    test_tree = bst.Binary_Search_Tree()
    for i in data:
        test_tree.insert(i)
    test_array = []
    test_generator = test_tree.breadth_first()
    while len(test_array) < test_tree.size():
        test_array.append(next(test_generator))
    assert test_array == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_PREORDER)
def test_pre_order(data, result):
    """test pre_order."""
    test_tree = bst.Binary_Search_Tree()
    for i in data:
        test_tree.insert(i)
    test_array = []
    test_generator = test_tree.pre_order()
    while len(test_array) < test_tree.size():
        test_array.append(next(test_generator))
    assert test_array == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_POSTORDER)
def test_post_order(data, result):
    """test post_order"""
    test_tree = bst.Binary_Search_Tree()
    for i in data:
        print(i)
        test_tree.insert(i)
    test_array = []
    test_generator = test_tree.post_order()
    while len(test_array) < test_tree.size():
        # import pdb; pdb.set_trace()
        test_array.append(next(test_generator))
    print('result is ', result)
    print('test_array is ', test_array)
    assert test_array == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_INORDER)
def test_in_order(data, result):
    """test in_order"""
    test_tree = bst.Binary_Search_Tree()
    for i in data:
        test_tree.insert(i)
    # import pdb; pdb.set_trace()
    test_array = []
    test_generator = test_tree.in_order()
    while len(test_array) < test_tree.size():
        test_array.append(next(test_generator))
    assert test_array == result