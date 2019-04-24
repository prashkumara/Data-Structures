class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        sum = 0
        for i in s:
            sum *= 26
            sum += (ord(i) - ord('A') + 1)
        return (sum)