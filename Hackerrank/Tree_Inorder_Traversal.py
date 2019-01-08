def inOrder(root):
    #Write your code here
    curr=root
    if root==None:
        return
    else:
        inOrder(curr.left)
        print(curr.info,end=" ")
        inOrder(curr.right)