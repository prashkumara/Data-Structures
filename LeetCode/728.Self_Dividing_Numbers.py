def selfDividingNumbers(self, left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    lis = []
    flag = False
    for i in range(left, right + 1):
        l = list(map(int, str(i)))
        for j in l:
            if j != 0:

                if i % j == 0:
                    flag = True
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag:
            lis.append(i)
    return (lis)