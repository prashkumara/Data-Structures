def peakIndexInMountainArray(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    maximum = 0
    maxelement = 0

    for i in range(len(A)):
        if A[i] > maxelement:
            maxelement = A[i]
            maximum = i
    return maximum