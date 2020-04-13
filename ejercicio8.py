#!/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    minimum = []
    maximum = []
    arr.sort()
    for i in range(len(arr)):
        if i > 0 and i < 4:
            minimum.append(arr[i])
            maximum.append(arr[i])
        elif i == 0:
            minimum.append(arr[i])
        else:
            maximum.append(arr[i])
    print(sum(minimum), sum(maximum))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
