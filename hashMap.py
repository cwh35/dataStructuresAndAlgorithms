# Data Structure - Hash Map/Table
# Look up by key is O(1) on average
# Insertion/Deletion is O(1) on average

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def getHash(self, key):
        hash = 0
        for char in key:
            hash += ord(char) # ord function finds the ASCII value for a character
        return hash % self.MAX # MAX is the size of the hash table
    
    def __setitem__(self, key, value):
        hash = self.getHash(key)
        self.arr[hash] = value

    def add(self, key, value):
        hash = self.getHash(key)
        self.arr[hash] = value
    
    def __getitem__(self, key):
        hash = self.getHash(key)
        return self.arr[hash]
    
    def get(self, key):
        hash = self.getHash(key)
        return self.arr[hash]
    
    def __delitem__(self, key):
        hash = self.getHash(key)
        self.arr[hash] = None

    def delete(self, key):
        hash = self.getHash(key)
        self.arr[hash] = None

if __name__ == '__main__':
    table = HashTable()
    h = table.getHash('march 6')
    print(h)
    table.add('april 15', 200)
    val = table.get('april 15')
    print(val)
    table['june 5'] = 920
    table['july 12'] = 45
    print(table['june 5'])
    print(table['july 12'])
    del table['june 5']
    print(table['june 5'])
    table.delete('july 12')
    print(table['july 12'])