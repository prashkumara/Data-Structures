class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.height=None

class BST:
    def __init__(self):
        self.root=None

    def insertion(self,val):

        self._insertion(self.root,val)


    def _insertion(self,root,val):
        if self.root==None:
            self.root=Node(val)


        elif val<root.val:
            if root.left==None:
                root.left=Node(val)
            else:
                self._insertion(root.left, val)
        else:
            if root.right==None:
                root.right=Node(val)
            else:
                self._insertion(root.right, val)

    def printInOrder(self):
        self._printInOrder(self.root)

    def _printInOrder(self,root):
        if root!=None:
            self._printInOrder(root.left)
            print(root.val,end=" ")
            self._printInOrder(root.right)

bst = BST()

bst.insertion(self.root,10)
bst.insertion(20)
bst.insertion(7)


bst.printInOrder()





