#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    maxValue = 0
    counter = 0
    ar.sort()
    maxValue = max(ar)
    for i in ar:
        if i == maxValue:
            counter += 1
    return (counter)


if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)
