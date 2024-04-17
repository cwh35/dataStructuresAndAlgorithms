
# Data Structure: Doubly-Linked List

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
    
    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        
        iterator.next = Node(data, None, iterator)

    # Inserting a list of values into a new linked list
    def insertValues(self, dataList):
        self.head = None
        for data in dataList:
            self.insertAtEnd(data)

    # Get the length of the linked list
    def getLength(self):
        count = 0
        iterator = self.head
        while iterator:
            count += 1
            iterator = iterator.next
        return count
    
    def getLastNode(self):
        iterator = self.head

        while iterator.next:
            iterator = iterator.next

        return iterator
    
    # Remove an element at a specific index
    def removeAt(self, index):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        
        count = 0
        iterator = self.head
        while iterator:
            if count == index:
                iterator.prev.next = iterator.next
                if iterator.next:
                    iterator.next.prev = iterator.prev
                break
            iterator = iterator.next
            count += 1


    # Insert a value at a specific index
    def insertAt(self, index, data):
        if index < 0 or index > self.getLength():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insertAtBeginning(data)
            return
        
        count = 0
        iterator = self.head
        while iterator:
            if count == index - 1:
                node = Node(data, iterator.next, iterator)
                if node.next:
                    node.next.prev = node
                iterator.next = node
                break
            iterator = iterator.next
            count += 1

    def printForward(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        iterator = self.head
        linkedListStr = ""
        while iterator:
            linkedListStr += str(iterator.data) + " --> "
            iterator = iterator.next
        print(linkedListStr)
    
    def printBackward(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        lastNode = self.getLastNode()
        iterator = lastNode
        linkedListStr = ""

        while iterator:
            linkedListStr += iterator.data + " --> "
            iterator = iterator.prev
        print("Linked List in reverse:", linkedListStr)

if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insertValues(["banana","mango","grapes","orange"])
    ll.printForward()
    ll.printBackward()
    ll.insertAtEnd("figs")
    ll.printForward()
    ll.insertAt(0,"jackfruit")
    ll.printForward()
    ll.insertAt(6,"dates")
    ll.printForward()
    ll.insertAt(2,"kiwi")
    ll.printForward()