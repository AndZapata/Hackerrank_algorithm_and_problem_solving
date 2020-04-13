#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    p1=0
    p2=0
    for i, j in zip(a, b):
        if i < j:
            p2 += 1
        elif i > j:
            p1 += 1
        else:
            pass
        
    return [p1,p2]
          

if __name__ == '__main__':
    a = [5, 6, 7]
    b = [3, 6, 10]

    result = compareTriplets(a, b)
    
    print(result);
