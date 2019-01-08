def postOrder(root):
    #Write your code here
    if root==None:
        return root
    else:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info,end=' ')