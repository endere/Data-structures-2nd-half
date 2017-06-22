
"""The binary search tree data structure."""
import timeit

class Node(object):
    """I am a Node."""

    def __init__(self, value):
        """Init for our nodes."""
        self.value = value
        self.left = None
        self.right = None


class Binary_Search_Tree(object):
    """I am a search tree."""

    def __init__(self, iterable=None):
        """Init for our BST."""
        if iterable:
            if type(iterable) in [list, tuple]:
                for i in iterable:
                    self.insert(i)
        self.root = None
        self.length = 0
        self.right_depth = 0
        self.left_depth = 0

    def insert(self, val):
        """Insert a node for start and for right and left."""
        if type(val) not in [float, int]:
            raise TypeError('Numbers only >:(')
        if self.root is None:
            self.root = Node(val)
            self.length += 1
        else:
            if val > self.root.value:
                direction = 'right'
            else:
                direction = 'left'
            current = self.root
            depth = 0
            while current:
                depth += 1
                if val == current.value:
                    break
                if val > current.value:
                    if current.right is None:
                        current.right = Node(val)
                        if direction == 'right':
                            if depth > self.right_depth:
                                self.right_depth = depth
                        else:
                            if depth > self.left_depth:
                                self.left_depth = depth
                        self.length += 1
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        current.left = Node(val)
                        if direction == 'right':
                            if depth > self.right_depth:
                                self.right_depth = depth
                        else:
                            if depth > self.left_depth:
                                self.left_depth = depth
                        self.length += 1
                    else:
                        current = current.left

    def search(self, val):
        """Search binary tree for values."""
        current = self.root
        try:
            while True:
                if val > current.value:
                    current = current.right
                elif val < current.value:
                    current = current.left
                elif val == current.value:
                    return current
        except AttributeError:
            return None

    def size(self):
        """Return length of size."""
        return self.length

    def depth(self):
        """Return depth of left and right binary search tree."""
        if self.right_depth > self.left_depth:
            return self.right_depth
        else:
            return self.left_depth

    def contains(self, value):
        """Return True if value is there and False if not."""
        if self.search(value):
            return True
        else:
            return False

    def balance(self):
        """Return our balance for our binary search tree."""
        return self.right_depth - self.left_depth

    def breadth_first(self):
        current = self.root
        the_list = []
        while current:
            current.left and the_list.append(current.left)
            current.right and the_list.append(current.right)
            yield current.value
            current = the_list.pop(0)

    def pre_order(self):
        current = self.root
        the_list = []
        while current:
            current.right and the_list.append(current.right)
            yield current.value
            if current.left:
                current = current.left
            else:
                current = the_list.pop()

    def post_order(self):
        current = self.root
        the_list = []
        seen_parents = []
        while current:
            if current.left is None and current.right is None or current in seen_parents:
                yield current.value
            else:
                the_list = [current.left, current.right, current] + the_list
                the_list[:3] = [x for x in the_list[:3] if x is not None]
                seen_parents.append(current)
            if len(the_list) > 0:
                current = the_list.pop(0)


    def in_order(self):
        current = self.root
        the_list = []
        seen_parents = []
        while current:
            if current.left is None and current.right is None or current in seen_parents:
                yield current.value
            else:
                seen_parents.append(current)
                the_list = [current.left, current, current.right] + the_list
                the_list[:3] = [x for x in the_list[:3] if x is not None]
            if len(the_list) > 0:
                current = the_list.pop(0)



def wrapper(func, *args, **kwargs):
    """Creates a value for a function with a specific arguement called to it."""
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
    #code found at http://pythoncentral.io/time-a-python-function/

if __name__ == '__main__':
    Bullshit_tree = Binary_Search_Tree()
    import random
    data = [75, 97, 40, 7, 48, 65, 83, 27, 38, 1, 16, 86, 87, 100, 47, 53, 55, 54]
    print(data)
    for i in data:
        Bullshit_tree.insert(i)
    # wrapped1 = wrapper(Bullshit_tree.search, data[0])
    # wrapped2 = wrapper(Bullshit_tree.search, data[-1])
    # print(Bullshit_tree.size())
    # print(Bullshit_tree.depth())
    # print(Bullshit_tree.balance())
    # print(Bullshit_tree.right_depth)
    # print(Bullshit_tree.left_depth)
    # print(Bullshit_tree.root.value)
    # print(Bullshit_tree.root.right.value)
    # print(Bullshit_tree.root.right.left.value)
    # print(timeit.timeit(wrapped1))
    # print(timeit.timeit(wrapped2))
    thing = Bullshit_tree.in_order()
    array = []
    while len(array) < Bullshit_tree.size():
        array.append(next(thing))
        print(array)
    # print(Bullshit_tree.search(data[-1]))

