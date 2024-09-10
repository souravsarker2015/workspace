#!/bin/python3

import math
import os
import random
import re
import sys


def breakingRecords(scores):
    min_record = max_record = scores[0]
    min_breaks = max_breaks = 0

    for score in scores[1:]:
        if score > max_record:
            max_record = score
            max_breaks += 1
        elif score < min_record:
            min_record = score
            min_breaks += 1

    return [max_breaks, min_breaks]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
