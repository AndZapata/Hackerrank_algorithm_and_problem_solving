#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr, n):
    positives=0
    negatives=0
    zeros=0
    for i in arr:
        if i > 0:
            positives += 1
        elif i < 0:
            negatives += 1
        else:
            zeros += 1
    return "{:.6f}\n{:.6f}\n{:.6f}".format((positives/n), (negatives/n), (zeros/n))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(plusMinus(arr, n))
