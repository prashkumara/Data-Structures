# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        result = []
        self.preorder(root, result)
        return len(set(result)) == 1

    def preorder(self, root, result):
        if root:
            result.append(root.val)
            self.preorder(root.left, result)
            self.preorder(root.right, result)
