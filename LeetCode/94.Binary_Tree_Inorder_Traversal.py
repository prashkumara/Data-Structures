def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    op = []
    self.inorder(root, op)
    return op


def inorder(self, root, op):
    if root != None:
        self.inorder(root.left, op)
        op.append(root.val)
        self.inorder(root.right, op)