def arrayManipulation(n, queries):
    diffarr = [0 for i in range(n + 1)]

    for k in range(len(queries)):
        q = queries[k]
        print(q[0], q[1], q[2])
        diffarr[q[0] - 1] += q[2]
        diffarr[q[1]] -= q[2]
    print(diffarr)
    temp = maxi = 0

    for i in diffarr:
        temp += i;
        if (temp > maxi): maxi = temp;
    return (maxi)