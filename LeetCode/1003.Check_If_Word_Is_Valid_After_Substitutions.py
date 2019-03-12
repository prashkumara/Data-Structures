class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """

        if len(S) % 3 != 0:
            return False

        if 'abc' not in S:
            return False

        while len(S) > 3 and 'abc' in S:
            S = S.replace('abc', "")

        if S == 'abc' or len(S) == 0:
            return True
        else:
            return False