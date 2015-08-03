"""Contains a HashTable class. The hash table is implemented on a list of
lists, with a default table size of 8192. This table size can be overridden on
initialization by passing a size keyword argument. Insertion and lookup time
complexity ranges from O(1) at best to O(n) at worst.
"""


class HashTable(object):
    """A class for a hash table."""
    entries_count = 0
    alphabet_size = 52

    def __init__(self, size=8192):
        self.table_size = size
        self.hashtable = [[] for i in range(size)]

    def __repr__(self):
        return "<HashTable: {}>".format(self.hashtable)

    def __len__(self):
        count = 0
        for item in self.hashtable:
            count += len(item)
        return count

    def _hashing(self, key):
        """Create a hash from a given key.

        args:
            key: a string to hash

        returns: an integer corresponding to hashtable index
        """
        hash_ = 0
        for i, c in enumerate(key):
            hash_ += pow(
                self.alphabet_size, len(key) - i - 1) * ord(c)
        return hash_ % self.table_size

    def set(self, key, value):
        """Add a key and value into the hash table.

        args:
            key: the key to store
            value: the value to store
        """
        if not isinstance(key, str):
            raise TypeError('Only strings may be used as keys.')
        hash_ = self._hashing(key)
        for i, item in enumerate(self.hashtable[hash_]):
            if item[0] == key:
                del self.hashtable[hash_][i]
                self.entries_count -= 1
        self.hashtable[hash_].append((key, value))
        self.entries_count += 1

    def get(self, key):
        """Retrieve a value from the hash table by key.

        args:
            key: a string to find the value in the hash table

        returns: the value stored with the key
        """
        hash_ = self._hashing(key)
        for i, item in enumerate(self.hashtable[hash_]):
            if item[0] == key:
                return item[1]
        raise KeyError('Key not in hash table.')
