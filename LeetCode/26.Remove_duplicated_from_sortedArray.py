def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if len(nums) < 2:
        return len(nums)
    ind = 0

    for i in range(len(nums)):

        if nums[i] != nums[ind]:
            ind += 1
            nums[ind] = nums[i]
    return ind + 1 