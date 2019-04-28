# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res1 = []
        res2 = []

        self.inorder(root1, res1)
        self.inorder(root2, res2)

        return res1 == res2

    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            if (root.left == None and root.right == None):
                res.append(root.val)
            self.inorder(root.right, res)
