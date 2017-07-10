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
        if current.end == False:
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


if __name__ == '__main__':
    test__the_trie_tree = TrieTree()
    # print(test__the_trie_tree.insert('fire'))
    # print(test__the_trie_tree.insert('fig'))
    # print(test__the_trie_tree.contains('fire'))
    # print(test__the_trie_tree.contains('fig'))
    # print(test__the_trie_tree.contains('pig'))
    # print(test__the_trie_tree.remove('fire'))
    # print(test__the_trie_tree.contains('fire'))
    # print(test__the_trie_tree.contains('fig'))
    with open('/usr/share/dict/words') as dictionary:
        data = dictionary.read()
        data = data.split('\n')
    for i in range(len(data)):
        print(len(data) - i)
        print('-----')
        print(data[i])
        test__the_trie_tree.insert(data[i])
    # print(test__the_trie_tree.root.next_list)
    # gen = (o.value for o in test__the_trie_tree.root.next_list[1].next_list)
    # test_array = []
    # while len(test_array) < len(test__the_trie_tree.root.next_list[1].next_list):
    #     test_array.append(next(gen))

    # print(test_array)
    print(test__the_trie_tree.contains('dinosaurs'))
    print(test__the_trie_tree.contains('dinosaur'))

    # print(test__the_trie_tree.contains('skjdgjkdfkja'))
    test__the_trie_tree.remove('dinosaur')
    test__the_trie_tree.remove('dinosaurs')

    print(test__the_trie_tree.contains('dinosaurs'))
    print(test__the_trie_tree.contains('dinosaur'))
    print(test__the_trie_tree.size())
    print(len(data))
    # print(test__the_trie_tree.contains('fastidious'))
    # print(test__the_trie_tree.remove('pharaoh'))
    # print(test__the_trie_tree.contains('pharaoh'))
