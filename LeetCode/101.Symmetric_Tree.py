# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        root1 = root
        root2 = root
        return self.symmetric(root1, root2)

    def symmetric(self, r1, r2):
        if r1 == None and r2 == None:
            return True
        if r1 == None or r2 == None:
            return False

        if r1.val == r2.val:
            if (self.symmetric(r1.left, r2.right) and self.symmetric(r1.right, r2.left)):
                return True
        return False


