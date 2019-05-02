"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        self.dfs(root,res)
        return res

    def dfs(self,root,res):
        if root:
            for child in root.children:
                self.dfs(child,res)
            res.append(root.val)
