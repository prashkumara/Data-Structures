class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)
        for i in range(num + 1):
            b = bin(i)
            count = 0
            for s in b:
                if s == "1":
                    count += 1
            res[i] = count
        return res

