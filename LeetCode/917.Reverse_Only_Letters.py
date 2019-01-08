def reverseOnlyLetters(self, S):
    """
    :type S: str
    :rtype: str
    """
    str = ""
    for i in range(len(S)):
        if ((S[i]).isupper() or (S[i]).islower()):
            str = str + (S[i])
    str = str[::-1]
    index = 0
    op = ""
    for i in range(len(S)):
        if (S[i]).isupper() or (S[i]).islower():
            op = op + str[index]
            index += 1
        else:
            op = op + S[i]
    return op