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

if __name__ == '__main__':
    table = HashTable()
    table.getHash('march 6')