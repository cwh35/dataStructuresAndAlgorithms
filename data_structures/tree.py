# Data Structure - Tree

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self # child is an instance of TreeNode, it will have a parent property, i want to set that parent property to self
        self.children.append(child)

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def printTree(self):
        spaces = ' ' * self.getLevel() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printTree()

def buildProductTree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.addChild(TreeNode("Mac"))
    laptop.addChild(TreeNode("Surface"))
    laptop.addChild(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.addChild(TreeNode("iPhone"))
    cellphone.addChild(TreeNode("Google Pixel"))
    cellphone.addChild(TreeNode("Samsung Galaxy"))

    tv = TreeNode("TV")
    tv.addChild(TreeNode("Samsung"))
    tv.addChild(TreeNode("LG"))

    root.addChild(laptop)
    root.addChild(cellphone)
    root.addChild(tv)

    return root


if __name__ == '__main__':
    root = buildProductTree()
    root.printTree()
    
