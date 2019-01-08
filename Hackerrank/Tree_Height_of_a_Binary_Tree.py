def height(root):

    if root==None:
        return -1
    else:
        leftHeight=height(root.left)
        rightHeight=height(root.right)
        return max(leftHeight,rightHeight)+1