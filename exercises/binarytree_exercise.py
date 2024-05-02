import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.binaryTree import BinarySearchTreeNode, buildTree

def testBinarySearchTree():
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbersTree = buildTree(numbers)

    assert numbersTree.search(7) == False
    assert numbersTree.search(18) == True 

    assert numbersTree.calculateSum() == 126
    assert numbersTree.findMin() == 1
    assert numbersTree.findMax() == 34

    assert numbersTree.inOrderTraversal() == [1, 4, 9, 17, 18, 20, 23, 34]
    assert numbersTree.preOrderTraversal() == [17, 4, 1, 9, 20, 18, 23, 34]
    assert numbersTree.postOrderTraversal() == [1, 9, 4, 18, 34, 23, 20, 17]

    print("Binary Search Tree test passed")

if __name__ == "__main__":
    testBinarySearchTree()