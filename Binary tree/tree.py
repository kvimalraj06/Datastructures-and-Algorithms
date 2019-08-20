class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class Binarytree:
    def __init__(self):
        self.root=None
    def create(self,val):
        if self.root == None:
            self.root=Node(val)
        else:
            current=self.root
            while True:
                if val < current.value:
                    if current.left:
                        current=current.left
                    else:
                        current.left=Node(val)
                        break
                elif val > current.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
    def printTree(self,traversal_type):
        if(traversal_type=="preorder"):
            print(self.preorder(tree.root,""))
        elif (traversal_type == "inorder"):
            print(self.inorder(tree.root, ""))
        elif (traversal_type == "postorder"):
            print(self.postorder(tree.root, ""))
    def preorder(self,start,values):
        if start:
            values += (str(start.value) + "-")
            values=self.preorder(start.left,values)
            values=self.preorder(start.right,values)
        return values
    def inorder(self,start,values):
        if start:
            values=self.preorder(start.left,values)
            values += (str(start.value) + "-")
            values=self.preorder(start.right,values)
        return values
    def postorder(self,start,values):
        if start:
            values=self.preorder(start.left,values)
            values=self.preorder(start.right,values)
            values += (str(start.value) + "-")
        return values

tree=Binarytree()
tree.create(2)
tree.create(7)
tree.create(1)
tree.create(3)
tree.create(6)
tree.create(4)
tree.printTree("postorder")
tree.printTree("preorder")
tree.printTree("inorder")

"""
O/P:
1-7-3-6-4-2-
2-1-7-3-6-4-
1-2-7-3-6-4-
"""