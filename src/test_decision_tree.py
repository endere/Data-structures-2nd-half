"""Test for our decision tree data frame in pandas."""
import pandas as pd
import pytest

DECISION_PARAMS_TABLE = [
    ([
        [1.5, 0.1, 4.9, 3.1, 0, 'setosa'],
        [1.5, 0.2, 5.4, 3.7, 0, 'setosa'],
        [1.6, 0.2, 4.8, 3.4, 0, 'setosa'],
        [1.4, 0.1, 4.8, 3.0, 0, 'setosa'],
        [1.1, 0.1, 4.3, 3.0, 0, 'setosa'],
        [4.7, 1.5, 6.7, 3.1, 1, 'versicolor'],
        [4.4, 1.3, 6.3, 2.3, 1, 'versicolor'],
        [4.1, 1.3, 5.6, 3.0, 1, 'versicolor'],
        [4.0, 1.3, 5.5, 2.5, 1, 'versicolor'],
        [4.4, 1.2, 5.5, 2.6, 1, 'versicolor']
    ]),
    ((
        (1.5, 0.1, 4.9, 3.1, 0, 'setosa'),
        (1.5, 0.2, 5.4, 3.7, 0, 'setosa'),
        (1.6, 0.2, 4.8, 3.4, 0, 'setosa'),
        (1.4, 0.1, 4.8, 3.0, 0, 'setosa'),
        (1.1, 0.1, 4.3, 3.0, 0, 'setosa'),
        (4.7, 1.5, 6.7, 3.1, 1, 'versicolor'),
        (4.4, 1.3, 6.3, 2.3, 1, 'versicolor'),
        (4.1, 1.3, 5.6, 3.0, 1, 'versicolor'),
        (4.0, 1.3, 5.5, 2.5, 1, 'versicolor'),
        (4.4, 1.2, 5.5, 2.6, 1, 'versicolor')
    )),
    (pd.DataFrame([
        [1.5, 0.1, 4.9, 3.1, 0, 'setosa'],
        [1.5, 0.2, 5.4, 3.7, 0, 'setosa'],
        [1.6, 0.2, 4.8, 3.4, 0, 'setosa'],
        [1.4, 0.1, 4.8, 3.0, 0, 'setosa'],
        [1.1, 0.1, 4.3, 3.0, 0, 'setosa'],
        [4.7, 1.5, 6.7, 3.1, 1, 'versicolor'],
        [4.4, 1.3, 6.3, 2.3, 1, 'versicolor'],
        [4.1, 1.3, 5.6, 3.0, 1, 'versicolor'],
        [4.0, 1.3, 5.5, 2.5, 1, 'versicolor'],
        [4.4, 1.2, 5.5, 2.6, 1, 'versicolor']
    ], columns=['petal length (cm)', 'petal width (cm)', 'sepal length (cm)', 'sepal width (cm)', 'target', 'class_names']))
]

PREDICT_PARAMS_TABLE = [
    ([
        [1.5, 0.1, 4.9, 3.1],
        [1.5, 0.2, 5.4, 3.7],
        [1.6, 0.2, 4.8, 3.4],
        [1.4, 0.1, 4.8, 3.0],
        [1.1, 0.1, 4.3, 3.0],
        [4.7, 1.5, 6.7, 3.1],
        [4.4, 1.3, 6.3, 2.3],
        [4.1, 1.3, 5.6, 3.0],
        [4.0, 1.3, 5.5, 2.5],
        [4.4, 1.2, 5.5, 2.6]
    ]),
    ((
        (1.5, 0.1, 4.9, 3.1),
        (1.5, 0.2, 5.4, 3.7),
        (1.6, 0.2, 4.8, 3.4),
        (1.4, 0.1, 4.8, 3.0),
        (1.1, 0.1, 4.3, 3.0),
        (4.7, 1.5, 6.7, 3.1),
        (4.4, 1.3, 6.3, 2.3),
        (4.1, 1.3, 5.6, 3.0),
        (4.0, 1.3, 5.5, 2.5),
        (4.4, 1.2, 5.5, 2.6)
    )),
    (pd.DataFrame([
        [1.5, 0.1, 4.9, 3.1],
        [1.5, 0.2, 5.4, 3.7],
        [1.6, 0.2, 4.8, 3.4],
        [1.4, 0.1, 4.8, 3.0],
        [1.1, 0.1, 4.3, 3.0],
        [4.7, 1.5, 6.7, 3.1],
        [4.4, 1.3, 6.3, 2.3],
        [4.1, 1.3, 5.6, 3.0],
        [4.0, 1.3, 5.5, 2.5],
        [4.4, 1.2, 5.5, 2.6]
    ], columns=['petal length (cm)', 'petal width (cm)', 'sepal length (cm)', 'sepal width (cm)']))
]


@pytest.mark.parametrize("data", DECISION_PARAMS_TABLE)
def test_question_node_works_correctly(data):
    """Test that question node works correctly with data."""
    pass


@pytest.mark.parametrize("data", DECISION_PARAMS_TABLE)
def test_fit_works_with_decision_tree_list_tuple_df(data):
    """Test that fit works with decision tree on list, tuple and df."""
    pass


@pytest.mark.parametrize("data", DECISION_PARAMS_TABLE)
def test_predict_works_with_decision_tree_list_tuple_df(data):
    """Test that predict works with decision tree on list, tuple and df."""
    pass


@pytest.mark.parametrize("data", DECISION_PARAMS_TABLE)
def test_max_depth_works_correctly(data):
    """Test that max depth works correctly."""
    pass


@pytest.mark.parametrize("data", DECISION_PARAMS_TABLE)
def test_min_leaf_size_works_correctly(data):
    """Test that min leaf size works correctly."""
    pass


