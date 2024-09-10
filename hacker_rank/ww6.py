#!/bin/python3

import math
import os
import random
import re
import sys


def birthday(s, d, m):
    count = 0
    n = len(s)

    if n < m:
        return 0

    current_sum = sum(s[:m])

    if current_sum == d:
        count += 1

    for i in range(m, n):
        current_sum += s[i] - s[i - m]

        if current_sum == d:
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    d, m = map(int, input().rstrip().split())

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
