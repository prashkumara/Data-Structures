# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = set()
        self.inorder(root, result)
        result = list(result)
        result = sorted(result)
        if len(result) < 2:
            return -1
        else:
            return result[1]

    def inorder(self, root, result):
        if root:
            self.inorder(root.left, result)
            result.add(root.val)
            self.inorder(root.right, result)