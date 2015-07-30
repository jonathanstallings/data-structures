from __future__ import unicode_literals


class Item(object):
    """docstring for Item"""
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return "<Item: {}:{}>".format(self.key, self.value)


class HashTable(object):
    """docstring for HashTable"""
    table_size = 0
    entries_count = 0
    alphabet_size = 52
    # hash_table = []

    def __init__(self, size):
        self.size = size
        self.hashtable = [[] for i in range(size)]

    def char2int(self, char):
        """Convert a alpha character to an int."""
        # offset for ASCII table
        if char >= 'A' and char <= 'Z':
            return ord(char) - 65
        elif char >= 'a' and char <= 'z':
            return ord(char) - 65 - 7
        else:
            raise NameError('Invalid character in key! Use alpha character.')

    def hashing(self, key):
        """pass"""
        hash_ = 0
        for i, c in enumerate(key):
            hash_ += pow(
                self.alphabet_size, len(key) - i - 1) * self.char2int(c)
        return hash_ % self.table_size

    def insert(self, item):
        hash_ = self.hashing(item.key)
        for i, it in enumerate(self.hashtable[hash_]):
            if it.key == item.key:
                del self.hashtable[hash_][i]
                self.entries_count -= 1
        self.hashtable[hash_].append(item)
        self.entries_count += 1

    
