class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n > 0:
            if n == 1:
                return True
            if n % 2 != 0:
                return False
            n = n / 2