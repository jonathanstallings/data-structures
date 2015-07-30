from __future__ import unicode_literals


class HashTable(object):
    """docstring for HashTable"""
    table_size = 0
    entries_count = 0
    alphabet_size = 52

    def __init__(self, size=16):
        self.table_size = size
        self.hashtable = [[] for i in range(size)]

    def __repr__(self):
        return "<HashTable: {}>".format(self.hashtable)

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

    def set(self, key, value):  # Validate for string only
        hash_ = self.hashing(key)
        for i, item in enumerate(self.hashtable[hash_]):
            if item[0] == key:
                del self.hashtable[hash_][i]
                self.entries_count -= 1
        self.hashtable[hash_].append((key, value))
        self.entries_count += 1

    def get(self, key):
        hash_ = self.hashing(key)
        for i, item in enumerate(self.hashtable[hash_]):
            if item[0] == key:
                return self.hashtable[hash_]
        return None

