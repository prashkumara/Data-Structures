class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        lis = []
        for i in range(len(nums)):

            if nums[abs(nums[i]) - 1] >= 0:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
            else:
                lis.append(abs(nums[i]))
        return lis

