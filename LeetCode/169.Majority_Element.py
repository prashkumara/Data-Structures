def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    hash = {}
    for a in nums:
        if a in hash:
            hash.update({a: hash[a] + 1})
        else:
            hash.update({a: 1})

    return (max(hash, key=hash.get))