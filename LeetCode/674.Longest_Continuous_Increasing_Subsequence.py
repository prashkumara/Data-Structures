def findLengthOfLCIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2:
        return len(nums)
    maxseq = 1
    count = 1
    for i in range(1, len(nums)):

        if nums[i - 1] < nums[i]:
            count += 1

        else:
            if count > maxseq:
                maxseq = count
            count = 1
    if count > maxseq:
        maxseq = count
    return (maxseq)