"""Our decision tree data structure."""
import pandas as pd


class QuestionNode(object):
    """Class for our question node."""

    def __init__(self, axis, amount, result_one, result_two):
        """Initializer for question node."""
        self.axis = axis
        self.amount = amount
        self.result_one = result_one
        self.result_two = result_two

    def __call__(self, data):
        """When you call a class object it calls as the function."""
        if data[self.axis] > self.amount:
            return self.result_one if type(self.result_one) == str else self.result_one(data)
        else:
            return self.result_two if type(self.result_two) == str else self.result_two(data)


class DecisionTree(object):
    """Class for our decision tree."""

    def __init__(self, max_depth=10, max_leaf_size=10):
        """."""
        self.root = None
        self.max_depth = max_depth
        self.max_leaf_size = max_leaf_size

    def predict(self, data):
        """Return labels for your test data."""
        to_return = []
        for i in data:
            to_return.append(self.root(i))
        return to_return

    def _cut_helper(self, data, axis, amount):
        """Helper function for our fit function."""
        # return the amount of both types on each side
        left_side = []
        right_side = []
        for i in data:
            print(i)
        #     if i[axis] < amount:
        #         left_side.append(data["target"][i])
        #     else:
        #         right_side.append(data["target"][i])
        # return (left_side, right_side)

    def fit(self, data):
        """A decision tree based on some incoming data set; returns nothing."""
        if type(data) == str or type(data) == tuple:
            smallest_length = min([i[0] for i in data])
            biggest_length = max([i[0] for i in data])
        else:
            smallest_length = data["petal length (cm)"].min()
            biggest_length = data["petal length (cm)"].max()
        for i in range(int(smallest_length * 10), int(biggest_length * 10)):
            print(self._cut_helper(data, "petal length (cm)", i / 10))
        print(smallest_length)
        print(biggest_length)
        # print([i[0] for i in data])


if __name__ == '__main__':
    dimitri = DecisionTree()
    df = pd.read_csv("flowers_data.csv")
    dimitri.fit(df)
