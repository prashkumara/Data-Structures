def rotateString(self, A, B):
    """
    :type A: str
    :type B: str
    :rtype: bool
    """
    if len(A) != len(B):
        return False

    A = A + A
    if B in A:
        return True
    else:
        return False