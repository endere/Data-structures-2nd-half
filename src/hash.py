"""Hash tables."""
import bst

class HashTable(object):
    """Class object for our Hash Table."""

    def __init__(self, bucket_number):
        """Init for our hash."""
        self.dict_bst = {}
        for i in range(bucket_number):
            self.dict_bst[i] = bst.BinarySearchTree()

    def _additive_hash(self, key):
        """Hash they key provided."""
        h = 0
        for i in range(len(key)):
            h += ord(key[i])
        return h

    def additive_set(self, key, value):
        """Store the given value using the given key."""
        if self.additive_get(key) is None:
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
            try:
                number = self._additive_hash(key)
                return self.dict_bst[int(str(number)[-2:])].search(number)
            except AttributeError:
                return None

    def _fnv_hash(self, key):
        h = 2166136261
        for i in range(len(key)):
            h = (h * 16777619) ^ ord(key[i])
        return h

    def fnv_set(self, key, value):
        """."""
        if self.fnv_get(key) is None:
            if type(key) != str:
                raise TypeError("This is not the string you're looking for!")
            else:
                number = self._fnv_hash(key)
                self.dict_bst[int(str(number)[-3:])].insert(int(number), value)

    def fnv_get(self, key):
        """."""
        if type(key) != str:
            raise TypeError("This is not the string you're looking for!")
        else:
            try:
                number = self._fnv_hash(key)
                return self.dict_bst[int(str(number)[-3:])].search(number).stored_value
            except AttributeError:
                return None


if __name__ == '__main__':
    HashyMcHashTable = HashTable(1000)
    print(HashyMcHashTable.fnv_set("This is my strang", "I like strings a lot."))
    print(HashyMcHashTable.fnv_get("This is my strang"))
    print("-------------------------")
    print(HashyMcHashTable.fnv_set("This is my strang", "To Yo Bo Ho Fo So"))
    print(HashyMcHashTable.fnv_get("This is my strang"))
    file = open('words', 'r')
    data = file.read()
    file.close()
    data = data.split('\n')
    for i in range(len(data)):
        print(len(data) - i)
        HashyMcHashTable.fnv_set(data[i], data[i])
    print(HashyMcHashTable.fnv_get('yowling'))
    print(HashyMcHashTable.fnv_get('zodiac'))
    print(HashyMcHashTable.fnv_get('zebu'))
    print(HashyMcHashTable.fnv_get('eyed'))
    print(HashyMcHashTable.fnv_get('fable'))
    print(HashyMcHashTable.fnv_get('personality'))