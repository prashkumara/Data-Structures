def levelOrder(root):
    # Write your code here
    lis = []
    output = ""

    if root == None:
        return root
    lis.append(root)
    while len(lis) != 0:
        curr = lis.pop(0)

        output = output + str(curr.info) + ' '
        if curr.left != None:
            lis.append(curr.left)
        if curr.right != None:
            lis.append(curr.right)
    print(output)