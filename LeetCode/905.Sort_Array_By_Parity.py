def sortArrayByParity(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    if len(A) == 1:
        return A
    j = 0
    for i in range(len(A)):

        if A[i] % 2 == 0:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            j += 1
    return A