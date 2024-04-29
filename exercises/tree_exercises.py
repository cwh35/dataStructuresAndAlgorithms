import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.tree import TreeNode

def buildManagementTree():
    root = TreeNode("Nilupul", "CEO")

    chinmay = TreeNode("Chinmay", "CTO")
    chinmay.addChild(TreeNode("Vishwa", "Infrastructure Head"))
    chinmay.addChild(TreeNode("Aamir", "Application Head"))

    gels = TreeNode("Gels", "HR Head")
    gels.addChild(TreeNode("Peter", "Recruitment Manager"))
    gels.addChild(TreeNode("Waqas", "Policy Manager"))

    root.addChild(chinmay)
    root.addChild(gels)

    return root

def testManagementTree():
    root = buildManagementTree()
    root.printTree("name")
    root.printTree("designation")
    root.printTree("both")

if __name__ == "__main__":
    testManagementTree()