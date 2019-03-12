import collections


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res = []
        if len(A) == 0:
            return res
        counter1 = collections.Counter(A[0])

        for word in A:
            counter1 = counter1 & collections.Counter(word)

        for key in counter1:
            for i in range(counter1[key]):
                res.append(key)

        return res