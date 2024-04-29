# Data Structure - Tree
# works in a hierarchical structure

class TreeNode:
    def __init__(self, data, designation):
        self.data = data
        self.designation = designation
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

    def printTree(self, type):
        if type == "name":
            spaces = ' ' * self.getLevel() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data)
            if self.children:
                for child in self.children:
                    child.printTree("name")
        elif type == "designation":
            spaces = ' ' * self.getLevel() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.designation)
            if self.children:
                for child in self.children:
                    child.printTree("designation")
        elif type == "both":
            spaces = ' ' * self.getLevel() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data + " (" + self.designation + ")")
            if self.children:
                for child in self.children:
                    child.printTree("both")

    
