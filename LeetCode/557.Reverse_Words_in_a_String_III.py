def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """

    words = s.split(" ")
    op = ''
    for w in words:
        op = op + ' ' + w[::-1]

    return op[1:]

