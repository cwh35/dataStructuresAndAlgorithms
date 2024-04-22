# Data Structure - Stack

# LIFO - Last in First Out
# Push/Pop element: O(1)
# Search element by value: O(n)

# Use cases:
# 1. Undo operation in a text editor
# 2. Backtracking in a maze
# 3. Function calls in a program

from collections import deque

# Using list as a stack
stack = []
stack.append("https://www.google.com")
stack.append("https://www.youtube.com")
stack.append("https://www.github.com")
stack.append("https://www.linkedin.com")

# Get the last website visited
print("Last website visited:", stack.pop())
print("The list of websites now:", stack)

# To get the last website visited without removing the item
# Use the index -1
print("Last website visited:", stack[-1]) # Should be github

# Implementing stack using deque
stack2 = deque()

stack2.append("https://www.google.com")
stack2.append("https://www.youtube.com")
stack2.append("https://www.github.com")
stack2.append("https://www.linkedin.com")
print("Current stack:", stack2)
print("Last website visited:", stack2.pop()) # linked in and should be removed

# Stack Class
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def isEmpty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)