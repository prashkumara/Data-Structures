def arrayPairSum(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum1 = 0
    nums = sorted(nums)

    for i in range(0, len(nums) - 1, 2):
        sum1 = sum1 + min(nums[i], nums[i + 1])

    return sum1