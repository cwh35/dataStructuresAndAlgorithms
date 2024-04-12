
# Data Structure: Linked List

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insertAtEnd(self, data):
        if self.head is None:
            # since you're adding a new node at the end, it will be the last node, so it's next will be None
            self.head = Node(data, None)
            return
        
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        
        iterator.next = Node(data, None)

    # Inserting a list of values into a new linked list
    def insertValues(self, dataList):
        self.head = None
        for data in dataList:
            self.insertAtEnd(data)

    # Insert a value after a specific value
    def insertAfterValue(self, dataAfter, dataToInsert):
        # If there is nothing in the list
        if self.head is None:
            return
        
        # Check if dataAfter is in the head node
        if self.head.data == dataAfter:
            self.head.next = Node(dataToInsert, self.head.next)
            return
        
        iterator = self.head
        while iterator:
            if iterator.data == dataAfter:
                iterator.next = Node(dataToInsert, iterator.next)
                break
            iterator = iterator.next

    # Get the length of the linked list
    def getLength(self):
        count = 0
        iterator = self.head
        while iterator:
            count += 1
            iterator = iterator.next
        return count
    
    # Remove an element at a specific index
    def removeAt(self, index):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        iterator = self.head
        while iterator:
            if count == index - 1:
                iterator.next = iterator.next.next
                break
            iterator = iterator.next
            count += 1
    
    # Remove an element by value
    def removeByValue(self, data):
        if self.head is None:
            return
        
        # Check if data is the head node
        if self.head.data == data:
            self.head = self.head.next
            return
        
        iterator = self.head
        while iterator.next:
            if iterator.next.data == data:
                iterator.next = iterator.next.next
                break
            iterator = iterator.next



    # Insert a value at a specific index
    def insertAt(self, index, data):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insertAtBeginning(data)
            return
        
        count = 0
        iterator = self.head
        while iterator:
            if count == index - 1:
                node = Node(data, iterator.next)
                iterator.next = node
                break
            iterator = iterator.next
            count += 1
    
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        iterator = self.head
        linkedListString = ''

        while iterator:
            linkedListString += str(iterator.data) + '-->'
            iterator = iterator.next

        print(linkedListString)

if __name__ == '__main__':

    ll = LinkedList()
    ll.insertValues(["banana","mango","grapes","orange"])
    ll.print()
    ll.insertAfterValue("mango","apple") # insert apple after mango
    ll.print()
    ll.removeByValue("orange") # remove orange from linked list
    ll.print()
    ll.removeByValue("figs")
    ll.print()
    ll.removeByValue("banana")
    ll.removeByValue("mango")
    ll.removeByValue("apple")
    ll.removeByValue("grapes")
    ll.print()
    # ll = LinkedList()
    # ll.insertAtBeginning(300)
    # ll.insertAtBeginning(234)
    # ll.insertAtBeginning(7)
    # ll.insertAtEnd(10002)
    # ll.print()
    # ll.insertValues(["Volvo", "BMW", "Ford", "Mazda"])
    # ll.removeAt(2)
    # ll.insertAt(0, "Mercedes")
    # ll.print()
    # print("Length of my linked list:", ll.getLength())