
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

    def deletion(self, value):
        current = self.root
        if value > self.root.value:
            direction = 'right'
        else:
            direction = 'left'
        while True:
            try:
                if value > current.value:
                    if value == current.right.value:
                        if current.right.right is None and current.right.left is None:
                            current.right = None
                            depth_node = current
                            break
                        elif current.right.left is None:
                            current.right = current.right.right
                            depth_node = current
                            break
                        elif current.right.right is None:
                            current.right = current.right.left
                            depth_node = current
                            break
                        else:
                            parent = current
                            remove = parent.right
                            new = self._findmax(remove, remove.left)
                            if new[0] != remove:
                                new[0].right = None
                                if new[1].left:
                                    new[0].right = new[1].left
                            parent.right = new[1]
                            new[1].left = remove.left
                            new[1].right = remove.right
                            depth_node = current
                            break
                    current = current.right
                elif value < current.value:
                    if value == current.left.value:
                        if current.left.left is None and current.left.right is None:
                            current.left = None
                            depth_node = current
                            break
                        elif current.left.left is None:
                            current.left = current.left.right
                            depth_node = current
                            break
                        elif current.left.right is None:
                            current.left = current.left.left
                            depth_node = current
                            break
                        else:
                            parent = current
                            remove = parent.left
                            new = self._findmax(remove, remove.left)
                            if new[0] != remove:
                                new[0].right = None
                                if new[1].left:
                                    new[0].right = new[1].left
                            parent.right = new[1]
                            new[1].left = remove.left
                            new[1].right = remove.right
                            depth_node = current
                            break
                    current = current.left
                elif value == current.value:
                    if current.left is None and current.right is None:
                            self.root = None
                            depth_node = None
                            break
                    elif current.left is None:
                        self.root = current.right
                        depth_node = self.root
                    elif current.right is None:
                        self.root = current.left
                        depth_node = self.root
                    else:
                        new = self._findmax(current, current.left)
                        if new[0] != current:
                            new[0].right = None
                            if new[1].left:
                                new[0].right = new[1].left
                        self.root = new[1]
                        self.root.left = current.left
                        self.root.right = current.right
                        depth_node = self.root
                        break
            except AttributeError:
                break
        # print(self.breadth_first())
        # print(current.value)
        new_depth = self._depth_of_node(depth_node) + self._depth_of_branch(depth_node)
        if direction == 'right':
            self.right_depth = new_depth
        else:
            self.left_depth = new_depth

    def _findmax(self, remove, child):
        parent = remove
        current = child
        while current.right:
            parent = current
            current = current.right
        return [parent, current]

    def _depth_of_node(self, node):
        """Find the depth from top of tree to our node."""
        current = self.root
        depth = 0
        try:
            while True:
                if node.value > current.value:
                    current = current.right
                elif node.value < current.value:
                    current = current.left
                elif node.value == current.value:
                    return depth
                depth += 1
        except AttributeError:
            return None

    def _depth_of_branch(self, node):
        """Find depth of our branch from our found node."""
        current = [node, 0]
        the_list = []
        depth = 0
        while current:
            # print(current[0].value)
            current[0].left and the_list.append([current[0].left, current[1] + 1])
            current[0].right and the_list.append([current[0].right, current[1] + 1])
            depth = current[1]
            try:
                current = the_list.pop(0)
            except IndexError:
                return depth

    def update_balance(self, node):
        sides = self._check_right_left_depths(node)
        left_depth = sides[0]
        right_depth = sides[1]
        while right_depth - left_depth > 1:
            self.left_rotation(node)
            sides = self._check_right_left_depths(node)
            left_depth = sides[0]
            right_depth = sides[1]
        while right_depth - left_depth < -1:
            self.right_rotation(node)
            sides = self._check_right_left_depths(node)
            left_depth = sides[0]
            right_depth = sides[1]

    def _check_right_left_depths(self, node):
        left_side = 0
        right_side = 0
        if node.right:
            right_side = 1 + self._depth_of_branch(node.right)
        if node.left:
            left_side = 1 + self._depth_of_branch(node.left)
        return (left_side, right_side)

def wrapper(func, *args, **kwargs):
    """Creates a value for a function with a specific arguement called to it."""
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
    #code found at http://pythoncentral.io/time-a-python-function/

if __name__ == '__main__':
    Bullshit_tree = Binary_Search_Tree()
    import random
    data = [75, 97, 40, 7, 48, 65, 83, 27, 38, 1, 16, 86, 87, 100, 47, 53, 55, 54, 56, 57, 58, 59, 60]
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
    Bullshit_tree.deletion(75)
    gen = Bullshit_tree.breadth_first()
    array = []
    while len(array) < len(data) - 1:
        array.append(next(gen))

    print('update', Bullshit_tree.update_balance())
    print(Bullshit_tree.depth())
    print(Bullshit_tree.balance())


    # print(Bullshit_tree.search(data[-1]))

