"""Trie tree data structure."""


class Node(object):
    """Node object for trietree data structure."""

    def __init__(self, value, level, parent):
        """Set up Node."""
        self.parent = parent
        self.value = value
        self.next_list = []
        self.level = level


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
            if len(current.next_list) == 0:
                current.next_list.append(Node(string[i], i + 1, current))
                current = current.next_list[-1]
            else:
                for node in current.next_list:
                    if node == "$":
                        continue
                    elif string[i] == node.value:
                        current = node
                        break
                    elif node == current.next_list[-1]:
                        current.next_list.append(Node(string[i], i + 1, current))
                        current = current.next_list[-1]
        current.next_list.append("$")

    def contains(self, string):
        """Return true if string in tree."""
        current = self.root
        for i in range(len(string)):
            for node in current.next_list:
                if node == "$":
                    continue
                elif string[i] == node.value:
                    current = node
                elif node == current.next_list[-1]:
                    return False
        if "$" in current.next_list:
            return True
        else:
            return False

    def size(self):
        """Return total number of words in tree."""
        return self.length

    def remove(self, string):
        """Remove string from tree."""
        current = self.root
        for i in range(len(string)):
            for node in current.next_list:
                if node == "$":
                    continue
                elif string[i] == node.value:
                    current = node
                elif node == current.next_list[-1]:
                    raise IndexError("String not in tree.")
        current.next_list.remove("$")
        while True:
            child = current
            current = current.parent
            if len(current.next_list) > 1 or current == self.root:
                current.next_list.remove(child)
                break


if __name__ == '__main__':
    test__the_trie_tree = TrieTree()
    print(test__the_trie_tree.insert('fire'))
    print(test__the_trie_tree.insert('fig'))
    print(test__the_trie_tree.contains('fire'))
    print(test__the_trie_tree.contains('fig'))
    print(test__the_trie_tree.contains('pig'))
    print(test__the_trie_tree.remove('fire'))
    print(test__the_trie_tree.contains('fire'))
    print(test__the_trie_tree.contains('fig'))

    with open('/usr/share/dict/words') as dictionary:
        data = dictionary.read()
        data = data.split('\n')
    for i in range(len(data)):
        test__the_trie_tree.insert(data[i])
        print(len(data) - i)
    print(test__the_trie_tree.contains('dinosaur'))
    print(test__the_trie_tree.contains('skjdgjkdfkja'))
    print(test__the_trie_tree.contains('fastidious'))
    print(test__the_trie_tree.remove('pharaoh'))
    print(test__the_trie_tree.contains('pharaoh'))
