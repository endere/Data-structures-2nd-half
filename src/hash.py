"""Hash tables."""
import bst


class HashTable(object):
    """Class object for our Hash Table."""

    def __init__(self, bucket_number, function='fnv'):
        """Init for our hash.

        Accepts a string to determine which hash the table uses.
        """
        self.dict_bst = {}
        self.function = function
        for i in range(bucket_number):
                self.dict_bst[i] = bst.BinarySearchTree()

    def _hash(self, key):
        """Use fnv hash if function is fnv, or uses additive hash if function is add."""
        if self.function == 'fnv':
            h = 2166136261
            for i in range(len(key)):
                h = (h * 16777619) ^ ord(key[i])
            return h
        elif self.function == 'add':
            h = 0
            for i in range(len(key)):
                h += ord(key[i])
            return h

    def set(self, key, value):
        """Place an item in the hash table."""
        bucket_index = 3 if self.function == 'fnv' else 2
        number = self._hash(key)
        stored_key = number if self.function == 'fnv' else key
        if self.get(key) is None:
            self.dict_bst[int(str(number)[-bucket_index:])].insert(stored_key, value)

    def get(self, key):
        """Use a key to retrieve a stored value from the table."""
        if type(key) != str:
                raise TypeError("This is not the string you're looking for!")
        number = self._hash(key)
        bucket_index = 3 if self.function == 'fnv' else 2
        stored_key = number if self.function == 'fnv' else key
        try:
            return self.dict_bst[int(str(number)[-bucket_index:])].search(stored_key).stored_value
        except AttributeError:
            return None
