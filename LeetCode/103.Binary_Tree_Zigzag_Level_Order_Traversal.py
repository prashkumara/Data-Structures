# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        ret = []
        currLevel = [root]
        flag = 0
        while currLevel:
            temp =  [ node.val for node in currLevel ]
            if flag ==0:
                ret.append(temp)
                flag=1
            else:
                ret.append(temp[::-1])
                flag=0

            nextLevel = []
            for node in currLevel:
                if node.left:
                    nextLevel.append( node.left )
                if node.right:
                    nextLevel.append( node.right )

            currLevel = nextLevel

        return ret