import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.linkedList import Node, LinkedList

def test_node():
    node = Node(1)
    assert node.data == 1
    assert node.next == None

def test_insertAtBeginning():
    ll = LinkedList()
    ll.insertAtBeginning(1)
    assert ll.head.data == 1
    ll.insertAtBeginning(2)
    assert ll.head.data == 2
    assert ll.head.next.data == 1

def test_insertAtEnd():
    ll = LinkedList()
    ll.insertAtEnd(1)
    assert ll.head.data == 1
    ll.insertAtEnd(2)
    assert ll.head.data == 1
    assert ll.head.next.data == 2

def test_insertValues():
    ll = LinkedList()
    ll.insertValues([1, 2, 3, 4])
    assert ll.head.data == 1
    assert ll.head.next.data == 2
    assert ll.head.next.next.data == 3
    assert ll.head.next.next.next.data == 4

def test_getLength():
    ll = LinkedList()
    ll.insertValues([1, 2, 3, 4])
    assert ll.getLength() == 4

def test_insertAfterValue():
    ll = LinkedList()
    ll.insertValues([1, 2, 3, 4])
    ll.insertAfterValue(2, 5)
    assert ll.head.data == 1
    assert ll.head.next.data == 2
    assert ll.head.next.next.data == 5
    assert ll.head.next.next.next.data == 3
    assert ll.head.next.next.next.next.data == 4

def test_removeAt():
    ll = LinkedList()
    ll.insertValues([1, 2, 3, 4])
    ll.removeAt(2)
    assert ll.head.data == 1
    assert ll.head.next.data == 2
    assert ll.head.next.next.data == 4
    assert ll.getLength() == 3
    ll.removeAt(0)
    assert ll.head.data == 2
    assert ll.head.next.data == 4
    assert ll.getLength() == 2

def test_removeByValue():
    ll = LinkedList()
    ll.insertValues([1, 2, 3, 4])
    ll.removeByValue(2)
    assert ll.head.data == 1
    assert ll.head.next.data == 3
    assert ll.head.next.next.data == 4
    assert ll.getLength() == 3
    ll.removeByValue(4)
    assert ll.head.data == 1
    assert ll.head.next.data == 3
    assert ll.getLength() == 2

def test_insertAt():
    ll = LinkedList()
    ll.insertValues([1, 2, 3, 4])
    ll.insertAt(2, 5)
    assert ll.head.data == 1
    assert ll.head.next.data == 2
    assert ll.head.next.next.data == 5
    assert ll.head.next.next.next.data == 3
    assert ll.head.next.next.next.next.data == 4

def test_removeAt_invalidIndex():
    ll = LinkedList()
    ll.insertValues([1, 2, 3, 4])
    try:
        ll.removeAt(5)
    except Exception as e:
        assert str(e) == "Invalid Index"

def test_insertAt_invalidIndex():
    ll = LinkedList()
    ll.insertValues([1, 2, 3, 4])
    try:
        ll.insertAt(5, 5)
    except Exception as e:
        assert str(e) == "Invalid Index"