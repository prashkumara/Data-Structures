class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        for i in range(len(nums) +1):
            if i+1 not in nums:
                return i+1