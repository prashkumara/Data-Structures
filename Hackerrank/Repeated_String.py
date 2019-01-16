#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(string, n):
    count = 0

    for i in string:
        if i == 'a':
            count += 1
    cycle = n // len(string)
    count = count * cycle
    remainder = n % len(string)

    for i in range(remainder):
        if string[i] == 'a':
            count += 1
    return (count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
