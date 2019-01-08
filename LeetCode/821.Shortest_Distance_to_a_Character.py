def shortestToChar(self, S, C):
    """
    :type S: str
    :type C: str
    :rtype: List[int]
    """
    lis = [-1] * len(S)

    for i in range(len(S)):
        if S[i] == C:
            lis[i] = 0
    index = -1
    newindex = False
    for i in range(len(S)):
        if index >= 0:
            index += 1
            lis[i] = index
        else:
            lis[i] = -1
        if S[i] == C:
            lis[i] = 0
            index = 0

    index = lis[len(lis) - 1]
    for i in range(len(S) - 1, -1, -1):

        if index < lis[i]:
            index += 1
            lis[i] = index

        if S[i] == C:
            lis[i] = 0
            index = 0
        if lis[i] == -1:
            index += 1
            lis[i] = index
    return (lis)