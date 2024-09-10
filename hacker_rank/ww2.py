import math
import os
import random
import re
import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_landing_positions = [a + apple for apple in apples]
    oranges_landing_positions = [b + orange for orange in oranges]

    apples_on_house = sum(s <= position <= t for position in apples_landing_positions)

    oranges_on_house = sum(s <= position <= t for position in oranges_landing_positions)

    print(apples_on_house)
    print(oranges_on_house)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
