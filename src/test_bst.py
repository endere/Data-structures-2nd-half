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
    ([10, 5, 20, 35, 7], 137, None),
    ([], 137, None)
]

PARAMS_TABLE_SIZE = [
    ([5, 6, 3], 3),
    ([10, 5, 20, 35, 7], 5),
    ([], 0),
    ([1], 1)
]

PARAMS_TABLE_DEPTH = [
    ([5], 1),
    ([10, 5, 20, 35, 7], 3),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 4),
    ([5, 6, 3], 2),
    ([5, 1], 2)
]

PARAMS_TABLE_CONTAINS = [
    ([5], 5, True),
    ([10, 5, 20, 35, 7], 6, False),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 7, True)
]

PARAMS_TABLE_BALANCE = [
    ([], 0),
    ([5], 0),
    ([10, 5, 20, 35, 7], 0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1),
    ([6, 2, 3, 4, 1, 5, 7, 8, 9], 1)
]

PARAMS_TABLE_BREADTH = [
    ([], []),
    ([4, 2, 3, 1, 6, 5, 7], [3, 2, 5, 1, 4, 6, 7]),
    ([75, 97, 40, 7, 48, 65, 83, 27, 38, 1, 16, 86, 87, 100, 47, 53, 55, 54], [48, 27, 86, 7, 40, 55, 97, 1, 16, 38, 47, 53, 75, 87, 100, 54, 65, 83])
]

PARAMS_TABLE_PREORDER = [
    ([], []),
    ([4, 2, 3, 1, 6, 5, 7], [3, 2, 1, 5, 4, 6, 7]),
    ([75, 97, 40, 7, 48, 65, 83, 27, 38, 1, 16, 86, 87, 100, 47, 53, 55, 54], [48, 27, 7, 1, 16, 40, 38, 47, 86, 55, 53, 54, 75, 65, 83, 97, 87, 100])
]

PARAMS_TABLE_POSTORDER = [
    ([], []),
    ([4, 2, 3, 1, 6, 5, 7], [1, 2, 4, 7, 6, 5, 3]),
    ([75, 97, 40, 7, 48, 65, 83, 27, 38, 1, 16, 86, 87, 100, 47, 53, 55, 54], [1, 16, 7, 38, 47, 40, 27, 54, 53, 65, 83, 75, 55, 87, 100, 97, 86, 48])
]

PARAMS_TABLE_INORDER = [
    ([], []),
    ([4, 2, 3, 1, 6, 5, 7], [1, 2, 3, 4, 5, 6, 7]),
    ([75, 97, 40, 7, 48, 65, 83, 27, 38, 1, 16, 86, 87, 100, 47, 53, 55, 54], [1, 7, 16, 27, 38, 40, 47, 48, 53, 54, 55, 65, 75, 83, 86, 87, 97, 100])
]
PARAMS_TABLE_ITERABLES = [
    ((4, 2, 3, 1, 6, 5, 7), [1, 2, 3, 4, 5, 6, 7]),
    (([1]), ([1])),
    (({5: 5}), ([])),
    (("Strings are iterables too."), ([])),
    ([75, 97, 40, 7, 48, 65, 83, 27, 38, 1, 16, 86, 87, 100, 47, 53, 55, 54], [1, 7, 16, 27, 38, 40, 47, 48, 53, 54, 55, 65, 75, 83, 86, 87, 97, 100])
]

