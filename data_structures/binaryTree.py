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

    def addChild(self, data):
        # need to check value first
        if data == self.data: # if the value already exists
            return
        
        if data < self.data:
            # add data to the left
            if self.left: # if left element has a value (not a leaf node)
                self.left.addChild(data)
            else:
                # left node is empty
                self.left = BinarySearchTreeNode(data)
        else:
            # add data to the right
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def findMin(self):
        if self.left is None:
            return self.data
        return self.left.findMin()
    
    def findMax(self):
        if self.right is None:
            return self.data
        return self.right.findMax()
    
    def calculateSum(self):
        leftSum = self.left.calculateSum() if self.left else 0
        rightSum = self.right.calculateSum() if self.right else 0
        return self.data + leftSum + rightSum
    
    def preOrderTraversal(self):
        elements = []

        # visit root node
        elements.append(self.data)

        # visit left tree
        if self.left:
            elements += self.left.preOrderTraversal()

        # visit right tree
        if self.right:
            elements += self.right.preOrderTraversal()

        return elements
    
    def postOrderTraversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.postOrderTraversal()

        # visit right tree
        if self.right:
            elements += self.right.postOrderTraversal()
        
        # visit root node
        elements.append(self.data)

        return elements

    def inOrderTraversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.inOrderTraversal()
        # visit root node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.inOrderTraversal()

        return elements
    
    def search(self, value):
        if self.data == value:
            return True
        
        if value < self.data:
            # value might be in left subtree
            if self.left:
                return self.left.search(value)
            else:
                return False # value does not exist in tree
        if value > self.data:
            # value might be in right subtree
            if self.right:
                return self.right.search(value)
            else:
                return False # value does not exist in tree
    
def buildTree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.addChild(elements[i])
    return root
    
if __name__ == '__main__':
    nums = [17, 4, 1, 20, 9, 23, 18, 34]
    numsTree = buildTree(nums)
    print(numsTree.inOrderTraversal()) # should return the list in ascending order
    print(numsTree.search(20))
    print(numsTree.search(200))