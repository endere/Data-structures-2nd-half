"""Trie tree data structure."""


class Node(object):
    """Node object for trietree data structure."""

    def __init__(self, value, level, parent):
        """Set up Node."""
        self.parent = parent
        self.value = value
        self.next_list = []
        self.level = level
        self.end = False


class TrieTree(object):
    """A trietree data structure."""

    def __init__(self):
        """Set up die tree."""
        self.length = 0
        self.root = Node('.', 0, None)

    def insert(self, string):
        """Insert a node into the tree."""
        current = self.root
        for i in range(len(string)):
            try:
                current = list(filter(lambda x: x.value == string[i], current.next_list))[0]
            except IndexError:
                current.next_list.append(Node(string[i], i + 1, current))
                current = current.next_list[-1]
        self.length += 1
        current.end = True

    def contains(self, string):
        """Return true if string in tree."""
        current = self.root
        print('checking if {} is in tree'.format(string))
        for i in range(len(string)):
            try:
                current = list(filter(lambda x: x.value == string[i], current.next_list))[0]
            except IndexError:
                return False
        return current.end

    def size(self):
        """Return total number of words in tree."""
        return self.length

    def remove(self, string):
        """Remove string from tree."""
        current = self.root
        for i in range(len(string)):
            try:
                current = list(filter(lambda x: x.value == string[i], current.next_list))[0]
            except IndexError:
                raise IndexError("String not in tree.")
        if current.end is False:
            raise IndexError("String not in tree.")
        if len(current.next_list) > 0:
            current.end = False
            self.length -= 1
        else:
            while True:
                child = current
                current = current.parent
                if len(current.next_list) > 1 or current == self.root:
                    current.next_list.remove(child)
                    self.length -= 1
                    break

    def traversal(self, start):
        """Traverse through the tree and return a list of all strings with the given start."""
        pass

if __name__ == '__main__':
    test__the_trie_tree = TrieTree()
    with open('/usr/share/dict/words') as dictionary:
        data = dictionary.read()
        data = data.split('\n')
    import time
    import sys
   
    for i in range(len(data)):
        test__the_trie_tree.insert(data[i])
        x = i / len(data) * 100
        sys.stdout.write("\r%d%%" % x)
        sys.stdout.flush()
    print(test__the_trie_tree.size())
