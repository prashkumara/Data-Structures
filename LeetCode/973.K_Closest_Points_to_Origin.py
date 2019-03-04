import math


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        hashmap = {}

        for p in points:
            distance = math.sqrt((p[0] - 0) ** 2 + (p[1] - 0) ** 2)
            hashmap[distance] = p

        temp = sorted(hashmap.keys())

        op = []

        for i in range(K):
            op.append(hashmap[temp[i]])

        return op