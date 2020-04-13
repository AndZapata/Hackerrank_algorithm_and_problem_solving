#!/bin/python3

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    rounded = []

    for i in grades:
        if i >= 38:
            if (i + 1) % 5 == 0:
                rounded.append(i + 1) 
            elif (i + 2) % 5 == 0:
                rounded.append(i + 2)
            else:
                rounded.append(i)
        else:
            rounded.append(i)

    return rounded

if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)