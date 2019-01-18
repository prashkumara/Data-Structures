class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        total = 0

        for c in t:
            total += ord(c)
        for c in s:
            total -= ord(c)

        return chr(total)
