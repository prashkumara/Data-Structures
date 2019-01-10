# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        op = []
        self.inorder(root, op)

        sum = 0

        for i in op:
            if L <= i <= R:
                sum = sum + i

        return sum

    def inorder(self, root, op):
        if root != None:
            self.inorder(root.left, op)
            op.append(root.val)
            self.inorder(root.right, op)