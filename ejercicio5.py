#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    clock = []
    new_s=s[:-2]
    clock = new_s.split(":")
    if "PM" in s:
        if "12:" in s:
            return (new_s)
        else:
            clock[0] = str(int(clock[0]) + 12)
            return (":".join(clock))
    elif "AM" in s:
        if "12:" in s:
            clock[0] = "00"
            return (":".join(clock))
        else:
            return (new_s)

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)
