"""The binary search tree data structure."""


class Node(object):
    """Create a node object that points to a parent, left child, and right child."""

    def __init__(self, value, parent=None, stored_value=None):
        """Init for our nodes."""
        self.stored_value = stored_value
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None


class BinarySearchTree(object):
    """Create a Binary Search Tree Object."""

    def __init__(self, iterable=None):
        """Init for our BST."""
        self.root = None
        self.length = 0
        self.right_depth = 0
        self.left_depth = 0
        if iterable:
            if type(iterable) in [list, tuple]:
                for i in iterable:
                    self.insert(i)

    def insert(self, val, stored_value=None):
        """Insert a node for start and for right and left."""
        # if type(val) not in [float, int]:
        #     raise TypeError('Please insert only numbers.')
        if not isinstance(val, (int, float)):
            raise TypeError('Please insert a number.')
        if self.root is None:
            self.root = Node(val, None, stored_value)
            self.length += 1
        else:
            current = self.root
            while current:
                if val == current.value:
                    raise ValueError('Value already in tree.')
                if val > current.value:
                    if current.right is None:
                        current.right = Node(val, current, stored_value)
                        self._update_balance(current)
                        self.length += 1
                        break
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        current.left = Node(val, current, stored_value)
                        self._update_balance(current)
                        self.length += 1
                        break
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
        try:
            return self._depth_of_branch(self.root) + 1
        except AttributeError:
            return 0

    def contains(self, value):
        """Return True if value is there and False if not."""
        if self.search(value):
            return True
        else:
            return False

    def balance(self):
        """Return our balance for our binary search tree."""
        if self.length == 0:
            return 0
        sides = self._check_right_left_depths(self.root)
        return sides[1] - sides[0]

    def breadth_first(self):
        """Generator function that yields values from tree in breadth first order."""
        current = self.root
        the_list = []
        while current:
            current.left and the_list.append(current.left)
            current.right and the_list.append(current.right)
            yield current.value
            try:
                current = the_list.pop(0)
            except IndexError:
                current = None

    def pre_order(self):
        """Generator function that yields values from tree in pre order."""
        current = self.root
        the_list = []
        while current:
            current.right and the_list.append(current.right)
            yield current.value
            if current.left:
                current = current.left
            else:
                try:
                    current = the_list.pop()
                except IndexError:
                    current = None

    def post_order(self):
        """Generator function that yields values from tree in post order."""
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
            try:
                current = the_list.pop(0)
            except IndexError:
                current = None

    def in_order(self):
        """Generator function that yields values from tree in order."""
        """Get our bst back in order."""
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
            try:
                current = the_list.pop(0)
            except IndexError:
                current = None

    def deletion(self, value):
        """Delete our nodes in our bst."""
        current = self.root
        depth_node = None
        while True:
            try:
                if value > current.value:  # going down the right side of our tree
                    if value == current.right.value:  # case for just one node with no children
                        if current.right.right is None and current.right.left is None:
                            current.right = None
                            depth_node = current
                            self.length -= 1
                            break
                        elif current.right.left is None:  # case for just one child right not left
                            current.right = current.right.right
                            current.right.parent = current
                            depth_node = current
                            self.length -= 1
                            break
                        elif current.right.right is None:  # case for just one child left not right
                            current.right = current.right.left
                            current.right.parent = current
                            depth_node = current
                            self.length -= 1
                            break
                        else:  # case for two children left and then right most
                            parent = current
                            remove = parent.right
                            new = self._findmax(remove, remove.left)
                            if new[0] != remove:
                                new[0].right = None
                                if new[1].left:
                                    new[0].right = new[1].left
                                    new[0].right.parent = new[0]
                            parent.right = new[1]
                            new[1].parent = parent
                            new[1].right = remove.right
                            new[1].right.parent = new[1]
                            if new[1] != remove.left:
                                new[1].left = remove.left
                                new[1].left.parent = new[1]
                            depth_node = current
                            self.length -= 1
                            break
                    current = current.right
                elif value < current.value:  # going down the left side of our tree
                    if value == current.left.value:
                        if current.left.left is None and current.left.right is None:
                            current.left = None
                            depth_node = current
                            self.length -= 1
                            break
                        elif current.left.left is None:
                            current.left = current.left.right
                            current.left.parent = current
                            depth_node = current
                            self.length -= 1
                            break
                        elif current.left.right is None:
                            current.left = current.left.left
                            current.left.parent = current 
                            depth_node = current
                            self.length -= 1
                            break
                        else:
                            parent = current
                            remove = parent.left
                            new = self._findmax(remove, remove.left)
                            if new[0] != remove:
                                new[0].right = None
                                if new[1].left:
                                    new[0].right = new[1].left
                                    new[0].right.parent = new[0]
                            parent.left = new[1]
                            new[1].parent = parent
                            if new[1] != remove.left:
                                new[1].left = remove.left
                                new[1].left.parent = new[1]
                            new[1].right = remove.right
                            new[1].right.parent = new[1]
                            depth_node = current
                            self.length -= 1
                            break
                    current = current.left
                elif value == current.value:
                    if current.left is None and current.right is None:
                        self.root = None
                        depth_node = None
                        self.length -= 1
                        break
                    elif current.left is None:
                        self.root = current.right
                        self.root.parent = None 
                        depth_node = self.root
                        self.length -= 1
                        break
                    elif current.right is None:
                        self.root = current.left
                        self.root.parent = None
                        depth_node = self.root
                        self.length -= 1
                        break
                    else:
                        new = self._findmax(current, current.left)
                        if new[0] != current:
                            new[0].right = None
                            if new[1].left:
                                new[0].right = new[1].left
                        self.root = new[1]
                        if new[1] != current.left:
                            self.root.left = current.left
                            self.root.left.parent = self.root
                        if new[1] != current.right:  
                            self.root.right = current.right
                            self.root.right.parent = self.root
                        self.root.parent = None
                        depth_node = self.root
                        self.length -= 1
                        break
            except AttributeError:
                break
        if depth_node:
            self._update_balance(depth_node)

    def _findmax(self, remove, child):
        """Find the furthest right child of a node and returns it plus parent."""
        parent = remove
        current = child
        while current.right:
            parent = current
            current = current.right
        return [parent, current]

    def _depth_of_branch(self, node):
        """Find depth of our branch from our found node."""
        current = [node, 0]
        the_list = []
        depth = 0
        while current:
            current[0].left and the_list.append([current[0].left, current[1] + 1])
            current[0].right and the_list.append([current[0].right, current[1] + 1])
            depth = current[1]
            try:
                current = the_list.pop(0)
            except IndexError:
                return depth

    def _update_balance(self, node):
        """Update our balance of the tree."""
        sides = self._check_right_left_depths(node)
        if sides[1] - sides[0] > 1:  # for right side being heavier
            child_sides = self._check_right_left_depths(node.right)
            if child_sides[1] - child_sides[0] < 0:
                node = self._double_rotate_right_left(node)
            else:
                node = self._left_rotation(node)
        elif sides[1] - sides[0] < -1:  # for the left side being heavier
            child_sides = self._check_right_left_depths(node.left)
            if child_sides[1] - child_sides[0] > 0:

                node = self._double_rotate_left_right(node)
            else:
                node = self._right_rotation(node)
        if node is not self.root:
            self._update_balance(node.parent)

    def _check_right_left_depths(self, node):
        """Helper function to check depth of both branches of a node."""
        left_side = 0
        right_side = 0
        if node.right:
            right_side = 1 + self._depth_of_branch(node.right)
        if node.left:
            left_side = 1 + self._depth_of_branch(node.left)
        return (left_side, right_side)

    def _right_rotation(self, node):
        """Do a right rotation of an AVL balanced tree. Returns the new branche's root."""
        n2 = node
        k = n2.left
        n2.left = k.right
        if n2.left:
            n2.left.parent = n2
        k.parent = n2.parent
        if n2.parent is None:
            k.parent = None
            self.root = k
        elif n2.parent.left == n2:
            n2.parent.left = k
        else:
            n2.parent.right = k
        k.right = n2
        k.right.parent = k
        return k

    def _left_rotation(self, node):
        """Do a left rotation of an AVL balanced tree. Returns the new branche's root."""
        n2 = node
        k = n2.right
        n2.right = k.left
        if n2.right:
            n2.right.parent = n2
        k.parent = n2.parent
        if n2.parent is None:
            k.parent = None
            self.root = k
        elif n2.parent.right == n2:
            n2.parent.right = k
        else:
            n2.parent.left = k
        k.left = n2
        k.left.parent = k
        return k

    def _double_rotate_left_right(self, node):
        """Do a double left right rotation of an AVL balanced tree. Returns the new branche's root."""
        node.left = self._left_rotation(node.left)
        k = self._right_rotation(node)
        return k

    def _double_rotate_right_left(self, node):
        """Do a double right left rotation of an AVL balanced tree. Returns the new branche's root."""
        node.right = self._right_rotation(node.right)
        k = self._left_rotation(node)
        return k