PARAMS_TABLE_DELETION = [
    ([1, 2], 1, [2]),
    ([2, 1], 2, [1]),
    ([1], 1, []),
    ([1], 9, [1]),
    ([], 9, []),
    ([40, 60, 20, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75], 20, [5, 10, 15, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]),
    ([8, 4, 12, 10, 14, 2, 6, 3], 4, [2, 3, 6, 8, 10, 12, 14]),
    ([8, 4, 12, 10, 14, 2, 6, 11], 12, [2, 4, 6, 8, 10, 11, 14]),
    ([4, 2, 6, 5], 6, [2, 4, 5]),
    ([4, 2, 3, 1, 6, 5, 7], 1, [2, 3, 4, 5, 6, 7]),
    ([4, 2, 3, 1, 6, 5, 7], 2, [1, 3, 4, 5, 6, 7]),
    ([4, 2, 3, 1, 6, 5, 7], 3, [1, 2, 4, 5, 6, 7]),
    ([4, 2, 3, 1, 6, 5, 7], 4, [1, 2, 3, 5, 6, 7]),
    ([4, 2, 3, 1, 6, 5, 7], 5, [1, 2, 3, 4, 6, 7]),
    ([4, 2, 3, 1, 6, 5, 7], 6, [1, 2, 3, 4, 5, 7]),
    ([4, 2, 3, 1, 6, 5, 7], 7, [1, 2, 3, 4, 5, 6]),
    ([4, 2, 3, 1, 6, 5, 7], 8, [1, 2, 3, 4, 5, 6, 7]),
    ([75, 97, 40, 7, 48, 65, 83, 27, 38, 1, 16, 86, 87, 100, 47, 53, 55, 54], 48, [1, 7, 16, 27, 38, 40, 47, 53, 54, 55, 65, 75, 83, 86, 87, 97, 100])
]

PARAMS_TABLE_NAN = [
    ("test"),
    # (True),
    ([1, 2, 3]),
    ({'a key': 'a value'})
]


@pytest.mark.parametrize("data, results", PARAMS_TABLE_INSERT)
def test_insert(data, results):
    """Test if insertion works correctly."""
    test_tree = bst.BinarySearchTree()
    assert test_tree.root is None
    for i in data:
        test_tree.insert(i)
    assert test_tree.root.value == results[0]
    assert test_tree.root.right.value == results[1]
    assert test_tree.root.left.value == results[2]
    assert test_tree.root.left.right.value == results[3]


@pytest.mark.parametrize("data, result", PARAMS_TABLE_ITERABLES)
def test_set_up_tree_with_iterables(data, result):
    """Test if tree properly loads with different iterables given as arguements."""
    test_tree = bst.BinarySearchTree(data)
    test_array = []
    test_generator = test_tree.in_order()
    while len(test_array) < test_tree.size():
        test_array.append(next(test_generator))
    assert test_array == result


@pytest.mark.parametrize("data, search_for_me, result", PARAMS_TABLE_SEARCH)
def test_search(data, search_for_me, result):
    """Test if search works correctly."""
    test_tree = bst.BinarySearchTree(data)
    assert test_tree.search(search_for_me).value == result


@pytest.mark.parametrize("data, search_for_me, result", PARAMS_TABLE_SEARCH_NONE)
def test_search_not_there(data, search_for_me, result):
    """Test if search works correctly."""
    test_tree = bst.BinarySearchTree(data)
    assert test_tree.search(search_for_me) == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_SIZE)
def test_size(data, result):
    """Test if size works correctly."""
    test_tree = bst.BinarySearchTree(data)
    print(test_tree.size())
    assert test_tree.size() == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_DEPTH)
def test_depth(data, result):
    """Test if depth works correctly."""
    test_tree = bst.BinarySearchTree(data)
    assert test_tree.depth() == result


@pytest.mark.parametrize("data, contains_me, result", PARAMS_TABLE_CONTAINS)
def test_contains(data, contains_me, result):
    """Test if contains works correctly."""
    test_tree = bst.BinarySearchTree(data)
    assert test_tree.contains(contains_me) == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_BALANCE)
def test_balance(data, result):
    """Test if balance works correctly."""
    test_tree = bst.BinarySearchTree(data)
    assert test_tree.balance() == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_BREADTH)
def test_breadth_first(data, result):
    """Test breadth first."""
    test_tree = bst.BinarySearchTree(data)
    test_array = []
    test_generator = test_tree.breadth_first()
    while len(test_array) < test_tree.size():
        test_array.append(next(test_generator))
    assert test_array == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_BREADTH)
def test_breadth_first_for_loop(data, result):
    """Test breadth first called with a loop in a list."""
    test_tree = bst.BinarySearchTree(data)
    test_array = [i for i in test_tree.breadth_first()]
    assert test_array == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_PREORDER)
