def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxsum = nums[0]
    index = 0

    for i in nums:
        index = index + i

        if index > maxsum:
            maxsum = index
        if index < 0:
            index = 0

    return (maxsum)