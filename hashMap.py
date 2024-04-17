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
        self.arr[hash] = None

    def delete(self, key):
        hash = self.getHash(key)
        self.arr[hash] = None

if __name__ == '__main__':
    table = HashTable()
    # h = table.getHash('march 6')
    # print(h)
    # table.add('april 15', 200)
    # val = table.get('april 15')
    # print(val)
    # table['june 5'] = 920
    # table['july 12'] = 45
    # print(table['june 5'])
    # print(table['july 12'])
    # del table['june 5']
    # print(table['june 5'])
    # table.delete('july 12')
    # print(table['july 12'])
    table.add('march 6', 310)
    table['march 17'] = 420
    print(table['march 6'])