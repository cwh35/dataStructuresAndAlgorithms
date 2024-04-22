import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.stack import Stack
from collections import deque

def test_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.container == deque([1, 2, 3])

def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    lastNum = stack.pop()
    assert lastNum == 2
    assert stack.container == deque([1])

def test_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    lastNum = stack.peek()
    assert lastNum == 2

def test_isEmpty():
    stack = Stack()
    assert stack.isEmpty() == True
    stack.push(1)
    assert stack.isEmpty() == False

def test_size():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.size() == 3
