#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            if (i == j) and ((i + j) != (len(arr) - 1)):
                sum1 += arr[i][j]
                print("sum1", sum1)
            elif ((i + j) == (len(arr) - 1)) and (i != j):
                sum2 += arr[i][j]
                print("sum2", sum2)
            elif (i == j) and (i + j) == (len(arr) - 1):
                sum1 += arr[i][j]
                sum2 += arr[i][j]
    return(abs(sum1 - sum2))
    
if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)