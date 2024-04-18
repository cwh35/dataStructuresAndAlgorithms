# Data Structure - Hash Map/Table (using Linear Probing)
# Look up by key is O(1) on average
# Insertion/Deletion is O(1) on average

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def getHash(self, key):
        hash = 0
        for char in key:
            hash += ord(char) # ord function finds the ASCII value for a character
        return hash % self.MAX # MAX is the size of the hash table
    
    def __setitem__(self, key, value):
        hash = self.getHash(key)
        if self.arr[hash] is None:
            self.arr[hash] = (key, value)
        else:
            newHash = self.findEmpty(key, hash)
            self.arr[newHash] = (key, value)
        print(self.arr)
    
    def __getitem__(self, key):
        hash = self.getHash(key)

        if self.arr[hash] is None:
            return
        probRange = self.getProbRange(hash)
        for index in probRange:
            element = self.arr[index]
            if element is None:
                return
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        hash = self.getHash(key)
        probRange = self.getProbRange(hash)
        for index in probRange:
            if self.arr[index] is None:
                return # item not found --> return
            if self.arr[index][0] == key:
                self.arr[index] = None
        print(self.arr)

    def findEmpty(self, key, index):
        probRange = self.getProbRange(index)
        for i in probRange:
            if self.arr[i] is None:
                return i
            if self.arr[i][0] == key:
                return i
        raise Exception("Hash Table is full")

    def getProbRange(self, index):
        return [*range(index, len(self.arr))] + [*range(0,index)]
