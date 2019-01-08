def findDisappearedNumbers(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    lis = []
    sets = set(nums)
    for i in range(1, len(nums) + 1):
        if i not in sets:
            lis.append(i)
    return lis