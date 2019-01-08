def preOrder(root):
    # Write your code here
    temp = root

    if root == None:
        return root
    if temp != None:
        print(temp.info, end=" ")
        preOrder(temp.left)
        preOrder(temp.right)