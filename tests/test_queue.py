import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.queue import Queue
from collections import deque

def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.queue == deque([3, 2, 1])

def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    firstNum = queue.dequeue()
    assert firstNum == 1
    assert queue.queue == deque([2])

def test_isEmpty():
    queue = Queue()
    assert queue.isEmpty() == True
    queue.enqueue(1)
    assert queue.isEmpty() == False

def test_size():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.size() == 3