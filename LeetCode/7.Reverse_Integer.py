def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    x = str(x)
    if x[0] == '-':
        if int(x[1:][::-1]) > pow(2, 31) - 1:
            return 0  # overflow
        else:
            return int('-' + x[1:][::-1])
    else:
        if int(x[::-1]) > pow(2, 31) - 1:
            return 0
        else:
            return int(x[::-1])