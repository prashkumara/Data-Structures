import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr=sorted(arr)
    res=[]
    mindiff = sys.maxsize-1

    for i in range(1,len(arr)):
        mindiff = min(mindiff,arr[i]-arr[i-1])

    for i in range(1,len(arr)):
        if mindiff == arr[i]-arr[i-1]:
            res.append(arr[i-1])
            res.append(arr[i])

    return (res)