def repeatedNTimes(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    sets = set()

    for a in A:
        if a not in sets:
            sets.add(a)
        else:
            return a