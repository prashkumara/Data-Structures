import collections


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        op = []
        count = collections.Counter(nums)

        for key in count:
            if count[key] == 1:
                op.append(key)

        return op