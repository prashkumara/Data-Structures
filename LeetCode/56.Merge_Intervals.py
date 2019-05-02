class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        intervals = sorted(intervals)
        for i in (intervals):
            if result and i[0] <= result[len(result)-1][1]:
                result[len(result)-1][1] = max(result[len(result)-1][1], i[1])
            else:
                result += i,
        return result