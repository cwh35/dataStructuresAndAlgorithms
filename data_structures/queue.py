# Data Structure: Queue

# Establishes loosing coupling between producer and consumer
# FIFO (First In First Out) data structure

from collections import deque

# Examples
stock_prices = []
stock_prices.insert(0, 98.05)
stock_prices.insert(0, 98.03)
stock_prices.insert(0, 98.07)
print("Current stock prices:",stock_prices)

print(stock_prices.pop()) # removes the first element that was put in --> in this case it should be 98.05
print(stock_prices) # now the list should be only [98.07, 98.03]

# Using deque (can be used for both stack and queue data structure)
stock_prices = deque()

stock_prices.appendleft(100)
stock_prices.appendleft(101)
stock_prices.appendleft(99)

print(stock_prices) # this should print deque([99, 101, 100])


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value): # placing an element in the queue
        self.queue.appendleft(value)

    def dequeue(self): # removing an element from the queue
        return self.queue.pop()
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)