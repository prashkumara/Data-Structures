class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxconsecutive = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count = 0
            else:
                count += 1
                maxconsecutive = max(maxconsecutive, count)
        return maxconsecutive
