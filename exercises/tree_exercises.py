import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.tree import TreeNode, TreeNode2

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

def buildLocationTree():
    root = TreeNode2("Global")

    india = TreeNode2("India")

    gujarat = TreeNode2("Gujarat")
    gujarat.addChild(TreeNode2("Ahmedabad"))
    gujarat.addChild(TreeNode2("Baroda"))

    karnataka = TreeNode2("Karnataka")
    karnataka.addChild(TreeNode2("Bangluru"))
    karnataka.addChild(TreeNode2("Mysore"))

    india.addChild(gujarat)
    india.addChild(karnataka)

    usa = TreeNode2("USA")

    new_jersey = TreeNode2("New Jersey")
    new_jersey.addChild(TreeNode2("Princeton"))
    new_jersey.addChild(TreeNode2("Trenton"))

    california = TreeNode2("California")
    california.addChild(TreeNode2("San Francisco"))
    california.addChild(TreeNode2("Mountain View"))
    california.addChild(TreeNode2("Palo Alto"))

    usa.addChild(new_jersey)
    usa.addChild(california)

    root.addChild(india)
    root.addChild(usa)

    return root


def testManagementTree():
    root = buildManagementTree()
    root.printTree("name")
    root.printTree("designation")
    root.printTree("both")

def testLocationTree():
    root = buildLocationTree()
    root.printTree(1)
    root.printTree(2)
    root.printTree(3)

if __name__ == "__main__":
    testManagementTree()
    testLocationTree()