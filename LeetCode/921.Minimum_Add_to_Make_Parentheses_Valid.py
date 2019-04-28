class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []

        for s in S:
            if not stack:
                stack.append(s)
            else:
                if s == ")" and stack[len(stack) - 1] == "(":
                    stack.pop()


                else:
                    stack.append(s)
        return len(stack)