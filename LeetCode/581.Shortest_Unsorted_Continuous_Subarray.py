class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = end = -1
        snums = sorted(nums)
        for i in range(len(nums)):
            if snums[i] != nums[i]:
                if start == -1:
                    start = i
                end = i
        if end != start:
            return end-start+1
        else:
            return 0
