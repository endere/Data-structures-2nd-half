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
        self.bucket_number = bucket_number
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
        number = self._hash(key)
        stored_key = number if self.function == 'fnv' else key
        if self.get(key) is None:
            self.dict_bst[number % self.bucket_number].insert(stored_key, value)

    def get(self, key):
        """Use a key to retrieve a stored value from the table."""
        if type(key) != str:
                raise TypeError("This is not the string you're looking for!")
        number = self._hash(key)
        stored_key = number if self.function == 'fnv' else key
        try:
            return self.dict_bst[number % self.bucket_number].search(stored_key).stored_value
        except AttributeError:
            return None

if __name__ == '__main__':
    test_table = HashTable(1000000)
    with open('/usr/share/dict/words') as dictionary:
        data = dictionary.read()
        data = data.split('\n')
    for i in range(len(data)):
        print(len(data) - i)
        test_table.set(data[i], data[i])
    print(type(test_table.dict_bst))
    for key in test_table.dict_bst:
        print("key: {} , len: {}".format(key, test_table.dict_bst[key].size()))