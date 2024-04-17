# Data Structure - Hash Map/Table
# Look up by key is O(1) on average
# Insertion/Deletion is O(1) on average

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def getHash(self, key):
        hash = 0
        for char in key:
            hash += ord(char) # ord function finds the ASCII value for a character
        return hash % self.MAX # MAX is the size of the hash table
    
    def __setitem__(self, key, value):
        hash = self.getHash(key)

        found = False
        for index, element in enumerate(self.arr[hash]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[hash].append((key, value))

    def add(self, key, value):
        hash = self.getHash(key)

        found = False
        for index, element in enumerate(self.arr[hash]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[hash].append((key, value))
    
    def __getitem__(self, key):
        hash = self.getHash(key)

        for element in self.arr[hash]:
            if element[0] == key:
                return element[1]
    
    def get(self, key):
        hash = self.getHash(key)

        for element in self.arr[hash]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        hash = self.getHash(key)
        
        for index, element in enumerate(self.arr[hash]):
            if element[0] == key:
                del self.arr[hash][index]

    def delete(self, key):
        hash = self.getHash(key)
        
        for index, element in enumerate(self.arr[hash]):
            if element[0] == key:
                del self.arr[hash][index]
