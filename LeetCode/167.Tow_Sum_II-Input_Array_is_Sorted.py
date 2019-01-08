def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    maphash = {}
    index = 1
    result = []

    for n in numbers:
        if target - n not in maphash:
            maphash.update({n: index})
        else:
            result.append(maphash[target - n])
            result.append(index)
            return result
        index += 1