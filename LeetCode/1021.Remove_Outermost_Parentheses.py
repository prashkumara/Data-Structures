class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type S: str
        :rtype: str
        """
        res = ""
        open = 0

        for c in s:
            if c=='(' and open > 0:
                res+=c

            if c==')' and open > 1:
                res+=c

            if c=='(':
                open+=1
            else:
                open-=1

        return res