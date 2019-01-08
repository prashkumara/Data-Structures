def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    exor = 0
    for num in nums:
        exor = num ^ exor

    return exor 