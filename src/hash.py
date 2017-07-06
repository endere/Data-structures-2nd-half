"""Hash tables."""
import hash_bst
from faker import Faker

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

    def additive_set(self, key, value):
        """Store the given value using the given key."""
        if type(key) != str:
            raise TypeError("This is not the string you're looking for!")
        else:
            number = self._additive_hash(key)
            self.dict_bst[int(str(number)[-2:])].insert(number, value)

    def additive_get(self, key):
        """Return the value stored with the given key."""
        if type(key) != str:
            raise TypeError("This is not the string you're looking for!")
        else:
            number = self._additive_hash(key)
            return self.dict_bst[int(str(number)[-2:])].search(number)

    def _fnv_hash(self, key):
        p = key
        h = 2166136261
        for i in range(len(key)):
            h = (h * 16777619) ^ ord(key[i])
        return h

    def fnv_set(self, key, value):
        """."""
        if type(key) != str:
            raise TypeError("This is not the string you're looking for!")
        else:
            number = self._fnv_hash(key)
            print(type(number))
            self.dict_bst[int(str(number)[-3:])].insert(int(number), value)

    def fnv_get(self, key):
        """."""
        if type(key) != str:
            raise TypeError("This is not the string you're looking for!")
        else:
            number = self._fnv_hash(key)
            return self.dict_bst[int(str(number)[-3:])].search(number)


if __name__ == '__main__':
    HashyMcHashTable = HashTable(1000)
    print(HashyMcHashTable.fnv_set("This is my strang", "I like strings a lot."))
    print(HashyMcHashTable.fnv_get("This is my strang").stored_value)
    fake = Faker()
    for i in range(100):
        word = fake.word()
        name = fake.name()
        HashyMcHashTable.fnv_set(str(word), str(name))
        print(str(word), str(name))
    print("--------------------------")
    print(HashyMcHashTable.fnv_get(str(word)).stored_value)
    print(str(word))

