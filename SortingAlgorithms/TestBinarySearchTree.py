class Node:
    def __init__(self,val=None):
        self.val=val
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insertion(self,val):
        root=self.root

        if root == None:
            self.root=Node(val)
        else:
            self.Rec_insertion(root,val)

    def Rec_insertion(self,curr_node,val):
        if curr_node.val>val:
            if curr_node.left==None:
                curr_node.left=Node(val)
            else:
                self.Rec_insertion(curr_node.left, val)
        else:
            if curr_node.right==None:
                curr_node.right=Node(val)
            else:
                self.Rec_insertion(curr_node.right, val)


    def printInorder(self):
        if self.root == None:
            print("No values in tree")
        else:
            self.printInorderTraverasal(self.root)

    def printInorderTraverasal(self,root):
        if root!=None:
            self.printInorderTraverasal(root.left)
            print(root.val,end=' ')
            self.printInorderTraverasal(root.right)

bst=BinarySearchTree()

bst.printInorder()
bst.insertion(10)
bst.insertion(8)
bst.insertion(12)
bst.insertion(7)
bst.insertion(17)
bst.printInorder()