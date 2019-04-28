class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        maxnum = max(A)
        minnum = min(A)

        if 2 * K >= (maxnum - minnum):
            return 0
        return abs(2 * K - (maxnum - minnum))