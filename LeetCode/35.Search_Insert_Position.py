def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target in nums:
        return nums.index(target)
    else:
        for i in nums:
            if i > target:
                return nums.index(i)
        return len(nums)