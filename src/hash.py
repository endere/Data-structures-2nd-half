"""Hash tables."""
import hash_bst

class HashTable(object):
    """Class object for our Hash Table."""

    def __init__(self, bucket_number):
        """Init for our hash."""
        self.dict_bst = {}
        for i in range(bucket_number):
            self.dict_bst[i] = hash_bst.BinarySearchTree()

    def _additive_hash(self, key):
        """Hash they key provided."""
        p = key
        h = 0
        for i in range(len(key)):
            h += ord(key[i])
        return h

    def set(self, key, value):
        """Store the given value using the given key."""
        if type(key) != str:
            raise TypeError("This is not the string you're looking for!")
        else:
            number = self._additive_hash(key)
            self.dict_bst[int(str(number)[-2:])].insert(number, value)


    def get(self, key):
        """Return the value stored with the given key."""
        if type(key) != str:
            raise TypeError("This is not the string you're looking for!")
        else:
            number = self._additive_hash(key)
            return self.dict_bst[int(str(number)[-2:])].search(number)


if __name__ == '__main__':
    HashyMcHashTable = HashTable(100)
    print(HashyMcHashTable.set("This is my strang", "I like strings a lot."))
    # print(HashyMcHashTable.dict_bst)
    print(HashyMcHashTable.get("This is my strang").stored_value)

