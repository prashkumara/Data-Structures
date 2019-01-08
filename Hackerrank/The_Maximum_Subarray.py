#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxSubarray function below.
def maxSubarray(arr):
    maxSum = arr[0]
    localsum = -(sys.maxsize - 1)
    positivesum = 0

    for i in range(len(arr)):

        localsum = max(localsum + arr[i], arr[i])
        maxSum = max(maxSum, localsum)

        if arr[i] > 0:
            positivesum = positivesum + arr[i]
    if positivesum == 0:
        positivesum = max(arr)
    return (maxSum, positivesum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