def test_pre_order(data, result):
    """Test pre_order."""
    test_tree = bst.BinarySearchTree(data)
    test_array = []
    test_generator = test_tree.pre_order()
    while len(test_array) < test_tree.size():
        test_array.append(next(test_generator))
    assert test_array == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_PREORDER)
def test_pre_order_for_loop(data, result):
    """Test pre_order called with a loop in a list."""
    test_tree = bst.BinarySearchTree(data)
    test_array = [i for i in test_tree.pre_order()]
    assert test_array == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_POSTORDER)
def test_post_order(data, result):
    """Test post_order."""
    test_tree = bst.BinarySearchTree(data)
    test_array = []
    test_generator = test_tree.post_order()
    while len(test_array) < test_tree.size():
        test_array.append(next(test_generator))
    assert test_array == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_POSTORDER)
def test_post_order_for_loop(data, result):
    """Test post_order called with a loop in a list."""
    test_tree = bst.BinarySearchTree(data)
    test_array = [i for i in test_tree.post_order()]
    assert test_array == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_INORDER)
def test_in_order(data, result):
    """Test in_order."""
    test_tree = bst.BinarySearchTree(data)
    test_array = []
    test_generator = test_tree.in_order()
    while len(test_array) < test_tree.size():
        test_array.append(next(test_generator))
    assert test_array == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_INORDER)
def test_in_order_for_loop(data, result):
    """Test in_order called with a loop in a list."""
    test_tree = bst.BinarySearchTree(data)
    test_array = [i for i in test_tree.in_order()]
    assert test_array == result


@pytest.mark.parametrize("data, delete_me, result", PARAMS_TABLE_DELETION)
def test_deletion(data, delete_me, result):
    """Test if deletion works correctly."""
    test_tree = bst.BinarySearchTree(data)
    test_tree.deletion(delete_me)
    test_array = []
    test_generator = test_tree.in_order()
    while len(test_array) < test_tree.size():
        test_array.append(next(test_generator))
    assert test_array == result


def test_self_balancing():
    """Create 20 random trees of 50 numbers and check that they are self balancing."""
    import random
    for i in range(20):
        data = random.sample(range(1, 100), 50)
        test_tree = bst.BinarySearchTree(data)
        assert test_tree.balance() >= -1
        assert test_tree.balance() <= 1


def test_self_balancing_with_deletion():
    """Create 20 random trees of 50 numbers and check that they are self balancing, even after deletion."""
    import random
    for i in range(20):
        data = random.sample(range(1, 100), 50)
        test_tree = bst.BinarySearchTree(data)
        test_tree.deletion(data[10])
        assert test_tree.balance() >= -1
        assert test_tree.balance() <= 1


def test_tree_always_retains_proper_nodes_when_one_is_deleted():
    """Create 10x99 random trees of varying numbers and check that no numbers are accidentally dropped upon deletion.

    Also used to hit edge cases we may not be able to come up with.
    This test faces errors when i iterates above 100. It is a nested
    for loop to ensure 100% coverage, though the code still has 98-100%
    with only the lower loop. Random chance determines which edge cases it hits.
    """
    import random
    for x in range(10):
        for i in range(99):
            data = random.sample(range(1, 100), i + 1)
            test_tree = bst.BinarySearchTree(data)
            num = random.randint(0, i)
            test_tree.deletion(data[num])
            del data[num]
            test_array = []
            test_generator = test_tree.in_order()
            while len(test_array) < test_tree.size():
                test_array.append(next(test_generator))
            assert test_array == sorted(data)


# @pytest.mark.parametrize("data", PARAMS_TABLE_NAN)
# def test_inserting_not_a_number(data):
#     """Check if tree raises a keyerror when something that is not a number is inserted."""
#     test_tree = bst.BinarySearchTree()
#     with pytest.raises(TypeError):
#         test_tree.insert(data)


# def test_inserting_duplicate_number():
#     """Check if tree raises a value error when a duplicate node is inserted."""
#     test_tree = bst.BinarySearchTree()
#     test_tree.insert(4)
#     with pytest.raises(ValueError):
#         test_tree.insert(4)
