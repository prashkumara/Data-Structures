def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []

    ret = []
    currLevel = [root]

    while currLevel:
        ret.append([node.val for node in currLevel])

        nextLevel = []
        for node in currLevel:
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)

        currLevel = nextLevel

    return ret