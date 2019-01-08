def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashmap = {}
    for i, n in enumerate(nums, 1):
        if (target - n) in hashmap:
            return [hashmap[target - n] - 1, i - 1]
        else:
            hashmap[n] = i
    return []