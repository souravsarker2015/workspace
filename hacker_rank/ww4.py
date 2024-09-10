from functools import reduce
import math
import os
import random
import re
import sys


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


def lcm_of_list(lst):
    return reduce(lcm, lst)


def gcd_of_list(lst):
    return reduce(math.gcd, lst)


def getTotalX(a, b):
    lcm_a = lcm_of_list(a)

    gcd_b = gcd_of_list(b)

    count = 0

    multiple = lcm_a
    while multiple <= gcd_b:
        if gcd_b % multiple == 0:
            count += 1
        multiple += lcm_a

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
