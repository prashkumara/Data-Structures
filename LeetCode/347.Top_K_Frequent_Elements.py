import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < 1:
            return []

        num = collections.Counter(nums)
        res = []

        for key, valye in num.most_common():
            if k > 0:
                res.append(key)
                k -= 1
            else:
                break

        return (res)