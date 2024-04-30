# Data Structure - Binary Tree

# every node has at most 2 child nodes
# binary search tree is also known as BST
# elements have some kind of order:
## any value less than the parent node goes to the left
## any value greater than the parent node goes to the right
# elements are not duplicated

# SEARCH COMPLEXITY
# every iteration --> reduce search space by 1/2
# ex: nodes = 8  8 -> 4 -> 2 -> 1
# 3 iterations
# log2(8) = 3
# Search complexity: O(log n)

# INSERTION COMPLEXITY
# O(log n)

# Traversal techniques for binary trees
## 1. Breadth first search (BFS)
## 2. Depth first search (DFS)
### a. In-order traversal [7, 12, 14, 15, 20, 23, 27, 88] first visit left child, then root node, then right child
### b. Pre-order traversal [15, 12, 7, 14, 27, 20, 23, 88] first visit root node, then left child, then right child
### c. Post-order traversal [7, 14, 12, 23, 20, 88, 27, 15] first visit left child, then right child, then root node

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None