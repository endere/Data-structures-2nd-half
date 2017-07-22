"""Our decision tree data structure."""
import pandas as pd 


class DecisionTree(object):
    """."""

    def __init__(self, max_depth=10, max_leaf_size=10):
        """."""
        pass

    def fit(self, data):
        """construct a decision tree based on some incoming data set; returns nothing."""
        print(data)

    def predict(self, data):
        """returns labels for your test data."""
        pass


if __name__ == '__main__':
    dimitri = DecisionTree()
    df = pd.read_csv("flowers_data.csv")
    dimitri.fit(df)
