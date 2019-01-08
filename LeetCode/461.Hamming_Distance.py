def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    x = '{0:032b}'.format(x)
    y = "{0:032b}".format(y)

    count = 0

    for i in range(32):
        if x[i] != y[i]:
            count += 1
    return count