#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    res = []
    for c in s:
        if res and res[len(res)-1] == c:
            res.pop()
        else:
            res.append(c)
    res = ''.join(res)
    return res or 'Empty String'