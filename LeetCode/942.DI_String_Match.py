def diStringMatch(self, S):
    """
    :type S: str
    :rtype: List[int]
    """
    dlis = 0
    ilis = len(S)
    lis = []
    for s in S:
        if s == "I":
            lis.append(dlis)
            dlis += 1
        else:
            lis.append(ilis)
            ilis -= 1
    lis.append(dlis)
    return (lis)