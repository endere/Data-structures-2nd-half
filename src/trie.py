"""Trie tree data structure."""


class Node(object):
    """Node object for trietree data structure."""

    def __init__(self, value):
        """Set up Node."""
        self.value = value
        self.next_list = []


class TrieTree(object):
    """A trietree data structure."""

    def __init__(self):
        """Set up die tree."""
        self.length = 0
        self.root = Node('.')

    def insert(self, string):
        """Insert a node into the tree."""
        current = self.root
        for i in range(len(string)):
            print('------------')
            print('current letter:', string[i])
            if len(current.next_list) == 0:
                print('it was an empty list.')
                current.next_list.append(Node(string[i]))
                current = current.next_list[-1]
            else:
                for node in current.next_list:
                    print('current node value: ', node.value)
                    if string[i] == node.value:
                        print('node found in list.')
                        current = node
                        break
                    elif node == current.next_list[-1]:
                        print('node not found in list.')
                        current.next_list.append(Node(string[i]))
                        current = current.next_list[-1]

    def contains(self, string):
        """Return true if string in tree."""
        pass

    def size(self):
        """Return total number of words in tree."""
        return self.length

    def remove(self, string):
        """Remove string from tree."""
        pass


if __name__ == '__main__':
    test__the_trie_tree = TrieTree()
    print(test__the_trie_tree.insert('fire'))
    print(test__the_trie_tree.insert('fire'))
