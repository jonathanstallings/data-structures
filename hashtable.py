

class HashTable(object):
    """docstring for HashTable"""
    table_size = 0
    entries_count = 0
    alphabet_size = 52

    def __init__(self, size=1024):
        self.table_size = size
        self.hashtable = [[] for i in range(size)]

    def __repr__(self):
        return "<HashTable: {}>".format(self.hashtable)

    def __len__(self):
        count = 0
        for item in self.hashtable:
            if len(item) != 0:
                count += 1
        return count

    def hashing(self, key):
        """pass"""
        hash_ = 0
        for i, c in enumerate(key):
            hash_ += pow(
                self.alphabet_size, len(key) - i - 1) * ord(c)
        return hash_ % self.table_size

    def set(self, key, value):
        if not isinstance(key, str):
            raise TypeError('Only strings may be used as keys.')
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
                return item[1]
        raise KeyError('Key not in hash table.')

if __name__ == '__main__':
    pass
