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
        print('---------------------')
        print('asking question, if the', [self.axis], 'is less than,', self.amount)
        print('it will go to:', self.result_one, 'else', self.result_two)
        print('the number is:', data[1][self.axis])
        if data[1][self.axis] < self.amount:
            print('it is less')
            return self.result_one if type(self.result_one) == str else self.result_one(data)
        else:
            print('it is more')
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
        # df = pd.DataFrame(data, columns=["sepal length (cm)", "sepal width (cm)", "sepal length (cm)", "sepal width (cm)"])
        results = []
        for row in data.iterrows():
            results.append(self.root(row))
        data['results'] = results
        return data

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

    def fit(self, data, recur=True):
        """A decision tree based on some incoming data set; returns nothing."""
        best_score = float("inf")
        if type(data) == str or type(data) == tuple:
            smallest_length = min([i[2] for i in data])
            biggest_length = max([i[2] for i in data])
        else:
            smallest_length = data["sepal length (cm)"].min()
            biggest_length = data["sepal length (cm)"].max()
        data = data.sort_values(["sepal length (cm)"])
        for i in range(int(smallest_length * 10), int(biggest_length * 10) + 1):
            left_side = data[data["sepal length (cm)"] < i / 10]
            right_side = data[data["sepal length (cm)"] >= i / 10]
            left_sum = left_side["target"].sum()
            left_score = left_sum if left_sum < (len(left_side) - left_sum) else (len(left_side) - left_sum)
            right_sum = right_side["target"].sum()
            right_score = right_sum if right_sum < (len(right_side) - right_sum) else (len(right_side) - right_sum)
            score = left_score + right_score
            if score < best_score:
                best_left_side = left_side
                best_right_side = right_side
                best_score = score
                best_axis = "sepal length (cm)"
                best_amount = i / 10
            elif score == best_score:
                if abs(len(right_side) - len(left_side)) < abs(len(best_right_side) - len(best_left_side)):
                    best_left_side = left_side
                    best_right_side = right_side
                    best_score = score
                    best_axis = "sepal length (cm)"
                    best_amount = i / 10
        if type(data) == str or type(data) == tuple:
            smallest_width = min([i[3] for i in data])
            biggest_width = max([i[3] for i in data])
        else:
            smallest_width = data["sepal width (cm)"].min()
            biggest_width = data["sepal width (cm)"].max()
        data = data.sort_values(["sepal width (cm)"])
        for i in range(int(smallest_width * 10), int(biggest_width * 10) + 1):
            left_side = data[data["sepal width (cm)"] < i / 10]
            right_side = data[data["sepal width (cm)"] >= i / 10]
            left_sum = left_side["target"].sum()
            left_score = left_sum if left_sum < (len(left_side) - left_sum) else (len(left_side) - left_sum)
            right_sum = right_side["target"].sum()
            right_score = right_sum if right_sum < (len(right_side) - right_sum) else (len(right_side) - right_sum)
            score = left_score + right_score
            if score <= best_score:
                best_left_side = left_side
                best_right_side = right_side
                best_score = score
                best_axis = "sepal width (cm)"
                best_amount = i / 10
            elif score == best_score:
                if abs(len(right_side) - len(left_side)) < abs(len(best_right_side) - len(best_left_side)):
                    best_left_side = left_side
                    best_right_side = right_side
                    best_score = score
                    best_axis = "sepal width (cm)"
                    best_amount = i / 10
        left_sum = best_left_side["target"].sum()
        left_score = left_sum if left_sum < (len(best_left_side) - left_sum) else (len(best_left_side) - left_sum)
        right_sum = best_right_side["target"].sum()
        right_score = right_sum if right_sum < (len(best_right_side) - right_sum) else (len(best_right_side) - right_sum)
        if recur is True:
            if left_score == 0 and right_score == 0:
                self.root = QuestionNode(best_axis, best_amount, best_left_side['class_names'].iloc[0], best_right_side['class_names'].iloc[0])
            elif left_score == 0:
                self.root = QuestionNode(best_axis, best_amount, best_left_side['class_names'].iloc[0], self.fit(best_right_side, False))
            elif right_score == 0:
                self.root = QuestionNode(best_axis, best_amount, self.fit(best_left_side, False), best_right_side['class_names'].iloc[0])
            else:
                self.root = QuestionNode(best_axis, best_amount, self.fit(best_left_side, False), self.fit(best_right_side, False))
        else:
            if left_score == 0 and right_score == 0:
                return QuestionNode(best_axis, best_amount, best_left_side['class_names'].iloc[0], best_right_side['class_names'].iloc[0])
            elif left_score == 0:
                return QuestionNode(best_axis, best_amount, best_left_side['class_names'].iloc[0], self.fit(best_right_side, False))
            elif right_score == 0:
                return QuestionNode(best_axis, best_amount, self.fit(best_left_side, False), best_right_side['class_names'].iloc[0])
            else:
                return QuestionNode(best_axis, best_amount, self.fit(best_left_side, False), self.fit(best_right_side, False))


if __name__ == '__main__':
    dimitri = DecisionTree()
    df = pd.read_csv("flowers_data.csv")
    dimitri.fit(df)
    new_data = pd.read_csv("flower2.csv")
    print(dimitri.predict(new_data))

    # print(dimitri.root.axis)


    