class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """

        res = []
        totalStr = ""

        for i in A:
            totalStr = totalStr + str(i)

        totalStr = str(int(totalStr) + K)

        for i in totalStr:
            res.append(int(i))

        return res