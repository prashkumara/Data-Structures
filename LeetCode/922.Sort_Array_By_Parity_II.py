def sortArrayByParityII(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    odd = []
    even = []
    for i in A:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    for i in range(0, len(A) - 1, 2):
        A[i] = even[i // 2]
    for i in range(1, len(A), 2):
        A[i] = odd[(i // 2)]

    return (A)