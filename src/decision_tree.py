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
        df = pd.DataFrame(data, columns=["petal length (cm)", "petal width (cm)", "sepal length (cm)", "sepal width (cm)"])
        to_return = []
        for row in df.iterrows():
            to_return.append(self.root(row))
        return to_return

    # def _cut_helper(self, data, axis, amount):
    #     """Helper function for our fit function."""
    #     # return the amount of both types on each side
    #     left_side = []
    #     right_side = []

        # print(amount)
        # print('--------------------')
        # for i in data:
        #     print(i)
        #     if i[axis] < amount:
        #         left_side.append(data["target"][i])
        #     else:
        #         right_side.append(data["target"][i])
        # return (left_side, right_side)

    def fit(self, data):
        """A decision tree based on some incoming data set; returns nothing."""
        best_score = float("inf")
        if type(data) == str or type(data) == tuple:
            smallest_length = min([i[0] for i in data])
            biggest_length = max([i[0] for i in data])
        else:
            smallest_length = data["petal length (cm)"].min()
            biggest_length = data["petal length (cm)"].max()
        data = data.sort_values(["petal length (cm)"])
        for i in range(int(smallest_length * 10), int(biggest_length * 10)):
            left_side = data[data["petal length (cm)"] < i / 10]
            right_side = data[data["petal length (cm)"] >= i / 10]
            score = left_side["target"].sum() + (len(right_side) - right_side["target"].sum())
            if score < best_score:
                best_left_side = left_side
                best_right_side = right_side
                best_score = score
                best_axis = "petal length (cm)"
                best_amount = i / 10
        best_score = float("inf")
        if type(data) == str or type(data) == tuple:
            smallest_width = min([i[1] for i in data])
            biggest_width = max([i[1] for i in data])
        else:
            smallest_width = data["petal width (cm)"].min()
            biggest_width = data["petal width (cm)"].max()
        data = data.sort_values(["petal width (cm)"])
        for i in range(int(smallest_width * 10), int(biggest_width * 10)):
            left_side = data[data["petal width (cm)"] < i / 10]
            right_side = data[data["petal width (cm)"] >= i / 10]
            score = left_side["target"].sum() + (len(right_side) - right_side["target"].sum())
            if score < best_score:
                best_left_side = left_side
                best_right_side = right_side
                best_score = score
                best_axis = "petal width (cm)"
                best_amount = i / 10
        if not self.root:
            if best_left_side["target"].sum() == 0 and len(best_right_side) - best_right_side["target"].sum() == 0:
                self.root = QuestionNode(best_axis, best_amount, "setosa", "versicolor")
            elif best_left_side["target"].sum() == 0:
                self.root = QuestionNode(best_axis, best_amount, "setosa", self.fit(best_right_side))
            elif len(best_right_side) - best_right_side["target"].sum() == 0:
                self.root = QuestionNode(best_axis, best_amount, self.fit(best_left_side), "versicolor")
            else:
                self.root = QuestionNode(best_axis, best_amount, self.fit(best_left_side), self.fit(best_right_side))
        else:
            if best_left_side["target"].sum() == 0 and len(best_right_side) - best_right_side["target"].sum() == 0:
                return QuestionNode(best_axis, best_amount, "setosa", "versicolor")
            elif best_left_side["target"].sum() == 0:
                return QuestionNode(best_axis, best_amount, "setosa", self.fit(best_right_side))
            elif len(best_right_side) - best_right_side["target"].sum() == 0:
                return QuestionNode(best_axis, best_amount, self.fit(best_left_side), "versicolor")
            else:
                return QuestionNode(best_axis, best_amount, self.fit(best_left_side), self.fit(best_right_side))


if __name__ == '__main__':
    dimitri = DecisionTree()
    df = pd.read_csv("flowers_data.csv")
    dimitri.fit(df)
    print(dimitri.predict([1.4, 0.1, 4.8, 3.0]))
    # print(dimitri.root.axis)


    