def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    if not root:
        return 0
    else:
        return (max(self.maxDepth(root.left), self.maxDepth(root.right))) + 1