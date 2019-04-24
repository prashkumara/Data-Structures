class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 4:
            n = n // 5
            count = count + n * 1

        return count