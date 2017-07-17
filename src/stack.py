"""Stack implementation using Node objects."""


class Node(object):
    """Create Node structure."""

    def __init__(self, value, next_up):
        """Initialize with a value."""
        self.value = value
        self.next = next_up


class Stack(object):
    """Define the Stack object."""

    def __init__(self, optional_values=[]):
        """Initialize with a given list."""
        self.head = None
        self.length = 0
        for x in optional_values:
            self.push(x)

    def push(self, value):
        """Assign a value to a node and push it on top of the stack."""
        self.head = Node(value, self.head)
        self.length += 1

    def pop(self):
        """Pop a node and return it, modify length by one."""
        try:
            popped = self.head
            self.head = self.head.next
            self.length -= 1
            return popped
        except AttributeError:
            return None

    def __len__(self):
        """Overload the str function of len to print the length of Stack."""
        return self.length
